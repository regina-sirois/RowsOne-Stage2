# Passport OAuth for the RowsOne platform, by environment
from __future__ import annotations

import time
from typing import Literal, NotRequired, TypedDict

import httpx

from framework.common.env.env import Environment, get_environment
from framework.common.env.users import User

DEFAULT_SCOPES = "employee.read employee.write"
_REFRESH_BEFORE_SECONDS = 300


class OAuthToken(TypedDict):
    access_token: str
    expires_in: int
    token_type: NotRequired[str]
    refresh_token: NotRequired[str]  # present for password grant
    scope: NotRequired[str]


class PassportOAuth:
    env: Environment
    user: User
    token: OAuthToken | None

    def __init__(
        self,
        user: User,
        scope: str = DEFAULT_SCOPES,
        grant: Literal["client_credentials", "password"] = "password",
    ) -> None:
        self.env = get_environment()
        self.user = user
        self._grant = grant
        if grant == "password" and (not self.user.email or not self.user.password):
            raise ValueError("Email and password are required for the password grant")
        if not self.user.client_id or not self.user.client_secret:
            raise ValueError("Client ID and secret are required for Passport authentication")

        self.token = None
        self._scope = scope
        self._expires_at = 0.0
        self._http = httpx.Client(timeout=30.0)

    def close(self) -> None:
        self._http.close()

    def __enter__(self) -> PassportOAuth:
        return self

    def __exit__(self, *args: object) -> None:
        self.close()

    def get_token(self) -> OAuthToken:
        if self.token is not None and time.time() < self._expires_at - _REFRESH_BEFORE_SECONDS:
            return self.token

        client_id = self.user.client_id
        client_secret = self.user.client_secret
        assert client_id is not None and client_secret is not None

        data: dict[str, str] = {
            "grant_type": self._grant,
            "client_id": client_id,
            "client_secret": client_secret,
            "scope": self._scope,
        }
        if self._grant == "password":
            # Passport's password grant uses "username" as the field name,
            # even when the value is an email address.
            data["username"] = self.user.email
            data["password"] = self.user.password

        try:
            response = self._http.post(
                self.env.urls.get_oauth_url(),  # {base}/oauth/token
                data=data,
                headers={"Accept": "application/json"},
            )
            response.raise_for_status()
            token: OAuthToken = response.json()
            self.token = token
            self._expires_at = time.time() + token["expires_in"]
            return token
        except httpx.HTTPStatusError as e:
            if e.response.status_code in (400, 401):
                raise ValueError(
                    f"Passport token request failed ({self._grant} grant): "
                    f"{e.response.text}"
                ) from e
            raise

    def auth_header(self) -> dict[str, str]:
        return {"Authorization": f"Bearer {self.get_token()['access_token']}"}
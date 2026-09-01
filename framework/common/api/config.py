from __future__ import annotations

import base64

from framework.common.api.passport import PassportOAuth
from framework.common.env.users import User


class ApiConfig:
    base_url: str
    timeout: int
    user: User
    headers: dict[str, str]

    def __init__(self, base_url: str, user: User, timeout: int = 10) -> None:
        self.base_url = base_url
        self.timeout = timeout
        self.user = user
        if not self.user.client_id or not self.user.client_secret:
            self.headers = {
                "Authorization": self._basic_auth_header(
                    self.user.email, self.user.password
                ),
            }
        else:
            with PassportOAuth(self.user) as oauth:
                token = oauth.get_token()
                self.headers = oauth.auth_header()

    @staticmethod
    def _basic_auth_header(username: str, password: str) -> str:
        credentials = base64.b64encode(f"{username}:{password}".encode()).decode()
        return f"Basic {credentials}"

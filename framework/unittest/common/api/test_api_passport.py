"""Unit tests for framework.common.api.passport.PassportOAuth."""

from __future__ import annotations

from unittest.mock import MagicMock, patch

import httpx
import pytest

from framework.common.api.passport import DEFAULT_SCOPES, OAuthToken, PassportOAuth
from framework.common.env.users import User


@pytest.fixture
def oauth_user() -> User:
    return User(
        email="sdet@example.com",
        password="secret",
        client_id="client-id",
        client_secret="client-secret",
    )


@pytest.fixture
def token_payload() -> OAuthToken:
    return {
        "access_token": "access-token-1",
        "token_type": "Bearer",
        "expires_in": 3600,
        "scope": DEFAULT_SCOPES,
    }


@pytest.fixture
def mock_env() -> MagicMock:
    env = MagicMock()
    env.urls.get_oauth_url.return_value = "https://example.com/oauth/token"
    return env


def _ok_response(payload: OAuthToken) -> MagicMock:
    response = MagicMock()
    response.json.return_value = payload
    response.raise_for_status = MagicMock()
    return response


class TestPassportOAuthInit:
    def test_requires_client_id(self, mock_env: MagicMock) -> None:
        user = User(
            email="a@b.com",
            password="pw",
            client_id=None,
            client_secret="secret",
        )
        with patch("framework.common.api.passport.get_environment", return_value=mock_env):
            with pytest.raises(ValueError, match="Client ID and secret"):
                PassportOAuth(user)

    def test_requires_client_secret(self, mock_env: MagicMock) -> None:
        user = User(
            email="a@b.com",
            password="pw",
            client_id="id",
            client_secret=None,
        )
        with patch("framework.common.api.passport.get_environment", return_value=mock_env):
            with pytest.raises(ValueError, match="Client ID and secret"):
                PassportOAuth(user)

    def test_password_grant_requires_email_and_password(
        self, mock_env: MagicMock
    ) -> None:
        user = User(
            email="",
            password="",
            client_id="id",
            client_secret="secret",
        )
        with patch("framework.common.api.passport.get_environment", return_value=mock_env):
            with pytest.raises(ValueError, match="Email and password"):
                PassportOAuth(user, grant="password")

    def test_stores_user_env_and_default_scope(
        self, oauth_user: User, mock_env: MagicMock
    ) -> None:
        with patch("framework.common.api.passport.get_environment", return_value=mock_env):
            oauth = PassportOAuth(oauth_user)
        try:
            assert oauth.user is oauth_user
            assert oauth.env is mock_env
            assert oauth._scope == DEFAULT_SCOPES
            assert oauth.token is None
            assert oauth._grant == "password"
        finally:
            oauth.close()

    def test_accepts_custom_scope_and_grant(
        self, oauth_user: User, mock_env: MagicMock
    ) -> None:
        with patch("framework.common.api.passport.get_environment", return_value=mock_env):
            oauth = PassportOAuth(
                oauth_user, scope="custom.scope", grant="client_credentials"
            )
        try:
            assert oauth._scope == "custom.scope"
            assert oauth._grant == "client_credentials"
        finally:
            oauth.close()


class TestPassportOAuthGetToken:
    def test_fetches_and_caches_token_password_grant(
        self,
        oauth_user: User,
        mock_env: MagicMock,
        token_payload: OAuthToken,
    ) -> None:
        response = _ok_response(token_payload)

        with patch("framework.common.api.passport.get_environment", return_value=mock_env):
            oauth = PassportOAuth(oauth_user, grant="password")

        try:
            with patch.object(oauth._http, "post", return_value=response) as post:
                first = oauth.get_token()
                second = oauth.get_token()

            assert first == token_payload
            assert second is first
            assert first["access_token"] == "access-token-1"
            assert oauth.token == token_payload
            post.assert_called_once_with(
                "https://example.com/oauth/token",
                data={
                    "grant_type": "password",
                    "client_id": "client-id",
                    "client_secret": "client-secret",
                    "scope": DEFAULT_SCOPES,
                    "username": "sdet@example.com",
                    "password": "secret",
                },
                headers={"Accept": "application/json"},
            )
        finally:
            oauth.close()

    def test_refreshes_when_near_expiry(
        self,
        oauth_user: User,
        mock_env: MagicMock,
        token_payload: OAuthToken,
    ) -> None:
        refreshed: OAuthToken = {
            **token_payload,
            "access_token": "access-token-2",
        }

        with patch("framework.common.api.passport.get_environment", return_value=mock_env):
            oauth = PassportOAuth(oauth_user)

        try:
            with patch.object(
                oauth._http,
                "post",
                side_effect=[_ok_response(token_payload), _ok_response(refreshed)],
            ) as post:
                assert oauth.get_token()["access_token"] == "access-token-1"
                # Within _REFRESH_BEFORE_SECONDS of expiry → force a refresh
                oauth._expires_at = 1_700_000_000.0
                with patch(
                    "framework.common.api.passport.time.time",
                    return_value=1_700_000_000.0,
                ):
                    assert oauth.get_token()["access_token"] == "access-token-2"

            assert post.call_count == 2
            assert oauth.token == refreshed
        finally:
            oauth.close()

    def test_raises_value_error_on_401(
        self, oauth_user: User, mock_env: MagicMock
    ) -> None:
        response = MagicMock(status_code=401, text="invalid_client")
        response.raise_for_status.side_effect = httpx.HTTPStatusError(
            "unauthorized",
            request=MagicMock(),
            response=response,
        )

        with patch("framework.common.api.passport.get_environment", return_value=mock_env):
            oauth = PassportOAuth(oauth_user)

        try:
            with patch.object(oauth._http, "post", return_value=response):
                with pytest.raises(ValueError, match="Passport token request failed"):
                    oauth.get_token()
            assert oauth.token is None
        finally:
            oauth.close()

    def test_reraises_http_status_error_on_500(
        self, oauth_user: User, mock_env: MagicMock
    ) -> None:
        response = MagicMock(status_code=500, text="boom")
        response.raise_for_status.side_effect = httpx.HTTPStatusError(
            "server error",
            request=MagicMock(),
            response=response,
        )

        with patch("framework.common.api.passport.get_environment", return_value=mock_env):
            oauth = PassportOAuth(oauth_user)

        try:
            with patch.object(oauth._http, "post", return_value=response):
                with pytest.raises(httpx.HTTPStatusError):
                    oauth.get_token()
        finally:
            oauth.close()

    def test_auth_header(self, oauth_user: User, mock_env: MagicMock, token_payload: OAuthToken) -> None:
        with patch("framework.common.api.passport.get_environment", return_value=mock_env):
            oauth = PassportOAuth(oauth_user)

        try:
            with patch.object(oauth._http, "post", return_value=_ok_response(token_payload)):
                assert oauth.auth_header() == {
                    "Authorization": "Bearer access-token-1"
                }
        finally:
            oauth.close()

    def test_context_manager_closes_client(
        self, oauth_user: User, mock_env: MagicMock
    ) -> None:
        with patch("framework.common.api.passport.get_environment", return_value=mock_env):
            with PassportOAuth(oauth_user) as oauth:
                assert not oauth._http.is_closed
            assert oauth._http.is_closed

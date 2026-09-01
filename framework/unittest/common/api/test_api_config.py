"""Unit tests for framework.common.api.config.ApiConfig."""

from __future__ import annotations

from unittest.mock import MagicMock, patch

import pytest

from framework.common.api.config import ApiConfig
from framework.common.env.users import User


@pytest.fixture
def basic_user() -> User:
    return User(
        email="sdet@example.com",
        password="s3cret",
        client_id=None,
        client_secret=None,
    )


@pytest.fixture
def oauth_user() -> User:
    return User(
        email="sdet@example.com",
        password="s3cret",
        client_id="client-id",
        client_secret="client-secret",
    )


class TestApiConfigBasicAuth:
    def test_uses_basic_auth_when_client_credentials_missing(
        self, basic_user: User
    ) -> None:
        config = ApiConfig("https://api.example.com", basic_user)

        assert config.base_url == "https://api.example.com"
        assert config.timeout == 10
        assert config.user is basic_user
        assert config.headers == {
            "Authorization": ApiConfig._basic_auth_header(
                "sdet@example.com", "s3cret"
            ),
        }
        assert config.headers["Authorization"].startswith("Basic ")

    def test_uses_basic_auth_when_only_client_id_set(self) -> None:
        user = User(
            email="a@b.com",
            password="pw",
            client_id="id-only",
            client_secret=None,
        )
        config = ApiConfig("https://api.example.com", user)

        assert config.headers["Authorization"].startswith("Basic ")

    def test_uses_basic_auth_when_only_client_secret_set(self) -> None:
        user = User(
            email="a@b.com",
            password="pw",
            client_id=None,
            client_secret="secret-only",
        )
        config = ApiConfig("https://api.example.com", user)

        assert config.headers["Authorization"].startswith("Basic ")

    def test_custom_timeout(self, basic_user: User) -> None:
        config = ApiConfig("https://api.example.com", basic_user, timeout=30)
        assert config.timeout == 30

    def test_basic_auth_header_encoding(self) -> None:
        # echo -n 'user:pass' | base64 → dXNlcjpwYXNz
        assert ApiConfig._basic_auth_header("user", "pass") == "Basic dXNlcjpwYXNz"


class TestApiConfigOAuth:
    def test_uses_bearer_token_when_client_credentials_present(
        self, oauth_user: User
    ) -> None:
        mock_oauth = MagicMock()
        mock_oauth.get_token.return_value = {
            "access_token": "access-token-1",
            "token_type": "Bearer",
            "expires_in": 3600,
        }
        mock_oauth.auth_header.return_value = {
            "Authorization": "Bearer access-token-1"
        }
        mock_oauth.__enter__.return_value = mock_oauth
        mock_oauth.__exit__.return_value = None

        with patch(
            "framework.common.api.config.PassportOAuth", return_value=mock_oauth
        ) as oauth_cls:
            config = ApiConfig("https://api.example.com", oauth_user)

        oauth_cls.assert_called_once_with(oauth_user)
        mock_oauth.auth_header.assert_called_once_with()
        mock_oauth.__enter__.assert_called_once()
        mock_oauth.__exit__.assert_called_once()
        assert config.headers == {"Authorization": "Bearer access-token-1"}

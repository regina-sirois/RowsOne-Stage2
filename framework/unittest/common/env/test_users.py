"""Unit tests for framework.common.env.users."""

from __future__ import annotations

import pytest

from framework.common.env.users import User, Users


@pytest.fixture
def dev_env(monkeypatch: pytest.MonkeyPatch) -> None:
    monkeypatch.setenv("SDET_EMAIL_DEV", "sdet@example.com")
    monkeypatch.setenv("SDET_PASSWORD_DEV", "secret")
    monkeypatch.delenv("SDET_CLIENT_ID_DEV", raising=False)
    monkeypatch.delenv("SDET_CLIENT_SECRET_DEV", raising=False)


class TestUser:
    def test_is_frozen_dataclass(self) -> None:
        user = User(
            email="a@b.com",
            password="pw",
            client_id=None,
            client_secret=None,
        )
        with pytest.raises(AttributeError):
            user.email = "other@b.com"  # type: ignore[misc]


class TestUsersInit:
    def test_normalizes_environment_to_uppercase(self) -> None:
        users = Users("dev")
        assert users.environment == "DEV"


class TestUsersGetSdetUser:
    def test_returns_user_with_required_credentials(self, dev_env: None) -> None:
        user = Users("dev").get_sdet_user()

        assert user == User(
            email="sdet@example.com",
            password="secret",
            client_id=None,
            client_secret=None,
        )

    def test_returns_user_with_optional_oauth_credentials(
        self, monkeypatch: pytest.MonkeyPatch
    ) -> None:
        monkeypatch.setenv("SDET_EMAIL_DEV", "sdet@example.com")
        monkeypatch.setenv("SDET_PASSWORD_DEV", "secret")
        monkeypatch.setenv("SDET_CLIENT_ID_DEV", "client-id")
        monkeypatch.setenv("SDET_CLIENT_SECRET_DEV", "client-secret")

        user = Users("dev").get_sdet_user()

        assert user.client_id == "client-id"
        assert user.client_secret == "client-secret"

    def test_raises_when_email_missing(self, monkeypatch: pytest.MonkeyPatch) -> None:
        monkeypatch.delenv("SDET_EMAIL_DEV", raising=False)
        monkeypatch.setenv("SDET_PASSWORD_DEV", "secret")

        with pytest.raises(ValueError, match="Variable not found for environment"):
            Users("dev").get_sdet_user()

    def test_raises_when_password_missing(self, monkeypatch: pytest.MonkeyPatch) -> None:
        monkeypatch.setenv("SDET_EMAIL_DEV", "sdet@example.com")
        monkeypatch.delenv("SDET_PASSWORD_DEV", raising=False)

        with pytest.raises(ValueError, match="Variable not found for environment"):
            Users("dev").get_sdet_user()

    def test_uses_environment_specific_variable_names(
        self, monkeypatch: pytest.MonkeyPatch
    ) -> None:
        monkeypatch.setenv("SDET_EMAIL_STAGING", "staging@example.com")
        monkeypatch.setenv("SDET_PASSWORD_STAGING", "staging-secret")

        user = Users("staging").get_sdet_user()

        assert user.email == "staging@example.com"
        assert user.password == "staging-secret"

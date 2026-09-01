"""Unit tests for framework.common.env.env."""

from __future__ import annotations

import pytest

from framework.common.env.env import VALID_ENVS, Environment, get_environment


@pytest.fixture(autouse=True)
def clear_environment_cache() -> None:
    get_environment.cache_clear()
    yield
    get_environment.cache_clear()


class TestEnvironment:
    @pytest.mark.parametrize("name", sorted(VALID_ENVS))
    def test_accepts_valid_environment_names(self, name: str) -> None:
        env = Environment(name=name, urls=object(), users=object())  # type: ignore[arg-type]

        assert env.name == name

    def test_rejects_invalid_environment_name(self) -> None:
        with pytest.raises(ValueError, match="Invalid environment 'qa'"):
            Environment(name="qa", urls=object(), users=object())  # type: ignore[arg-type]


class TestGetEnvironment:
    def test_defaults_to_dev_when_test_env_unset(self, monkeypatch: pytest.MonkeyPatch) -> None:
        monkeypatch.delenv("TEST_ENV", raising=False)

        env = get_environment()

        assert env.name == "dev"
        assert env.urls.environment == "dev"
        assert env.users.environment == "DEV"

    def test_normalizes_test_env_to_lowercase(self, monkeypatch: pytest.MonkeyPatch) -> None:
        monkeypatch.setenv("TEST_ENV", "STAGING")

        env = get_environment()

        assert env.name == "staging"
        assert env.urls.environment == "staging"
        assert env.users.environment == "STAGING"

    def test_returns_cached_instance(self, monkeypatch: pytest.MonkeyPatch) -> None:
        monkeypatch.setenv("TEST_ENV", "dev")

        assert get_environment() is get_environment()

    def test_wires_urls_and_users_for_environment(self, monkeypatch: pytest.MonkeyPatch) -> None:
        monkeypatch.setenv("TEST_ENV", "prod")

        env = get_environment()

        assert env.urls.get_employee_mgmt_base_url() == "https://1385-api-prod.rowstest.com"
        assert env.users.environment == "PROD"

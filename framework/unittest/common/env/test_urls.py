"""Unit tests for framework.common.env.urls.Urls."""

from __future__ import annotations

import pytest

from framework.common.env.urls import Urls


class TestUrlsInit:
    def test_normalizes_environment_to_lowercase(self) -> None:
        urls = Urls("DEV")
        assert urls.environment == "dev"


class TestUrlsEmployeeMgmt:
    @pytest.mark.parametrize(
        ("environment", "expected"),
        [
            ("dev", "https://1385-api-dev.rowstest.com"),
            ("staging", "https://1385-api-staging.rowstest.com"),
            ("prod", "https://1385-api-prod.rowstest.com"),
        ],
    )
    def test_get_employee_mgmt_base_url(self, environment: str, expected: str) -> None:
        assert Urls(environment).get_employee_mgmt_base_url() == expected


class TestUrlsOAuth:
    def test_get_oauth_url_dev(self) -> None:
        assert Urls("dev").get_oauth_url() == "https://one-example.rowsone.com/oauth"

    def test_get_oauth_url_qa(self) -> None:
        assert Urls("qa").get_oauth_url() == "https://another-example.rowsone.com/oauth"

    def test_get_oauth_url_prod_not_supported(self) -> None:
        with pytest.raises(NotImplementedError, match="Production environment"):
            Urls("prod").get_oauth_url()

    def test_get_oauth_url_invalid_environment(self) -> None:
        with pytest.raises(ValueError, match="Invalid environment: staging"):
            Urls("staging").get_oauth_url()


class TestUrlsRowsoneUi:
    @pytest.mark.parametrize(
        ("environment", "expected"),
        [
            ("dev", "https://dev.rowsone.com"),
            ("qa", "https://qa.rowsone.com"),
        ],
    )
    def test_get_rowsone_ui_base_url(self, environment: str, expected: str) -> None:
        assert Urls(environment).get_rowsone_ui_base_url() == expected

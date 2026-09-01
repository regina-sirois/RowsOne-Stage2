"""Unit tests for framework.common.api.api.ApiClient."""

from __future__ import annotations

from unittest.mock import MagicMock, patch

import httpx
import pytest

from framework.common.api.api import ApiClient
from framework.common.api.config import ApiConfig
from framework.common.env.users import User


@pytest.fixture
def config() -> ApiConfig:
    user = User(
        email="sdet@example.com",
        password="secret",
        client_id=None,
        client_secret=None,
    )
    return ApiConfig("https://api.example.com", user)


@pytest.fixture
def client(config: ApiConfig) -> ApiClient:
    with ApiClient(config) as api_client:
        yield api_client


def _response(payload: dict, status_code: int = 200) -> MagicMock:
    response = MagicMock(spec=httpx.Response)
    response.status_code = status_code
    response.json.return_value = payload
    response.raise_for_status = MagicMock()
    if status_code >= 400:
        response.raise_for_status.side_effect = httpx.HTTPStatusError(
            "error",
            request=MagicMock(),
            response=response,
        )
    return response


class TestApiClientMethods:
    def test_get_includes_pagination_params(self, client: ApiClient) -> None:
        response = _response({"data": []})
        with patch.object(client._client, "get", return_value=response) as get:
            result = client.get("/api/companies", page=2, items_per_page=25, params={"q": "acme"})

        assert result is response
        get.assert_called_once_with(
            "/api/companies",
            params={"q": "acme", "page": 2, "itemsPerPage": 25},
        )
        response.raise_for_status.assert_called_once()

    def test_get_can_skip_raise_for_status(self, client: ApiClient) -> None:
        response = _response({"error": True}, status_code=404)
        # Clear the side effect so raise_for_status is a no-op when not called
        response.raise_for_status = MagicMock()
        with patch.object(client._client, "get", return_value=response):
            result = client.get("/api/missing", raise_for_status=False)

        assert result is response
        response.raise_for_status.assert_not_called()

    def test_post_sends_json_body(self, client: ApiClient) -> None:
        response = _response({"ok": True}, status_code=201)
        body = {"email": "a@b.com", "password": "x"}
        with patch.object(client._client, "post", return_value=response) as post:
            result = client.post("/api/login", json=body)

        assert result is response
        post.assert_called_once_with("/api/login", json=body, data=None, params=None)

    def test_put_sends_json_body(self, client: ApiClient) -> None:
        response = _response({"ok": True})
        body = {"first_name": "Ada"}
        with patch.object(client._client, "put", return_value=response) as put:
            result = client.put("/api/employees/1", json=body, params={"force": "1"})

        assert result is response
        put.assert_called_once_with(
            "/api/employees/1",
            json=body,
            data=None,
            params={"force": "1"},
        )


class TestApiClientPagination:
    def test_get_page_returns_json(self, client: ApiClient) -> None:
        payload = {"data": {"items": [{"id": 1}], "meta": {"current_page": 1, "last_page": 1}}}
        with patch.object(client._client, "get", return_value=_response(payload)) as get:
            body = client.get_page("/api/companies", page=1, items_per_page=10)

        assert body == payload
        get.assert_called_once_with(
            "/api/companies",
            params={"page": 1, "itemsPerPage": 10},
        )

    def test_iter_pages_follows_data_meta(self, client: ApiClient) -> None:
        page1 = {
            "data": {
                "items": [{"id": 1}],
                "meta": {"current_page": 1, "last_page": 2},
            }
        }
        page2 = {
            "data": {
                "items": [{"id": 2}],
                "meta": {"current_page": 2, "last_page": 2},
            }
        }
        with patch.object(
            client._client,
            "get",
            side_effect=[_response(page1), _response(page2)],
        ) as get:
            pages = list(client.iter_pages("/api/companies", items_per_page=10))

        assert pages == [page1, page2]
        assert get.call_count == 2
        assert get.call_args_list[0].kwargs["params"]["page"] == 1
        assert get.call_args_list[1].kwargs["params"]["page"] == 2

    def test_get_all_pages_with_flat_meta(self, client: ApiClient) -> None:
        page1 = {"data": {"items": [{"id": 1}], "page": 1, "totalPages": 2}}
        page2 = {"data": {"items": [{"id": 2}], "page": 2, "totalPages": 2}}
        with patch.object(
            client._client,
            "get",
            side_effect=[_response(page1), _response(page2)],
        ):
            pages = client.get_all_pages("/api/employees", items_per_page="*")

        assert pages == [page1, page2]

    def test_iter_pages_stops_when_meta_missing(self, client: ApiClient) -> None:
        payload = {"data": {"items": [{"id": 1}]}}
        with patch.object(client._client, "get", return_value=_response(payload)) as get:
            pages = list(client.iter_pages("/api/companies"))

        assert pages == [payload]
        assert get.call_count == 1

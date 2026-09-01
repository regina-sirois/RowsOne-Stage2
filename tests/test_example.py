import httpx
import pytest


def test_api_is_reachable(api_client) -> None:
    """Replace /health with a real endpoint from your API."""
    response = api_client.http.get("/health")
    response.raise_for_status()
    assert response.status_code == 200


def test_json_response_shape(api_client) -> None:
    """Example assertion pattern for JSON APIs."""
    response = api_client.http.get("/health")
    response.raise_for_status()

    payload = response.json()
    assert isinstance(payload, dict)


def test_not_found_returns_404(api_client) -> None:
    with pytest.raises(httpx.HTTPStatusError) as exc_info:
        api_client.http.get("/this-route-should-not-exist").raise_for_status()

    assert exc_info.value.response.status_code == 404

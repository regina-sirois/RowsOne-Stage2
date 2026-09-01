from __future__ import annotations
import httpx
from collections.abc import Iterator, Mapping
from typing import Any, TypeVar
from pydantic import BaseModel, ValidationError

from framework.common.api.config import ApiConfig

T = TypeVar("T", bound=BaseModel)

JsonDict = dict[str, Any]
QueryParams = Mapping[str, Any]


class ApiClient:
    """Thin httpx wrapper for API integration tests."""

    def __init__(self, config: ApiConfig) -> None:
        self._client = httpx.Client(
            base_url=config.base_url,
            headers=config.headers,
            timeout=config.timeout,
        )

    def __enter__(self) -> ApiClient:
        return self

    def __exit__(self, *args: object) -> None:
        self.close()

    def close(self) -> None:
        self._client.close()

    @property
    def http(self) -> httpx.Client:
        return self._client

    def get(
        self,
        path: str,
        *,
        response_model: type[T],
        params: QueryParams | None = None,
        page: int | None = None,
        items_per_page: int | str | None = None,
        raise_for_status: bool = True,
    ) -> httpx.Response:
        response = self._client.get(
            path,
            params=self._with_pagination(params, page=page, items_per_page=items_per_page),
        )
        if raise_for_status:
            response.raise_for_status()
        if response_model is not None:
            return response_model.model_validate(response.json())
        return response

    def post(
        self,
        path: str,
        *,
        response_model: type[T],
        json: Any = None,
        data: Any = None,
        params: QueryParams | None = None,
        raise_for_status: bool = True,
    ) -> httpx.Response:
        response = self._client.post(path, json=json, data=data, params=params)
        if raise_for_status:
            response.raise_for_status()
        if response_model is not None:
            return response_model.validate_model(response.json())
        return response

    def put(
        self,
        path: str,
        *,
        response_model: type[T],
        json: Any = None,
        data: Any = None,
        params: QueryParams | None = None,
        raise_for_status: bool = True,
    ) -> httpx.Response:
        response = self._client.put(path, json=json, data=data, params=params)
        if raise_for_status:
            response.raise_for_status()
        if response_model is not None:
            return response_model.validate_model(response.json())
        return response

    def get_page(
        self,
        path: str,
        *,
        page: int = 1,
        items_per_page: int | str = 10,
        params: QueryParams | None = None,
    ) -> JsonDict:
        """GET one paginated page and return the JSON body."""
        return self.get(
            path,
            params=params,
            page=page,
            items_per_page=items_per_page,
        ).json()

    def iter_pages(
        self,
        path: str,
        *,
        items_per_page: int | str = 10,
        params: QueryParams | None = None,
        start_page: int = 1,
    ) -> Iterator[JsonDict]:
        """Yield each page of a paginated GET until the last page.

        Supports both API pagination shapes:
        - ``data.meta`` (``PaginationMeta``: ``current_page`` / ``last_page``)
        - flat siblings of ``data`` (``PaginationFlatMeta``: ``page`` / ``totalPages``)
        """
        page = start_page
        while True:
            body = self.get_page(
                path,
                page=page,
                items_per_page=items_per_page,
                params=params,
            )
            yield body

            current, last = self._pagination_bounds(body)
            if last is None or current is None or current >= last:
                break
            page = current + 1

    def get_all_pages(
        self,
        path: str,
        *,
        items_per_page: int | str = 10,
        params: QueryParams | None = None,
        start_page: int = 1,
    ) -> list[JsonDict]:
        """Collect every page from a paginated GET."""
        return list(
            self.iter_pages(
                path,
                items_per_page=items_per_page,
                params=params,
                start_page=start_page,
            )
        )

    @staticmethod
    def _with_pagination(
        params: QueryParams | None,
        *,
        page: int | None,
        items_per_page: int | str | None,
    ) -> dict[str, Any] | None:
        merged: dict[str, Any] = dict(params or {})
        if page is not None:
            merged["page"] = page
        if items_per_page is not None:
            merged["itemsPerPage"] = items_per_page
        return merged or None

    @staticmethod
    def _pagination_bounds(body: JsonDict) -> tuple[int | None, int | None]:
        data = body.get("data")
        if isinstance(data, dict):
            meta = data.get("meta")
            if isinstance(meta, dict):
                current = meta.get("current_page")
                last = meta.get("last_page")
                if current is not None or last is not None:
                    return _as_int(current), _as_int(last)

            # Flat meta may sit on data itself or at the top level.
            current = data.get("page")
            last = data.get("totalPages")
            if current is not None or last is not None:
                return _as_int(current), _as_int(last)

        current = body.get("page")
        last = body.get("totalPages")
        return _as_int(current), _as_int(last)


def validate_model(response: httpx.Response, response_model: type[T]) -> T:
    if isinstance(response.json(), list):
        for item in response.json():
            response_model.model_validate(item)
        return [response_model.model_validate(item) for item in response.json()]
    elif isinstance(response.json(), dict):
        return response_model.model_validate(response.json())
    else:
        raise ValueError(f"Invalid response type: {type(response.json())}")

def _as_int(value: Any) -> int | None:
    if value is None:
        return None
    return int(value)

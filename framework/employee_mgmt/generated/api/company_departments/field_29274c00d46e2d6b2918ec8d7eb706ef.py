from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote
from uuid import UUID

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.field_29274c00d46e2d6b2918_ec_8d7_eb_706_ef_response_200 import (
    Field29274C00D46E2D6B2918Ec8D7Eb706EfResponse200,
)
from ...models.field_29274c00d46e2d6b2918_ec_8d7_eb_706_ef_response_500 import (
    Field29274C00D46E2D6B2918Ec8D7Eb706EfResponse500,
)
from ...types import UNSET, Response, Unset


def _get_kwargs(
    company_id: UUID,
    *,
    items_per_page: str | Unset = UNSET,
    sort: str | Unset = "name asc",
) -> dict[str, Any]:

    params: dict[str, Any] = {}

    params["itemsPerPage"] = items_per_page

    params["sort"] = sort

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/api/companies/{company_id}/departments".format(
            company_id=quote(str(company_id), safe=""),
        ),
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Any | Field29274C00D46E2D6B2918Ec8D7Eb706EfResponse200 | Field29274C00D46E2D6B2918Ec8D7Eb706EfResponse500 | None:
    if response.status_code == 200:
        response_200 = Field29274C00D46E2D6B2918Ec8D7Eb706EfResponse200.from_dict(response.json())

        return response_200

    if response.status_code == 422:
        response_422 = cast(Any, None)
        return response_422

    if response.status_code == 500:
        response_500 = Field29274C00D46E2D6B2918Ec8D7Eb706EfResponse500.from_dict(response.json())

        return response_500

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[
    Any | Field29274C00D46E2D6B2918Ec8D7Eb706EfResponse200 | Field29274C00D46E2D6B2918Ec8D7Eb706EfResponse500
]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    company_id: UUID,
    *,
    client: AuthenticatedClient | Client,
    items_per_page: str | Unset = UNSET,
    sort: str | Unset = "name asc",
) -> Response[
    Any | Field29274C00D46E2D6B2918Ec8D7Eb706EfResponse200 | Field29274C00D46E2D6B2918Ec8D7Eb706EfResponse500
]:
    """Get a paginated list of Company Departments

    Args:
        company_id (UUID):  Example: 550e8400-e29b-41d4-a716-446655440001.
        items_per_page (str | Unset):  Example: 10.
        sort (str | Unset):  Default: 'name asc'.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | Field29274C00D46E2D6B2918Ec8D7Eb706EfResponse200 | Field29274C00D46E2D6B2918Ec8D7Eb706EfResponse500]
    """

    kwargs = _get_kwargs(
        company_id=company_id,
        items_per_page=items_per_page,
        sort=sort,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    company_id: UUID,
    *,
    client: AuthenticatedClient | Client,
    items_per_page: str | Unset = UNSET,
    sort: str | Unset = "name asc",
) -> Any | Field29274C00D46E2D6B2918Ec8D7Eb706EfResponse200 | Field29274C00D46E2D6B2918Ec8D7Eb706EfResponse500 | None:
    """Get a paginated list of Company Departments

    Args:
        company_id (UUID):  Example: 550e8400-e29b-41d4-a716-446655440001.
        items_per_page (str | Unset):  Example: 10.
        sort (str | Unset):  Default: 'name asc'.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | Field29274C00D46E2D6B2918Ec8D7Eb706EfResponse200 | Field29274C00D46E2D6B2918Ec8D7Eb706EfResponse500
    """

    return sync_detailed(
        company_id=company_id,
        client=client,
        items_per_page=items_per_page,
        sort=sort,
    ).parsed


async def asyncio_detailed(
    company_id: UUID,
    *,
    client: AuthenticatedClient | Client,
    items_per_page: str | Unset = UNSET,
    sort: str | Unset = "name asc",
) -> Response[
    Any | Field29274C00D46E2D6B2918Ec8D7Eb706EfResponse200 | Field29274C00D46E2D6B2918Ec8D7Eb706EfResponse500
]:
    """Get a paginated list of Company Departments

    Args:
        company_id (UUID):  Example: 550e8400-e29b-41d4-a716-446655440001.
        items_per_page (str | Unset):  Example: 10.
        sort (str | Unset):  Default: 'name asc'.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | Field29274C00D46E2D6B2918Ec8D7Eb706EfResponse200 | Field29274C00D46E2D6B2918Ec8D7Eb706EfResponse500]
    """

    kwargs = _get_kwargs(
        company_id=company_id,
        items_per_page=items_per_page,
        sort=sort,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    company_id: UUID,
    *,
    client: AuthenticatedClient | Client,
    items_per_page: str | Unset = UNSET,
    sort: str | Unset = "name asc",
) -> Any | Field29274C00D46E2D6B2918Ec8D7Eb706EfResponse200 | Field29274C00D46E2D6B2918Ec8D7Eb706EfResponse500 | None:
    """Get a paginated list of Company Departments

    Args:
        company_id (UUID):  Example: 550e8400-e29b-41d4-a716-446655440001.
        items_per_page (str | Unset):  Example: 10.
        sort (str | Unset):  Default: 'name asc'.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | Field29274C00D46E2D6B2918Ec8D7Eb706EfResponse200 | Field29274C00D46E2D6B2918Ec8D7Eb706EfResponse500
    """

    return (
        await asyncio_detailed(
            company_id=company_id,
            client=client,
            items_per_page=items_per_page,
            sort=sort,
        )
    ).parsed

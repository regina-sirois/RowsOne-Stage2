from http import HTTPStatus
from typing import Any
from urllib.parse import quote
from uuid import UUID

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.get_company_sites_response_200 import GetCompanySitesResponse200
from ...models.get_company_sites_response_500 import GetCompanySitesResponse500
from ...types import UNSET, Response, Unset


def _get_kwargs(
    company_id: UUID,
    *,
    page: int | Unset = 1,
    items_per_page: str | Unset = UNSET,
    all_: bool | Unset = UNSET,
) -> dict[str, Any]:

    params: dict[str, Any] = {}

    params["page"] = page

    params["itemsPerPage"] = items_per_page

    params["all"] = all_

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/api/companies/{company_id}/sites".format(
            company_id=quote(str(company_id), safe=""),
        ),
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> GetCompanySitesResponse200 | GetCompanySitesResponse500 | None:
    if response.status_code == 200:
        response_200 = GetCompanySitesResponse200.from_dict(response.json())

        return response_200

    if response.status_code == 500:
        response_500 = GetCompanySitesResponse500.from_dict(response.json())

        return response_500

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[GetCompanySitesResponse200 | GetCompanySitesResponse500]:
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
    page: int | Unset = 1,
    items_per_page: str | Unset = UNSET,
    all_: bool | Unset = UNSET,
) -> Response[GetCompanySitesResponse200 | GetCompanySitesResponse500]:
    """Get sites and their units for a specific company (with pagination)

     Returns a paginated list of sites associated with a company, along with their units. Use query
    params to control pagination or retrieve all items.

    Args:
        company_id (UUID):  Example: 550e8400-e29b-41d4-a716-446655440001.
        page (int | Unset):  Default: 1.
        items_per_page (str | Unset):  Example: 10.
        all_ (bool | Unset):  Example: True.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[GetCompanySitesResponse200 | GetCompanySitesResponse500]
    """

    kwargs = _get_kwargs(
        company_id=company_id,
        page=page,
        items_per_page=items_per_page,
        all_=all_,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    company_id: UUID,
    *,
    client: AuthenticatedClient | Client,
    page: int | Unset = 1,
    items_per_page: str | Unset = UNSET,
    all_: bool | Unset = UNSET,
) -> GetCompanySitesResponse200 | GetCompanySitesResponse500 | None:
    """Get sites and their units for a specific company (with pagination)

     Returns a paginated list of sites associated with a company, along with their units. Use query
    params to control pagination or retrieve all items.

    Args:
        company_id (UUID):  Example: 550e8400-e29b-41d4-a716-446655440001.
        page (int | Unset):  Default: 1.
        items_per_page (str | Unset):  Example: 10.
        all_ (bool | Unset):  Example: True.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        GetCompanySitesResponse200 | GetCompanySitesResponse500
    """

    return sync_detailed(
        company_id=company_id,
        client=client,
        page=page,
        items_per_page=items_per_page,
        all_=all_,
    ).parsed


async def asyncio_detailed(
    company_id: UUID,
    *,
    client: AuthenticatedClient | Client,
    page: int | Unset = 1,
    items_per_page: str | Unset = UNSET,
    all_: bool | Unset = UNSET,
) -> Response[GetCompanySitesResponse200 | GetCompanySitesResponse500]:
    """Get sites and their units for a specific company (with pagination)

     Returns a paginated list of sites associated with a company, along with their units. Use query
    params to control pagination or retrieve all items.

    Args:
        company_id (UUID):  Example: 550e8400-e29b-41d4-a716-446655440001.
        page (int | Unset):  Default: 1.
        items_per_page (str | Unset):  Example: 10.
        all_ (bool | Unset):  Example: True.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[GetCompanySitesResponse200 | GetCompanySitesResponse500]
    """

    kwargs = _get_kwargs(
        company_id=company_id,
        page=page,
        items_per_page=items_per_page,
        all_=all_,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    company_id: UUID,
    *,
    client: AuthenticatedClient | Client,
    page: int | Unset = 1,
    items_per_page: str | Unset = UNSET,
    all_: bool | Unset = UNSET,
) -> GetCompanySitesResponse200 | GetCompanySitesResponse500 | None:
    """Get sites and their units for a specific company (with pagination)

     Returns a paginated list of sites associated with a company, along with their units. Use query
    params to control pagination or retrieve all items.

    Args:
        company_id (UUID):  Example: 550e8400-e29b-41d4-a716-446655440001.
        page (int | Unset):  Default: 1.
        items_per_page (str | Unset):  Example: 10.
        all_ (bool | Unset):  Example: True.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        GetCompanySitesResponse200 | GetCompanySitesResponse500
    """

    return (
        await asyncio_detailed(
            company_id=company_id,
            client=client,
            page=page,
            items_per_page=items_per_page,
            all_=all_,
        )
    ).parsed

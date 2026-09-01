from http import HTTPStatus
from typing import Any
from uuid import UUID

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.get_companies_response_200 import GetCompaniesResponse200
from ...models.get_companies_response_500 import GetCompaniesResponse500
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    items_per_page: str | Unset = UNSET,
    page: int | Unset = 1,
    q: str | Unset = UNSET,
    sort: str | Unset = UNSET,
    company_id: UUID | Unset = UNSET,
) -> dict[str, Any]:

    params: dict[str, Any] = {}

    params["itemsPerPage"] = items_per_page

    params["page"] = page

    params["q"] = q

    params["sort"] = sort

    json_company_id: str | Unset = UNSET
    if not isinstance(company_id, Unset):
        json_company_id = str(company_id)
    params["company_id"] = json_company_id

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/api/companies",
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> GetCompaniesResponse200 | GetCompaniesResponse500 | None:
    if response.status_code == 200:
        response_200 = GetCompaniesResponse200.from_dict(response.json())

        return response_200

    if response.status_code == 500:
        response_500 = GetCompaniesResponse500.from_dict(response.json())

        return response_500

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[GetCompaniesResponse200 | GetCompaniesResponse500]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient | Client,
    items_per_page: str | Unset = UNSET,
    page: int | Unset = 1,
    q: str | Unset = UNSET,
    sort: str | Unset = UNSET,
    company_id: UUID | Unset = UNSET,
) -> Response[GetCompaniesResponse200 | GetCompaniesResponse500]:
    """Retrieve a paginated list of companies

     Fetches companies with pagination, search, and sorting. See CompanyFilterRequest and
    CompanySortRequest schemas for options.

    Args:
        items_per_page (str | Unset):  Example: 10.
        page (int | Unset):  Default: 1.
        q (str | Unset):
        sort (str | Unset):  Example: name asc.
        company_id (UUID | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[GetCompaniesResponse200 | GetCompaniesResponse500]
    """

    kwargs = _get_kwargs(
        items_per_page=items_per_page,
        page=page,
        q=q,
        sort=sort,
        company_id=company_id,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: AuthenticatedClient | Client,
    items_per_page: str | Unset = UNSET,
    page: int | Unset = 1,
    q: str | Unset = UNSET,
    sort: str | Unset = UNSET,
    company_id: UUID | Unset = UNSET,
) -> GetCompaniesResponse200 | GetCompaniesResponse500 | None:
    """Retrieve a paginated list of companies

     Fetches companies with pagination, search, and sorting. See CompanyFilterRequest and
    CompanySortRequest schemas for options.

    Args:
        items_per_page (str | Unset):  Example: 10.
        page (int | Unset):  Default: 1.
        q (str | Unset):
        sort (str | Unset):  Example: name asc.
        company_id (UUID | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        GetCompaniesResponse200 | GetCompaniesResponse500
    """

    return sync_detailed(
        client=client,
        items_per_page=items_per_page,
        page=page,
        q=q,
        sort=sort,
        company_id=company_id,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient | Client,
    items_per_page: str | Unset = UNSET,
    page: int | Unset = 1,
    q: str | Unset = UNSET,
    sort: str | Unset = UNSET,
    company_id: UUID | Unset = UNSET,
) -> Response[GetCompaniesResponse200 | GetCompaniesResponse500]:
    """Retrieve a paginated list of companies

     Fetches companies with pagination, search, and sorting. See CompanyFilterRequest and
    CompanySortRequest schemas for options.

    Args:
        items_per_page (str | Unset):  Example: 10.
        page (int | Unset):  Default: 1.
        q (str | Unset):
        sort (str | Unset):  Example: name asc.
        company_id (UUID | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[GetCompaniesResponse200 | GetCompaniesResponse500]
    """

    kwargs = _get_kwargs(
        items_per_page=items_per_page,
        page=page,
        q=q,
        sort=sort,
        company_id=company_id,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient | Client,
    items_per_page: str | Unset = UNSET,
    page: int | Unset = 1,
    q: str | Unset = UNSET,
    sort: str | Unset = UNSET,
    company_id: UUID | Unset = UNSET,
) -> GetCompaniesResponse200 | GetCompaniesResponse500 | None:
    """Retrieve a paginated list of companies

     Fetches companies with pagination, search, and sorting. See CompanyFilterRequest and
    CompanySortRequest schemas for options.

    Args:
        items_per_page (str | Unset):  Example: 10.
        page (int | Unset):  Default: 1.
        q (str | Unset):
        sort (str | Unset):  Example: name asc.
        company_id (UUID | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        GetCompaniesResponse200 | GetCompaniesResponse500
    """

    return (
        await asyncio_detailed(
            client=client,
            items_per_page=items_per_page,
            page=page,
            q=q,
            sort=sort,
            company_id=company_id,
        )
    ).parsed

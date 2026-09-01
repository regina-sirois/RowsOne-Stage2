from http import HTTPStatus
from typing import Any
from urllib.parse import quote
from uuid import UUID

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.c13_eb_606_ef_7_aa_3e15_ff_1593217d3d973_response_200 import C13Eb606Ef7Aa3E15Ff1593217D3D973Response200
from ...models.c13_eb_606_ef_7_aa_3e15_ff_1593217d3d973_response_404 import C13Eb606Ef7Aa3E15Ff1593217D3D973Response404
from ...models.c13_eb_606_ef_7_aa_3e15_ff_1593217d3d973_response_500 import C13Eb606Ef7Aa3E15Ff1593217D3D973Response500
from ...types import UNSET, Response, Unset


def _get_kwargs(
    company: UUID,
    *,
    company_department_id: int | Unset = UNSET,
    items_per_page: str | Unset = UNSET,
    page: int | Unset = 1,
    sort: str | Unset = "name asc",
) -> dict[str, Any]:

    params: dict[str, Any] = {}

    params["company_department_id"] = company_department_id

    params["itemsPerPage"] = items_per_page

    params["page"] = page

    params["sort"] = sort

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/api/companies/{company}/positions".format(
            company=quote(str(company), safe=""),
        ),
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> (
    C13Eb606Ef7Aa3E15Ff1593217D3D973Response200
    | C13Eb606Ef7Aa3E15Ff1593217D3D973Response404
    | C13Eb606Ef7Aa3E15Ff1593217D3D973Response500
    | None
):
    if response.status_code == 200:
        response_200 = C13Eb606Ef7Aa3E15Ff1593217D3D973Response200.from_dict(response.json())

        return response_200

    if response.status_code == 404:
        response_404 = C13Eb606Ef7Aa3E15Ff1593217D3D973Response404.from_dict(response.json())

        return response_404

    if response.status_code == 500:
        response_500 = C13Eb606Ef7Aa3E15Ff1593217D3D973Response500.from_dict(response.json())

        return response_500

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[
    C13Eb606Ef7Aa3E15Ff1593217D3D973Response200
    | C13Eb606Ef7Aa3E15Ff1593217D3D973Response404
    | C13Eb606Ef7Aa3E15Ff1593217D3D973Response500
]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    company: UUID,
    *,
    client: AuthenticatedClient | Client,
    company_department_id: int | Unset = UNSET,
    items_per_page: str | Unset = UNSET,
    page: int | Unset = 1,
    sort: str | Unset = "name asc",
) -> Response[
    C13Eb606Ef7Aa3E15Ff1593217D3D973Response200
    | C13Eb606Ef7Aa3E15Ff1593217D3D973Response404
    | C13Eb606Ef7Aa3E15Ff1593217D3D973Response500
]:
    """Get a paginated list of Company Positions

     Returns a paginated list of company positions. If company_department_id is provided as a query
    parameter, positions will be filtered by department.

    Args:
        company (UUID):  Example: 550e8400-e29b-41d4-a716-446655440001.
        company_department_id (int | Unset):
        items_per_page (str | Unset):  Example: 10.
        page (int | Unset):  Default: 1.
        sort (str | Unset):  Default: 'name asc'.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[C13Eb606Ef7Aa3E15Ff1593217D3D973Response200 | C13Eb606Ef7Aa3E15Ff1593217D3D973Response404 | C13Eb606Ef7Aa3E15Ff1593217D3D973Response500]
    """

    kwargs = _get_kwargs(
        company=company,
        company_department_id=company_department_id,
        items_per_page=items_per_page,
        page=page,
        sort=sort,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    company: UUID,
    *,
    client: AuthenticatedClient | Client,
    company_department_id: int | Unset = UNSET,
    items_per_page: str | Unset = UNSET,
    page: int | Unset = 1,
    sort: str | Unset = "name asc",
) -> (
    C13Eb606Ef7Aa3E15Ff1593217D3D973Response200
    | C13Eb606Ef7Aa3E15Ff1593217D3D973Response404
    | C13Eb606Ef7Aa3E15Ff1593217D3D973Response500
    | None
):
    """Get a paginated list of Company Positions

     Returns a paginated list of company positions. If company_department_id is provided as a query
    parameter, positions will be filtered by department.

    Args:
        company (UUID):  Example: 550e8400-e29b-41d4-a716-446655440001.
        company_department_id (int | Unset):
        items_per_page (str | Unset):  Example: 10.
        page (int | Unset):  Default: 1.
        sort (str | Unset):  Default: 'name asc'.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        C13Eb606Ef7Aa3E15Ff1593217D3D973Response200 | C13Eb606Ef7Aa3E15Ff1593217D3D973Response404 | C13Eb606Ef7Aa3E15Ff1593217D3D973Response500
    """

    return sync_detailed(
        company=company,
        client=client,
        company_department_id=company_department_id,
        items_per_page=items_per_page,
        page=page,
        sort=sort,
    ).parsed


async def asyncio_detailed(
    company: UUID,
    *,
    client: AuthenticatedClient | Client,
    company_department_id: int | Unset = UNSET,
    items_per_page: str | Unset = UNSET,
    page: int | Unset = 1,
    sort: str | Unset = "name asc",
) -> Response[
    C13Eb606Ef7Aa3E15Ff1593217D3D973Response200
    | C13Eb606Ef7Aa3E15Ff1593217D3D973Response404
    | C13Eb606Ef7Aa3E15Ff1593217D3D973Response500
]:
    """Get a paginated list of Company Positions

     Returns a paginated list of company positions. If company_department_id is provided as a query
    parameter, positions will be filtered by department.

    Args:
        company (UUID):  Example: 550e8400-e29b-41d4-a716-446655440001.
        company_department_id (int | Unset):
        items_per_page (str | Unset):  Example: 10.
        page (int | Unset):  Default: 1.
        sort (str | Unset):  Default: 'name asc'.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[C13Eb606Ef7Aa3E15Ff1593217D3D973Response200 | C13Eb606Ef7Aa3E15Ff1593217D3D973Response404 | C13Eb606Ef7Aa3E15Ff1593217D3D973Response500]
    """

    kwargs = _get_kwargs(
        company=company,
        company_department_id=company_department_id,
        items_per_page=items_per_page,
        page=page,
        sort=sort,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    company: UUID,
    *,
    client: AuthenticatedClient | Client,
    company_department_id: int | Unset = UNSET,
    items_per_page: str | Unset = UNSET,
    page: int | Unset = 1,
    sort: str | Unset = "name asc",
) -> (
    C13Eb606Ef7Aa3E15Ff1593217D3D973Response200
    | C13Eb606Ef7Aa3E15Ff1593217D3D973Response404
    | C13Eb606Ef7Aa3E15Ff1593217D3D973Response500
    | None
):
    """Get a paginated list of Company Positions

     Returns a paginated list of company positions. If company_department_id is provided as a query
    parameter, positions will be filtered by department.

    Args:
        company (UUID):  Example: 550e8400-e29b-41d4-a716-446655440001.
        company_department_id (int | Unset):
        items_per_page (str | Unset):  Example: 10.
        page (int | Unset):  Default: 1.
        sort (str | Unset):  Default: 'name asc'.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        C13Eb606Ef7Aa3E15Ff1593217D3D973Response200 | C13Eb606Ef7Aa3E15Ff1593217D3D973Response404 | C13Eb606Ef7Aa3E15Ff1593217D3D973Response500
    """

    return (
        await asyncio_detailed(
            company=company,
            client=client,
            company_department_id=company_department_id,
            items_per_page=items_per_page,
            page=page,
            sort=sort,
        )
    ).parsed

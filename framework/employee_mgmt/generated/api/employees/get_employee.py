from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote
from uuid import UUID

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.get_employee_response_200 import GetEmployeeResponse200
from ...types import Response


def _get_kwargs(
    employee: UUID,
) -> dict[str, Any]:

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/api/employees/{employee}".format(
            employee=quote(str(employee), safe=""),
        ),
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Any | GetEmployeeResponse200 | None:
    if response.status_code == 200:
        response_200 = GetEmployeeResponse200.from_dict(response.json())

        return response_200

    if response.status_code == 404:
        response_404 = cast(Any, None)
        return response_404

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[Any | GetEmployeeResponse200]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    employee: UUID,
    *,
    client: AuthenticatedClient | Client,
) -> Response[Any | GetEmployeeResponse200]:
    """Get employee details

     Retrieves detailed information about a specific employee

    Args:
        employee (UUID):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | GetEmployeeResponse200]
    """

    kwargs = _get_kwargs(
        employee=employee,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    employee: UUID,
    *,
    client: AuthenticatedClient | Client,
) -> Any | GetEmployeeResponse200 | None:
    """Get employee details

     Retrieves detailed information about a specific employee

    Args:
        employee (UUID):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | GetEmployeeResponse200
    """

    return sync_detailed(
        employee=employee,
        client=client,
    ).parsed


async def asyncio_detailed(
    employee: UUID,
    *,
    client: AuthenticatedClient | Client,
) -> Response[Any | GetEmployeeResponse200]:
    """Get employee details

     Retrieves detailed information about a specific employee

    Args:
        employee (UUID):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | GetEmployeeResponse200]
    """

    kwargs = _get_kwargs(
        employee=employee,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    employee: UUID,
    *,
    client: AuthenticatedClient | Client,
) -> Any | GetEmployeeResponse200 | None:
    """Get employee details

     Retrieves detailed information about a specific employee

    Args:
        employee (UUID):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | GetEmployeeResponse200
    """

    return (
        await asyncio_detailed(
            employee=employee,
            client=client,
        )
    ).parsed

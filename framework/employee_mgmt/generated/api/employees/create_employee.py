from http import HTTPStatus
from typing import Any, cast

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.create_employee_response_201 import CreateEmployeeResponse201
from ...models.employee_create_request import EmployeeCreateRequest
from ...types import Response


def _get_kwargs(
    *,
    body: EmployeeCreateRequest,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/api/employees",
    }

    _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Any | CreateEmployeeResponse201 | None:
    if response.status_code == 201:
        response_201 = CreateEmployeeResponse201.from_dict(response.json())

        return response_201

    if response.status_code == 422:
        response_422 = cast(Any, None)
        return response_422

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[Any | CreateEmployeeResponse201]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient | Client,
    body: EmployeeCreateRequest,
) -> Response[Any | CreateEmployeeResponse201]:
    """Create a new employee

     Creates a new employee with a primary position and primary company. For adding a secondary position
    to an existing employee, use POST /api/employees/{employee}/secondary-position instead.

    Args:
        body (EmployeeCreateRequest): Request schema for creating a new employee with a primary
            position

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | CreateEmployeeResponse201]
    """

    kwargs = _get_kwargs(
        body=body,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: AuthenticatedClient | Client,
    body: EmployeeCreateRequest,
) -> Any | CreateEmployeeResponse201 | None:
    """Create a new employee

     Creates a new employee with a primary position and primary company. For adding a secondary position
    to an existing employee, use POST /api/employees/{employee}/secondary-position instead.

    Args:
        body (EmployeeCreateRequest): Request schema for creating a new employee with a primary
            position

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | CreateEmployeeResponse201
    """

    return sync_detailed(
        client=client,
        body=body,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient | Client,
    body: EmployeeCreateRequest,
) -> Response[Any | CreateEmployeeResponse201]:
    """Create a new employee

     Creates a new employee with a primary position and primary company. For adding a secondary position
    to an existing employee, use POST /api/employees/{employee}/secondary-position instead.

    Args:
        body (EmployeeCreateRequest): Request schema for creating a new employee with a primary
            position

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | CreateEmployeeResponse201]
    """

    kwargs = _get_kwargs(
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient | Client,
    body: EmployeeCreateRequest,
) -> Any | CreateEmployeeResponse201 | None:
    """Create a new employee

     Creates a new employee with a primary position and primary company. For adding a secondary position
    to an existing employee, use POST /api/employees/{employee}/secondary-position instead.

    Args:
        body (EmployeeCreateRequest): Request schema for creating a new employee with a primary
            position

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | CreateEmployeeResponse201
    """

    return (
        await asyncio_detailed(
            client=client,
            body=body,
        )
    ).parsed

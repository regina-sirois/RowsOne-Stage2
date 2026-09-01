from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote
from uuid import UUID

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.employee_update_request import EmployeeUpdateRequest
from ...models.update_employee_response_200 import UpdateEmployeeResponse200
from ...types import Response


def _get_kwargs(
    employee: UUID,
    *,
    body: EmployeeUpdateRequest,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "put",
        "url": "/api/employees/{employee}".format(
            employee=quote(str(employee), safe=""),
        ),
    }

    _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Any | UpdateEmployeeResponse200 | None:
    if response.status_code == 200:
        response_200 = UpdateEmployeeResponse200.from_dict(response.json())

        return response_200

    if response.status_code == 403:
        response_403 = cast(Any, None)
        return response_403

    if response.status_code == 422:
        response_422 = cast(Any, None)
        return response_422

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[Any | UpdateEmployeeResponse200]:
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
    body: EmployeeUpdateRequest,
) -> Response[Any | UpdateEmployeeResponse200]:
    """Update employee person-level details

     Updates person-level fields only (name, address, email, phone, SSN). Does not modify position,
    company, or status — those are managed by dedicated endpoints.

    Args:
        employee (UUID):
        body (EmployeeUpdateRequest): Request schema for updating person-level employee details
            (name, address, email, phone, SSN)

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | UpdateEmployeeResponse200]
    """

    kwargs = _get_kwargs(
        employee=employee,
        body=body,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    employee: UUID,
    *,
    client: AuthenticatedClient | Client,
    body: EmployeeUpdateRequest,
) -> Any | UpdateEmployeeResponse200 | None:
    """Update employee person-level details

     Updates person-level fields only (name, address, email, phone, SSN). Does not modify position,
    company, or status — those are managed by dedicated endpoints.

    Args:
        employee (UUID):
        body (EmployeeUpdateRequest): Request schema for updating person-level employee details
            (name, address, email, phone, SSN)

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | UpdateEmployeeResponse200
    """

    return sync_detailed(
        employee=employee,
        client=client,
        body=body,
    ).parsed


async def asyncio_detailed(
    employee: UUID,
    *,
    client: AuthenticatedClient | Client,
    body: EmployeeUpdateRequest,
) -> Response[Any | UpdateEmployeeResponse200]:
    """Update employee person-level details

     Updates person-level fields only (name, address, email, phone, SSN). Does not modify position,
    company, or status — those are managed by dedicated endpoints.

    Args:
        employee (UUID):
        body (EmployeeUpdateRequest): Request schema for updating person-level employee details
            (name, address, email, phone, SSN)

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | UpdateEmployeeResponse200]
    """

    kwargs = _get_kwargs(
        employee=employee,
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    employee: UUID,
    *,
    client: AuthenticatedClient | Client,
    body: EmployeeUpdateRequest,
) -> Any | UpdateEmployeeResponse200 | None:
    """Update employee person-level details

     Updates person-level fields only (name, address, email, phone, SSN). Does not modify position,
    company, or status — those are managed by dedicated endpoints.

    Args:
        employee (UUID):
        body (EmployeeUpdateRequest): Request schema for updating person-level employee details
            (name, address, email, phone, SSN)

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | UpdateEmployeeResponse200
    """

    return (
        await asyncio_detailed(
            employee=employee,
            client=client,
            body=body,
        )
    ).parsed

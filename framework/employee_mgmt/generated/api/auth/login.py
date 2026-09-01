from http import HTTPStatus
from typing import Any

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.login_body import LoginBody
from ...models.login_response_401 import LoginResponse401
from ...models.login_response_403_type_0 import LoginResponse403Type0
from ...models.login_response_403_type_1 import LoginResponse403Type1
from ...models.login_response_403_type_2 import LoginResponse403Type2
from ...models.login_response_422 import LoginResponse422
from ...models.login_response_500 import LoginResponse500
from ...models.login_success_response import LoginSuccessResponse
from ...types import Response


def _get_kwargs(
    *,
    body: LoginBody,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/api/login",
    }

    _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> (
    LoginResponse401
    | LoginResponse403Type0
    | LoginResponse403Type1
    | LoginResponse403Type2
    | LoginResponse422
    | LoginResponse500
    | LoginSuccessResponse
    | None
):
    if response.status_code == 200:
        response_200 = LoginSuccessResponse.from_dict(response.json())

        return response_200

    if response.status_code == 401:
        response_401 = LoginResponse401.from_dict(response.json())

        return response_401

    if response.status_code == 403:

        def _parse_response_403(data: object) -> LoginResponse403Type0 | LoginResponse403Type1 | LoginResponse403Type2:
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                response_403_type_0 = LoginResponse403Type0.from_dict(data)

                return response_403_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                response_403_type_1 = LoginResponse403Type1.from_dict(data)

                return response_403_type_1
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            if not isinstance(data, dict):
                raise TypeError()
            response_403_type_2 = LoginResponse403Type2.from_dict(data)

            return response_403_type_2

        response_403 = _parse_response_403(response.json())

        return response_403

    if response.status_code == 422:
        response_422 = LoginResponse422.from_dict(response.json())

        return response_422

    if response.status_code == 500:
        response_500 = LoginResponse500.from_dict(response.json())

        return response_500

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[
    LoginResponse401
    | LoginResponse403Type0
    | LoginResponse403Type1
    | LoginResponse403Type2
    | LoginResponse422
    | LoginResponse500
    | LoginSuccessResponse
]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient | Client,
    body: LoginBody,
) -> Response[
    LoginResponse401
    | LoginResponse403Type0
    | LoginResponse403Type1
    | LoginResponse403Type2
    | LoginResponse422
    | LoginResponse500
    | LoginSuccessResponse
]:
    """Authenticate a user

     Logs in a user and creates a cookied-based session. Implements account lockout and status checks.
    Email is case insensitive and normalized to lowercase before authentication.

    Args:
        body (LoginBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[LoginResponse401 | LoginResponse403Type0 | LoginResponse403Type1 | LoginResponse403Type2 | LoginResponse422 | LoginResponse500 | LoginSuccessResponse]
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
    body: LoginBody,
) -> (
    LoginResponse401
    | LoginResponse403Type0
    | LoginResponse403Type1
    | LoginResponse403Type2
    | LoginResponse422
    | LoginResponse500
    | LoginSuccessResponse
    | None
):
    """Authenticate a user

     Logs in a user and creates a cookied-based session. Implements account lockout and status checks.
    Email is case insensitive and normalized to lowercase before authentication.

    Args:
        body (LoginBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        LoginResponse401 | LoginResponse403Type0 | LoginResponse403Type1 | LoginResponse403Type2 | LoginResponse422 | LoginResponse500 | LoginSuccessResponse
    """

    return sync_detailed(
        client=client,
        body=body,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient | Client,
    body: LoginBody,
) -> Response[
    LoginResponse401
    | LoginResponse403Type0
    | LoginResponse403Type1
    | LoginResponse403Type2
    | LoginResponse422
    | LoginResponse500
    | LoginSuccessResponse
]:
    """Authenticate a user

     Logs in a user and creates a cookied-based session. Implements account lockout and status checks.
    Email is case insensitive and normalized to lowercase before authentication.

    Args:
        body (LoginBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[LoginResponse401 | LoginResponse403Type0 | LoginResponse403Type1 | LoginResponse403Type2 | LoginResponse422 | LoginResponse500 | LoginSuccessResponse]
    """

    kwargs = _get_kwargs(
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient | Client,
    body: LoginBody,
) -> (
    LoginResponse401
    | LoginResponse403Type0
    | LoginResponse403Type1
    | LoginResponse403Type2
    | LoginResponse422
    | LoginResponse500
    | LoginSuccessResponse
    | None
):
    """Authenticate a user

     Logs in a user and creates a cookied-based session. Implements account lockout and status checks.
    Email is case insensitive and normalized to lowercase before authentication.

    Args:
        body (LoginBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        LoginResponse401 | LoginResponse403Type0 | LoginResponse403Type1 | LoginResponse403Type2 | LoginResponse422 | LoginResponse500 | LoginSuccessResponse
    """

    return (
        await asyncio_detailed(
            client=client,
            body=body,
        )
    ).parsed

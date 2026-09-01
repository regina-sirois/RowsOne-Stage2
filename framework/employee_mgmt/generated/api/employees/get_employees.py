import datetime
from http import HTTPStatus
from typing import Any, cast

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.get_employees_response_200 import GetEmployeesResponse200
from ...models.get_employees_status_item import GetEmployeesStatusItem
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    items_per_page: str | Unset = UNSET,
    page: int | Unset = 1,
    q: str | Unset = UNSET,
    sort: str | Unset = UNSET,
    status: list[GetEmployeesStatusItem] | Unset = UNSET,
    rehire_flag: bool | Unset = UNSET,
    eligible_for_rehire: bool | Unset = UNSET,
    is_shared_employee: bool | Unset = UNSET,
    work_mode: list[str] | Unset = UNSET,
    company: list[str] | Unset = UNSET,
    department: list[str] | Unset = UNSET,
    position: list[str] | Unset = UNSET,
    site: list[str] | Unset = UNSET,
    employment_type: list[str] | Unset = UNSET,
    job_title: list[str] | Unset = UNSET,
    date_of_hire_from: datetime.date | Unset = UNSET,
    date_of_hire_to: datetime.date | Unset = UNSET,
    date_of_termination_from: datetime.date | Unset = UNSET,
    date_of_termination_to: datetime.date | Unset = UNSET,
) -> dict[str, Any]:

    params: dict[str, Any] = {}

    params["itemsPerPage"] = items_per_page

    params["page"] = page

    params["q"] = q

    params["sort"] = sort

    json_status: list[str] | Unset = UNSET
    if not isinstance(status, Unset):
        json_status = []
        for status_item_data in status:
            status_item = status_item_data.value
            json_status.append(status_item)

    params["status[]"] = json_status

    params["rehire_flag"] = rehire_flag

    params["eligible_for_rehire"] = eligible_for_rehire

    params["is_shared_employee"] = is_shared_employee

    json_work_mode: list[str] | Unset = UNSET
    if not isinstance(work_mode, Unset):
        json_work_mode = work_mode

    params["work_mode[]"] = json_work_mode

    json_company: list[str] | Unset = UNSET
    if not isinstance(company, Unset):
        json_company = company

    params["company[]"] = json_company

    json_department: list[str] | Unset = UNSET
    if not isinstance(department, Unset):
        json_department = department

    params["department[]"] = json_department

    json_position: list[str] | Unset = UNSET
    if not isinstance(position, Unset):
        json_position = position

    params["position[]"] = json_position

    json_site: list[str] | Unset = UNSET
    if not isinstance(site, Unset):
        json_site = site

    params["site[]"] = json_site

    json_employment_type: list[str] | Unset = UNSET
    if not isinstance(employment_type, Unset):
        json_employment_type = employment_type

    params["employment_type[]"] = json_employment_type

    json_job_title: list[str] | Unset = UNSET
    if not isinstance(job_title, Unset):
        json_job_title = job_title

    params["job_title[]"] = json_job_title

    json_date_of_hire_from: str | Unset = UNSET
    if not isinstance(date_of_hire_from, Unset):
        json_date_of_hire_from = date_of_hire_from.isoformat()
    params["date_of_hire_from"] = json_date_of_hire_from

    json_date_of_hire_to: str | Unset = UNSET
    if not isinstance(date_of_hire_to, Unset):
        json_date_of_hire_to = date_of_hire_to.isoformat()
    params["date_of_hire_to"] = json_date_of_hire_to

    json_date_of_termination_from: str | Unset = UNSET
    if not isinstance(date_of_termination_from, Unset):
        json_date_of_termination_from = date_of_termination_from.isoformat()
    params["date_of_termination_from"] = json_date_of_termination_from

    json_date_of_termination_to: str | Unset = UNSET
    if not isinstance(date_of_termination_to, Unset):
        json_date_of_termination_to = date_of_termination_to.isoformat()
    params["date_of_termination_to"] = json_date_of_termination_to

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/api/employees",
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Any | GetEmployeesResponse200 | None:
    if response.status_code == 200:
        response_200 = GetEmployeesResponse200.from_dict(response.json())

        return response_200

    if response.status_code == 401:
        response_401 = cast(Any, None)
        return response_401

    if response.status_code == 403:
        response_403 = cast(Any, None)
        return response_403

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[Any | GetEmployeesResponse200]:
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
    status: list[GetEmployeesStatusItem] | Unset = UNSET,
    rehire_flag: bool | Unset = UNSET,
    eligible_for_rehire: bool | Unset = UNSET,
    is_shared_employee: bool | Unset = UNSET,
    work_mode: list[str] | Unset = UNSET,
    company: list[str] | Unset = UNSET,
    department: list[str] | Unset = UNSET,
    position: list[str] | Unset = UNSET,
    site: list[str] | Unset = UNSET,
    employment_type: list[str] | Unset = UNSET,
    job_title: list[str] | Unset = UNSET,
    date_of_hire_from: datetime.date | Unset = UNSET,
    date_of_hire_to: datetime.date | Unset = UNSET,
    date_of_termination_from: datetime.date | Unset = UNSET,
    date_of_termination_to: datetime.date | Unset = UNSET,
) -> Response[Any | GetEmployeesResponse200]:
    """Retrieve a paginated list of employees

     Fetches a paginated list of employees from the database. Supports filtering, sorting, and pagination
    through query parameters.

    Args:
        items_per_page (str | Unset):  Example: 10.
        page (int | Unset):  Default: 1.
        q (str | Unset):
        sort (str | Unset):  Example: name asc.
        status (list[GetEmployeesStatusItem] | Unset):
        rehire_flag (bool | Unset):
        eligible_for_rehire (bool | Unset):
        is_shared_employee (bool | Unset):
        work_mode (list[str] | Unset):
        company (list[str] | Unset):
        department (list[str] | Unset):
        position (list[str] | Unset):
        site (list[str] | Unset):
        employment_type (list[str] | Unset):
        job_title (list[str] | Unset):
        date_of_hire_from (datetime.date | Unset):  Example: 2024-01-01.
        date_of_hire_to (datetime.date | Unset):  Example: 2124-12-31.
        date_of_termination_from (datetime.date | Unset):  Example: 2024-01-01.
        date_of_termination_to (datetime.date | Unset):  Example: 2124-12-31.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | GetEmployeesResponse200]
    """

    kwargs = _get_kwargs(
        items_per_page=items_per_page,
        page=page,
        q=q,
        sort=sort,
        status=status,
        rehire_flag=rehire_flag,
        eligible_for_rehire=eligible_for_rehire,
        is_shared_employee=is_shared_employee,
        work_mode=work_mode,
        company=company,
        department=department,
        position=position,
        site=site,
        employment_type=employment_type,
        job_title=job_title,
        date_of_hire_from=date_of_hire_from,
        date_of_hire_to=date_of_hire_to,
        date_of_termination_from=date_of_termination_from,
        date_of_termination_to=date_of_termination_to,
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
    status: list[GetEmployeesStatusItem] | Unset = UNSET,
    rehire_flag: bool | Unset = UNSET,
    eligible_for_rehire: bool | Unset = UNSET,
    is_shared_employee: bool | Unset = UNSET,
    work_mode: list[str] | Unset = UNSET,
    company: list[str] | Unset = UNSET,
    department: list[str] | Unset = UNSET,
    position: list[str] | Unset = UNSET,
    site: list[str] | Unset = UNSET,
    employment_type: list[str] | Unset = UNSET,
    job_title: list[str] | Unset = UNSET,
    date_of_hire_from: datetime.date | Unset = UNSET,
    date_of_hire_to: datetime.date | Unset = UNSET,
    date_of_termination_from: datetime.date | Unset = UNSET,
    date_of_termination_to: datetime.date | Unset = UNSET,
) -> Any | GetEmployeesResponse200 | None:
    """Retrieve a paginated list of employees

     Fetches a paginated list of employees from the database. Supports filtering, sorting, and pagination
    through query parameters.

    Args:
        items_per_page (str | Unset):  Example: 10.
        page (int | Unset):  Default: 1.
        q (str | Unset):
        sort (str | Unset):  Example: name asc.
        status (list[GetEmployeesStatusItem] | Unset):
        rehire_flag (bool | Unset):
        eligible_for_rehire (bool | Unset):
        is_shared_employee (bool | Unset):
        work_mode (list[str] | Unset):
        company (list[str] | Unset):
        department (list[str] | Unset):
        position (list[str] | Unset):
        site (list[str] | Unset):
        employment_type (list[str] | Unset):
        job_title (list[str] | Unset):
        date_of_hire_from (datetime.date | Unset):  Example: 2024-01-01.
        date_of_hire_to (datetime.date | Unset):  Example: 2124-12-31.
        date_of_termination_from (datetime.date | Unset):  Example: 2024-01-01.
        date_of_termination_to (datetime.date | Unset):  Example: 2124-12-31.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | GetEmployeesResponse200
    """

    return sync_detailed(
        client=client,
        items_per_page=items_per_page,
        page=page,
        q=q,
        sort=sort,
        status=status,
        rehire_flag=rehire_flag,
        eligible_for_rehire=eligible_for_rehire,
        is_shared_employee=is_shared_employee,
        work_mode=work_mode,
        company=company,
        department=department,
        position=position,
        site=site,
        employment_type=employment_type,
        job_title=job_title,
        date_of_hire_from=date_of_hire_from,
        date_of_hire_to=date_of_hire_to,
        date_of_termination_from=date_of_termination_from,
        date_of_termination_to=date_of_termination_to,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient | Client,
    items_per_page: str | Unset = UNSET,
    page: int | Unset = 1,
    q: str | Unset = UNSET,
    sort: str | Unset = UNSET,
    status: list[GetEmployeesStatusItem] | Unset = UNSET,
    rehire_flag: bool | Unset = UNSET,
    eligible_for_rehire: bool | Unset = UNSET,
    is_shared_employee: bool | Unset = UNSET,
    work_mode: list[str] | Unset = UNSET,
    company: list[str] | Unset = UNSET,
    department: list[str] | Unset = UNSET,
    position: list[str] | Unset = UNSET,
    site: list[str] | Unset = UNSET,
    employment_type: list[str] | Unset = UNSET,
    job_title: list[str] | Unset = UNSET,
    date_of_hire_from: datetime.date | Unset = UNSET,
    date_of_hire_to: datetime.date | Unset = UNSET,
    date_of_termination_from: datetime.date | Unset = UNSET,
    date_of_termination_to: datetime.date | Unset = UNSET,
) -> Response[Any | GetEmployeesResponse200]:
    """Retrieve a paginated list of employees

     Fetches a paginated list of employees from the database. Supports filtering, sorting, and pagination
    through query parameters.

    Args:
        items_per_page (str | Unset):  Example: 10.
        page (int | Unset):  Default: 1.
        q (str | Unset):
        sort (str | Unset):  Example: name asc.
        status (list[GetEmployeesStatusItem] | Unset):
        rehire_flag (bool | Unset):
        eligible_for_rehire (bool | Unset):
        is_shared_employee (bool | Unset):
        work_mode (list[str] | Unset):
        company (list[str] | Unset):
        department (list[str] | Unset):
        position (list[str] | Unset):
        site (list[str] | Unset):
        employment_type (list[str] | Unset):
        job_title (list[str] | Unset):
        date_of_hire_from (datetime.date | Unset):  Example: 2024-01-01.
        date_of_hire_to (datetime.date | Unset):  Example: 2124-12-31.
        date_of_termination_from (datetime.date | Unset):  Example: 2024-01-01.
        date_of_termination_to (datetime.date | Unset):  Example: 2124-12-31.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | GetEmployeesResponse200]
    """

    kwargs = _get_kwargs(
        items_per_page=items_per_page,
        page=page,
        q=q,
        sort=sort,
        status=status,
        rehire_flag=rehire_flag,
        eligible_for_rehire=eligible_for_rehire,
        is_shared_employee=is_shared_employee,
        work_mode=work_mode,
        company=company,
        department=department,
        position=position,
        site=site,
        employment_type=employment_type,
        job_title=job_title,
        date_of_hire_from=date_of_hire_from,
        date_of_hire_to=date_of_hire_to,
        date_of_termination_from=date_of_termination_from,
        date_of_termination_to=date_of_termination_to,
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
    status: list[GetEmployeesStatusItem] | Unset = UNSET,
    rehire_flag: bool | Unset = UNSET,
    eligible_for_rehire: bool | Unset = UNSET,
    is_shared_employee: bool | Unset = UNSET,
    work_mode: list[str] | Unset = UNSET,
    company: list[str] | Unset = UNSET,
    department: list[str] | Unset = UNSET,
    position: list[str] | Unset = UNSET,
    site: list[str] | Unset = UNSET,
    employment_type: list[str] | Unset = UNSET,
    job_title: list[str] | Unset = UNSET,
    date_of_hire_from: datetime.date | Unset = UNSET,
    date_of_hire_to: datetime.date | Unset = UNSET,
    date_of_termination_from: datetime.date | Unset = UNSET,
    date_of_termination_to: datetime.date | Unset = UNSET,
) -> Any | GetEmployeesResponse200 | None:
    """Retrieve a paginated list of employees

     Fetches a paginated list of employees from the database. Supports filtering, sorting, and pagination
    through query parameters.

    Args:
        items_per_page (str | Unset):  Example: 10.
        page (int | Unset):  Default: 1.
        q (str | Unset):
        sort (str | Unset):  Example: name asc.
        status (list[GetEmployeesStatusItem] | Unset):
        rehire_flag (bool | Unset):
        eligible_for_rehire (bool | Unset):
        is_shared_employee (bool | Unset):
        work_mode (list[str] | Unset):
        company (list[str] | Unset):
        department (list[str] | Unset):
        position (list[str] | Unset):
        site (list[str] | Unset):
        employment_type (list[str] | Unset):
        job_title (list[str] | Unset):
        date_of_hire_from (datetime.date | Unset):  Example: 2024-01-01.
        date_of_hire_to (datetime.date | Unset):  Example: 2124-12-31.
        date_of_termination_from (datetime.date | Unset):  Example: 2024-01-01.
        date_of_termination_to (datetime.date | Unset):  Example: 2124-12-31.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | GetEmployeesResponse200
    """

    return (
        await asyncio_detailed(
            client=client,
            items_per_page=items_per_page,
            page=page,
            q=q,
            sort=sort,
            status=status,
            rehire_flag=rehire_flag,
            eligible_for_rehire=eligible_for_rehire,
            is_shared_employee=is_shared_employee,
            work_mode=work_mode,
            company=company,
            department=department,
            position=position,
            site=site,
            employment_type=employment_type,
            job_title=job_title,
            date_of_hire_from=date_of_hire_from,
            date_of_hire_to=date_of_hire_to,
            date_of_termination_from=date_of_termination_from,
            date_of_termination_to=date_of_termination_to,
        )
    ).parsed

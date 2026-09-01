from __future__ import annotations
import logging
from typing import Any
from uuid import UUID

import httpx

from framework.common.api.config import ApiConfig
from framework.common.env.env import get_environment
from framework.common.env.users import User

from framework.employee_mgmt.generated.api import *
from framework.employee_mgmt.generated.models import *
from framework.employee_mgmt.generated.client import Client
from framework.employee_mgmt.generated.types import UNSET, Unset


def _opt(value: Any) -> Any | Unset:
    return UNSET if value is None or value == "" else value


class EmployeeMgmtApi:
    """Thin wrapper around the generated Employee Management OpenAPI client."""

    def __init__(self, user: User, *, timeout: float = 10.0) -> None:
        self.user = user
        self.env = get_environment()
        config = ApiConfig(
            base_url=self.env.urls.get_employee_mgmt_base_url(),
            user=user,
            timeout=int(timeout),
        )
        self._client = Client(
            base_url=config.base_url,
            headers={},
            timeout=httpx.Timeout(timeout),
            raise_on_unexpected_status=True,
        )

    def close(self) -> None:
        self._client.get_httpx_client().close()

    def __enter__(self) -> EmployeeMgmtApi:
        self._client.__enter__()
        return self

    def __exit__(self, *args: object) -> None:
        self._client.__exit__(*args)

    def auth_login(self, user: User | None = None, expect_error: bool = False) -> Any:
        login_user = user or self.user

        logging.info(f"Logging into EmployeeMgmtApi for user: {login_user.email}")
        body = LoginBody(email=login_user.email, password=login_user.password)
        response = auth_login_api.sync(client=self._client, body=body)

        return self._validate_response(response, LoginSuccessResponse, expect_error)

    def get_companies(
        self,
        items_per_page: int | str = 10,
        page: int = 1,
        q: str = "",
        sort: str = "",
        company_id: UUID | None = None,
        expect_error: bool = False,
    ) -> Any:
        logging.info(
            f"Getting companies with items_per_page: {items_per_page}, company_id: {company_id}"
        )
        response = get_companies_api.sync(
            client=self._client,
            items_per_page=str(items_per_page),
            page=page,
            q=_opt(q),
            sort=_opt(sort),
            company_id=_opt(company_id),
        )
        return self._validate_response(response, GetCompaniesResponse200, expect_error)

    def get_company_departments(
        self,
        company_id: UUID,
        *,
        items_per_page: int | str = 10,
        sort: str = "name asc",
        expect_error: bool = False,
    ) -> Any:
        logging.info(f"Getting company departments with company_id: {company_id}")
        response = get_company_departments_api.sync(
            company_id,
            client=self._client,
            items_per_page=str(items_per_page),
            sort=_opt(sort),
        )
        return self._validate_response(
            response, Field29274C00D46E2D6B2918Ec8D7Eb706EfResponse200, expect_error
        )

    def get_company_positions(
        self,
        company_id: UUID,
        *,
        company_department_id: int | None = None,
        items_per_page: int | str = 10,
        page: int = 1,
        sort: str = "name asc",
        expect_error: bool = False,
    ) -> Any:
        logging.info(
            f"Getting company positions with company_id: {company_id}, company_department_id: {company_department_id}"
        )
        response = get_company_positions_api.sync(
            company_id,
            client=self._client,
            company_department_id=_opt(company_department_id),
            items_per_page=str(items_per_page),
            page=page,
            sort=_opt(sort),
        )
        return self._validate_response(
            response, C13Eb606Ef7Aa3E15Ff1593217D3D973Response200, expect_error
        )

    def get_company_sites(
        self,
        company_id: UUID,
        *,
        page: int = 1,
        items_per_page: int | str = 10,
        all_items: bool | None = None,
        expect_error: bool = False,
    ) -> Any:
        logging.info(f"Getting company sites with company_id: {company_id}, all_items: {all_items}")
        response = get_company_sites_api.sync(
            company_id,
            client=self._client,
            page=page,
            items_per_page=str(items_per_page),
            all_=_opt(all_items),
        )
        return self._validate_response(response, GetCompanySitesResponse200, expect_error)

    def get_employees(
        self,
        *,
        items_per_page: int | str = 10,
        page: int = 1,
        q: str = "",
        sort: str = "",
        expect_error: bool = False,
    ) -> Any:
        logging.info(
            f"Getting employees with items_per_page: {items_per_page}, page: {page}, q: {q}, sort: {sort}"
        )
        response = get_employees_api.sync(
            client=self._client,
            items_per_page=str(items_per_page),
            page=page,
            q=_opt(q),
            sort=_opt(sort),
        )
        return self._validate_response(response, GetEmployeesResponse200, expect_error)

    def get_employee_details_by_id(self, employee_id: UUID, expect_error: bool = False) -> Any:
        logging.info(f"Getting employee details by id: {employee_id}")
        response = get_employee_api.sync(employee_id, client=self._client)
        return self._validate_response(response, GetEmployeeResponse200, expect_error)

    def create_employee(self, body: EmployeeCreateRequest, expect_error: bool = False) -> Any:
        logging.info(
            f"Creating employee: {body.first_name} {body.last_name} with email: {body.primary_email}"
        )
        detailed = create_employee_api.sync_detailed(client=self._client, body=body)
        response = detailed.parsed
        if not expect_error and response is None:
            raise Exception(
                f"create_employee failed with HTTP {detailed.status_code}: "
                f"{detailed.content.decode() if detailed.content else 'empty response'}"
            )
        return self._validate_response(response, CreateEmployeeResponse201, expect_error)

    def update_employee_details(
        self, employee_id: UUID, body: EmployeeUpdateRequest, expect_error: bool = False
    ) -> Any:
        logging.info(
            f"Updating employee: {body.first_name} {body.last_name} with email: {body.primary_email}"
        )
        response = update_employee_api.sync(employee_id, client=self._client, body=body)
        return self._validate_response(response, UpdateEmployeeResponse200, expect_error)

    def get_global_options(self, expect_error: bool = False) -> Any:
        logging.info("Getting global options")
        response = get_global_options_api.sync(client=self._client)
        return self._validate_response(
            response, Field1F79D1Bd647Dac8D72Ac267A8F4242AbResponse200, expect_error
        )

    def _validate_response(
        self, response: Any, expected_response_class: type[Any], expect_error: bool = False
    ) -> Any:
        if not expect_error and not isinstance(response, expected_response_class):
            raise Exception(
                f"Expected {expected_response_class.__name__}, got {response.__class__.__name__}"
            )
        return response

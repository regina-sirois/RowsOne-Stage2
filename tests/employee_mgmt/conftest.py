# Fixture module for tests of the Employee Management Service at RowsOne
import pytest
from collections.abc import Generator
from typing import Any
from framework import User
from framework import Environment
from framework import EmployeeMgmtApi
from framework import Company


@pytest.fixture(scope="session")
def api_user(environment: Environment) -> Generator[User, Any, None]:
    try:
        user = environment.users.get_sdet_user()
    except ValueError as exc:
        raise ValueError("User not found") from exc

    yield user


@pytest.fixture(scope="session")
def api_client(api_user: User) -> Generator[EmployeeMgmtApi, Any, None]:
    api_client = EmployeeMgmtApi(api_user)
    api_client.auth_login(expect_error=False)

    yield api_client

    api_client.close()


@pytest.fixture(scope="module")
def companies(api_client: EmployeeMgmtApi) -> Generator[list[Company], Any, None]:
    companies_response = api_client.get_companies(expect_error=False)
    if companies_response.data.items is None:
        raise Exception("No companies found")

    companies = []
    for c in companies_response.data.items:
        company_id = c.id

        company_positions_response = api_client.get_company_positions(company_id)
        if company_positions_response.data.items is None:
            raise Exception("No company positions found")
        position_ids = [p.id for p in company_positions_response.data.items]
        company_sites_response = api_client.get_company_sites(company_id)
        if company_sites_response.data.items is None:
            raise Exception("No company sites found")
        site_ids = [s.id for s in company_sites_response.data.items]
        company_departments_response = api_client.get_company_departments(company_id)
        if company_departments_response.data.items is None:
            raise Exception("No company departments found")
        department_ids = [d.id for d in company_departments_response.data.items]

        companies.append(
            Company(
                id=c.id,
                name=c.name,
                department_ids=department_ids,
                position_ids=position_ids,
                site_ids=site_ids,
            )
        )

    yield companies

# Tests for the Employees API of the RowsOne Employee Management Service
import pytest
import logging
from typing import Generator, Any
from framework import EmployeeMgmtApi, make_employee_requests
from framework.employee_mgmt.generated.models import EmployeeCreateRequest

NUMBER_OF_EMPLOYEES = 10


@pytest.fixture(scope="module")
def created_employees(
    api_client: EmployeeMgmtApi,
) -> Generator[list[EmployeeCreateRequest], Any, Any]:

    employee_requests = make_employee_requests(number_to_make=NUMBER_OF_EMPLOYEES)
    created_employees = []

    for request in employee_requests:
        response = api_client.create_employee(request, expect_error=False)
        created_employees.append(response.data)
    logging.info(f"Created {len(created_employees)} employees")

    yield created_employees


@pytest.mark.employee_mgmt
def test_get_employees(api_client: EmployeeMgmtApi, created_employees: list[EmployeeCreateRequest]):
    employees_response = api_client.get_employees()
    assert len(employees_response.data) >= NUMBER_OF_EMPLOYEES

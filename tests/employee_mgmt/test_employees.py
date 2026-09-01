# Tests for the Employees API of the RowsOne Employee Management Service
import pytest
import logging
from typing import Generator, Any
from framework import EmployeeMgmtApi, make_employee_requests
from framework.employee_mgmt.generated.models import EmployeeCreateRequest


@pytest.fixture(scope="module")
def created_employees(api_client: EmployeeMgmtApi) -> Generator[list[EmployeeCreateRequest], Any, Any]:
    employees = make_employee_requests(number_to_make=10)
    for employee in employees:
        api_client.create_employee(employee, expect_error=False)
    yield employees


@pytest.mark.employee_mgmt
def test_get_employees(api_client: EmployeeMgmtApi, created_employees: list[EmployeeCreateRequest]):
    employees_response = api_client.get_employees()
    assert len(created_employees) >= 10
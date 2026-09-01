# Tests for the Employees API of the RowsOne Employee Management Service
import pytest
import logging
import time
from typing import Generator, Any
from framework import (
    EmployeeMgmtApi,
    make_employee_requests,
    make_employee_update_requests,
    Company,
)
from framework.employee_mgmt.generated.models import (
    Employee,
)

NUMBER_OF_EMPLOYEES = 10


@pytest.fixture(scope="module")
def created_employees(
    api_client: EmployeeMgmtApi,
    companies: list[Company],
) -> Generator[list[Employee], Any, Any]:

    employees_response = api_client.get_employees()
    employees = employees_response.data.items
    logging.info(f"Found {len(employees)} existing employees in the database")
    if (
        employees is None or len(employees) <= NUMBER_OF_EMPLOYEES
    ):  # Don't create employees if we already have them.
        created_employees = []
        for company in companies:
            employee_requests = make_employee_requests(company, number_to_make=NUMBER_OF_EMPLOYEES)
            for request in employee_requests:
                response = api_client.create_employee(request, expect_error=False)
                created_employees.append(response.data)
    else:
        created_employees = employees
    yield created_employees

    # TODO: Delete employees when API supports it.


@pytest.mark.api
@pytest.mark.employee_mgmt
def test_get_employees(api_client: EmployeeMgmtApi, created_employees: list[Employee]):
    employees_response = api_client.get_employees()
    employees = employees_response.data.items

    assert len(employees) >= NUMBER_OF_EMPLOYEES, (
        f"Expected {NUMBER_OF_EMPLOYEES} employees, got {len(employees)}"
    )


@pytest.mark.api
@pytest.mark.employee_mgmt
def test_get_employee_details_by_id(api_client: EmployeeMgmtApi, created_employees: list[Employee]):
    for expected in created_employees:
        employee_response = api_client.get_employee_details_by_id(expected.id)
        received = employee_response.data

        assert expected.id == received.id, f"Expected {expected.id}, got {received.id}"
        assert expected.first_name == received.first_name, (
            f"Expected {expected.first_name}, got {received.first_name}"
        )
        assert expected.last_name == received.last_name, (
            f"Expected {expected.last_name}, got {received.last_name}"
        )
        assert expected.email == received.email, f"Expected {expected.email}, got {received.email}"


@pytest.mark.api
@pytest.mark.employee_mgmt
def test_create_employee(api_client: EmployeeMgmtApi, companies: list[Company]):
    for company in companies:
        requested = make_employee_requests(company, number_to_make=1)[0]
        employee_response = api_client.create_employee(requested)
        received = employee_response.data

        assert requested.first_name == received.first_name, (
            f"Expected {requested.first_name}, got {received.first_name}"
        )
        assert requested.last_name == received.last_name, (
            f"Expected {requested.last_name}, got {received.last_name}"
        )


@pytest.mark.api
@pytest.mark.employee_mgmt
def test_update_employee(api_client: EmployeeMgmtApi, created_employees: list[Employee]):
    for employee in created_employees:
        updated = make_employee_update_requests(employee)
        employee_response = api_client.update_employee_details(employee.id, updated)
        received = employee_response.data

        assert updated.first_name == received.first_name, (
            f"Expected {updated.first_name}, got {received.first_name}"
        )
        assert updated.last_name == received.last_name, (
            f"Expected {updated.last_name}, got {received.last_name}"
        )
        assert updated.primary_email == received.primary_email, (
            f"Expected {updated.primary_email}, got {received.primary_email}"
        )
        assert updated.phone_numbers == received.phone_numbers, (
            f"Expected {updated.phone_numbers}, got {received.phone_numbers}"
        )


@pytest.mark.api
@pytest.mark.employee_mgmt
def test_update_employee_is_idempotent(
    api_client: EmployeeMgmtApi, created_employees: list[Employee]
):

    employee = created_employees[0]
    updated = make_employee_update_requests(employee)

    logging.info(f"Updating employee {employee.id} 3 times to ensure idempotency")
    for _ in range(3):
        employee_response = api_client.update_employee_details(employee.id, updated)
        received = employee_response.data

        assert updated.first_name == received.first_name, (
            f"Expected {updated.first_name}, got {received.first_name}"
        )
        assert updated.phone_numbers == received.phone_numbers, (
            f"Expected {updated.primary_email}, got {received.primary_email}"
        )
        time.sleep(1)  # Wait 1 second to ensure the update is completed.

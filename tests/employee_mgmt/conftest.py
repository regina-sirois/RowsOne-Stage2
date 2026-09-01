# Fixture module for tests of the Employee Management Service at RowsOne
import pytest
from collections.abc import Generator
from typing import Any
from framework import User
from framework import Environment
from framework import EmployeeMgmtApi


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

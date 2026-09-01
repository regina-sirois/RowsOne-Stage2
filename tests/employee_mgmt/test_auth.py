# Tests for the Authentication API of the RowsOne platform
import pytest
from framework import User
from framework import EmployeeMgmtApi
from framework.employee_mgmt.generated.models import LoginResponse401, LoginResponse422


@pytest.mark.parametrize("email, password, expected_response", [
    ("gsirois@pm.me", "RowsOne123!", LoginResponse401),
    ("invalid@example.com", "invalidpassword", LoginResponse401),
    ("sdet@a1b2c3d4.rows-challenge.test", None, LoginResponse422),
])
def test_login_negative(email, password, expected_response):
    user = User(email=email, password=password, client_id='', client_secret='')
    api_client = EmployeeMgmtApi(user)
    response = api_client.auth_login(expect_error=True)
    assert isinstance(response, expected_response)
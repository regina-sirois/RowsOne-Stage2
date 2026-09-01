"""Contains methods for accessing the API"""
from framework.employee_mgmt.generated.api.auth import login as auth_login_api
from framework.employee_mgmt.generated.api.companies import get_companies as get_companies_api
# TODO: Create defect for this API name.
from framework.employee_mgmt.generated.api.company_departments import (
    field_29274c00d46e2d6b2918ec8d7eb706ef as get_company_departments_api,
)
# TODO: Create defect for this API name.
from framework.employee_mgmt.generated.api.company_positions import (
    c13eb606ef7aa3e15ff1593217d3d973 as get_company_positions_api,
)
from framework.employee_mgmt.generated.api.company_sites import (
    get_company_sites as get_company_sites_api,
)
from framework.employee_mgmt.generated.api.employees import create_employee as create_employee_api
from framework.employee_mgmt.generated.api.employees import get_employee as get_employee_api
from framework.employee_mgmt.generated.api.employees import get_employees as get_employees_api
from framework.employee_mgmt.generated.api.employees import update_employee as update_employee_api
from framework.employee_mgmt.generated.api.global_options import (
    field_1f79d1bd647dac8d72ac267a8f4242ab as get_global_options_api,
)
__all__ = [
    "auth_login_api",
    "get_companies_api",
    "get_company_departments_api",
    "get_company_positions_api",
    "get_company_sites_api",
    "create_employee_api",
    "get_employee_api",
    "get_employees_api",
    "update_employee_api",
    "get_global_options_api",
]
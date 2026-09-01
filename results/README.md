# RowsOne-Stage2

## Testing results, issues found

Click [here](results/integration.html) for an HTML test report of integration tests, and [here](results/unit.html) for unitttests.

The following issues were found and observations were made in the course of this testing:

### Naming

Swagger endpoints with names that should be fixed:


| Endpoint                   | Expected Name                                              |
| -------------------------- | --------------------------------------------------------- |
| `TEST_ENV`                 | Target environment: `dev` (default), `staging`, or `prod` |
| `SDET_EMAIL_<ENV>`         | SDET user email for that env (e.g. `SDET_EMAIL_DEV`)      |
| `SDET_PASSWORD_<ENV>`      | SDET user password                                        |
| `SDET_CLIENT_ID_<ENV>`     | Optional Passport OAuth client id                         |
| `SDET_CLIENT_SECRET_<ENV>` | Optional Passport OAuth client secret                     |




### Misc issues

**create_employee**: Creating an employee was hard.

The [generated parser](framework/employee_mgmt/generated/api/employees/create_employee.py) for the create_employee endpoint explicitly maps response_422 to a NoneType (ln 40-42), which caused me to pull my hair out trying to figure out why my create employee requests were going nowhere.

The address state values of MP (Northern Mariana Islands) and FM (Federated States of Micronesia) were flagged as invalid. A workaround exists in the employee requests helper.

**CompanyPositionResource.from_dict() and PhoneNumberResource.from_dict()**

Both of these generated model methods were casting company_id (already passed as a UUID) to a UUID (ln 249), which was causing the following attribute error:

self = <[AttributeError("'UUID' object has no attribute 'int'") raised in repr()] UUID object at 0x1046d3010>, hex = 1, bytes = None
bytes_le = None, fields = None, int = None, version = None, is_safe = <SafeUUID.unknown: None>

In both cases, I replaced the following in the generated code and left a # TODO comment:
        else:
            id = UUID(_id)
with:
        else:
            if isinstance(_id, str):
                id = UUID(_id)
            else:
                id = _id

**questions I have**

In some cases, API values that look like they should be int are strings, for example:

       "pbj_code": {
          "id": "9ec0478a-3595-4774-92db-272dfa2a9362",
          "code": "7",
          "position": "Registered Nurse (RN)",
          "description": "Licensed registered nurses providing direct care."
        },
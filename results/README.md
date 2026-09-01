# RowsOne-Stage2

## Testing results, issues found

Click <a href="integration.html" target="_blank" rel="noopener noreferrer">here</a> for an HTML test report of integration tests, and <a href="unit.html" target="_blank" rel="noopener noreferrer">here</a> for unit tests.

The following issues were found and observations were made in the course of this testing:

### Naming issues in generated code

Swagger endpoints with names that should be fixed:


| Endpoint                   | Expected Name                                             |
| -------------------------- | --------------------------------------------------------- |
| `field_29274c00d46e2d6b2918ec8d7eb706ef`   | get_company_departments_api               |
| `c13eb606ef7aa3e15ff1593217d3d973`         | get_company_positions_api                 |
| `field_1f79d1bd647dac8d72ac267a8f4242ab`   | get_global_options_api                    |

In the swagger, it appears that these are "operation id"s on the endpoint. This issue had 
a negative impact on some of the models as well.


### Misc issues

**create_employee**: Creating an employee was hard.

The [generated parser](framework/employee_mgmt/generated/api/employees/create_employee.py) for the create_employee endpoint explicitly maps response_422 to a NoneType (ln 40-42), which caused me to pull my hair out trying to figure out why my create employee requests were going nowhere.

The address state values of MP (Northern Mariana Islands) and FM (Federated States of Micronesia) were flagged as invalid. A workaround exists in the employee requests helper.


**CompanyPositionResource.from_dict() and PhoneNumberResource.from_dict()**

Both of these generated model methods were casting `company_id` (already passed as a `UUID`) to a `UUID` (ln 249), which was causing the following attribute error:

```
self = <[AttributeError("'UUID' object has no attribute 'int'") raised in repr()] UUID object at 0x1046d3010>, hex = 1, bytes = None
bytes_le = None, fields = None, int = None, version = None, is_safe = <SafeUUID.unknown: None>
```

In both cases, I replaced the following in the generated code and left a `# TODO` comment:

```python
        else:
            id = UUID(_id)
```

with:

```python
        else:
            if isinstance(_id, str):
                id = UUID(_id)
            else:
                id = _id
```

I am not sure whether this is just a python swagger generation problem, or...not.


**Questions I have**

In some cases, API values that look like they should be int are strings, for example:

```json
"pbj_code": {
  "id": "9ec0478a-3595-4774-92db-272dfa2a9362",
  "code": "7",
  "position": "Registered Nurse (RN)",
  "description": "Licensed registered nurses providing direct care."
}
```
This seems suboptimal.
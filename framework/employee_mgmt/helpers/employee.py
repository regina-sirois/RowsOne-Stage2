import random
from framework.employee_mgmt.models.company import Company
from faker import Faker

from framework.employee_mgmt.generated.models import (
    Employee,
    EmployeeCreateRequest,
    EmployeeCreateRequestAddress,
    EmployeeCreateRequestPhoneNumbersType0Item,
    EmployeeCreateRequestPreferredLanguage,
    EmployeeUpdateRequest,
    EmployeeUpdateRequestPreferredLanguage,
    EmployeeUpdateRequestAddressType0,
)
from framework.employee_mgmt.generated.models.employee_create_request_phone_numbers_type_0_item_type import (
    EmployeeCreateRequestPhoneNumbersType0ItemType,
)

_fake = Faker()
real_phone_numbers = [
    "+14185438090",
    "+15875302271",
    "+14047241937",
    "+14433071473",
    "+13294201792",
    "+17702126011",
]


def _make_phone_numbers() -> list[EmployeeCreateRequestPhoneNumbersType0Item]:
    return [
        EmployeeCreateRequestPhoneNumbersType0Item(
            phone_number=random.choice(real_phone_numbers),
            type_=random.choice(list(EmployeeCreateRequestPhoneNumbersType0ItemType)),
            is_primary=index == 0,
        )
        for index in range(2)
    ]


def make_employee_requests(
    company: Company, number_to_make: int = 10
) -> list[EmployeeCreateRequest]:
    state = _fake.state_abbr()
    # TODO: Remove this once the API is updated to support FM and MP, if ever.
    if state in ["FM", "MP"]:
        state = "CO"
    return [
        EmployeeCreateRequest(
            address=EmployeeCreateRequestAddress.from_dict(
                {
                    "address_line1": _fake.street_address(),
                    "address_line2": _fake.secondary_address(),
                    "city": _fake.city(),
                    "state": state,
                    "zip": _fake.zipcode(),
                    "country": "USA",
                }
            ),
            company_id=company.id,
            company_position_id=random.choice(company.position_ids),
            first_name=_fake.first_name(),
            middle_name=_fake.first_name(),
            last_name=_fake.last_name(),
            preferred_name=random.choice([_fake.first_name(), None]),
            preferred_language=random.choice(list(EmployeeCreateRequestPreferredLanguage)),
            prior_last_name=random.choice([_fake.last_name(), None]),
            ssn=_fake.ssn().replace("-", ""),
            primary_email=_fake.email(),
            emails=list({_fake.email() for _ in range(random.randint(1, 3))}),
            job_title=random.choice([_fake.job(), None]),
            location_type_id=random.randint(1, 3),
            company_site_ids=company.site_ids,
            phone_numbers=_make_phone_numbers(),
        )
        for _ in range(number_to_make)
    ]


def make_employee_update_requests(
    employee: Employee,
) -> EmployeeUpdateRequest:

    return EmployeeUpdateRequest(
        first_name=employee.first_name,
        middle_name=employee.middle_name,
        last_name=employee.last_name,
        preferred_name=employee.preferred_name,
        preferred_language=EmployeeUpdateRequestPreferredLanguage.EN,
        prior_last_name="Smith",
        ssn=employee.ssn,
        address=EmployeeUpdateRequestAddressType0.from_dict(
            {
                "address_line1": employee.address.address_line1 if employee.address else None,
                "address_line2": employee.address.address_line2 if employee.address else None,
                "city": employee.address.city if employee.address else None,
                "state": employee.address.state if employee.address else None,
                "zip": employee.address.zip_ if employee.address else None,
            }
        ),
        primary_email=employee.primary_email,
        phone_numbers=[],
    )

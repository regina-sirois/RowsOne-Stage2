from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast
from uuid import UUID

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.address_resource import AddressResource
    from ..models.employee_emails_item import EmployeeEmailsItem
    from ..models.employee_marked_ineligible_for_rehire_by_companies_item import (
        EmployeeMarkedIneligibleForRehireByCompaniesItem,
    )
    from ..models.employee_position import EmployeePosition
    from ..models.employee_profile_company import EmployeeProfileCompany
    from ..models.employee_secondary_emails_item import EmployeeSecondaryEmailsItem
    from ..models.phone_number_resource import PhoneNumberResource
    from ..models.user_emergency_contact_resource import UserEmergencyContactResource
    from ..models.user_resource import UserResource


T = TypeVar("T", bound="Employee")


@_attrs_define
class Employee:
    """Employee model representation for API responses (store, update, and show)

    Attributes:
        id (UUID):  Example: 550e8400-e29b-41d4-a716-446655440000.
        user (UserResource): User representation for API responses
        first_name (str):  Example: John.
        last_name (str):  Example: Doe.
        dob (datetime.date | None):  Example: 1990-01-01.
        gender (None | str):  Example: MALE.
        ethnicity (None | str):  Example: WHITE.
        badge_number (None | str | Unset): 7-digit numeric badge number for time clock identification Example: 0012345.
        middle_name (None | str | Unset):  Example: Michael.
        full_name (str | Unset):  Example: John Michael Doe.
        preferred_name (None | str | Unset):  Example: Johnny.
        preferred_language (None | str | Unset): Deprecated. Use user.preferred_language instead. Example: en.
        profile_picture_base64 (None | str | Unset): Base64 encoded profile picture
        ssn (str | Unset): Social Security Number. Masked (e.g. ***-**-6789) without VIEW_SOCIAL_SECURITY_NUMBER
            permission. Example: 123-45-6789.
        age (int | None | Unset):  Example: 33.
        address (AddressResource | Unset): Address resource
        email (None | str | Unset): Primary/login email. Masked without VIEW_USER_PERSONAL_PROFILE_PRIMARY_EMAIL.
            Example: john@example.com.
        primary_email (None | str | Unset): Deprecated. Use email instead. Retained for backwards compatibility until
            MVP. Example: john@example.com.
        secondary_emails (list[EmployeeSecondaryEmailsItem] | Unset): Additional (secondary) emails. Masked without
            VIEW_USER_PERSONAL_PROFILE_SECONDARY_EMAIL.
        emails (list[EmployeeEmailsItem] | Unset): Deprecated. Use secondary_emails instead. Retained for backwards
            compatibility until MVP.
        employment_type_id (None | Unset | UUID):  Example: 550e8400-e29b-41d4-a716-446655440000.
        employment_type (str | Unset):  Example: Full-time.
        pay_exception_category (None | str | Unset):  Example: no_benefits.
        eligible_for_rehire (bool | Unset):  Example: True.
        marked_ineligible_for_rehire_by_companies (list[EmployeeMarkedIneligibleForRehireByCompaniesItem] | Unset):
            Companies that have marked this employee ineligible for rehire
        allow_remote_punch (bool | Unset):  Example: False.
        geo_fence (bool | Unset):  Example: False.
        geo_fence_address_id (int | None | Unset):  Example: 42.
        geo_fence_radius_in_feet (int | Unset):  Example: 500.
        total_standard_hours_per_pay_period (None | str | Unset):  Example: 80.00.
        total_standard_days_per_pay_period (int | None | Unset):  Example: 10.
        years_of_service (int | None | Unset):  Example: 3.
        years_in_current_position (int | None | Unset):  Example: 2.
        is_shared (bool | Unset):  Example: False.
        is_shared_employee (bool | None | Unset):  Example: False.
        shared_company_names (list[str] | Unset): All companies the employee works for, regardless of the viewer's
            access scope (powers the Shared tooltip)
        is_pinned (bool | None | Unset): Whether the employee is pinned by the current user Example: False.
        notes_count (int | Unset): Number of notes associated with the employee Example: 3.
        employee_positions (list[EmployeePosition] | None | Unset):
        employee_companies (list[EmployeeProfileCompany] | Unset):
        emergency_contacts (list[UserEmergencyContactResource] | None | Unset):
        phone_numbers (list[PhoneNumberResource] | Unset): Employee's phone numbers
        created_at (datetime.datetime | Unset):  Example: 2025-01-01T00:00:00+00:00.
        updated_at (datetime.datetime | Unset):  Example: 2025-01-01T00:00:00+00:00.
    """

    id: UUID
    user: UserResource
    first_name: str
    last_name: str
    dob: datetime.date | None
    gender: None | str
    ethnicity: None | str
    badge_number: None | str | Unset = UNSET
    middle_name: None | str | Unset = UNSET
    full_name: str | Unset = UNSET
    preferred_name: None | str | Unset = UNSET
    preferred_language: None | str | Unset = UNSET
    profile_picture_base64: None | str | Unset = UNSET
    ssn: str | Unset = UNSET
    age: int | None | Unset = UNSET
    address: AddressResource | Unset = UNSET
    email: None | str | Unset = UNSET
    primary_email: None | str | Unset = UNSET
    secondary_emails: list[EmployeeSecondaryEmailsItem] | Unset = UNSET
    emails: list[EmployeeEmailsItem] | Unset = UNSET
    employment_type_id: None | Unset | UUID = UNSET
    employment_type: str | Unset = UNSET
    pay_exception_category: None | str | Unset = UNSET
    eligible_for_rehire: bool | Unset = UNSET
    marked_ineligible_for_rehire_by_companies: list[EmployeeMarkedIneligibleForRehireByCompaniesItem] | Unset = UNSET
    allow_remote_punch: bool | Unset = UNSET
    geo_fence: bool | Unset = UNSET
    geo_fence_address_id: int | None | Unset = UNSET
    geo_fence_radius_in_feet: int | Unset = UNSET
    total_standard_hours_per_pay_period: None | str | Unset = UNSET
    total_standard_days_per_pay_period: int | None | Unset = UNSET
    years_of_service: int | None | Unset = UNSET
    years_in_current_position: int | None | Unset = UNSET
    is_shared: bool | Unset = UNSET
    is_shared_employee: bool | None | Unset = UNSET
    shared_company_names: list[str] | Unset = UNSET
    is_pinned: bool | None | Unset = UNSET
    notes_count: int | Unset = UNSET
    employee_positions: list[EmployeePosition] | None | Unset = UNSET
    employee_companies: list[EmployeeProfileCompany] | Unset = UNSET
    emergency_contacts: list[UserEmergencyContactResource] | None | Unset = UNSET
    phone_numbers: list[PhoneNumberResource] | Unset = UNSET
    created_at: datetime.datetime | Unset = UNSET
    updated_at: datetime.datetime | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id = str(self.id)

        user = self.user.to_dict()

        first_name = self.first_name

        last_name = self.last_name

        dob: None | str
        if isinstance(self.dob, datetime.date):
            dob = self.dob.isoformat()
        else:
            dob = self.dob

        gender: None | str
        gender = self.gender

        ethnicity: None | str
        ethnicity = self.ethnicity

        badge_number: None | str | Unset
        if isinstance(self.badge_number, Unset):
            badge_number = UNSET
        else:
            badge_number = self.badge_number

        middle_name: None | str | Unset
        if isinstance(self.middle_name, Unset):
            middle_name = UNSET
        else:
            middle_name = self.middle_name

        full_name = self.full_name

        preferred_name: None | str | Unset
        if isinstance(self.preferred_name, Unset):
            preferred_name = UNSET
        else:
            preferred_name = self.preferred_name

        preferred_language: None | str | Unset
        if isinstance(self.preferred_language, Unset):
            preferred_language = UNSET
        else:
            preferred_language = self.preferred_language

        profile_picture_base64: None | str | Unset
        if isinstance(self.profile_picture_base64, Unset):
            profile_picture_base64 = UNSET
        else:
            profile_picture_base64 = self.profile_picture_base64

        ssn = self.ssn

        age: int | None | Unset
        if isinstance(self.age, Unset):
            age = UNSET
        else:
            age = self.age

        address: dict[str, Any] | Unset = UNSET
        if not isinstance(self.address, Unset):
            address = self.address.to_dict()

        email: None | str | Unset
        if isinstance(self.email, Unset):
            email = UNSET
        else:
            email = self.email

        primary_email: None | str | Unset
        if isinstance(self.primary_email, Unset):
            primary_email = UNSET
        else:
            primary_email = self.primary_email

        secondary_emails: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.secondary_emails, Unset):
            secondary_emails = []
            for secondary_emails_item_data in self.secondary_emails:
                secondary_emails_item = secondary_emails_item_data.to_dict()
                secondary_emails.append(secondary_emails_item)

        emails: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.emails, Unset):
            emails = []
            for emails_item_data in self.emails:
                emails_item = emails_item_data.to_dict()
                emails.append(emails_item)

        employment_type_id: None | str | Unset
        if isinstance(self.employment_type_id, Unset):
            employment_type_id = UNSET
        elif isinstance(self.employment_type_id, UUID):
            employment_type_id = str(self.employment_type_id)
        else:
            employment_type_id = self.employment_type_id

        employment_type = self.employment_type

        pay_exception_category: None | str | Unset
        if isinstance(self.pay_exception_category, Unset):
            pay_exception_category = UNSET
        else:
            pay_exception_category = self.pay_exception_category

        eligible_for_rehire = self.eligible_for_rehire

        marked_ineligible_for_rehire_by_companies: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.marked_ineligible_for_rehire_by_companies, Unset):
            marked_ineligible_for_rehire_by_companies = []
            for marked_ineligible_for_rehire_by_companies_item_data in self.marked_ineligible_for_rehire_by_companies:
                marked_ineligible_for_rehire_by_companies_item = (
                    marked_ineligible_for_rehire_by_companies_item_data.to_dict()
                )
                marked_ineligible_for_rehire_by_companies.append(marked_ineligible_for_rehire_by_companies_item)

        allow_remote_punch = self.allow_remote_punch

        geo_fence = self.geo_fence

        geo_fence_address_id: int | None | Unset
        if isinstance(self.geo_fence_address_id, Unset):
            geo_fence_address_id = UNSET
        else:
            geo_fence_address_id = self.geo_fence_address_id

        geo_fence_radius_in_feet = self.geo_fence_radius_in_feet

        total_standard_hours_per_pay_period: None | str | Unset
        if isinstance(self.total_standard_hours_per_pay_period, Unset):
            total_standard_hours_per_pay_period = UNSET
        else:
            total_standard_hours_per_pay_period = self.total_standard_hours_per_pay_period

        total_standard_days_per_pay_period: int | None | Unset
        if isinstance(self.total_standard_days_per_pay_period, Unset):
            total_standard_days_per_pay_period = UNSET
        else:
            total_standard_days_per_pay_period = self.total_standard_days_per_pay_period

        years_of_service: int | None | Unset
        if isinstance(self.years_of_service, Unset):
            years_of_service = UNSET
        else:
            years_of_service = self.years_of_service

        years_in_current_position: int | None | Unset
        if isinstance(self.years_in_current_position, Unset):
            years_in_current_position = UNSET
        else:
            years_in_current_position = self.years_in_current_position

        is_shared = self.is_shared

        is_shared_employee: bool | None | Unset
        if isinstance(self.is_shared_employee, Unset):
            is_shared_employee = UNSET
        else:
            is_shared_employee = self.is_shared_employee

        shared_company_names: list[str] | Unset = UNSET
        if not isinstance(self.shared_company_names, Unset):
            shared_company_names = self.shared_company_names

        is_pinned: bool | None | Unset
        if isinstance(self.is_pinned, Unset):
            is_pinned = UNSET
        else:
            is_pinned = self.is_pinned

        notes_count = self.notes_count

        employee_positions: list[dict[str, Any]] | None | Unset
        if isinstance(self.employee_positions, Unset):
            employee_positions = UNSET
        elif isinstance(self.employee_positions, list):
            employee_positions = []
            for employee_positions_type_0_item_data in self.employee_positions:
                employee_positions_type_0_item = employee_positions_type_0_item_data.to_dict()
                employee_positions.append(employee_positions_type_0_item)

        else:
            employee_positions = self.employee_positions

        employee_companies: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.employee_companies, Unset):
            employee_companies = []
            for employee_companies_item_data in self.employee_companies:
                employee_companies_item = employee_companies_item_data.to_dict()
                employee_companies.append(employee_companies_item)

        emergency_contacts: list[dict[str, Any]] | None | Unset
        if isinstance(self.emergency_contacts, Unset):
            emergency_contacts = UNSET
        elif isinstance(self.emergency_contacts, list):
            emergency_contacts = []
            for emergency_contacts_type_0_item_data in self.emergency_contacts:
                emergency_contacts_type_0_item = emergency_contacts_type_0_item_data.to_dict()
                emergency_contacts.append(emergency_contacts_type_0_item)

        else:
            emergency_contacts = self.emergency_contacts

        phone_numbers: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.phone_numbers, Unset):
            phone_numbers = []
            for phone_numbers_item_data in self.phone_numbers:
                phone_numbers_item = phone_numbers_item_data.to_dict()
                phone_numbers.append(phone_numbers_item)

        created_at: str | Unset = UNSET
        if not isinstance(self.created_at, Unset):
            created_at = self.created_at.isoformat()

        updated_at: str | Unset = UNSET
        if not isinstance(self.updated_at, Unset):
            updated_at = self.updated_at.isoformat()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id": id,
                "user": user,
                "first_name": first_name,
                "last_name": last_name,
                "dob": dob,
                "gender": gender,
                "ethnicity": ethnicity,
            }
        )
        if badge_number is not UNSET:
            field_dict["badge_number"] = badge_number
        if middle_name is not UNSET:
            field_dict["middle_name"] = middle_name
        if full_name is not UNSET:
            field_dict["full_name"] = full_name
        if preferred_name is not UNSET:
            field_dict["preferred_name"] = preferred_name
        if preferred_language is not UNSET:
            field_dict["preferred_language"] = preferred_language
        if profile_picture_base64 is not UNSET:
            field_dict["profile_picture_base64"] = profile_picture_base64
        if ssn is not UNSET:
            field_dict["ssn"] = ssn
        if age is not UNSET:
            field_dict["age"] = age
        if address is not UNSET:
            field_dict["address"] = address
        if email is not UNSET:
            field_dict["email"] = email
        if primary_email is not UNSET:
            field_dict["primary_email"] = primary_email
        if secondary_emails is not UNSET:
            field_dict["secondary_emails"] = secondary_emails
        if emails is not UNSET:
            field_dict["emails"] = emails
        if employment_type_id is not UNSET:
            field_dict["employment_type_id"] = employment_type_id
        if employment_type is not UNSET:
            field_dict["employment_type"] = employment_type
        if pay_exception_category is not UNSET:
            field_dict["pay_exception_category"] = pay_exception_category
        if eligible_for_rehire is not UNSET:
            field_dict["eligible_for_rehire"] = eligible_for_rehire
        if marked_ineligible_for_rehire_by_companies is not UNSET:
            field_dict["marked_ineligible_for_rehire_by_companies"] = marked_ineligible_for_rehire_by_companies
        if allow_remote_punch is not UNSET:
            field_dict["allow_remote_punch"] = allow_remote_punch
        if geo_fence is not UNSET:
            field_dict["geo_fence"] = geo_fence
        if geo_fence_address_id is not UNSET:
            field_dict["geo_fence_address_id"] = geo_fence_address_id
        if geo_fence_radius_in_feet is not UNSET:
            field_dict["geo_fence_radius_in_feet"] = geo_fence_radius_in_feet
        if total_standard_hours_per_pay_period is not UNSET:
            field_dict["total_standard_hours_per_pay_period"] = total_standard_hours_per_pay_period
        if total_standard_days_per_pay_period is not UNSET:
            field_dict["total_standard_days_per_pay_period"] = total_standard_days_per_pay_period
        if years_of_service is not UNSET:
            field_dict["years_of_service"] = years_of_service
        if years_in_current_position is not UNSET:
            field_dict["years_in_current_position"] = years_in_current_position
        if is_shared is not UNSET:
            field_dict["is_shared"] = is_shared
        if is_shared_employee is not UNSET:
            field_dict["is_shared_employee"] = is_shared_employee
        if shared_company_names is not UNSET:
            field_dict["shared_company_names"] = shared_company_names
        if is_pinned is not UNSET:
            field_dict["is_pinned"] = is_pinned
        if notes_count is not UNSET:
            field_dict["notes_count"] = notes_count
        if employee_positions is not UNSET:
            field_dict["employee_positions"] = employee_positions
        if employee_companies is not UNSET:
            field_dict["employee_companies"] = employee_companies
        if emergency_contacts is not UNSET:
            field_dict["emergency_contacts"] = emergency_contacts
        if phone_numbers is not UNSET:
            field_dict["phone_numbers"] = phone_numbers
        if created_at is not UNSET:
            field_dict["created_at"] = created_at
        if updated_at is not UNSET:
            field_dict["updated_at"] = updated_at

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.address_resource import AddressResource  # noqa: PLC0415
        from ..models.employee_emails_item import EmployeeEmailsItem  # noqa: PLC0415
        from ..models.employee_marked_ineligible_for_rehire_by_companies_item import (
            EmployeeMarkedIneligibleForRehireByCompaniesItem,  # noqa: PLC0415
        )
        from ..models.employee_position import EmployeePosition  # noqa: PLC0415
        from ..models.employee_profile_company import EmployeeProfileCompany  # noqa: PLC0415
        from ..models.employee_secondary_emails_item import EmployeeSecondaryEmailsItem  # noqa: PLC0415
        from ..models.phone_number_resource import PhoneNumberResource  # noqa: PLC0415
        from ..models.user_emergency_contact_resource import UserEmergencyContactResource  # noqa: PLC0415
        from ..models.user_resource import UserResource  # noqa: PLC0415

        d = dict(src_dict)
        id = UUID(d.pop("id"))

        user = UserResource.from_dict(d.pop("user"))

        first_name = d.pop("first_name")

        last_name = d.pop("last_name")

        def _parse_dob(data: object) -> datetime.date | None:
            if data is None:
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                dob_type_0 = datetime.date.fromisoformat(data)

                return dob_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(datetime.date | None, data)

        dob = _parse_dob(d.pop("dob"))

        def _parse_gender(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        gender = _parse_gender(d.pop("gender"))

        def _parse_ethnicity(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        ethnicity = _parse_ethnicity(d.pop("ethnicity"))

        def _parse_badge_number(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        badge_number = _parse_badge_number(d.pop("badge_number", UNSET))

        def _parse_middle_name(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        middle_name = _parse_middle_name(d.pop("middle_name", UNSET))

        full_name = d.pop("full_name", UNSET)

        def _parse_preferred_name(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        preferred_name = _parse_preferred_name(d.pop("preferred_name", UNSET))

        def _parse_preferred_language(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        preferred_language = _parse_preferred_language(d.pop("preferred_language", UNSET))

        def _parse_profile_picture_base64(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        profile_picture_base64 = _parse_profile_picture_base64(d.pop("profile_picture_base64", UNSET))

        ssn = d.pop("ssn", UNSET)

        def _parse_age(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        age = _parse_age(d.pop("age", UNSET))

        _address = d.pop("address", UNSET)
        address: AddressResource | Unset
        if isinstance(_address, Unset):
            address = UNSET
        else:
            address = AddressResource.from_dict(_address)

        def _parse_email(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        email = _parse_email(d.pop("email", UNSET))

        def _parse_primary_email(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        primary_email = _parse_primary_email(d.pop("primary_email", UNSET))

        _secondary_emails = d.pop("secondary_emails", UNSET)
        secondary_emails: list[EmployeeSecondaryEmailsItem] | Unset = UNSET
        if _secondary_emails is not UNSET:
            secondary_emails = []
            for secondary_emails_item_data in _secondary_emails:
                secondary_emails_item = EmployeeSecondaryEmailsItem.from_dict(secondary_emails_item_data)

                secondary_emails.append(secondary_emails_item)

        _emails = d.pop("emails", UNSET)
        emails: list[EmployeeEmailsItem] | Unset = UNSET
        if _emails is not UNSET:
            emails = []
            for emails_item_data in _emails:
                emails_item = EmployeeEmailsItem.from_dict(emails_item_data)

                emails.append(emails_item)

        def _parse_employment_type_id(data: object) -> None | Unset | UUID:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                employment_type_id_type_0 = UUID(data)

                return employment_type_id_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(None | Unset | UUID, data)

        employment_type_id = _parse_employment_type_id(d.pop("employment_type_id", UNSET))

        employment_type = d.pop("employment_type", UNSET)

        def _parse_pay_exception_category(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        pay_exception_category = _parse_pay_exception_category(d.pop("pay_exception_category", UNSET))

        eligible_for_rehire = d.pop("eligible_for_rehire", UNSET)

        _marked_ineligible_for_rehire_by_companies = d.pop("marked_ineligible_for_rehire_by_companies", UNSET)
        marked_ineligible_for_rehire_by_companies: list[EmployeeMarkedIneligibleForRehireByCompaniesItem] | Unset = (
            UNSET
        )
        if _marked_ineligible_for_rehire_by_companies is not UNSET:
            marked_ineligible_for_rehire_by_companies = []
            for marked_ineligible_for_rehire_by_companies_item_data in _marked_ineligible_for_rehire_by_companies:
                marked_ineligible_for_rehire_by_companies_item = (
                    EmployeeMarkedIneligibleForRehireByCompaniesItem.from_dict(
                        marked_ineligible_for_rehire_by_companies_item_data
                    )
                )

                marked_ineligible_for_rehire_by_companies.append(marked_ineligible_for_rehire_by_companies_item)

        allow_remote_punch = d.pop("allow_remote_punch", UNSET)

        geo_fence = d.pop("geo_fence", UNSET)

        def _parse_geo_fence_address_id(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        geo_fence_address_id = _parse_geo_fence_address_id(d.pop("geo_fence_address_id", UNSET))

        geo_fence_radius_in_feet = d.pop("geo_fence_radius_in_feet", UNSET)

        def _parse_total_standard_hours_per_pay_period(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        total_standard_hours_per_pay_period = _parse_total_standard_hours_per_pay_period(
            d.pop("total_standard_hours_per_pay_period", UNSET)
        )

        def _parse_total_standard_days_per_pay_period(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        total_standard_days_per_pay_period = _parse_total_standard_days_per_pay_period(
            d.pop("total_standard_days_per_pay_period", UNSET)
        )

        def _parse_years_of_service(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        years_of_service = _parse_years_of_service(d.pop("years_of_service", UNSET))

        def _parse_years_in_current_position(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        years_in_current_position = _parse_years_in_current_position(d.pop("years_in_current_position", UNSET))

        is_shared = d.pop("is_shared", UNSET)

        def _parse_is_shared_employee(data: object) -> bool | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(bool | None | Unset, data)

        is_shared_employee = _parse_is_shared_employee(d.pop("is_shared_employee", UNSET))

        shared_company_names = cast(list[str], d.pop("shared_company_names", UNSET))

        def _parse_is_pinned(data: object) -> bool | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(bool | None | Unset, data)

        is_pinned = _parse_is_pinned(d.pop("is_pinned", UNSET))

        notes_count = d.pop("notes_count", UNSET)

        def _parse_employee_positions(data: object) -> list[EmployeePosition] | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                employee_positions_type_0 = []
                _employee_positions_type_0 = data
                for employee_positions_type_0_item_data in _employee_positions_type_0:
                    employee_positions_type_0_item = EmployeePosition.from_dict(employee_positions_type_0_item_data)

                    employee_positions_type_0.append(employee_positions_type_0_item)

                return employee_positions_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[EmployeePosition] | None | Unset, data)

        employee_positions = _parse_employee_positions(d.pop("employee_positions", UNSET))

        _employee_companies = d.pop("employee_companies", UNSET)
        employee_companies: list[EmployeeProfileCompany] | Unset = UNSET
        if _employee_companies is not UNSET:
            employee_companies = []
            for employee_companies_item_data in _employee_companies:
                employee_companies_item = EmployeeProfileCompany.from_dict(employee_companies_item_data)

                employee_companies.append(employee_companies_item)

        def _parse_emergency_contacts(data: object) -> list[UserEmergencyContactResource] | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                emergency_contacts_type_0 = []
                _emergency_contacts_type_0 = data
                for emergency_contacts_type_0_item_data in _emergency_contacts_type_0:
                    emergency_contacts_type_0_item = UserEmergencyContactResource.from_dict(
                        emergency_contacts_type_0_item_data
                    )

                    emergency_contacts_type_0.append(emergency_contacts_type_0_item)

                return emergency_contacts_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[UserEmergencyContactResource] | None | Unset, data)

        emergency_contacts = _parse_emergency_contacts(d.pop("emergency_contacts", UNSET))

        _phone_numbers = d.pop("phone_numbers", UNSET)
        phone_numbers: list[PhoneNumberResource] | Unset = UNSET
        if _phone_numbers is not UNSET:
            phone_numbers = []
            for phone_numbers_item_data in _phone_numbers:
                phone_numbers_item = PhoneNumberResource.from_dict(phone_numbers_item_data)

                phone_numbers.append(phone_numbers_item)

        _created_at = d.pop("created_at", UNSET)
        created_at: datetime.datetime | Unset
        if isinstance(_created_at, Unset):
            created_at = UNSET
        else:
            created_at = datetime.datetime.fromisoformat(_created_at)

        _updated_at = d.pop("updated_at", UNSET)
        updated_at: datetime.datetime | Unset
        if isinstance(_updated_at, Unset):
            updated_at = UNSET
        else:
            updated_at = datetime.datetime.fromisoformat(_updated_at)

        employee = cls(
            id=id,
            user=user,
            first_name=first_name,
            last_name=last_name,
            dob=dob,
            gender=gender,
            ethnicity=ethnicity,
            badge_number=badge_number,
            middle_name=middle_name,
            full_name=full_name,
            preferred_name=preferred_name,
            preferred_language=preferred_language,
            profile_picture_base64=profile_picture_base64,
            ssn=ssn,
            age=age,
            address=address,
            email=email,
            primary_email=primary_email,
            secondary_emails=secondary_emails,
            emails=emails,
            employment_type_id=employment_type_id,
            employment_type=employment_type,
            pay_exception_category=pay_exception_category,
            eligible_for_rehire=eligible_for_rehire,
            marked_ineligible_for_rehire_by_companies=marked_ineligible_for_rehire_by_companies,
            allow_remote_punch=allow_remote_punch,
            geo_fence=geo_fence,
            geo_fence_address_id=geo_fence_address_id,
            geo_fence_radius_in_feet=geo_fence_radius_in_feet,
            total_standard_hours_per_pay_period=total_standard_hours_per_pay_period,
            total_standard_days_per_pay_period=total_standard_days_per_pay_period,
            years_of_service=years_of_service,
            years_in_current_position=years_in_current_position,
            is_shared=is_shared,
            is_shared_employee=is_shared_employee,
            shared_company_names=shared_company_names,
            is_pinned=is_pinned,
            notes_count=notes_count,
            employee_positions=employee_positions,
            employee_companies=employee_companies,
            emergency_contacts=emergency_contacts,
            phone_numbers=phone_numbers,
            created_at=created_at,
            updated_at=updated_at,
        )

        employee.additional_properties = d
        return employee

    @property
    def additional_keys(self) -> list[str]:
        return list(self.additional_properties.keys())

    def __getitem__(self, key: str) -> Any:
        return self.additional_properties[key]

    def __setitem__(self, key: str, value: Any) -> None:
        self.additional_properties[key] = value

    def __delitem__(self, key: str) -> None:
        del self.additional_properties[key]

    def __contains__(self, key: str) -> bool:
        return key in self.additional_properties

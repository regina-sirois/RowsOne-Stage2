from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast
from uuid import UUID

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.employee_create_request_preferred_language import EmployeeCreateRequestPreferredLanguage
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.employee_create_request_address import EmployeeCreateRequestAddress
    from ..models.employee_create_request_phone_numbers_type_0_item import EmployeeCreateRequestPhoneNumbersType0Item


T = TypeVar("T", bound="EmployeeCreateRequest")


@_attrs_define
class EmployeeCreateRequest:
    """Request schema for creating a new employee with a primary position

    Attributes:
        address (EmployeeCreateRequestAddress):  Example: {'address_line1': '123 Main St', 'address_line2': 'Apt 4B',
            'city': 'Anytown', 'state': 'CA', 'zip': '12345', 'country': 'USA'}.
        company_id (UUID):  Example: 9a7b8c3d-1e2f-3a4b-5c6d-7e8f9a0b1c2d.
        company_position_id (int): Primary position - company position ID Example: 1.
        first_name (str | Unset): Required when user_id is not provided. Prohibited when user_id is provided. Example:
            John.
        middle_name (None | str | Unset): Prohibited when user_id is provided. Example: Michael.
        last_name (str | Unset): Required when user_id is not provided. Prohibited when user_id is provided. Example:
            Doe.
        preferred_name (None | str | Unset):  Example: Johnny.
        preferred_language (EmployeeCreateRequestPreferredLanguage | Unset): ISO 639-1 language code. English, Spanish,
            Chinese, Vietnamese, Tagalog, Korean, French, Arabic, Russian, Portuguese, or Other. Example: en.
        prior_last_name (None | str | Unset):  Example: Smith.
        ssn (None | str | Unset):  Example: 123456789.
        primary_email (str | Unset): Required when user_id is not provided. Prohibited when user_id is provided.
            Example: john.doe@example.com.
        emails (list[str] | None | Unset): Prohibited when user_id is provided.
        job_title (None | str | Unset):  Example: Software Engineer.
        location_type_id (int | Unset): Primary position - location type (OnSite, Hybrid, Remote). Optional — defaults
            to OnSite if omitted. Example: 1.
        company_site_ids (list[int] | Unset): Primary position - company sites. Optional — when omitted, authorization
            falls back to a company-level permission check.
        phone_numbers (list[EmployeeCreateRequestPhoneNumbersType0Item] | None | Unset): When user_id is provided:
            required (with exactly one primary) if the user has no primary phone number; prohibited if they already have
            one. When user_id is not provided: optional.
    """

    address: EmployeeCreateRequestAddress
    company_id: UUID
    company_position_id: int
    first_name: str | Unset = UNSET
    middle_name: None | str | Unset = UNSET
    last_name: str | Unset = UNSET
    preferred_name: None | str | Unset = UNSET
    preferred_language: EmployeeCreateRequestPreferredLanguage | Unset = UNSET
    prior_last_name: None | str | Unset = UNSET
    ssn: None | str | Unset = UNSET
    primary_email: str | Unset = UNSET
    emails: list[str] | None | Unset = UNSET
    job_title: None | str | Unset = UNSET
    location_type_id: int | Unset = UNSET
    company_site_ids: list[int] | Unset = UNSET
    phone_numbers: list[EmployeeCreateRequestPhoneNumbersType0Item] | None | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        address = self.address.to_dict()

        company_id = str(self.company_id)

        company_position_id = self.company_position_id

        first_name = self.first_name

        middle_name: None | str | Unset
        if isinstance(self.middle_name, Unset):
            middle_name = UNSET
        else:
            middle_name = self.middle_name

        last_name = self.last_name

        preferred_name: None | str | Unset
        if isinstance(self.preferred_name, Unset):
            preferred_name = UNSET
        else:
            preferred_name = self.preferred_name

        preferred_language: str | Unset = UNSET
        if not isinstance(self.preferred_language, Unset):
            preferred_language = self.preferred_language.value

        prior_last_name: None | str | Unset
        if isinstance(self.prior_last_name, Unset):
            prior_last_name = UNSET
        else:
            prior_last_name = self.prior_last_name

        ssn: None | str | Unset
        if isinstance(self.ssn, Unset):
            ssn = UNSET
        else:
            ssn = self.ssn

        primary_email = self.primary_email

        emails: list[str] | None | Unset
        if isinstance(self.emails, Unset):
            emails = UNSET
        elif isinstance(self.emails, list):
            emails = self.emails

        else:
            emails = self.emails

        job_title: None | str | Unset
        if isinstance(self.job_title, Unset):
            job_title = UNSET
        else:
            job_title = self.job_title

        location_type_id = self.location_type_id

        company_site_ids: list[int] | Unset = UNSET
        if not isinstance(self.company_site_ids, Unset):
            company_site_ids = self.company_site_ids

        phone_numbers: list[dict[str, Any]] | None | Unset
        if isinstance(self.phone_numbers, Unset):
            phone_numbers = UNSET
        elif isinstance(self.phone_numbers, list):
            phone_numbers = []
            for phone_numbers_type_0_item_data in self.phone_numbers:
                phone_numbers_type_0_item = phone_numbers_type_0_item_data.to_dict()
                phone_numbers.append(phone_numbers_type_0_item)

        else:
            phone_numbers = self.phone_numbers

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "address": address,
                "company_id": company_id,
                "company_position_id": company_position_id,
            }
        )
        if first_name is not UNSET:
            field_dict["first_name"] = first_name
        if middle_name is not UNSET:
            field_dict["middle_name"] = middle_name
        if last_name is not UNSET:
            field_dict["last_name"] = last_name
        if preferred_name is not UNSET:
            field_dict["preferred_name"] = preferred_name
        if preferred_language is not UNSET:
            field_dict["preferred_language"] = preferred_language
        if prior_last_name is not UNSET:
            field_dict["prior_last_name"] = prior_last_name
        if ssn is not UNSET:
            field_dict["ssn"] = ssn
        if primary_email is not UNSET:
            field_dict["primary_email"] = primary_email
        if emails is not UNSET:
            field_dict["emails"] = emails
        if job_title is not UNSET:
            field_dict["job_title"] = job_title
        if location_type_id is not UNSET:
            field_dict["location_type_id"] = location_type_id
        if company_site_ids is not UNSET:
            field_dict["company_site_ids"] = company_site_ids
        if phone_numbers is not UNSET:
            field_dict["phone_numbers"] = phone_numbers

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.employee_create_request_address import EmployeeCreateRequestAddress  # noqa: PLC0415
        from ..models.employee_create_request_phone_numbers_type_0_item import (
            EmployeeCreateRequestPhoneNumbersType0Item,  # noqa: PLC0415
        )

        d = dict(src_dict)
        address = EmployeeCreateRequestAddress.from_dict(d.pop("address"))

        company_id = UUID(d.pop("company_id"))

        company_position_id = d.pop("company_position_id")

        first_name = d.pop("first_name", UNSET)

        def _parse_middle_name(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        middle_name = _parse_middle_name(d.pop("middle_name", UNSET))

        last_name = d.pop("last_name", UNSET)

        def _parse_preferred_name(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        preferred_name = _parse_preferred_name(d.pop("preferred_name", UNSET))

        _preferred_language = d.pop("preferred_language", UNSET)
        preferred_language: EmployeeCreateRequestPreferredLanguage | Unset
        if isinstance(_preferred_language, Unset):
            preferred_language = UNSET
        else:
            preferred_language = EmployeeCreateRequestPreferredLanguage(_preferred_language)

        def _parse_prior_last_name(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        prior_last_name = _parse_prior_last_name(d.pop("prior_last_name", UNSET))

        def _parse_ssn(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        ssn = _parse_ssn(d.pop("ssn", UNSET))

        primary_email = d.pop("primary_email", UNSET)

        def _parse_emails(data: object) -> list[str] | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                emails_type_0 = cast(list[str], data)

                return emails_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[str] | None | Unset, data)

        emails = _parse_emails(d.pop("emails", UNSET))

        def _parse_job_title(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        job_title = _parse_job_title(d.pop("job_title", UNSET))

        location_type_id = d.pop("location_type_id", UNSET)

        company_site_ids = cast(list[int], d.pop("company_site_ids", UNSET))

        def _parse_phone_numbers(data: object) -> list[EmployeeCreateRequestPhoneNumbersType0Item] | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                phone_numbers_type_0 = []
                _phone_numbers_type_0 = data
                for phone_numbers_type_0_item_data in _phone_numbers_type_0:
                    phone_numbers_type_0_item = EmployeeCreateRequestPhoneNumbersType0Item.from_dict(
                        phone_numbers_type_0_item_data
                    )

                    phone_numbers_type_0.append(phone_numbers_type_0_item)

                return phone_numbers_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[EmployeeCreateRequestPhoneNumbersType0Item] | None | Unset, data)

        phone_numbers = _parse_phone_numbers(d.pop("phone_numbers", UNSET))

        employee_create_request = cls(
            address=address,
            company_id=company_id,
            company_position_id=company_position_id,
            first_name=first_name,
            middle_name=middle_name,
            last_name=last_name,
            preferred_name=preferred_name,
            preferred_language=preferred_language,
            prior_last_name=prior_last_name,
            ssn=ssn,
            primary_email=primary_email,
            emails=emails,
            job_title=job_title,
            location_type_id=location_type_id,
            company_site_ids=company_site_ids,
            phone_numbers=phone_numbers,
        )

        employee_create_request.additional_properties = d
        return employee_create_request

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

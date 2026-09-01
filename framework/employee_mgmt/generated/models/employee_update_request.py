from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.employee_update_request_preferred_language import EmployeeUpdateRequestPreferredLanguage
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.employee_update_request_address_type_0 import EmployeeUpdateRequestAddressType0
    from ..models.employee_update_request_phone_numbers_type_0_item import EmployeeUpdateRequestPhoneNumbersType0Item


T = TypeVar("T", bound="EmployeeUpdateRequest")


@_attrs_define
class EmployeeUpdateRequest:
    """Request schema for updating person-level employee details (name, address, email, phone, SSN)

    Attributes:
        first_name (None | str | Unset): Validates person-level employee updates only.

            Does not accept position, company, or status fields — those are managed
            by dedicated endpoints (transfers, terminations, addSecondaryPosition). Example: John.
        middle_name (None | str | Unset):  Example: Michael.
        last_name (None | str | Unset):  Example: Doe.
        preferred_name (None | str | Unset):  Example: Johnny.
        preferred_language (EmployeeUpdateRequestPreferredLanguage | Unset): ISO 639-1 language code. English, Spanish,
            Chinese, Vietnamese, Tagalog, Korean, French, Arabic, Russian, Portuguese, or Other. Example: en.
        prior_last_name (None | str | Unset):  Example: Smith.
        ssn (None | str | Unset):  Example: 123-45-6789.
        address (EmployeeUpdateRequestAddressType0 | None | Unset):
        primary_email (None | str | Unset):  Example: john@example.com.
        emails (list[str] | None | Unset):
        phone_numbers (list[EmployeeUpdateRequestPhoneNumbersType0Item] | None | Unset):
    """

    first_name: None | str | Unset = UNSET
    middle_name: None | str | Unset = UNSET
    last_name: None | str | Unset = UNSET
    preferred_name: None | str | Unset = UNSET
    preferred_language: EmployeeUpdateRequestPreferredLanguage | Unset = UNSET
    prior_last_name: None | str | Unset = UNSET
    ssn: None | str | Unset = UNSET
    address: EmployeeUpdateRequestAddressType0 | None | Unset = UNSET
    primary_email: None | str | Unset = UNSET
    emails: list[str] | None | Unset = UNSET
    phone_numbers: list[EmployeeUpdateRequestPhoneNumbersType0Item] | None | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.employee_update_request_address_type_0 import EmployeeUpdateRequestAddressType0  # noqa: PLC0415

        first_name: None | str | Unset
        if isinstance(self.first_name, Unset):
            first_name = UNSET
        else:
            first_name = self.first_name

        middle_name: None | str | Unset
        if isinstance(self.middle_name, Unset):
            middle_name = UNSET
        else:
            middle_name = self.middle_name

        last_name: None | str | Unset
        if isinstance(self.last_name, Unset):
            last_name = UNSET
        else:
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

        address: dict[str, Any] | None | Unset
        if isinstance(self.address, Unset):
            address = UNSET
        elif isinstance(self.address, EmployeeUpdateRequestAddressType0):
            address = self.address.to_dict()
        else:
            address = self.address

        primary_email: None | str | Unset
        if isinstance(self.primary_email, Unset):
            primary_email = UNSET
        else:
            primary_email = self.primary_email

        emails: list[str] | None | Unset
        if isinstance(self.emails, Unset):
            emails = UNSET
        elif isinstance(self.emails, list):
            emails = self.emails

        else:
            emails = self.emails

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
        field_dict.update({})
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
        if address is not UNSET:
            field_dict["address"] = address
        if primary_email is not UNSET:
            field_dict["primary_email"] = primary_email
        if emails is not UNSET:
            field_dict["emails"] = emails
        if phone_numbers is not UNSET:
            field_dict["phone_numbers"] = phone_numbers

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.employee_update_request_address_type_0 import EmployeeUpdateRequestAddressType0  # noqa: PLC0415
        from ..models.employee_update_request_phone_numbers_type_0_item import (
            EmployeeUpdateRequestPhoneNumbersType0Item,  # noqa: PLC0415
        )

        d = dict(src_dict)

        def _parse_first_name(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        first_name = _parse_first_name(d.pop("first_name", UNSET))

        def _parse_middle_name(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        middle_name = _parse_middle_name(d.pop("middle_name", UNSET))

        def _parse_last_name(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        last_name = _parse_last_name(d.pop("last_name", UNSET))

        def _parse_preferred_name(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        preferred_name = _parse_preferred_name(d.pop("preferred_name", UNSET))

        _preferred_language = d.pop("preferred_language", UNSET)
        preferred_language: EmployeeUpdateRequestPreferredLanguage | Unset
        if isinstance(_preferred_language, Unset):
            preferred_language = UNSET
        else:
            preferred_language = EmployeeUpdateRequestPreferredLanguage(_preferred_language)

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

        def _parse_address(data: object) -> EmployeeUpdateRequestAddressType0 | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                address_type_0 = EmployeeUpdateRequestAddressType0.from_dict(data)

                return address_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(EmployeeUpdateRequestAddressType0 | None | Unset, data)

        address = _parse_address(d.pop("address", UNSET))

        def _parse_primary_email(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        primary_email = _parse_primary_email(d.pop("primary_email", UNSET))

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

        def _parse_phone_numbers(data: object) -> list[EmployeeUpdateRequestPhoneNumbersType0Item] | None | Unset:
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
                    phone_numbers_type_0_item = EmployeeUpdateRequestPhoneNumbersType0Item.from_dict(
                        phone_numbers_type_0_item_data
                    )

                    phone_numbers_type_0.append(phone_numbers_type_0_item)

                return phone_numbers_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[EmployeeUpdateRequestPhoneNumbersType0Item] | None | Unset, data)

        phone_numbers = _parse_phone_numbers(d.pop("phone_numbers", UNSET))

        employee_update_request = cls(
            first_name=first_name,
            middle_name=middle_name,
            last_name=last_name,
            preferred_name=preferred_name,
            preferred_language=preferred_language,
            prior_last_name=prior_last_name,
            ssn=ssn,
            address=address,
            primary_email=primary_email,
            emails=emails,
            phone_numbers=phone_numbers,
        )

        employee_update_request.additional_properties = d
        return employee_update_request

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

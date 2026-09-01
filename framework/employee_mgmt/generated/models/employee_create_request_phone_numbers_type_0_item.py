from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.employee_create_request_phone_numbers_type_0_item_type import (
    EmployeeCreateRequestPhoneNumbersType0ItemType,
)

T = TypeVar("T", bound="EmployeeCreateRequestPhoneNumbersType0Item")


@_attrs_define
class EmployeeCreateRequestPhoneNumbersType0Item:
    """
    Attributes:
        phone_number (str):  Example: +12015550123.
        type_ (EmployeeCreateRequestPhoneNumbersType0ItemType):  Example: mobile.
        is_primary (bool): Exactly one phone number must be marked as primary Example: True.
    """

    phone_number: str
    type_: EmployeeCreateRequestPhoneNumbersType0ItemType
    is_primary: bool
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        phone_number = self.phone_number

        type_ = self.type_.value

        is_primary = self.is_primary

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "phone_number": phone_number,
                "type": type_,
                "is_primary": is_primary,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        phone_number = d.pop("phone_number")

        type_ = EmployeeCreateRequestPhoneNumbersType0ItemType(d.pop("type"))

        is_primary = d.pop("is_primary")

        employee_create_request_phone_numbers_type_0_item = cls(
            phone_number=phone_number,
            type_=type_,
            is_primary=is_primary,
        )

        employee_create_request_phone_numbers_type_0_item.additional_properties = d
        return employee_create_request_phone_numbers_type_0_item

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

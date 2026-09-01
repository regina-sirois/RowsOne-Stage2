from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="EmployeeProfileCompanyScheduledTerminationType0")


@_attrs_define
class EmployeeProfileCompanyScheduledTerminationType0:
    """
    Attributes:
        id (int | Unset):  Example: 123.
        date_of_termination (datetime.date | Unset):  Example: 2026-06-30.
    """

    id: int | Unset = UNSET
    date_of_termination: datetime.date | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id = self.id

        date_of_termination: str | Unset = UNSET
        if not isinstance(self.date_of_termination, Unset):
            date_of_termination = self.date_of_termination.isoformat()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if id is not UNSET:
            field_dict["id"] = id
        if date_of_termination is not UNSET:
            field_dict["date_of_termination"] = date_of_termination

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        id = d.pop("id", UNSET)

        _date_of_termination = d.pop("date_of_termination", UNSET)
        date_of_termination: datetime.date | Unset
        if isinstance(_date_of_termination, Unset):
            date_of_termination = UNSET
        else:
            date_of_termination = datetime.date.fromisoformat(_date_of_termination)

        employee_profile_company_scheduled_termination_type_0 = cls(
            id=id,
            date_of_termination=date_of_termination,
        )

        employee_profile_company_scheduled_termination_type_0.additional_properties = d
        return employee_profile_company_scheduled_termination_type_0

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

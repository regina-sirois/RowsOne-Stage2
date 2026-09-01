from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar
from uuid import UUID

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="CompanyPositionResourceDesignatedShiftsItem")


@_attrs_define
class CompanyPositionResourceDesignatedShiftsItem:
    """
    Attributes:
        id (UUID | Unset):  Example: 550e8400-e29b-41d4-a716-446655440002.
        name (str | Unset):  Example: Day Shift.
        shift_start_time (str | Unset):  Example: 07:00:00.
        shift_end_time (str | Unset):  Example: 15:00:00.
        max_shift_length (str | Unset):  Example: 12:00:00.
        in_use (bool | Unset): Only present on single-position endpoints. True when the shift is active and in use
            (referenced by an employee shift, needed-shift slot, or rotation day for this position) and therefore cannot be
            removed. Example: True.
    """

    id: UUID | Unset = UNSET
    name: str | Unset = UNSET
    shift_start_time: str | Unset = UNSET
    shift_end_time: str | Unset = UNSET
    max_shift_length: str | Unset = UNSET
    in_use: bool | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id: str | Unset = UNSET
        if not isinstance(self.id, Unset):
            id = str(self.id)

        name = self.name

        shift_start_time = self.shift_start_time

        shift_end_time = self.shift_end_time

        max_shift_length = self.max_shift_length

        in_use = self.in_use

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if id is not UNSET:
            field_dict["id"] = id
        if name is not UNSET:
            field_dict["name"] = name
        if shift_start_time is not UNSET:
            field_dict["shift_start_time"] = shift_start_time
        if shift_end_time is not UNSET:
            field_dict["shift_end_time"] = shift_end_time
        if max_shift_length is not UNSET:
            field_dict["max_shift_length"] = max_shift_length
        if in_use is not UNSET:
            field_dict["in_use"] = in_use

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        _id = d.pop("id", UNSET)
        id: UUID | Unset
        if isinstance(_id, Unset):
            id = UNSET
        else:
            id = UUID(_id)

        name = d.pop("name", UNSET)

        shift_start_time = d.pop("shift_start_time", UNSET)

        shift_end_time = d.pop("shift_end_time", UNSET)

        max_shift_length = d.pop("max_shift_length", UNSET)

        in_use = d.pop("in_use", UNSET)

        company_position_resource_designated_shifts_item = cls(
            id=id,
            name=name,
            shift_start_time=shift_start_time,
            shift_end_time=shift_end_time,
            max_shift_length=max_shift_length,
            in_use=in_use,
        )

        company_position_resource_designated_shifts_item.additional_properties = d
        return company_position_resource_designated_shifts_item

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

from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="C13Eb606Ef7Aa3E15Ff1593217D3D973Response200DataItemsItemDesignatedShiftsItem")


@_attrs_define
class C13Eb606Ef7Aa3E15Ff1593217D3D973Response200DataItemsItemDesignatedShiftsItem:
    """
    Attributes:
        id (int | Unset):  Example: 115.
        name (str | Unset):  Example: Afternoon Crew.
        shift_start_time (str | Unset):  Example: 08:00:00.
        shift_end_time (str | Unset):  Example: 15:00:00.
        max_shift_length (float | Unset):  Example: 7.
    """

    id: int | Unset = UNSET
    name: str | Unset = UNSET
    shift_start_time: str | Unset = UNSET
    shift_end_time: str | Unset = UNSET
    max_shift_length: float | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id = self.id

        name = self.name

        shift_start_time = self.shift_start_time

        shift_end_time = self.shift_end_time

        max_shift_length = self.max_shift_length

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

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        id = d.pop("id", UNSET)

        name = d.pop("name", UNSET)

        shift_start_time = d.pop("shift_start_time", UNSET)

        shift_end_time = d.pop("shift_end_time", UNSET)

        max_shift_length = d.pop("max_shift_length", UNSET)

        c13_eb_606_ef_7_aa_3e15_ff_1593217d3d973_response_200_data_items_item_designated_shifts_item = cls(
            id=id,
            name=name,
            shift_start_time=shift_start_time,
            shift_end_time=shift_end_time,
            max_shift_length=max_shift_length,
        )

        c13_eb_606_ef_7_aa_3e15_ff_1593217d3d973_response_200_data_items_item_designated_shifts_item.additional_properties = d
        return c13_eb_606_ef_7_aa_3e15_ff_1593217d3d973_response_200_data_items_item_designated_shifts_item

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

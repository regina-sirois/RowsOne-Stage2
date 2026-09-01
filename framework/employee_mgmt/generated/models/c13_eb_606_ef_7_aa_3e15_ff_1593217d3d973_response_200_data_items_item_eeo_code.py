from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar
from uuid import UUID

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="C13Eb606Ef7Aa3E15Ff1593217D3D973Response200DataItemsItemEeoCode")


@_attrs_define
class C13Eb606Ef7Aa3E15Ff1593217D3D973Response200DataItemsItemEeoCode:
    """
    Attributes:
        id (UUID | Unset):  Example: 9ec0478a-309b-4df0-94e7-8654c9af6864.
        name (str | Unset):  Example: Code 9.
        description (str | Unset):  Example: Service Workers.
    """

    id: UUID | Unset = UNSET
    name: str | Unset = UNSET
    description: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id: str | Unset = UNSET
        if not isinstance(self.id, Unset):
            id = str(self.id)

        name = self.name

        description = self.description

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if id is not UNSET:
            field_dict["id"] = id
        if name is not UNSET:
            field_dict["name"] = name
        if description is not UNSET:
            field_dict["description"] = description

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

        description = d.pop("description", UNSET)

        c13_eb_606_ef_7_aa_3e15_ff_1593217d3d973_response_200_data_items_item_eeo_code = cls(
            id=id,
            name=name,
            description=description,
        )

        c13_eb_606_ef_7_aa_3e15_ff_1593217d3d973_response_200_data_items_item_eeo_code.additional_properties = d
        return c13_eb_606_ef_7_aa_3e15_ff_1593217d3d973_response_200_data_items_item_eeo_code

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

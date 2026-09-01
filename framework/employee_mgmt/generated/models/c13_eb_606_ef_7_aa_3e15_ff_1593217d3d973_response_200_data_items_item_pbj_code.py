from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar
from uuid import UUID

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="C13Eb606Ef7Aa3E15Ff1593217D3D973Response200DataItemsItemPbjCode")


@_attrs_define
class C13Eb606Ef7Aa3E15Ff1593217D3D973Response200DataItemsItemPbjCode:
    """
    Attributes:
        id (UUID | Unset):  Example: 9ec0478a-3595-4774-92db-272dfa2a9362.
        code (str | Unset):  Example: 7.
        position (str | Unset):  Example: Registered Nurse (RN).
        description (str | Unset):  Example: Licensed registered nurses providing direct care..
    """

    id: UUID | Unset = UNSET
    code: str | Unset = UNSET
    position: str | Unset = UNSET
    description: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id: str | Unset = UNSET
        if not isinstance(self.id, Unset):
            id = str(self.id)

        code = self.code

        position = self.position

        description = self.description

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if id is not UNSET:
            field_dict["id"] = id
        if code is not UNSET:
            field_dict["code"] = code
        if position is not UNSET:
            field_dict["position"] = position
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

        code = d.pop("code", UNSET)

        position = d.pop("position", UNSET)

        description = d.pop("description", UNSET)

        c13_eb_606_ef_7_aa_3e15_ff_1593217d3d973_response_200_data_items_item_pbj_code = cls(
            id=id,
            code=code,
            position=position,
            description=description,
        )

        c13_eb_606_ef_7_aa_3e15_ff_1593217d3d973_response_200_data_items_item_pbj_code.additional_properties = d
        return c13_eb_606_ef_7_aa_3e15_ff_1593217d3d973_response_200_data_items_item_pbj_code

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

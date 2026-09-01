from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar
from uuid import UUID

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="CompanyDepartmentSimpleResource")


@_attrs_define
class CompanyDepartmentSimpleResource:
    """Simplified company department resource

    Attributes:
        id (int | Unset):  Example: 1.
        name (str | Unset):  Example: Nursing.
        company_id (UUID | Unset):  Example: 550e8400-e29b-41d4-a716-446655440001.
    """

    id: int | Unset = UNSET
    name: str | Unset = UNSET
    company_id: UUID | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id = self.id

        name = self.name

        company_id: str | Unset = UNSET
        if not isinstance(self.company_id, Unset):
            company_id = str(self.company_id)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if id is not UNSET:
            field_dict["id"] = id
        if name is not UNSET:
            field_dict["name"] = name
        if company_id is not UNSET:
            field_dict["company_id"] = company_id

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        id = d.pop("id", UNSET)

        name = d.pop("name", UNSET)

        _company_id = d.pop("company_id", UNSET)
        company_id: UUID | Unset
        if isinstance(_company_id, Unset):
            company_id = UNSET
        else:
            company_id = UUID(_company_id)

        company_department_simple_resource = cls(
            id=id,
            name=name,
            company_id=company_id,
        )

        company_department_simple_resource.additional_properties = d
        return company_department_simple_resource

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

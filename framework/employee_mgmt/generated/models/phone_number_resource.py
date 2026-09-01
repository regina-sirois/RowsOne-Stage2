from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import Any, TypeVar
from uuid import UUID

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.phone_number_resource_type import PhoneNumberResourceType
from ..types import UNSET, Unset

T = TypeVar("T", bound="PhoneNumberResource")


@_attrs_define
class PhoneNumberResource:
    """Phone number resource for API responses

    Attributes:
        id (UUID | Unset): Phone number ID Example: 550e8400-e29b-41d4-a716-446655440000.
        phone_number (str | Unset): The phone number Example: +12015550123.
        type_ (PhoneNumberResourceType | Unset): Type of phone number Example: mobile.
        type_name (str | Unset): Display name of the phone number type Example: Mobile.
        is_primary (bool | Unset): Whether this is the primary phone number Example: True.
        created_at (datetime.datetime | Unset):  Example: 2025-01-01T00:00:00+00:00.
        updated_at (datetime.datetime | Unset):  Example: 2025-01-01T00:00:00+00:00.
    """

    id: UUID | Unset = UNSET
    phone_number: str | Unset = UNSET
    type_: PhoneNumberResourceType | Unset = UNSET
    type_name: str | Unset = UNSET
    is_primary: bool | Unset = UNSET
    created_at: datetime.datetime | Unset = UNSET
    updated_at: datetime.datetime | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id: str | Unset = UNSET
        if not isinstance(self.id, Unset):
            id = str(self.id)

        phone_number = self.phone_number

        type_: str | Unset = UNSET
        if not isinstance(self.type_, Unset):
            type_ = self.type_.value

        type_name = self.type_name

        is_primary = self.is_primary

        created_at: str | Unset = UNSET
        if not isinstance(self.created_at, Unset):
            created_at = self.created_at.isoformat()

        updated_at: str | Unset = UNSET
        if not isinstance(self.updated_at, Unset):
            updated_at = self.updated_at.isoformat()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if id is not UNSET:
            field_dict["id"] = id
        if phone_number is not UNSET:
            field_dict["phone_number"] = phone_number
        if type_ is not UNSET:
            field_dict["type"] = type_
        if type_name is not UNSET:
            field_dict["type_name"] = type_name
        if is_primary is not UNSET:
            field_dict["is_primary"] = is_primary
        if created_at is not UNSET:
            field_dict["created_at"] = created_at
        if updated_at is not UNSET:
            field_dict["updated_at"] = updated_at

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

        phone_number = d.pop("phone_number", UNSET)

        _type_ = d.pop("type", UNSET)
        type_: PhoneNumberResourceType | Unset
        if isinstance(_type_, Unset):
            type_ = UNSET
        else:
            type_ = PhoneNumberResourceType(_type_)

        type_name = d.pop("type_name", UNSET)

        is_primary = d.pop("is_primary", UNSET)

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

        phone_number_resource = cls(
            id=id,
            phone_number=phone_number,
            type_=type_,
            type_name=type_name,
            is_primary=is_primary,
            created_at=created_at,
            updated_at=updated_at,
        )

        phone_number_resource.additional_properties = d
        return phone_number_resource

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

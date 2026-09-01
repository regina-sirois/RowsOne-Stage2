from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast
from uuid import UUID

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.user_emergency_contact_resource_address_type_0 import UserEmergencyContactResourceAddressType0


T = TypeVar("T", bound="UserEmergencyContactResource")


@_attrs_define
class UserEmergencyContactResource:
    """Emergency contact stored on the user (shared across all employee records).

    Attributes:
        id (UUID | Unset):
        user_id (UUID | Unset):
        name (str | Unset):  Example: Jane Doe.
        relationship (str | Unset):  Example: Spouse.
        phone (str | Unset):  Example: +12015550123.
        email (str | Unset):  Example: jane@example.com.
        address (None | Unset | UserEmergencyContactResourceAddressType0): Only present when the address relation is
            eager-loaded.
        created_at (datetime.datetime | Unset):  Example: 2025-01-01T00:00:00+00:00.
        updated_at (datetime.datetime | Unset):  Example: 2025-01-01T00:00:00+00:00.
    """

    id: UUID | Unset = UNSET
    user_id: UUID | Unset = UNSET
    name: str | Unset = UNSET
    relationship: str | Unset = UNSET
    phone: str | Unset = UNSET
    email: str | Unset = UNSET
    address: None | Unset | UserEmergencyContactResourceAddressType0 = UNSET
    created_at: datetime.datetime | Unset = UNSET
    updated_at: datetime.datetime | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.user_emergency_contact_resource_address_type_0 import (
            UserEmergencyContactResourceAddressType0,  # noqa: PLC0415
        )

        id: str | Unset = UNSET
        if not isinstance(self.id, Unset):
            id = str(self.id)

        user_id: str | Unset = UNSET
        if not isinstance(self.user_id, Unset):
            user_id = str(self.user_id)

        name = self.name

        relationship = self.relationship

        phone = self.phone

        email = self.email

        address: dict[str, Any] | None | Unset
        if isinstance(self.address, Unset):
            address = UNSET
        elif isinstance(self.address, UserEmergencyContactResourceAddressType0):
            address = self.address.to_dict()
        else:
            address = self.address

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
        if user_id is not UNSET:
            field_dict["user_id"] = user_id
        if name is not UNSET:
            field_dict["name"] = name
        if relationship is not UNSET:
            field_dict["relationship"] = relationship
        if phone is not UNSET:
            field_dict["phone"] = phone
        if email is not UNSET:
            field_dict["email"] = email
        if address is not UNSET:
            field_dict["address"] = address
        if created_at is not UNSET:
            field_dict["created_at"] = created_at
        if updated_at is not UNSET:
            field_dict["updated_at"] = updated_at

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.user_emergency_contact_resource_address_type_0 import (
            UserEmergencyContactResourceAddressType0,  # noqa: PLC0415
        )

        d = dict(src_dict)
        _id = d.pop("id", UNSET)
        id: UUID | Unset
        if isinstance(_id, Unset):
            id = UNSET
        else:
            id = UUID(_id)

        _user_id = d.pop("user_id", UNSET)
        user_id: UUID | Unset
        if isinstance(_user_id, Unset):
            user_id = UNSET
        else:
            user_id = UUID(_user_id)

        name = d.pop("name", UNSET)

        relationship = d.pop("relationship", UNSET)

        phone = d.pop("phone", UNSET)

        email = d.pop("email", UNSET)

        def _parse_address(data: object) -> None | Unset | UserEmergencyContactResourceAddressType0:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                address_type_0 = UserEmergencyContactResourceAddressType0.from_dict(data)

                return address_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(None | Unset | UserEmergencyContactResourceAddressType0, data)

        address = _parse_address(d.pop("address", UNSET))

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

        user_emergency_contact_resource = cls(
            id=id,
            user_id=user_id,
            name=name,
            relationship=relationship,
            phone=phone,
            email=email,
            address=address,
            created_at=created_at,
            updated_at=updated_at,
        )

        user_emergency_contact_resource.additional_properties = d
        return user_emergency_contact_resource

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

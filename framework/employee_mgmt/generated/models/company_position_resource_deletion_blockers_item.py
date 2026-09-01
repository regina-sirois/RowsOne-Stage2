from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="CompanyPositionResourceDeletionBlockersItem")


@_attrs_define
class CompanyPositionResourceDeletionBlockersItem:
    """
    Attributes:
        type_ (str | Unset):  Example: job_listings.
        count (int | Unset):  Example: 2.
        message (str | Unset):  Example: 2 job listing(s) reference this position. Remove them before deleting..
        ids (list[int] | Unset):
        permanent (bool | Unset):  Example: True.
    """

    type_: str | Unset = UNSET
    count: int | Unset = UNSET
    message: str | Unset = UNSET
    ids: list[int] | Unset = UNSET
    permanent: bool | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        type_ = self.type_

        count = self.count

        message = self.message

        ids: list[int] | Unset = UNSET
        if not isinstance(self.ids, Unset):
            ids = self.ids

        permanent = self.permanent

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if type_ is not UNSET:
            field_dict["type"] = type_
        if count is not UNSET:
            field_dict["count"] = count
        if message is not UNSET:
            field_dict["message"] = message
        if ids is not UNSET:
            field_dict["ids"] = ids
        if permanent is not UNSET:
            field_dict["permanent"] = permanent

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        type_ = d.pop("type", UNSET)

        count = d.pop("count", UNSET)

        message = d.pop("message", UNSET)

        ids = cast(list[int], d.pop("ids", UNSET))

        permanent = d.pop("permanent", UNSET)

        company_position_resource_deletion_blockers_item = cls(
            type_=type_,
            count=count,
            message=message,
            ids=ids,
            permanent=permanent,
        )

        company_position_resource_deletion_blockers_item.additional_properties = d
        return company_position_resource_deletion_blockers_item

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

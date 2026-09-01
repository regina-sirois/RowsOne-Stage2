from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar
from uuid import UUID

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="EmployeeMarkedIneligibleForRehireByCompaniesItem")


@_attrs_define
class EmployeeMarkedIneligibleForRehireByCompaniesItem:
    """
    Attributes:
        company_id (UUID | Unset):
        reason (str | Unset):
    """

    company_id: UUID | Unset = UNSET
    reason: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        company_id: str | Unset = UNSET
        if not isinstance(self.company_id, Unset):
            company_id = str(self.company_id)

        reason = self.reason

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if company_id is not UNSET:
            field_dict["company_id"] = company_id
        if reason is not UNSET:
            field_dict["reason"] = reason

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        _company_id = d.pop("company_id", UNSET)
        company_id: UUID | Unset
        if isinstance(_company_id, Unset):
            company_id = UNSET
        else:
            company_id = UUID(_company_id)

        reason = d.pop("reason", UNSET)

        employee_marked_ineligible_for_rehire_by_companies_item = cls(
            company_id=company_id,
            reason=reason,
        )

        employee_marked_ineligible_for_rehire_by_companies_item.additional_properties = d
        return employee_marked_ineligible_for_rehire_by_companies_item

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

from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="GetCompanySitesResponse200DataItemsItemCompanyUnitsItem")


@_attrs_define
class GetCompanySitesResponse200DataItemsItemCompanyUnitsItem:
    """
    Attributes:
        id (int | Unset):  Example: 1.
        company_site_id (int | Unset):  Example: 1.
        name (str | Unset):  Example: Unit A.
        max_resident_occupancy (int | None | Unset):
        created_at (datetime.datetime | Unset):  Example: 2025-04-03T08:17:00+00:00.
        updated_at (datetime.datetime | Unset):  Example: 2025-04-03T08:17:00+00:00.
    """

    id: int | Unset = UNSET
    company_site_id: int | Unset = UNSET
    name: str | Unset = UNSET
    max_resident_occupancy: int | None | Unset = UNSET
    created_at: datetime.datetime | Unset = UNSET
    updated_at: datetime.datetime | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id = self.id

        company_site_id = self.company_site_id

        name = self.name

        max_resident_occupancy: int | None | Unset
        if isinstance(self.max_resident_occupancy, Unset):
            max_resident_occupancy = UNSET
        else:
            max_resident_occupancy = self.max_resident_occupancy

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
        if company_site_id is not UNSET:
            field_dict["company_site_id"] = company_site_id
        if name is not UNSET:
            field_dict["name"] = name
        if max_resident_occupancy is not UNSET:
            field_dict["max_resident_occupancy"] = max_resident_occupancy
        if created_at is not UNSET:
            field_dict["created_at"] = created_at
        if updated_at is not UNSET:
            field_dict["updated_at"] = updated_at

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        id = d.pop("id", UNSET)

        company_site_id = d.pop("company_site_id", UNSET)

        name = d.pop("name", UNSET)

        def _parse_max_resident_occupancy(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        max_resident_occupancy = _parse_max_resident_occupancy(d.pop("max_resident_occupancy", UNSET))

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

        get_company_sites_response_200_data_items_item_company_units_item = cls(
            id=id,
            company_site_id=company_site_id,
            name=name,
            max_resident_occupancy=max_resident_occupancy,
            created_at=created_at,
            updated_at=updated_at,
        )

        get_company_sites_response_200_data_items_item_company_units_item.additional_properties = d
        return get_company_sites_response_200_data_items_item_company_units_item

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

from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar
from uuid import UUID

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.address_resource import AddressResource
    from ..models.get_company_sites_response_200_data_items_item_company_units_item import (
        GetCompanySitesResponse200DataItemsItemCompanyUnitsItem,
    )


T = TypeVar("T", bound="GetCompanySitesResponse200DataItemsItem")


@_attrs_define
class GetCompanySitesResponse200DataItemsItem:
    """
    Attributes:
        id (int | Unset):  Example: 1.
        company_id (UUID | Unset):  Example: 9e95efc2-b6e1-4646-845e-96f05ae0e04c.
        name (str | Unset):  Example: Cluj Central Office.
        site_type (str | Unset):  Example: Headquarters.
        address (AddressResource | Unset): Address resource
        phone_number (str | Unset):  Example: +40740123456.
        max_resident_occupancy (int | Unset):  Example: 50.
        is_remote (bool | Unset):  Example: False.
        exclude_from_job_listings (bool | Unset):  Example: False.
        status (str | Unset):  Example: ACTIVE.
        created_at (datetime.datetime | Unset):  Example: 2025-04-03T08:15:40+00:00.
        updated_at (datetime.datetime | Unset):  Example: 2025-04-03T08:15:40+00:00.
        company_units (list[GetCompanySitesResponse200DataItemsItemCompanyUnitsItem] | Unset):
    """

    id: int | Unset = UNSET
    company_id: UUID | Unset = UNSET
    name: str | Unset = UNSET
    site_type: str | Unset = UNSET
    address: AddressResource | Unset = UNSET
    phone_number: str | Unset = UNSET
    max_resident_occupancy: int | Unset = UNSET
    is_remote: bool | Unset = UNSET
    exclude_from_job_listings: bool | Unset = UNSET
    status: str | Unset = UNSET
    created_at: datetime.datetime | Unset = UNSET
    updated_at: datetime.datetime | Unset = UNSET
    company_units: list[GetCompanySitesResponse200DataItemsItemCompanyUnitsItem] | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id = self.id

        company_id: str | Unset = UNSET
        if not isinstance(self.company_id, Unset):
            company_id = str(self.company_id)

        name = self.name

        site_type = self.site_type

        address: dict[str, Any] | Unset = UNSET
        if not isinstance(self.address, Unset):
            address = self.address.to_dict()

        phone_number = self.phone_number

        max_resident_occupancy = self.max_resident_occupancy

        is_remote = self.is_remote

        exclude_from_job_listings = self.exclude_from_job_listings

        status = self.status

        created_at: str | Unset = UNSET
        if not isinstance(self.created_at, Unset):
            created_at = self.created_at.isoformat()

        updated_at: str | Unset = UNSET
        if not isinstance(self.updated_at, Unset):
            updated_at = self.updated_at.isoformat()

        company_units: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.company_units, Unset):
            company_units = []
            for company_units_item_data in self.company_units:
                company_units_item = company_units_item_data.to_dict()
                company_units.append(company_units_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if id is not UNSET:
            field_dict["id"] = id
        if company_id is not UNSET:
            field_dict["company_id"] = company_id
        if name is not UNSET:
            field_dict["name"] = name
        if site_type is not UNSET:
            field_dict["site_type"] = site_type
        if address is not UNSET:
            field_dict["address"] = address
        if phone_number is not UNSET:
            field_dict["phone_number"] = phone_number
        if max_resident_occupancy is not UNSET:
            field_dict["max_resident_occupancy"] = max_resident_occupancy
        if is_remote is not UNSET:
            field_dict["is_remote"] = is_remote
        if exclude_from_job_listings is not UNSET:
            field_dict["exclude_from_job_listings"] = exclude_from_job_listings
        if status is not UNSET:
            field_dict["status"] = status
        if created_at is not UNSET:
            field_dict["created_at"] = created_at
        if updated_at is not UNSET:
            field_dict["updated_at"] = updated_at
        if company_units is not UNSET:
            field_dict["company_units"] = company_units

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.address_resource import AddressResource  # noqa: PLC0415
        from ..models.get_company_sites_response_200_data_items_item_company_units_item import (
            GetCompanySitesResponse200DataItemsItemCompanyUnitsItem,  # noqa: PLC0415
        )

        d = dict(src_dict)
        id = d.pop("id", UNSET)

        _company_id = d.pop("company_id", UNSET)
        company_id: UUID | Unset
        if isinstance(_company_id, Unset):
            company_id = UNSET
        else:
            company_id = UUID(_company_id)

        name = d.pop("name", UNSET)

        site_type = d.pop("site_type", UNSET)

        _address = d.pop("address", UNSET)
        address: AddressResource | Unset
        if isinstance(_address, Unset):
            address = UNSET
        else:
            address = AddressResource.from_dict(_address)

        phone_number = d.pop("phone_number", UNSET)

        max_resident_occupancy = d.pop("max_resident_occupancy", UNSET)

        is_remote = d.pop("is_remote", UNSET)

        exclude_from_job_listings = d.pop("exclude_from_job_listings", UNSET)

        status = d.pop("status", UNSET)

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

        _company_units = d.pop("company_units", UNSET)
        company_units: list[GetCompanySitesResponse200DataItemsItemCompanyUnitsItem] | Unset = UNSET
        if _company_units is not UNSET:
            company_units = []
            for company_units_item_data in _company_units:
                company_units_item = GetCompanySitesResponse200DataItemsItemCompanyUnitsItem.from_dict(
                    company_units_item_data
                )

                company_units.append(company_units_item)

        get_company_sites_response_200_data_items_item = cls(
            id=id,
            company_id=company_id,
            name=name,
            site_type=site_type,
            address=address,
            phone_number=phone_number,
            max_resident_occupancy=max_resident_occupancy,
            is_remote=is_remote,
            exclude_from_job_listings=exclude_from_job_listings,
            status=status,
            created_at=created_at,
            updated_at=updated_at,
            company_units=company_units,
        )

        get_company_sites_response_200_data_items_item.additional_properties = d
        return get_company_sites_response_200_data_items_item

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

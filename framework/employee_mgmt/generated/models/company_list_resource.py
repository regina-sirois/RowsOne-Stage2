from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast
from uuid import UUID

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.company_list_resource_company_type_type_0 import CompanyListResourceCompanyTypeType0
    from ..models.company_list_resource_sites_type_0_item import CompanyListResourceSitesType0Item


T = TypeVar("T", bound="CompanyListResource")


@_attrs_define
class CompanyListResource:
    """Company list resource (list view)

    Attributes:
        id (UUID):  Example: 9e7a662a-2cc7-43fb-8877-88a400d55788.
        company_type_id (int):  Example: 1.
        name (str):  Example: Acme Corp.
        ein (str):  Example: 12-3456789.
        is_active (bool):  Example: True.
        company_type (CompanyListResourceCompanyTypeType0 | None | Unset): Loaded relationship
        sites (list[CompanyListResourceSitesType0Item] | None | Unset): Company sites
        employees_count (int | None | Unset):  Example: 75.
        job_listings_count (int | None | Unset):  Example: 10.
        job_applications_count (int | None | Unset): All job applications for the company, including every status
            Example: 100.
        candidates_count (int | None | Unset):  Example: 25.
        users_count (int | None | Unset): Active workspace users for the company; excludes Candidate/Employee-only and
            Rows Admin/Support users scoped here Example: 50.
        time_clocks_count (int | None | Unset):  Example: 5.
        created_at (datetime.datetime | None | Unset):  Example: 2025-01-01T00:00:00+00:00.
        updated_at (datetime.datetime | None | Unset):  Example: 2025-01-01T00:00:00+00:00.
        deleted_at (datetime.datetime | None | Unset):
    """

    id: UUID
    company_type_id: int
    name: str
    ein: str
    is_active: bool
    company_type: CompanyListResourceCompanyTypeType0 | None | Unset = UNSET
    sites: list[CompanyListResourceSitesType0Item] | None | Unset = UNSET
    employees_count: int | None | Unset = UNSET
    job_listings_count: int | None | Unset = UNSET
    job_applications_count: int | None | Unset = UNSET
    candidates_count: int | None | Unset = UNSET
    users_count: int | None | Unset = UNSET
    time_clocks_count: int | None | Unset = UNSET
    created_at: datetime.datetime | None | Unset = UNSET
    updated_at: datetime.datetime | None | Unset = UNSET
    deleted_at: datetime.datetime | None | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.company_list_resource_company_type_type_0 import (
            CompanyListResourceCompanyTypeType0,  # noqa: PLC0415
        )

        id = str(self.id)

        company_type_id = self.company_type_id

        name = self.name

        ein = self.ein

        is_active = self.is_active

        company_type: dict[str, Any] | None | Unset
        if isinstance(self.company_type, Unset):
            company_type = UNSET
        elif isinstance(self.company_type, CompanyListResourceCompanyTypeType0):
            company_type = self.company_type.to_dict()
        else:
            company_type = self.company_type

        sites: list[dict[str, Any]] | None | Unset
        if isinstance(self.sites, Unset):
            sites = UNSET
        elif isinstance(self.sites, list):
            sites = []
            for sites_type_0_item_data in self.sites:
                sites_type_0_item = sites_type_0_item_data.to_dict()
                sites.append(sites_type_0_item)

        else:
            sites = self.sites

        employees_count: int | None | Unset
        if isinstance(self.employees_count, Unset):
            employees_count = UNSET
        else:
            employees_count = self.employees_count

        job_listings_count: int | None | Unset
        if isinstance(self.job_listings_count, Unset):
            job_listings_count = UNSET
        else:
            job_listings_count = self.job_listings_count

        job_applications_count: int | None | Unset
        if isinstance(self.job_applications_count, Unset):
            job_applications_count = UNSET
        else:
            job_applications_count = self.job_applications_count

        candidates_count: int | None | Unset
        if isinstance(self.candidates_count, Unset):
            candidates_count = UNSET
        else:
            candidates_count = self.candidates_count

        users_count: int | None | Unset
        if isinstance(self.users_count, Unset):
            users_count = UNSET
        else:
            users_count = self.users_count

        time_clocks_count: int | None | Unset
        if isinstance(self.time_clocks_count, Unset):
            time_clocks_count = UNSET
        else:
            time_clocks_count = self.time_clocks_count

        created_at: None | str | Unset
        if isinstance(self.created_at, Unset):
            created_at = UNSET
        elif isinstance(self.created_at, datetime.datetime):
            created_at = self.created_at.isoformat()
        else:
            created_at = self.created_at

        updated_at: None | str | Unset
        if isinstance(self.updated_at, Unset):
            updated_at = UNSET
        elif isinstance(self.updated_at, datetime.datetime):
            updated_at = self.updated_at.isoformat()
        else:
            updated_at = self.updated_at

        deleted_at: None | str | Unset
        if isinstance(self.deleted_at, Unset):
            deleted_at = UNSET
        elif isinstance(self.deleted_at, datetime.datetime):
            deleted_at = self.deleted_at.isoformat()
        else:
            deleted_at = self.deleted_at

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id": id,
                "company_type_id": company_type_id,
                "name": name,
                "ein": ein,
                "is_active": is_active,
            }
        )
        if company_type is not UNSET:
            field_dict["company_type"] = company_type
        if sites is not UNSET:
            field_dict["sites"] = sites
        if employees_count is not UNSET:
            field_dict["employees_count"] = employees_count
        if job_listings_count is not UNSET:
            field_dict["job_listings_count"] = job_listings_count
        if job_applications_count is not UNSET:
            field_dict["job_applications_count"] = job_applications_count
        if candidates_count is not UNSET:
            field_dict["candidates_count"] = candidates_count
        if users_count is not UNSET:
            field_dict["users_count"] = users_count
        if time_clocks_count is not UNSET:
            field_dict["time_clocks_count"] = time_clocks_count
        if created_at is not UNSET:
            field_dict["created_at"] = created_at
        if updated_at is not UNSET:
            field_dict["updated_at"] = updated_at
        if deleted_at is not UNSET:
            field_dict["deleted_at"] = deleted_at

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.company_list_resource_company_type_type_0 import (
            CompanyListResourceCompanyTypeType0,  # noqa: PLC0415
        )
        from ..models.company_list_resource_sites_type_0_item import CompanyListResourceSitesType0Item  # noqa: PLC0415

        d = dict(src_dict)
        id = UUID(d.pop("id"))

        company_type_id = d.pop("company_type_id")

        name = d.pop("name")

        ein = d.pop("ein")

        is_active = d.pop("is_active")

        def _parse_company_type(data: object) -> CompanyListResourceCompanyTypeType0 | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                company_type_type_0 = CompanyListResourceCompanyTypeType0.from_dict(data)

                return company_type_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(CompanyListResourceCompanyTypeType0 | None | Unset, data)

        company_type = _parse_company_type(d.pop("company_type", UNSET))

        def _parse_sites(data: object) -> list[CompanyListResourceSitesType0Item] | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                sites_type_0 = []
                _sites_type_0 = data
                for sites_type_0_item_data in _sites_type_0:
                    sites_type_0_item = CompanyListResourceSitesType0Item.from_dict(sites_type_0_item_data)

                    sites_type_0.append(sites_type_0_item)

                return sites_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[CompanyListResourceSitesType0Item] | None | Unset, data)

        sites = _parse_sites(d.pop("sites", UNSET))

        def _parse_employees_count(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        employees_count = _parse_employees_count(d.pop("employees_count", UNSET))

        def _parse_job_listings_count(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        job_listings_count = _parse_job_listings_count(d.pop("job_listings_count", UNSET))

        def _parse_job_applications_count(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        job_applications_count = _parse_job_applications_count(d.pop("job_applications_count", UNSET))

        def _parse_candidates_count(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        candidates_count = _parse_candidates_count(d.pop("candidates_count", UNSET))

        def _parse_users_count(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        users_count = _parse_users_count(d.pop("users_count", UNSET))

        def _parse_time_clocks_count(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        time_clocks_count = _parse_time_clocks_count(d.pop("time_clocks_count", UNSET))

        def _parse_created_at(data: object) -> datetime.datetime | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                created_at_type_0 = datetime.datetime.fromisoformat(data)

                return created_at_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(datetime.datetime | None | Unset, data)

        created_at = _parse_created_at(d.pop("created_at", UNSET))

        def _parse_updated_at(data: object) -> datetime.datetime | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                updated_at_type_0 = datetime.datetime.fromisoformat(data)

                return updated_at_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(datetime.datetime | None | Unset, data)

        updated_at = _parse_updated_at(d.pop("updated_at", UNSET))

        def _parse_deleted_at(data: object) -> datetime.datetime | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                deleted_at_type_0 = datetime.datetime.fromisoformat(data)

                return deleted_at_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(datetime.datetime | None | Unset, data)

        deleted_at = _parse_deleted_at(d.pop("deleted_at", UNSET))

        company_list_resource = cls(
            id=id,
            company_type_id=company_type_id,
            name=name,
            ein=ein,
            is_active=is_active,
            company_type=company_type,
            sites=sites,
            employees_count=employees_count,
            job_listings_count=job_listings_count,
            job_applications_count=job_applications_count,
            candidates_count=candidates_count,
            users_count=users_count,
            time_clocks_count=time_clocks_count,
            created_at=created_at,
            updated_at=updated_at,
            deleted_at=deleted_at,
        )

        company_list_resource.additional_properties = d
        return company_list_resource

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

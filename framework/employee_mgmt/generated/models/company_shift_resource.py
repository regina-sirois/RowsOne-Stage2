from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.company_department_simple_resource import CompanyDepartmentSimpleResource


T = TypeVar("T", bound="CompanyShiftResource")


@_attrs_define
class CompanyShiftResource:
    """Company shift resource representation

    Attributes:
        id (int | Unset):  Example: 1.
        name (str | Unset): Calculated from the department shift abbreviation and the shift times Example: NUR
            7:30AM-4PM.
        shift_start_time (str | Unset):  Example: 19:00.
        shift_end_time (str | Unset):  Example: 07:00.
        max_shift_length (None | str | Unset): Decimal value as string with 2 decimal places Example: 12.00.
        company_department (CompanyDepartmentSimpleResource | None | Unset): Company department information (when
            loaded)
        designated_shifts_count (int | None | Unset): Count of designated shifts (when relationship is loaded) Example:
            5.
        created_at (datetime.datetime | Unset):  Example: 2025-01-01T00:00:00+00:00.
        updated_at (datetime.datetime | Unset):  Example: 2025-01-01T00:00:00+00:00.
        deleted_at (datetime.datetime | None | Unset):
    """

    id: int | Unset = UNSET
    name: str | Unset = UNSET
    shift_start_time: str | Unset = UNSET
    shift_end_time: str | Unset = UNSET
    max_shift_length: None | str | Unset = UNSET
    company_department: CompanyDepartmentSimpleResource | None | Unset = UNSET
    designated_shifts_count: int | None | Unset = UNSET
    created_at: datetime.datetime | Unset = UNSET
    updated_at: datetime.datetime | Unset = UNSET
    deleted_at: datetime.datetime | None | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.company_department_simple_resource import CompanyDepartmentSimpleResource  # noqa: PLC0415

        id = self.id

        name = self.name

        shift_start_time = self.shift_start_time

        shift_end_time = self.shift_end_time

        max_shift_length: None | str | Unset
        if isinstance(self.max_shift_length, Unset):
            max_shift_length = UNSET
        else:
            max_shift_length = self.max_shift_length

        company_department: dict[str, Any] | None | Unset
        if isinstance(self.company_department, Unset):
            company_department = UNSET
        elif isinstance(self.company_department, CompanyDepartmentSimpleResource):
            company_department = self.company_department.to_dict()
        else:
            company_department = self.company_department

        designated_shifts_count: int | None | Unset
        if isinstance(self.designated_shifts_count, Unset):
            designated_shifts_count = UNSET
        else:
            designated_shifts_count = self.designated_shifts_count

        created_at: str | Unset = UNSET
        if not isinstance(self.created_at, Unset):
            created_at = self.created_at.isoformat()

        updated_at: str | Unset = UNSET
        if not isinstance(self.updated_at, Unset):
            updated_at = self.updated_at.isoformat()

        deleted_at: None | str | Unset
        if isinstance(self.deleted_at, Unset):
            deleted_at = UNSET
        elif isinstance(self.deleted_at, datetime.datetime):
            deleted_at = self.deleted_at.isoformat()
        else:
            deleted_at = self.deleted_at

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if id is not UNSET:
            field_dict["id"] = id
        if name is not UNSET:
            field_dict["name"] = name
        if shift_start_time is not UNSET:
            field_dict["shift_start_time"] = shift_start_time
        if shift_end_time is not UNSET:
            field_dict["shift_end_time"] = shift_end_time
        if max_shift_length is not UNSET:
            field_dict["max_shift_length"] = max_shift_length
        if company_department is not UNSET:
            field_dict["company_department"] = company_department
        if designated_shifts_count is not UNSET:
            field_dict["designated_shifts_count"] = designated_shifts_count
        if created_at is not UNSET:
            field_dict["created_at"] = created_at
        if updated_at is not UNSET:
            field_dict["updated_at"] = updated_at
        if deleted_at is not UNSET:
            field_dict["deleted_at"] = deleted_at

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.company_department_simple_resource import CompanyDepartmentSimpleResource  # noqa: PLC0415

        d = dict(src_dict)
        id = d.pop("id", UNSET)

        name = d.pop("name", UNSET)

        shift_start_time = d.pop("shift_start_time", UNSET)

        shift_end_time = d.pop("shift_end_time", UNSET)

        def _parse_max_shift_length(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        max_shift_length = _parse_max_shift_length(d.pop("max_shift_length", UNSET))

        def _parse_company_department(data: object) -> CompanyDepartmentSimpleResource | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                company_department_type_0 = CompanyDepartmentSimpleResource.from_dict(data)

                return company_department_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(CompanyDepartmentSimpleResource | None | Unset, data)

        company_department = _parse_company_department(d.pop("company_department", UNSET))

        def _parse_designated_shifts_count(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        designated_shifts_count = _parse_designated_shifts_count(d.pop("designated_shifts_count", UNSET))

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

        company_shift_resource = cls(
            id=id,
            name=name,
            shift_start_time=shift_start_time,
            shift_end_time=shift_end_time,
            max_shift_length=max_shift_length,
            company_department=company_department,
            designated_shifts_count=designated_shifts_count,
            created_at=created_at,
            updated_at=updated_at,
            deleted_at=deleted_at,
        )

        company_shift_resource.additional_properties = d
        return company_shift_resource

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

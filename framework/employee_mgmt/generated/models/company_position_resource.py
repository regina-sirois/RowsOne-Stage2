from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast
from uuid import UUID

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.company_position_resource_deletion_blockers_item import CompanyPositionResourceDeletionBlockersItem
    from ..models.company_position_resource_designated_shifts_item import CompanyPositionResourceDesignatedShiftsItem
    from ..models.company_position_resource_eeo_code_type_0 import CompanyPositionResourceEeoCodeType0
    from ..models.company_position_resource_license_types_item import CompanyPositionResourceLicenseTypesItem
    from ..models.company_position_resource_pbj_code_type_0 import CompanyPositionResourcePbjCodeType0


T = TypeVar("T", bound="CompanyPositionResource")


@_attrs_define
class CompanyPositionResource:
    """Company position resource representation

    Attributes:
        id (UUID | Unset):  Example: 550e8400-e29b-41d4-a716-446655440000.
        company_department_id (int | Unset):  Example: 1.
        department_name (None | str | Unset):  Example: Nursing.
        position_id (UUID | Unset):  Example: 550e8400-e29b-41d4-a716-446655440001.
        position_name (None | str | Unset):  Example: Registered Nurse.
        pbj_code (CompanyPositionResourcePbjCodeType0 | None | Unset):
        eeo_code (CompanyPositionResourceEeoCodeType0 | None | Unset):
        gl_code (None | str | Unset):  Example: 4000.
        qb_code (None | str | Unset):  Example: QB001.
        workers_comp_code (None | str | Unset):  Example: WC001.
        is_direct_care (bool | Unset):  Example: True.
        status (str | Unset):  Example: active.
        is_union (bool | Unset):  Example: False.
        is_in_use (bool | Unset): Only present on single-position endpoints. True when the position is in use
            (active/upcoming employee assignment, any job listing, or any labor budget grouping) and therefore cannot be
            renamed. Example: True.
        can_be_deleted (bool | Unset): Only present on single-position endpoints. False when the position has any
            deletion blocker (see deletion_blockers). Example: False.
        deletion_blockers (list[CompanyPositionResourceDeletionBlockersItem] | Unset): Only present on single-position
            endpoints. Structured reasons the position cannot be deleted; empty when it is safe to delete.
        license_types (list[CompanyPositionResourceLicenseTypesItem] | Unset):
        designated_shifts (list[CompanyPositionResourceDesignatedShiftsItem] | Unset):
        created_at (datetime.datetime | Unset):  Example: 2025-01-01T00:00:00+00:00.
        updated_at (datetime.datetime | Unset):  Example: 2025-01-01T00:00:00+00:00.
    """

    id: UUID | Unset = UNSET
    company_department_id: int | Unset = UNSET
    department_name: None | str | Unset = UNSET
    position_id: UUID | Unset = UNSET
    position_name: None | str | Unset = UNSET
    pbj_code: CompanyPositionResourcePbjCodeType0 | None | Unset = UNSET
    eeo_code: CompanyPositionResourceEeoCodeType0 | None | Unset = UNSET
    gl_code: None | str | Unset = UNSET
    qb_code: None | str | Unset = UNSET
    workers_comp_code: None | str | Unset = UNSET
    is_direct_care: bool | Unset = UNSET
    status: str | Unset = UNSET
    is_union: bool | Unset = UNSET
    is_in_use: bool | Unset = UNSET
    can_be_deleted: bool | Unset = UNSET
    deletion_blockers: list[CompanyPositionResourceDeletionBlockersItem] | Unset = UNSET
    license_types: list[CompanyPositionResourceLicenseTypesItem] | Unset = UNSET
    designated_shifts: list[CompanyPositionResourceDesignatedShiftsItem] | Unset = UNSET
    created_at: datetime.datetime | Unset = UNSET
    updated_at: datetime.datetime | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.company_position_resource_eeo_code_type_0 import (
            CompanyPositionResourceEeoCodeType0,  # noqa: PLC0415
        )
        from ..models.company_position_resource_pbj_code_type_0 import (
            CompanyPositionResourcePbjCodeType0,  # noqa: PLC0415
        )

        id: str | Unset = UNSET
        if not isinstance(self.id, Unset):
            id = str(self.id)

        company_department_id = self.company_department_id

        department_name: None | str | Unset
        if isinstance(self.department_name, Unset):
            department_name = UNSET
        else:
            department_name = self.department_name

        position_id: str | Unset = UNSET
        if not isinstance(self.position_id, Unset):
            position_id = str(self.position_id)

        position_name: None | str | Unset
        if isinstance(self.position_name, Unset):
            position_name = UNSET
        else:
            position_name = self.position_name

        pbj_code: dict[str, Any] | None | Unset
        if isinstance(self.pbj_code, Unset):
            pbj_code = UNSET
        elif isinstance(self.pbj_code, CompanyPositionResourcePbjCodeType0):
            pbj_code = self.pbj_code.to_dict()
        else:
            pbj_code = self.pbj_code

        eeo_code: dict[str, Any] | None | Unset
        if isinstance(self.eeo_code, Unset):
            eeo_code = UNSET
        elif isinstance(self.eeo_code, CompanyPositionResourceEeoCodeType0):
            eeo_code = self.eeo_code.to_dict()
        else:
            eeo_code = self.eeo_code

        gl_code: None | str | Unset
        if isinstance(self.gl_code, Unset):
            gl_code = UNSET
        else:
            gl_code = self.gl_code

        qb_code: None | str | Unset
        if isinstance(self.qb_code, Unset):
            qb_code = UNSET
        else:
            qb_code = self.qb_code

        workers_comp_code: None | str | Unset
        if isinstance(self.workers_comp_code, Unset):
            workers_comp_code = UNSET
        else:
            workers_comp_code = self.workers_comp_code

        is_direct_care = self.is_direct_care

        status = self.status

        is_union = self.is_union

        is_in_use = self.is_in_use

        can_be_deleted = self.can_be_deleted

        deletion_blockers: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.deletion_blockers, Unset):
            deletion_blockers = []
            for deletion_blockers_item_data in self.deletion_blockers:
                deletion_blockers_item = deletion_blockers_item_data.to_dict()
                deletion_blockers.append(deletion_blockers_item)

        license_types: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.license_types, Unset):
            license_types = []
            for license_types_item_data in self.license_types:
                license_types_item = license_types_item_data.to_dict()
                license_types.append(license_types_item)

        designated_shifts: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.designated_shifts, Unset):
            designated_shifts = []
            for designated_shifts_item_data in self.designated_shifts:
                designated_shifts_item = designated_shifts_item_data.to_dict()
                designated_shifts.append(designated_shifts_item)

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
        if company_department_id is not UNSET:
            field_dict["company_department_id"] = company_department_id
        if department_name is not UNSET:
            field_dict["department_name"] = department_name
        if position_id is not UNSET:
            field_dict["position_id"] = position_id
        if position_name is not UNSET:
            field_dict["position_name"] = position_name
        if pbj_code is not UNSET:
            field_dict["pbj_code"] = pbj_code
        if eeo_code is not UNSET:
            field_dict["eeo_code"] = eeo_code
        if gl_code is not UNSET:
            field_dict["gl_code"] = gl_code
        if qb_code is not UNSET:
            field_dict["qb_code"] = qb_code
        if workers_comp_code is not UNSET:
            field_dict["workers_comp_code"] = workers_comp_code
        if is_direct_care is not UNSET:
            field_dict["is_direct_care"] = is_direct_care
        if status is not UNSET:
            field_dict["status"] = status
        if is_union is not UNSET:
            field_dict["is_union"] = is_union
        if is_in_use is not UNSET:
            field_dict["is_in_use"] = is_in_use
        if can_be_deleted is not UNSET:
            field_dict["can_be_deleted"] = can_be_deleted
        if deletion_blockers is not UNSET:
            field_dict["deletion_blockers"] = deletion_blockers
        if license_types is not UNSET:
            field_dict["license_types"] = license_types
        if designated_shifts is not UNSET:
            field_dict["designated_shifts"] = designated_shifts
        if created_at is not UNSET:
            field_dict["created_at"] = created_at
        if updated_at is not UNSET:
            field_dict["updated_at"] = updated_at

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.company_position_resource_deletion_blockers_item import (
            CompanyPositionResourceDeletionBlockersItem,  # noqa: PLC0415
        )
        from ..models.company_position_resource_designated_shifts_item import (
            CompanyPositionResourceDesignatedShiftsItem,  # noqa: PLC0415
        )
        from ..models.company_position_resource_eeo_code_type_0 import (
            CompanyPositionResourceEeoCodeType0,  # noqa: PLC0415
        )
        from ..models.company_position_resource_license_types_item import (
            CompanyPositionResourceLicenseTypesItem,  # noqa: PLC0415
        )
        from ..models.company_position_resource_pbj_code_type_0 import (
            CompanyPositionResourcePbjCodeType0,  # noqa: PLC0415
        )

        d = dict(src_dict)
        _id = d.pop("id", UNSET)
        id: UUID | Unset
        if isinstance(_id, Unset):
            id = UNSET
        else:
            # TODO: This is modified from the generated code, potentially create defect.
            if isinstance(_id, str):
                id = UUID(_id)
            else:
                id = _id

        company_department_id = d.pop("company_department_id", UNSET)

        def _parse_department_name(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        department_name = _parse_department_name(d.pop("department_name", UNSET))

        _position_id = d.pop("position_id", UNSET)
        position_id: UUID | Unset
        if isinstance(_position_id, Unset):
            position_id = UNSET
        else:
            position_id = UUID(_position_id)

        def _parse_position_name(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        position_name = _parse_position_name(d.pop("position_name", UNSET))

        def _parse_pbj_code(data: object) -> CompanyPositionResourcePbjCodeType0 | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                pbj_code_type_0 = CompanyPositionResourcePbjCodeType0.from_dict(data)

                return pbj_code_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(CompanyPositionResourcePbjCodeType0 | None | Unset, data)

        pbj_code = _parse_pbj_code(d.pop("pbj_code", UNSET))

        def _parse_eeo_code(data: object) -> CompanyPositionResourceEeoCodeType0 | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                eeo_code_type_0 = CompanyPositionResourceEeoCodeType0.from_dict(data)

                return eeo_code_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(CompanyPositionResourceEeoCodeType0 | None | Unset, data)

        eeo_code = _parse_eeo_code(d.pop("eeo_code", UNSET))

        def _parse_gl_code(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        gl_code = _parse_gl_code(d.pop("gl_code", UNSET))

        def _parse_qb_code(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        qb_code = _parse_qb_code(d.pop("qb_code", UNSET))

        def _parse_workers_comp_code(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        workers_comp_code = _parse_workers_comp_code(d.pop("workers_comp_code", UNSET))

        is_direct_care = d.pop("is_direct_care", UNSET)

        status = d.pop("status", UNSET)

        is_union = d.pop("is_union", UNSET)

        is_in_use = d.pop("is_in_use", UNSET)

        can_be_deleted = d.pop("can_be_deleted", UNSET)

        _deletion_blockers = d.pop("deletion_blockers", UNSET)
        deletion_blockers: list[CompanyPositionResourceDeletionBlockersItem] | Unset = UNSET
        if _deletion_blockers is not UNSET:
            deletion_blockers = []
            for deletion_blockers_item_data in _deletion_blockers:
                deletion_blockers_item = CompanyPositionResourceDeletionBlockersItem.from_dict(
                    deletion_blockers_item_data
                )

                deletion_blockers.append(deletion_blockers_item)

        _license_types = d.pop("license_types", UNSET)
        license_types: list[CompanyPositionResourceLicenseTypesItem] | Unset = UNSET
        if _license_types is not UNSET:
            license_types = []
            for license_types_item_data in _license_types:
                license_types_item = CompanyPositionResourceLicenseTypesItem.from_dict(license_types_item_data)

                license_types.append(license_types_item)

        _designated_shifts = d.pop("designated_shifts", UNSET)
        designated_shifts: list[CompanyPositionResourceDesignatedShiftsItem] | Unset = UNSET
        if _designated_shifts is not UNSET:
            designated_shifts = []
            for designated_shifts_item_data in _designated_shifts:
                designated_shifts_item = CompanyPositionResourceDesignatedShiftsItem.from_dict(
                    designated_shifts_item_data
                )

                designated_shifts.append(designated_shifts_item)

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

        company_position_resource = cls(
            id=id,
            company_department_id=company_department_id,
            department_name=department_name,
            position_id=position_id,
            position_name=position_name,
            pbj_code=pbj_code,
            eeo_code=eeo_code,
            gl_code=gl_code,
            qb_code=qb_code,
            workers_comp_code=workers_comp_code,
            is_direct_care=is_direct_care,
            status=status,
            is_union=is_union,
            is_in_use=is_in_use,
            can_be_deleted=can_be_deleted,
            deletion_blockers=deletion_blockers,
            license_types=license_types,
            designated_shifts=designated_shifts,
            created_at=created_at,
            updated_at=updated_at,
        )

        company_position_resource.additional_properties = d
        return company_position_resource

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

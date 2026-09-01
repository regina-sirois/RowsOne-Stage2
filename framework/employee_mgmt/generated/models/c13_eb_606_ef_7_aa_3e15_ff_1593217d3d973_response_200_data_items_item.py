from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast
from uuid import UUID

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.c13_eb_606_ef_7_aa_3e15_ff_1593217d3d973_response_200_data_items_item_designated_shifts_item import (
        C13Eb606Ef7Aa3E15Ff1593217D3D973Response200DataItemsItemDesignatedShiftsItem,
    )
    from ..models.c13_eb_606_ef_7_aa_3e15_ff_1593217d3d973_response_200_data_items_item_eeo_code import (
        C13Eb606Ef7Aa3E15Ff1593217D3D973Response200DataItemsItemEeoCode,
    )
    from ..models.c13_eb_606_ef_7_aa_3e15_ff_1593217d3d973_response_200_data_items_item_license_types_item import (
        C13Eb606Ef7Aa3E15Ff1593217D3D973Response200DataItemsItemLicenseTypesItem,
    )
    from ..models.c13_eb_606_ef_7_aa_3e15_ff_1593217d3d973_response_200_data_items_item_pbj_code import (
        C13Eb606Ef7Aa3E15Ff1593217D3D973Response200DataItemsItemPbjCode,
    )


T = TypeVar("T", bound="C13Eb606Ef7Aa3E15Ff1593217D3D973Response200DataItemsItem")


@_attrs_define
class C13Eb606Ef7Aa3E15Ff1593217D3D973Response200DataItemsItem:
    """
    Attributes:
        id (int | Unset):  Example: 75.
        company_department_id (int | Unset):  Example: 8.
        department_name (str | Unset):  Example: Nursing/Rehab.
        position_id (UUID | Unset):  Example: 9ec04789-53c4-4352-8ae3-e029a86f4991.
        position_name (str | Unset):  Example: Assistant Director of Nursing (ADON).
        pbj_code (C13Eb606Ef7Aa3E15Ff1593217D3D973Response200DataItemsItemPbjCode | Unset):
        eeo_code (C13Eb606Ef7Aa3E15Ff1593217D3D973Response200DataItemsItemEeoCode | Unset):
        gl_code (str | Unset):  Example: GL567.
        qb_code (str | Unset):  Example: QB234.
        workers_comp_code (str | Unset):  Example: WC123.
        is_direct_care (bool | Unset):  Example: True.
        license_types (list[C13Eb606Ef7Aa3E15Ff1593217D3D973Response200DataItemsItemLicenseTypesItem] | Unset):
        designated_shifts (list[C13Eb606Ef7Aa3E15Ff1593217D3D973Response200DataItemsItemDesignatedShiftsItem] | Unset):
        created_at (datetime.datetime | Unset):  Example: 2025-04-24T09:25:13+00:00.
        updated_at (datetime.datetime | Unset):  Example: 2025-04-24T09:25:13+00:00.
        deleted_at (datetime.datetime | None | Unset):
    """

    id: int | Unset = UNSET
    company_department_id: int | Unset = UNSET
    department_name: str | Unset = UNSET
    position_id: UUID | Unset = UNSET
    position_name: str | Unset = UNSET
    pbj_code: C13Eb606Ef7Aa3E15Ff1593217D3D973Response200DataItemsItemPbjCode | Unset = UNSET
    eeo_code: C13Eb606Ef7Aa3E15Ff1593217D3D973Response200DataItemsItemEeoCode | Unset = UNSET
    gl_code: str | Unset = UNSET
    qb_code: str | Unset = UNSET
    workers_comp_code: str | Unset = UNSET
    is_direct_care: bool | Unset = UNSET
    license_types: list[C13Eb606Ef7Aa3E15Ff1593217D3D973Response200DataItemsItemLicenseTypesItem] | Unset = UNSET
    designated_shifts: list[C13Eb606Ef7Aa3E15Ff1593217D3D973Response200DataItemsItemDesignatedShiftsItem] | Unset = (
        UNSET
    )
    created_at: datetime.datetime | Unset = UNSET
    updated_at: datetime.datetime | Unset = UNSET
    deleted_at: datetime.datetime | None | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id = self.id

        company_department_id = self.company_department_id

        department_name = self.department_name

        position_id: str | Unset = UNSET
        if not isinstance(self.position_id, Unset):
            position_id = str(self.position_id)

        position_name = self.position_name

        pbj_code: dict[str, Any] | Unset = UNSET
        if not isinstance(self.pbj_code, Unset):
            pbj_code = self.pbj_code.to_dict()

        eeo_code: dict[str, Any] | Unset = UNSET
        if not isinstance(self.eeo_code, Unset):
            eeo_code = self.eeo_code.to_dict()

        gl_code = self.gl_code

        qb_code = self.qb_code

        workers_comp_code = self.workers_comp_code

        is_direct_care = self.is_direct_care

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
        if license_types is not UNSET:
            field_dict["license_types"] = license_types
        if designated_shifts is not UNSET:
            field_dict["designated_shifts"] = designated_shifts
        if created_at is not UNSET:
            field_dict["created_at"] = created_at
        if updated_at is not UNSET:
            field_dict["updated_at"] = updated_at
        if deleted_at is not UNSET:
            field_dict["deleted_at"] = deleted_at

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.c13_eb_606_ef_7_aa_3e15_ff_1593217d3d973_response_200_data_items_item_designated_shifts_item import (
            C13Eb606Ef7Aa3E15Ff1593217D3D973Response200DataItemsItemDesignatedShiftsItem,  # noqa: PLC0415
        )
        from ..models.c13_eb_606_ef_7_aa_3e15_ff_1593217d3d973_response_200_data_items_item_eeo_code import (
            C13Eb606Ef7Aa3E15Ff1593217D3D973Response200DataItemsItemEeoCode,  # noqa: PLC0415
        )
        from ..models.c13_eb_606_ef_7_aa_3e15_ff_1593217d3d973_response_200_data_items_item_license_types_item import (
            C13Eb606Ef7Aa3E15Ff1593217D3D973Response200DataItemsItemLicenseTypesItem,  # noqa: PLC0415
        )
        from ..models.c13_eb_606_ef_7_aa_3e15_ff_1593217d3d973_response_200_data_items_item_pbj_code import (
            C13Eb606Ef7Aa3E15Ff1593217D3D973Response200DataItemsItemPbjCode,  # noqa: PLC0415
        )

        d = dict(src_dict)
        id = d.pop("id", UNSET)

        company_department_id = d.pop("company_department_id", UNSET)

        department_name = d.pop("department_name", UNSET)

        _position_id = d.pop("position_id", UNSET)
        position_id: UUID | Unset
        if isinstance(_position_id, Unset):
            position_id = UNSET
        else:
            position_id = UUID(_position_id)

        position_name = d.pop("position_name", UNSET)

        _pbj_code = d.pop("pbj_code", UNSET)
        pbj_code: C13Eb606Ef7Aa3E15Ff1593217D3D973Response200DataItemsItemPbjCode | Unset
        if isinstance(_pbj_code, Unset):
            pbj_code = UNSET
        else:
            pbj_code = C13Eb606Ef7Aa3E15Ff1593217D3D973Response200DataItemsItemPbjCode.from_dict(_pbj_code)

        _eeo_code = d.pop("eeo_code", UNSET)
        eeo_code: C13Eb606Ef7Aa3E15Ff1593217D3D973Response200DataItemsItemEeoCode | Unset
        if isinstance(_eeo_code, Unset):
            eeo_code = UNSET
        else:
            eeo_code = C13Eb606Ef7Aa3E15Ff1593217D3D973Response200DataItemsItemEeoCode.from_dict(_eeo_code)

        gl_code = d.pop("gl_code", UNSET)

        qb_code = d.pop("qb_code", UNSET)

        workers_comp_code = d.pop("workers_comp_code", UNSET)

        is_direct_care = d.pop("is_direct_care", UNSET)

        _license_types = d.pop("license_types", UNSET)
        license_types: list[C13Eb606Ef7Aa3E15Ff1593217D3D973Response200DataItemsItemLicenseTypesItem] | Unset = UNSET
        if _license_types is not UNSET:
            license_types = []
            for license_types_item_data in _license_types:
                license_types_item = C13Eb606Ef7Aa3E15Ff1593217D3D973Response200DataItemsItemLicenseTypesItem.from_dict(
                    license_types_item_data
                )

                license_types.append(license_types_item)

        _designated_shifts = d.pop("designated_shifts", UNSET)
        designated_shifts: (
            list[C13Eb606Ef7Aa3E15Ff1593217D3D973Response200DataItemsItemDesignatedShiftsItem] | Unset
        ) = UNSET
        if _designated_shifts is not UNSET:
            designated_shifts = []
            for designated_shifts_item_data in _designated_shifts:
                designated_shifts_item = (
                    C13Eb606Ef7Aa3E15Ff1593217D3D973Response200DataItemsItemDesignatedShiftsItem.from_dict(
                        designated_shifts_item_data
                    )
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

        c13_eb_606_ef_7_aa_3e15_ff_1593217d3d973_response_200_data_items_item = cls(
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
            license_types=license_types,
            designated_shifts=designated_shifts,
            created_at=created_at,
            updated_at=updated_at,
            deleted_at=deleted_at,
        )

        c13_eb_606_ef_7_aa_3e15_ff_1593217d3d973_response_200_data_items_item.additional_properties = d
        return c13_eb_606_ef_7_aa_3e15_ff_1593217d3d973_response_200_data_items_item

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

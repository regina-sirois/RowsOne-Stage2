from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar
from uuid import UUID

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.company_department_resource_department import CompanyDepartmentResourceDepartment
    from ..models.company_position_resource import CompanyPositionResource
    from ..models.company_shift_resource import CompanyShiftResource


T = TypeVar("T", bound="CompanyDepartmentResource")


@_attrs_define
class CompanyDepartmentResource:
    """
    Attributes:
        id (int):  Example: 2.
        company_id (UUID):
        department_id (UUID):
        status (str):  Example: ACTIVE.
        department (CompanyDepartmentResourceDepartment | Unset):
        company_positions (list[CompanyPositionResource] | Unset):
        company_shifts (list[CompanyShiftResource] | Unset):
    """

    id: int
    company_id: UUID
    department_id: UUID
    status: str
    department: CompanyDepartmentResourceDepartment | Unset = UNSET
    company_positions: list[CompanyPositionResource] | Unset = UNSET
    company_shifts: list[CompanyShiftResource] | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id = self.id

        company_id = str(self.company_id)

        department_id = str(self.department_id)

        status = self.status

        department: dict[str, Any] | Unset = UNSET
        if not isinstance(self.department, Unset):
            department = self.department.to_dict()

        company_positions: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.company_positions, Unset):
            company_positions = []
            for company_positions_item_data in self.company_positions:
                company_positions_item = company_positions_item_data.to_dict()
                company_positions.append(company_positions_item)

        company_shifts: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.company_shifts, Unset):
            company_shifts = []
            for company_shifts_item_data in self.company_shifts:
                company_shifts_item = company_shifts_item_data.to_dict()
                company_shifts.append(company_shifts_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id": id,
                "company_id": company_id,
                "department_id": department_id,
                "status": status,
            }
        )
        if department is not UNSET:
            field_dict["department"] = department
        if company_positions is not UNSET:
            field_dict["company_positions"] = company_positions
        if company_shifts is not UNSET:
            field_dict["company_shifts"] = company_shifts

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.company_department_resource_department import CompanyDepartmentResourceDepartment  # noqa: PLC0415
        from ..models.company_position_resource import CompanyPositionResource  # noqa: PLC0415
        from ..models.company_shift_resource import CompanyShiftResource  # noqa: PLC0415

        d = dict(src_dict)
        id = d.pop("id")

        company_id = UUID(d.pop("company_id"))

        department_id = UUID(d.pop("department_id"))

        status = d.pop("status")

        _department = d.pop("department", UNSET)
        department: CompanyDepartmentResourceDepartment | Unset
        if isinstance(_department, Unset):
            department = UNSET
        else:
            department = CompanyDepartmentResourceDepartment.from_dict(_department)

        _company_positions = d.pop("company_positions", UNSET)
        company_positions: list[CompanyPositionResource] | Unset = UNSET
        if _company_positions is not UNSET:
            company_positions = []
            for company_positions_item_data in _company_positions:
                company_positions_item = CompanyPositionResource.from_dict(company_positions_item_data)

                company_positions.append(company_positions_item)

        _company_shifts = d.pop("company_shifts", UNSET)
        company_shifts: list[CompanyShiftResource] | Unset = UNSET
        if _company_shifts is not UNSET:
            company_shifts = []
            for company_shifts_item_data in _company_shifts:
                company_shifts_item = CompanyShiftResource.from_dict(company_shifts_item_data)

                company_shifts.append(company_shifts_item)

        company_department_resource = cls(
            id=id,
            company_id=company_id,
            department_id=department_id,
            status=status,
            department=department,
            company_positions=company_positions,
            company_shifts=company_shifts,
        )

        company_department_resource.additional_properties = d
        return company_department_resource

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

from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast
from uuid import UUID

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.employee_index_company import EmployeeIndexCompany


T = TypeVar("T", bound="EmployeeIndex")


@_attrs_define
class EmployeeIndex:
    """Trimmed employee representation for the Employees table list view

    Attributes:
        id (UUID):  Example: 550e8400-e29b-41d4-a716-446655440000.
        first_name (str):  Example: John.
        last_name (str):  Example: Doe.
        total_notes (int):  Example: 3.
        badge_number (None | str | Unset):  Example: 0001234.
        middle_name (None | str | Unset):  Example: Michael.
        profile_picture_base64 (None | str | Unset): Base64 encoded profile picture
        employment_type (None | str | Unset):  Example: Full-time.
        pay_exception_category_name (None | str | Unset):  Example: No frills (no benefits).
        is_shared (bool | Unset):  Example: False.
        shared_company_names (list[str] | Unset): All companies the employee works for, regardless of the viewer's
            access scope (powers the Shared tooltip)
        is_pinned (bool | Unset): Whether the employee is pinned by the current user Example: False.
        employee_companies (list[EmployeeIndexCompany] | Unset):
    """

    id: UUID
    first_name: str
    last_name: str
    total_notes: int
    badge_number: None | str | Unset = UNSET
    middle_name: None | str | Unset = UNSET
    profile_picture_base64: None | str | Unset = UNSET
    employment_type: None | str | Unset = UNSET
    pay_exception_category_name: None | str | Unset = UNSET
    is_shared: bool | Unset = UNSET
    shared_company_names: list[str] | Unset = UNSET
    is_pinned: bool | Unset = UNSET
    employee_companies: list[EmployeeIndexCompany] | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id = str(self.id)

        first_name = self.first_name

        last_name = self.last_name

        total_notes = self.total_notes

        badge_number: None | str | Unset
        if isinstance(self.badge_number, Unset):
            badge_number = UNSET
        else:
            badge_number = self.badge_number

        middle_name: None | str | Unset
        if isinstance(self.middle_name, Unset):
            middle_name = UNSET
        else:
            middle_name = self.middle_name

        profile_picture_base64: None | str | Unset
        if isinstance(self.profile_picture_base64, Unset):
            profile_picture_base64 = UNSET
        else:
            profile_picture_base64 = self.profile_picture_base64

        employment_type: None | str | Unset
        if isinstance(self.employment_type, Unset):
            employment_type = UNSET
        else:
            employment_type = self.employment_type

        pay_exception_category_name: None | str | Unset
        if isinstance(self.pay_exception_category_name, Unset):
            pay_exception_category_name = UNSET
        else:
            pay_exception_category_name = self.pay_exception_category_name

        is_shared = self.is_shared

        shared_company_names: list[str] | Unset = UNSET
        if not isinstance(self.shared_company_names, Unset):
            shared_company_names = self.shared_company_names

        is_pinned = self.is_pinned

        employee_companies: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.employee_companies, Unset):
            employee_companies = []
            for employee_companies_item_data in self.employee_companies:
                employee_companies_item = employee_companies_item_data.to_dict()
                employee_companies.append(employee_companies_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id": id,
                "first_name": first_name,
                "last_name": last_name,
                "total_notes": total_notes,
            }
        )
        if badge_number is not UNSET:
            field_dict["badge_number"] = badge_number
        if middle_name is not UNSET:
            field_dict["middle_name"] = middle_name
        if profile_picture_base64 is not UNSET:
            field_dict["profile_picture_base64"] = profile_picture_base64
        if employment_type is not UNSET:
            field_dict["employment_type"] = employment_type
        if pay_exception_category_name is not UNSET:
            field_dict["pay_exception_category_name"] = pay_exception_category_name
        if is_shared is not UNSET:
            field_dict["is_shared"] = is_shared
        if shared_company_names is not UNSET:
            field_dict["shared_company_names"] = shared_company_names
        if is_pinned is not UNSET:
            field_dict["is_pinned"] = is_pinned
        if employee_companies is not UNSET:
            field_dict["employee_companies"] = employee_companies

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.employee_index_company import EmployeeIndexCompany  # noqa: PLC0415

        d = dict(src_dict)
        id = UUID(d.pop("id"))

        first_name = d.pop("first_name")

        last_name = d.pop("last_name")

        total_notes = d.pop("total_notes")

        def _parse_badge_number(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        badge_number = _parse_badge_number(d.pop("badge_number", UNSET))

        def _parse_middle_name(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        middle_name = _parse_middle_name(d.pop("middle_name", UNSET))

        def _parse_profile_picture_base64(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        profile_picture_base64 = _parse_profile_picture_base64(d.pop("profile_picture_base64", UNSET))

        def _parse_employment_type(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        employment_type = _parse_employment_type(d.pop("employment_type", UNSET))

        def _parse_pay_exception_category_name(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        pay_exception_category_name = _parse_pay_exception_category_name(d.pop("pay_exception_category_name", UNSET))

        is_shared = d.pop("is_shared", UNSET)

        shared_company_names = cast(list[str], d.pop("shared_company_names", UNSET))

        is_pinned = d.pop("is_pinned", UNSET)

        _employee_companies = d.pop("employee_companies", UNSET)
        employee_companies: list[EmployeeIndexCompany] | Unset = UNSET
        if _employee_companies is not UNSET:
            employee_companies = []
            for employee_companies_item_data in _employee_companies:
                employee_companies_item = EmployeeIndexCompany.from_dict(employee_companies_item_data)

                employee_companies.append(employee_companies_item)

        employee_index = cls(
            id=id,
            first_name=first_name,
            last_name=last_name,
            total_notes=total_notes,
            badge_number=badge_number,
            middle_name=middle_name,
            profile_picture_base64=profile_picture_base64,
            employment_type=employment_type,
            pay_exception_category_name=pay_exception_category_name,
            is_shared=is_shared,
            shared_company_names=shared_company_names,
            is_pinned=is_pinned,
            employee_companies=employee_companies,
        )

        employee_index.additional_properties = d
        return employee_index

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

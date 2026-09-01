from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast
from uuid import UUID

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.login_company_department_summary import LoginCompanyDepartmentSummary
    from ..models.login_company_site_summary import LoginCompanySiteSummary


T = TypeVar("T", bound="LoginCompanySummary")


@_attrs_define
class LoginCompanySummary:
    """
    Attributes:
        id (UUID):  Example: 123e4567-e89b-12d3-a456-426614174000.
        name (str):  Example: Company Name.
        departments (list[LoginCompanyDepartmentSummary]):
        sites (list[LoginCompanySiteSummary]):
        logo (None | str | Unset):  Example: data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAA....
    """

    id: UUID
    name: str
    departments: list[LoginCompanyDepartmentSummary]
    sites: list[LoginCompanySiteSummary]
    logo: None | str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id = str(self.id)

        name = self.name

        departments = []
        for departments_item_data in self.departments:
            departments_item = departments_item_data.to_dict()
            departments.append(departments_item)

        sites = []
        for sites_item_data in self.sites:
            sites_item = sites_item_data.to_dict()
            sites.append(sites_item)

        logo: None | str | Unset
        if isinstance(self.logo, Unset):
            logo = UNSET
        else:
            logo = self.logo

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id": id,
                "name": name,
                "departments": departments,
                "sites": sites,
            }
        )
        if logo is not UNSET:
            field_dict["logo"] = logo

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.login_company_department_summary import LoginCompanyDepartmentSummary  # noqa: PLC0415
        from ..models.login_company_site_summary import LoginCompanySiteSummary  # noqa: PLC0415

        d = dict(src_dict)
        id = UUID(d.pop("id"))

        name = d.pop("name")

        departments = []
        _departments = d.pop("departments")
        for departments_item_data in _departments:
            departments_item = LoginCompanyDepartmentSummary.from_dict(departments_item_data)

            departments.append(departments_item)

        sites = []
        _sites = d.pop("sites")
        for sites_item_data in _sites:
            sites_item = LoginCompanySiteSummary.from_dict(sites_item_data)

            sites.append(sites_item)

        def _parse_logo(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        logo = _parse_logo(d.pop("logo", UNSET))

        login_company_summary = cls(
            id=id,
            name=name,
            departments=departments,
            sites=sites,
            logo=logo,
        )

        login_company_summary.additional_properties = d
        return login_company_summary

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

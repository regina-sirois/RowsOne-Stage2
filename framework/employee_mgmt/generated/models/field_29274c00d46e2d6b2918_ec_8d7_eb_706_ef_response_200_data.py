from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.company_department_resource import CompanyDepartmentResource


T = TypeVar("T", bound="Field29274C00D46E2D6B2918Ec8D7Eb706EfResponse200Data")


@_attrs_define
class Field29274C00D46E2D6B2918Ec8D7Eb706EfResponse200Data:
    """
    Attributes:
        total_items (int | Unset):  Example: 25.
        total_pages (int | Unset):  Example: 3.
        page (int | Unset):  Example: 1.
        items_per_page (int | Unset): Items per page. `0` when fetching all items (itemsPerPage=*) with an empty result
            set. Example: 10.
        items (list[CompanyDepartmentResource] | Unset):
    """

    total_items: int | Unset = UNSET
    total_pages: int | Unset = UNSET
    page: int | Unset = UNSET
    items_per_page: int | Unset = UNSET
    items: list[CompanyDepartmentResource] | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        total_items = self.total_items

        total_pages = self.total_pages

        page = self.page

        items_per_page = self.items_per_page

        items: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.items, Unset):
            items = []
            for items_item_data in self.items:
                items_item = items_item_data.to_dict()
                items.append(items_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if total_items is not UNSET:
            field_dict["totalItems"] = total_items
        if total_pages is not UNSET:
            field_dict["totalPages"] = total_pages
        if page is not UNSET:
            field_dict["page"] = page
        if items_per_page is not UNSET:
            field_dict["itemsPerPage"] = items_per_page
        if items is not UNSET:
            field_dict["items"] = items

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.company_department_resource import CompanyDepartmentResource  # noqa: PLC0415

        d = dict(src_dict)
        total_items = d.pop("totalItems", UNSET)

        total_pages = d.pop("totalPages", UNSET)

        page = d.pop("page", UNSET)

        items_per_page = d.pop("itemsPerPage", UNSET)

        _items = d.pop("items", UNSET)
        items: list[CompanyDepartmentResource] | Unset = UNSET
        if _items is not UNSET:
            items = []
            for items_item_data in _items:
                items_item = CompanyDepartmentResource.from_dict(items_item_data)

                items.append(items_item)

        field_29274c00d46e2d6b2918_ec_8d7_eb_706_ef_response_200_data = cls(
            total_items=total_items,
            total_pages=total_pages,
            page=page,
            items_per_page=items_per_page,
            items=items,
        )

        field_29274c00d46e2d6b2918_ec_8d7_eb_706_ef_response_200_data.additional_properties = d
        return field_29274c00d46e2d6b2918_ec_8d7_eb_706_ef_response_200_data

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

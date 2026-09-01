from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="PaginationFlatMeta")


@_attrs_define
class PaginationFlatMeta:
    """Flat pagination fields emitted alongside `data.items` by legacy paginated responses.

    Attributes:
        total_items (int | Unset):  Example: 25.
        total_pages (int | Unset):  Example: 3.
        page (int | Unset):  Example: 1.
        items_per_page (int | Unset): Items per page. `0` when fetching all items (itemsPerPage=*) with an empty result
            set. Example: 10.
    """

    total_items: int | Unset = UNSET
    total_pages: int | Unset = UNSET
    page: int | Unset = UNSET
    items_per_page: int | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        total_items = self.total_items

        total_pages = self.total_pages

        page = self.page

        items_per_page = self.items_per_page

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

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        total_items = d.pop("totalItems", UNSET)

        total_pages = d.pop("totalPages", UNSET)

        page = d.pop("page", UNSET)

        items_per_page = d.pop("itemsPerPage", UNSET)

        pagination_flat_meta = cls(
            total_items=total_items,
            total_pages=total_pages,
            page=page,
            items_per_page=items_per_page,
        )

        pagination_flat_meta.additional_properties = d
        return pagination_flat_meta

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

from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.company_list_resource import CompanyListResource
    from ..models.get_companies_response_200_data_meta import GetCompaniesResponse200DataMeta


T = TypeVar("T", bound="GetCompaniesResponse200Data")


@_attrs_define
class GetCompaniesResponse200Data:
    """
    Attributes:
        items (list[CompanyListResource] | Unset):
        meta (GetCompaniesResponse200DataMeta | Unset):
    """

    items: list[CompanyListResource] | Unset = UNSET
    meta: GetCompaniesResponse200DataMeta | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        items: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.items, Unset):
            items = []
            for items_item_data in self.items:
                items_item = items_item_data.to_dict()
                items.append(items_item)

        meta: dict[str, Any] | Unset = UNSET
        if not isinstance(self.meta, Unset):
            meta = self.meta.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if items is not UNSET:
            field_dict["items"] = items
        if meta is not UNSET:
            field_dict["meta"] = meta

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.company_list_resource import CompanyListResource  # noqa: PLC0415
        from ..models.get_companies_response_200_data_meta import GetCompaniesResponse200DataMeta  # noqa: PLC0415

        d = dict(src_dict)
        _items = d.pop("items", UNSET)
        items: list[CompanyListResource] | Unset = UNSET
        if _items is not UNSET:
            items = []
            for items_item_data in _items:
                items_item = CompanyListResource.from_dict(items_item_data)

                items.append(items_item)

        _meta = d.pop("meta", UNSET)
        meta: GetCompaniesResponse200DataMeta | Unset
        if isinstance(_meta, Unset):
            meta = UNSET
        else:
            meta = GetCompaniesResponse200DataMeta.from_dict(_meta)

        get_companies_response_200_data = cls(
            items=items,
            meta=meta,
        )

        get_companies_response_200_data.additional_properties = d
        return get_companies_response_200_data

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

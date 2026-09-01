from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.pagination_meta_links_item import PaginationMetaLinksItem


T = TypeVar("T", bound="PaginationMeta")


@_attrs_define
class PaginationMeta:
    """Pagination metadata emitted under `data.meta` (Laravel paginator meta).

    Attributes:
        current_page (int | Unset): Reusable OpenAPI schemas for paginated API responses.

            Two response shapes exist:
            - `PaginationMeta` is emitted under `data.meta` by {@see ApiResponse::paginatedWithMeta()}.
            - `PaginationFlatMeta` is emitted as flat siblings of `data.items` by {@see ApiResponse::paginated()}. Example:
            1.
        from_ (int | None | Unset):  Example: 1.
        to (int | None | Unset):  Example: 10.
        per_page (int | Unset): Items per page. `0` when fetching all items (itemsPerPage=*) with an empty result set.
            Example: 10.
        last_page (int | Unset):  Example: 3.
        total (int | Unset):  Example: 25.
        path (str | Unset):  Example: https://api.example.com/api/resource.
        first_page_url (None | str | Unset):
        last_page_url (None | str | Unset):
        next_page_url (None | str | Unset):
        prev_page_url (None | str | Unset):
        links (list[PaginationMetaLinksItem] | Unset):
    """

    current_page: int | Unset = UNSET
    from_: int | None | Unset = UNSET
    to: int | None | Unset = UNSET
    per_page: int | Unset = UNSET
    last_page: int | Unset = UNSET
    total: int | Unset = UNSET
    path: str | Unset = UNSET
    first_page_url: None | str | Unset = UNSET
    last_page_url: None | str | Unset = UNSET
    next_page_url: None | str | Unset = UNSET
    prev_page_url: None | str | Unset = UNSET
    links: list[PaginationMetaLinksItem] | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        current_page = self.current_page

        from_: int | None | Unset
        if isinstance(self.from_, Unset):
            from_ = UNSET
        else:
            from_ = self.from_

        to: int | None | Unset
        if isinstance(self.to, Unset):
            to = UNSET
        else:
            to = self.to

        per_page = self.per_page

        last_page = self.last_page

        total = self.total

        path = self.path

        first_page_url: None | str | Unset
        if isinstance(self.first_page_url, Unset):
            first_page_url = UNSET
        else:
            first_page_url = self.first_page_url

        last_page_url: None | str | Unset
        if isinstance(self.last_page_url, Unset):
            last_page_url = UNSET
        else:
            last_page_url = self.last_page_url

        next_page_url: None | str | Unset
        if isinstance(self.next_page_url, Unset):
            next_page_url = UNSET
        else:
            next_page_url = self.next_page_url

        prev_page_url: None | str | Unset
        if isinstance(self.prev_page_url, Unset):
            prev_page_url = UNSET
        else:
            prev_page_url = self.prev_page_url

        links: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.links, Unset):
            links = []
            for links_item_data in self.links:
                links_item = links_item_data.to_dict()
                links.append(links_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if current_page is not UNSET:
            field_dict["current_page"] = current_page
        if from_ is not UNSET:
            field_dict["from"] = from_
        if to is not UNSET:
            field_dict["to"] = to
        if per_page is not UNSET:
            field_dict["per_page"] = per_page
        if last_page is not UNSET:
            field_dict["last_page"] = last_page
        if total is not UNSET:
            field_dict["total"] = total
        if path is not UNSET:
            field_dict["path"] = path
        if first_page_url is not UNSET:
            field_dict["first_page_url"] = first_page_url
        if last_page_url is not UNSET:
            field_dict["last_page_url"] = last_page_url
        if next_page_url is not UNSET:
            field_dict["next_page_url"] = next_page_url
        if prev_page_url is not UNSET:
            field_dict["prev_page_url"] = prev_page_url
        if links is not UNSET:
            field_dict["links"] = links

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.pagination_meta_links_item import PaginationMetaLinksItem  # noqa: PLC0415

        d = dict(src_dict)
        current_page = d.pop("current_page", UNSET)

        def _parse_from_(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        from_ = _parse_from_(d.pop("from", UNSET))

        def _parse_to(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        to = _parse_to(d.pop("to", UNSET))

        per_page = d.pop("per_page", UNSET)

        last_page = d.pop("last_page", UNSET)

        total = d.pop("total", UNSET)

        path = d.pop("path", UNSET)

        def _parse_first_page_url(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        first_page_url = _parse_first_page_url(d.pop("first_page_url", UNSET))

        def _parse_last_page_url(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        last_page_url = _parse_last_page_url(d.pop("last_page_url", UNSET))

        def _parse_next_page_url(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        next_page_url = _parse_next_page_url(d.pop("next_page_url", UNSET))

        def _parse_prev_page_url(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        prev_page_url = _parse_prev_page_url(d.pop("prev_page_url", UNSET))

        _links = d.pop("links", UNSET)
        links: list[PaginationMetaLinksItem] | Unset = UNSET
        if _links is not UNSET:
            links = []
            for links_item_data in _links:
                links_item = PaginationMetaLinksItem.from_dict(links_item_data)

                links.append(links_item)

        pagination_meta = cls(
            current_page=current_page,
            from_=from_,
            to=to,
            per_page=per_page,
            last_page=last_page,
            total=total,
            path=path,
            first_page_url=first_page_url,
            last_page_url=last_page_url,
            next_page_url=next_page_url,
            prev_page_url=prev_page_url,
            links=links,
        )

        pagination_meta.additional_properties = d
        return pagination_meta

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

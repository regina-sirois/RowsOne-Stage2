from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="AddressResource")


@_attrs_define
class AddressResource:
    """Address resource

    Attributes:
        id (int | Unset): Address ID Example: 1.
        address_line1 (str | Unset): First line of the address
        address_line2 (None | str | Unset): Second line of the address
        city (str | Unset): City
        state (str | Unset): State abbreviation (2 characters)
        zip_ (str | Unset): ZIP code
        country (str | Unset): Country
        latitude (float | None | Unset): Latitude
        longitude (float | None | Unset): Longitude
    """

    id: int | Unset = UNSET
    address_line1: str | Unset = UNSET
    address_line2: None | str | Unset = UNSET
    city: str | Unset = UNSET
    state: str | Unset = UNSET
    zip_: str | Unset = UNSET
    country: str | Unset = UNSET
    latitude: float | None | Unset = UNSET
    longitude: float | None | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id = self.id

        address_line1 = self.address_line1

        address_line2: None | str | Unset
        if isinstance(self.address_line2, Unset):
            address_line2 = UNSET
        else:
            address_line2 = self.address_line2

        city = self.city

        state = self.state

        zip_ = self.zip_

        country = self.country

        latitude: float | None | Unset
        if isinstance(self.latitude, Unset):
            latitude = UNSET
        else:
            latitude = self.latitude

        longitude: float | None | Unset
        if isinstance(self.longitude, Unset):
            longitude = UNSET
        else:
            longitude = self.longitude

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if id is not UNSET:
            field_dict["id"] = id
        if address_line1 is not UNSET:
            field_dict["address_line1"] = address_line1
        if address_line2 is not UNSET:
            field_dict["address_line2"] = address_line2
        if city is not UNSET:
            field_dict["city"] = city
        if state is not UNSET:
            field_dict["state"] = state
        if zip_ is not UNSET:
            field_dict["zip"] = zip_
        if country is not UNSET:
            field_dict["country"] = country
        if latitude is not UNSET:
            field_dict["latitude"] = latitude
        if longitude is not UNSET:
            field_dict["longitude"] = longitude

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        id = d.pop("id", UNSET)

        address_line1 = d.pop("address_line1", UNSET)

        def _parse_address_line2(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        address_line2 = _parse_address_line2(d.pop("address_line2", UNSET))

        city = d.pop("city", UNSET)

        state = d.pop("state", UNSET)

        zip_ = d.pop("zip", UNSET)

        country = d.pop("country", UNSET)

        def _parse_latitude(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        latitude = _parse_latitude(d.pop("latitude", UNSET))

        def _parse_longitude(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        longitude = _parse_longitude(d.pop("longitude", UNSET))

        address_resource = cls(
            id=id,
            address_line1=address_line1,
            address_line2=address_line2,
            city=city,
            state=state,
            zip_=zip_,
            country=country,
            latitude=latitude,
            longitude=longitude,
        )

        address_resource.additional_properties = d
        return address_resource

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

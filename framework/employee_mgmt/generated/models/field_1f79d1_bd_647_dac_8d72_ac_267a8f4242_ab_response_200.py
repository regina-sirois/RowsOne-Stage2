from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.location_type_resource import LocationTypeResource


T = TypeVar("T", bound="Field1F79D1Bd647Dac8D72Ac267A8F4242AbResponse200")


@_attrs_define
class Field1F79D1Bd647Dac8D72Ac267A8F4242AbResponse200:
    """
    Attributes:
        message (str | Unset):  Example: Location types retrieved successfully..
        error (bool | Unset):  Example: False.
        data (list[LocationTypeResource] | Unset):
    """

    message: str | Unset = UNSET
    error: bool | Unset = UNSET
    data: list[LocationTypeResource] | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        message = self.message

        error = self.error

        data: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.data, Unset):
            data = []
            for data_item_data in self.data:
                data_item = data_item_data.to_dict()
                data.append(data_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if message is not UNSET:
            field_dict["message"] = message
        if error is not UNSET:
            field_dict["error"] = error
        if data is not UNSET:
            field_dict["data"] = data

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.location_type_resource import LocationTypeResource  # noqa: PLC0415

        d = dict(src_dict)
        message = d.pop("message", UNSET)

        error = d.pop("error", UNSET)

        _data = d.pop("data", UNSET)
        data: list[LocationTypeResource] | Unset = UNSET
        if _data is not UNSET:
            data = []
            for data_item_data in _data:
                data_item = LocationTypeResource.from_dict(data_item_data)

                data.append(data_item)

        field_1f79d1_bd_647_dac_8d72_ac_267a8f4242_ab_response_200 = cls(
            message=message,
            error=error,
            data=data,
        )

        field_1f79d1_bd_647_dac_8d72_ac_267a8f4242_ab_response_200.additional_properties = d
        return field_1f79d1_bd_647_dac_8d72_ac_267a8f4242_ab_response_200

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

from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="EmployeePositionRate")


@_attrs_define
class EmployeePositionRate:
    """A single pay rate for an employee position. Monetary fields are masked when the viewer lacks the pay-rate permission
    for the host company.

        Attributes:
            amount (Any | Unset): Numeric when visible, otherwise a masked string Example: 25.5.
            exception_rate (Any | Unset): Numeric when visible, otherwise a masked string Example: 30.
            pay_classification (str | Unset):  Example: hourly.
            flsa_status (str | Unset):  Example: non_exempt.
            start_date (datetime.datetime | Unset):  Example: 2024-01-15T00:00:00+00:00.
            end_date (datetime.datetime | None | Unset):  Example: 2025-06-30T00:00:00+00:00.
    """

    amount: Any | Unset = UNSET
    exception_rate: Any | Unset = UNSET
    pay_classification: str | Unset = UNSET
    flsa_status: str | Unset = UNSET
    start_date: datetime.datetime | Unset = UNSET
    end_date: datetime.datetime | None | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        amount = self.amount

        exception_rate = self.exception_rate

        pay_classification = self.pay_classification

        flsa_status = self.flsa_status

        start_date: str | Unset = UNSET
        if not isinstance(self.start_date, Unset):
            start_date = self.start_date.isoformat()

        end_date: None | str | Unset
        if isinstance(self.end_date, Unset):
            end_date = UNSET
        elif isinstance(self.end_date, datetime.datetime):
            end_date = self.end_date.isoformat()
        else:
            end_date = self.end_date

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if amount is not UNSET:
            field_dict["amount"] = amount
        if exception_rate is not UNSET:
            field_dict["exception_rate"] = exception_rate
        if pay_classification is not UNSET:
            field_dict["pay_classification"] = pay_classification
        if flsa_status is not UNSET:
            field_dict["flsa_status"] = flsa_status
        if start_date is not UNSET:
            field_dict["start_date"] = start_date
        if end_date is not UNSET:
            field_dict["end_date"] = end_date

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        amount = d.pop("amount", UNSET)

        exception_rate = d.pop("exception_rate", UNSET)

        pay_classification = d.pop("pay_classification", UNSET)

        flsa_status = d.pop("flsa_status", UNSET)

        _start_date = d.pop("start_date", UNSET)
        start_date: datetime.datetime | Unset
        if isinstance(_start_date, Unset):
            start_date = UNSET
        else:
            start_date = datetime.datetime.fromisoformat(_start_date)

        def _parse_end_date(data: object) -> datetime.datetime | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                end_date_type_0 = datetime.datetime.fromisoformat(data)

                return end_date_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(datetime.datetime | None | Unset, data)

        end_date = _parse_end_date(d.pop("end_date", UNSET))

        employee_position_rate = cls(
            amount=amount,
            exception_rate=exception_rate,
            pay_classification=pay_classification,
            flsa_status=flsa_status,
            start_date=start_date,
            end_date=end_date,
        )

        employee_position_rate.additional_properties = d
        return employee_position_rate

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

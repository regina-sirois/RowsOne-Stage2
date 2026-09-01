from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast
from uuid import UUID

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.employee_position_rate import EmployeePositionRate


T = TypeVar("T", bound="EmployeePosition")


@_attrs_define
class EmployeePosition:
    """Employee position representation for API responses

    Attributes:
        employee_position_id (int):  Example: 1.
        company_position_id (int):  Example: 42.
        is_primary (bool):  Example: True.
        employee_company_id (int | Unset):  Example: 10.
        position_name (str | Unset): Catalog position name from the Position model. Not the optional job_title override.
            Example: Registered Nurse.
        company_position_name (str | Unset): Deprecated. Use position_name instead. Retained for backwards compatibility
            until MVP. Example: Registered Nurse.
        department_name (None | str | Unset): Name of the department the company position belongs to. Example: Nursing.
        company_department_name (str | Unset): Deprecated. Use department_name instead. Retained for backwards
            compatibility until MVP. Example: Engineering.
        company_id (UUID | Unset):  Example: 550e8400-e29b-41d4-a716-446655440000.
        company_name (str | Unset):  Example: Acme Corp.
        site_names (list[str] | Unset):
        job_title (None | str | Unset): Optional employee-specific title for this assignment. Matches request field
            job_title; null when unset — does not fall back to position_name. Example: Charge Nurse.
        upcoming_primary_start_date (datetime.datetime | None | Unset): When this position becomes primary via a
            scheduled primary switch. Null unless this position is the destination of a pending switch. Example:
            2026-02-28T00:00:00+00:00.
        status (str | Unset):  Example: active.
        is_enrolled_in_union (bool | Unset):  Example: False.
        start_date (datetime.datetime | None | Unset):  Example: 2024-01-15T00:00:00+00:00.
        end_date (datetime.datetime | None | Unset):  Example: 2025-06-30T00:00:00+00:00.
        pay_classification (None | str | Unset):  Example: hourly.
        flsa_status (None | str | Unset):  Example: non_exempt.
        allocated_standard_hours (float | None | Unset):  Example: 40.
        rate_of_pay (EmployeePositionRate | None | Unset): Current pay rate; monetary fields are masked without the pay-
            rate permission. Null when no active rate exists.
        rates (list[EmployeePositionRate] | Unset):
    """

    employee_position_id: int
    company_position_id: int
    is_primary: bool
    employee_company_id: int | Unset = UNSET
    position_name: str | Unset = UNSET
    company_position_name: str | Unset = UNSET
    department_name: None | str | Unset = UNSET
    company_department_name: str | Unset = UNSET
    company_id: UUID | Unset = UNSET
    company_name: str | Unset = UNSET
    site_names: list[str] | Unset = UNSET
    job_title: None | str | Unset = UNSET
    upcoming_primary_start_date: datetime.datetime | None | Unset = UNSET
    status: str | Unset = UNSET
    is_enrolled_in_union: bool | Unset = UNSET
    start_date: datetime.datetime | None | Unset = UNSET
    end_date: datetime.datetime | None | Unset = UNSET
    pay_classification: None | str | Unset = UNSET
    flsa_status: None | str | Unset = UNSET
    allocated_standard_hours: float | None | Unset = UNSET
    rate_of_pay: EmployeePositionRate | None | Unset = UNSET
    rates: list[EmployeePositionRate] | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.employee_position_rate import EmployeePositionRate  # noqa: PLC0415

        employee_position_id = self.employee_position_id

        company_position_id = self.company_position_id

        is_primary = self.is_primary

        employee_company_id = self.employee_company_id

        position_name = self.position_name

        company_position_name = self.company_position_name

        department_name: None | str | Unset
        if isinstance(self.department_name, Unset):
            department_name = UNSET
        else:
            department_name = self.department_name

        company_department_name = self.company_department_name

        company_id: str | Unset = UNSET
        if not isinstance(self.company_id, Unset):
            company_id = str(self.company_id)

        company_name = self.company_name

        site_names: list[str] | Unset = UNSET
        if not isinstance(self.site_names, Unset):
            site_names = self.site_names

        job_title: None | str | Unset
        if isinstance(self.job_title, Unset):
            job_title = UNSET
        else:
            job_title = self.job_title

        upcoming_primary_start_date: None | str | Unset
        if isinstance(self.upcoming_primary_start_date, Unset):
            upcoming_primary_start_date = UNSET
        elif isinstance(self.upcoming_primary_start_date, datetime.datetime):
            upcoming_primary_start_date = self.upcoming_primary_start_date.isoformat()
        else:
            upcoming_primary_start_date = self.upcoming_primary_start_date

        status = self.status

        is_enrolled_in_union = self.is_enrolled_in_union

        start_date: None | str | Unset
        if isinstance(self.start_date, Unset):
            start_date = UNSET
        elif isinstance(self.start_date, datetime.datetime):
            start_date = self.start_date.isoformat()
        else:
            start_date = self.start_date

        end_date: None | str | Unset
        if isinstance(self.end_date, Unset):
            end_date = UNSET
        elif isinstance(self.end_date, datetime.datetime):
            end_date = self.end_date.isoformat()
        else:
            end_date = self.end_date

        pay_classification: None | str | Unset
        if isinstance(self.pay_classification, Unset):
            pay_classification = UNSET
        else:
            pay_classification = self.pay_classification

        flsa_status: None | str | Unset
        if isinstance(self.flsa_status, Unset):
            flsa_status = UNSET
        else:
            flsa_status = self.flsa_status

        allocated_standard_hours: float | None | Unset
        if isinstance(self.allocated_standard_hours, Unset):
            allocated_standard_hours = UNSET
        else:
            allocated_standard_hours = self.allocated_standard_hours

        rate_of_pay: dict[str, Any] | None | Unset
        if isinstance(self.rate_of_pay, Unset):
            rate_of_pay = UNSET
        elif isinstance(self.rate_of_pay, EmployeePositionRate):
            rate_of_pay = self.rate_of_pay.to_dict()
        else:
            rate_of_pay = self.rate_of_pay

        rates: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.rates, Unset):
            rates = []
            for rates_item_data in self.rates:
                rates_item = rates_item_data.to_dict()
                rates.append(rates_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "employee_position_id": employee_position_id,
                "company_position_id": company_position_id,
                "is_primary": is_primary,
            }
        )
        if employee_company_id is not UNSET:
            field_dict["employee_company_id"] = employee_company_id
        if position_name is not UNSET:
            field_dict["position_name"] = position_name
        if company_position_name is not UNSET:
            field_dict["company_position_name"] = company_position_name
        if department_name is not UNSET:
            field_dict["department_name"] = department_name
        if company_department_name is not UNSET:
            field_dict["company_department_name"] = company_department_name
        if company_id is not UNSET:
            field_dict["company_id"] = company_id
        if company_name is not UNSET:
            field_dict["company_name"] = company_name
        if site_names is not UNSET:
            field_dict["site_names"] = site_names
        if job_title is not UNSET:
            field_dict["job_title"] = job_title
        if upcoming_primary_start_date is not UNSET:
            field_dict["upcoming_primary_start_date"] = upcoming_primary_start_date
        if status is not UNSET:
            field_dict["status"] = status
        if is_enrolled_in_union is not UNSET:
            field_dict["is_enrolled_in_union"] = is_enrolled_in_union
        if start_date is not UNSET:
            field_dict["start_date"] = start_date
        if end_date is not UNSET:
            field_dict["end_date"] = end_date
        if pay_classification is not UNSET:
            field_dict["pay_classification"] = pay_classification
        if flsa_status is not UNSET:
            field_dict["flsa_status"] = flsa_status
        if allocated_standard_hours is not UNSET:
            field_dict["allocated_standard_hours"] = allocated_standard_hours
        if rate_of_pay is not UNSET:
            field_dict["rate_of_pay"] = rate_of_pay
        if rates is not UNSET:
            field_dict["rates"] = rates

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.employee_position_rate import EmployeePositionRate  # noqa: PLC0415

        d = dict(src_dict)
        employee_position_id = d.pop("employee_position_id")

        company_position_id = d.pop("company_position_id")

        is_primary = d.pop("is_primary")

        employee_company_id = d.pop("employee_company_id", UNSET)

        position_name = d.pop("position_name", UNSET)

        company_position_name = d.pop("company_position_name", UNSET)

        def _parse_department_name(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        department_name = _parse_department_name(d.pop("department_name", UNSET))

        company_department_name = d.pop("company_department_name", UNSET)

        _company_id = d.pop("company_id", UNSET)
        company_id: UUID | Unset
        if isinstance(_company_id, Unset):
            company_id = UNSET
        else:
            company_id = UUID(_company_id)

        company_name = d.pop("company_name", UNSET)

        site_names = cast(list[str], d.pop("site_names", UNSET))

        def _parse_job_title(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        job_title = _parse_job_title(d.pop("job_title", UNSET))

        def _parse_upcoming_primary_start_date(data: object) -> datetime.datetime | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                upcoming_primary_start_date_type_0 = datetime.datetime.fromisoformat(data)

                return upcoming_primary_start_date_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(datetime.datetime | None | Unset, data)

        upcoming_primary_start_date = _parse_upcoming_primary_start_date(d.pop("upcoming_primary_start_date", UNSET))

        status = d.pop("status", UNSET)

        is_enrolled_in_union = d.pop("is_enrolled_in_union", UNSET)

        def _parse_start_date(data: object) -> datetime.datetime | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                start_date_type_0 = datetime.datetime.fromisoformat(data)

                return start_date_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(datetime.datetime | None | Unset, data)

        start_date = _parse_start_date(d.pop("start_date", UNSET))

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

        def _parse_pay_classification(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        pay_classification = _parse_pay_classification(d.pop("pay_classification", UNSET))

        def _parse_flsa_status(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        flsa_status = _parse_flsa_status(d.pop("flsa_status", UNSET))

        def _parse_allocated_standard_hours(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        allocated_standard_hours = _parse_allocated_standard_hours(d.pop("allocated_standard_hours", UNSET))

        def _parse_rate_of_pay(data: object) -> EmployeePositionRate | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                rate_of_pay_type_0 = EmployeePositionRate.from_dict(data)

                return rate_of_pay_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(EmployeePositionRate | None | Unset, data)

        rate_of_pay = _parse_rate_of_pay(d.pop("rate_of_pay", UNSET))

        _rates = d.pop("rates", UNSET)
        rates: list[EmployeePositionRate] | Unset = UNSET
        if _rates is not UNSET:
            rates = []
            for rates_item_data in _rates:
                rates_item = EmployeePositionRate.from_dict(rates_item_data)

                rates.append(rates_item)

        employee_position = cls(
            employee_position_id=employee_position_id,
            company_position_id=company_position_id,
            is_primary=is_primary,
            employee_company_id=employee_company_id,
            position_name=position_name,
            company_position_name=company_position_name,
            department_name=department_name,
            company_department_name=company_department_name,
            company_id=company_id,
            company_name=company_name,
            site_names=site_names,
            job_title=job_title,
            upcoming_primary_start_date=upcoming_primary_start_date,
            status=status,
            is_enrolled_in_union=is_enrolled_in_union,
            start_date=start_date,
            end_date=end_date,
            pay_classification=pay_classification,
            flsa_status=flsa_status,
            allocated_standard_hours=allocated_standard_hours,
            rate_of_pay=rate_of_pay,
            rates=rates,
        )

        employee_position.additional_properties = d
        return employee_position

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

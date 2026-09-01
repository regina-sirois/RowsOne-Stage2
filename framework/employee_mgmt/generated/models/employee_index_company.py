from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.employee_index_company_status import EmployeeIndexCompanyStatus
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.employee_index_position import EmployeeIndexPosition


T = TypeVar("T", bound="EmployeeIndexCompany")


@_attrs_define
class EmployeeIndexCompany:
    """The current state of one employee-company relationship, nested under an employee in the Employees table. Superseded
    rehire history is omitted, so a company appears at most once per employee; use GET /api/employees/{employee} for the
    full employment history.

        Attributes:
            company_name (str):  Example: Acme Corp.
            status (EmployeeIndexCompanyStatus): Current status of this employee-company relationship. Example: active.
            is_primary (bool):  Example: True.
            positions (list[EmployeeIndexPosition]):
            date_of_hire (datetime.date | None | Unset):  Example: 2024-01-15.
            date_of_termination (datetime.date | None | Unset):  Example: 2025-06-30.
            termination_reason (None | str | Unset):  Example: Voluntary resignation.
            close_reason (None | str | Unset):  Example: Withdrew before start date.
            probation_start_date (datetime.date | None | Unset):  Example: 2024-01-15.
            probation_end_date (datetime.date | None | Unset):  Example: 2024-04-15.
            scheduled_suspension_start_date (datetime.date | None | Unset):  Example: 2026-04-08.
            rehire_flag (bool | Unset):  Example: False.
            agency_name (None | str | Unset):  Example: ABC Agency.
    """

    company_name: str
    status: EmployeeIndexCompanyStatus
    is_primary: bool
    positions: list[EmployeeIndexPosition]
    date_of_hire: datetime.date | None | Unset = UNSET
    date_of_termination: datetime.date | None | Unset = UNSET
    termination_reason: None | str | Unset = UNSET
    close_reason: None | str | Unset = UNSET
    probation_start_date: datetime.date | None | Unset = UNSET
    probation_end_date: datetime.date | None | Unset = UNSET
    scheduled_suspension_start_date: datetime.date | None | Unset = UNSET
    rehire_flag: bool | Unset = UNSET
    agency_name: None | str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        company_name = self.company_name

        status = self.status.value

        is_primary = self.is_primary

        positions = []
        for positions_item_data in self.positions:
            positions_item = positions_item_data.to_dict()
            positions.append(positions_item)

        date_of_hire: None | str | Unset
        if isinstance(self.date_of_hire, Unset):
            date_of_hire = UNSET
        elif isinstance(self.date_of_hire, datetime.date):
            date_of_hire = self.date_of_hire.isoformat()
        else:
            date_of_hire = self.date_of_hire

        date_of_termination: None | str | Unset
        if isinstance(self.date_of_termination, Unset):
            date_of_termination = UNSET
        elif isinstance(self.date_of_termination, datetime.date):
            date_of_termination = self.date_of_termination.isoformat()
        else:
            date_of_termination = self.date_of_termination

        termination_reason: None | str | Unset
        if isinstance(self.termination_reason, Unset):
            termination_reason = UNSET
        else:
            termination_reason = self.termination_reason

        close_reason: None | str | Unset
        if isinstance(self.close_reason, Unset):
            close_reason = UNSET
        else:
            close_reason = self.close_reason

        probation_start_date: None | str | Unset
        if isinstance(self.probation_start_date, Unset):
            probation_start_date = UNSET
        elif isinstance(self.probation_start_date, datetime.date):
            probation_start_date = self.probation_start_date.isoformat()
        else:
            probation_start_date = self.probation_start_date

        probation_end_date: None | str | Unset
        if isinstance(self.probation_end_date, Unset):
            probation_end_date = UNSET
        elif isinstance(self.probation_end_date, datetime.date):
            probation_end_date = self.probation_end_date.isoformat()
        else:
            probation_end_date = self.probation_end_date

        scheduled_suspension_start_date: None | str | Unset
        if isinstance(self.scheduled_suspension_start_date, Unset):
            scheduled_suspension_start_date = UNSET
        elif isinstance(self.scheduled_suspension_start_date, datetime.date):
            scheduled_suspension_start_date = self.scheduled_suspension_start_date.isoformat()
        else:
            scheduled_suspension_start_date = self.scheduled_suspension_start_date

        rehire_flag = self.rehire_flag

        agency_name: None | str | Unset
        if isinstance(self.agency_name, Unset):
            agency_name = UNSET
        else:
            agency_name = self.agency_name

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "company_name": company_name,
                "status": status,
                "is_primary": is_primary,
                "positions": positions,
            }
        )
        if date_of_hire is not UNSET:
            field_dict["date_of_hire"] = date_of_hire
        if date_of_termination is not UNSET:
            field_dict["date_of_termination"] = date_of_termination
        if termination_reason is not UNSET:
            field_dict["termination_reason"] = termination_reason
        if close_reason is not UNSET:
            field_dict["close_reason"] = close_reason
        if probation_start_date is not UNSET:
            field_dict["probation_start_date"] = probation_start_date
        if probation_end_date is not UNSET:
            field_dict["probation_end_date"] = probation_end_date
        if scheduled_suspension_start_date is not UNSET:
            field_dict["scheduled_suspension_start_date"] = scheduled_suspension_start_date
        if rehire_flag is not UNSET:
            field_dict["rehire_flag"] = rehire_flag
        if agency_name is not UNSET:
            field_dict["agency_name"] = agency_name

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.employee_index_position import EmployeeIndexPosition  # noqa: PLC0415

        d = dict(src_dict)
        company_name = d.pop("company_name")

        status = EmployeeIndexCompanyStatus(d.pop("status"))

        is_primary = d.pop("is_primary")

        positions = []
        _positions = d.pop("positions")
        for positions_item_data in _positions:
            positions_item = EmployeeIndexPosition.from_dict(positions_item_data)

            positions.append(positions_item)

        def _parse_date_of_hire(data: object) -> datetime.date | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                date_of_hire_type_0 = datetime.date.fromisoformat(data)

                return date_of_hire_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(datetime.date | None | Unset, data)

        date_of_hire = _parse_date_of_hire(d.pop("date_of_hire", UNSET))

        def _parse_date_of_termination(data: object) -> datetime.date | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                date_of_termination_type_0 = datetime.date.fromisoformat(data)

                return date_of_termination_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(datetime.date | None | Unset, data)

        date_of_termination = _parse_date_of_termination(d.pop("date_of_termination", UNSET))

        def _parse_termination_reason(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        termination_reason = _parse_termination_reason(d.pop("termination_reason", UNSET))

        def _parse_close_reason(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        close_reason = _parse_close_reason(d.pop("close_reason", UNSET))

        def _parse_probation_start_date(data: object) -> datetime.date | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                probation_start_date_type_0 = datetime.date.fromisoformat(data)

                return probation_start_date_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(datetime.date | None | Unset, data)

        probation_start_date = _parse_probation_start_date(d.pop("probation_start_date", UNSET))

        def _parse_probation_end_date(data: object) -> datetime.date | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                probation_end_date_type_0 = datetime.date.fromisoformat(data)

                return probation_end_date_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(datetime.date | None | Unset, data)

        probation_end_date = _parse_probation_end_date(d.pop("probation_end_date", UNSET))

        def _parse_scheduled_suspension_start_date(data: object) -> datetime.date | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                scheduled_suspension_start_date_type_0 = datetime.date.fromisoformat(data)

                return scheduled_suspension_start_date_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(datetime.date | None | Unset, data)

        scheduled_suspension_start_date = _parse_scheduled_suspension_start_date(
            d.pop("scheduled_suspension_start_date", UNSET)
        )

        rehire_flag = d.pop("rehire_flag", UNSET)

        def _parse_agency_name(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        agency_name = _parse_agency_name(d.pop("agency_name", UNSET))

        employee_index_company = cls(
            company_name=company_name,
            status=status,
            is_primary=is_primary,
            positions=positions,
            date_of_hire=date_of_hire,
            date_of_termination=date_of_termination,
            termination_reason=termination_reason,
            close_reason=close_reason,
            probation_start_date=probation_start_date,
            probation_end_date=probation_end_date,
            scheduled_suspension_start_date=scheduled_suspension_start_date,
            rehire_flag=rehire_flag,
            agency_name=agency_name,
        )

        employee_index_company.additional_properties = d
        return employee_index_company

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

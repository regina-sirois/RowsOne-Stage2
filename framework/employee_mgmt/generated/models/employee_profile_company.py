from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast
from uuid import UUID

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.employee_profile_company_status import EmployeeProfileCompanyStatus
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.employee_position import EmployeePosition
    from ..models.employee_profile_company_scheduled_termination_type_0 import (
        EmployeeProfileCompanyScheduledTerminationType0,
    )
    from ..models.employee_profile_company_suspension_type_0 import EmployeeProfileCompanySuspensionType0


T = TypeVar("T", bound="EmployeeProfileCompany")


@_attrs_define
class EmployeeProfileCompany:
    """A company employment group nested under an employee profile payload.

    Attributes:
        employee_company_id (int | Unset):  Example: 42.
        company_id (UUID | Unset):  Example: 550e8400-e29b-41d4-a716-446655440000.
        company_name (str | Unset):  Example: Evergreen Wellness Center.
        status (EmployeeProfileCompanyStatus | Unset):  Example: active.
        rehire_flag (bool | Unset):  Example: False.
        is_primary (bool | Unset):  Example: True.
        agency_id (None | Unset | UUID):  Example: 550e8400-e29b-41d4-a716-446655440000.
        agency_name (None | str | Unset):  Example: Bright Staffing.
        is_suspended (bool | Unset): Whether this employment is under an active suspension Example: False.
        has_workspace_role (bool | Unset): Whether the employee's user has a non-employee workspace role scoped to this
            company (or its sites/departments, or org-wide). The Front End uses this to show a non-blocking 'still has
            workspace access' warning in the termination modal; termination does not revoke workspace access. Example:
            False.
        termination_reason (None | str | Unset):  Example: Voluntary resignation.
        close_reason (None | str | Unset):  Example: Withdrew before start date.
        date_of_hire (datetime.date | None | Unset):  Example: 2024-01-15.
        last_day_worked (datetime.date | None | Unset): Latest clock_out date for this company, or null if none Example:
            2024-06-30.
        probation_end_date (datetime.date | None | Unset):  Example: 2026-03-30.
        scheduled_termination (EmployeeProfileCompanyScheduledTerminationType0 | None | Unset):
        suspension (EmployeeProfileCompanySuspensionType0 | None | Unset):
        positions (list[EmployeePosition] | Unset):
    """

    employee_company_id: int | Unset = UNSET
    company_id: UUID | Unset = UNSET
    company_name: str | Unset = UNSET
    status: EmployeeProfileCompanyStatus | Unset = UNSET
    rehire_flag: bool | Unset = UNSET
    is_primary: bool | Unset = UNSET
    agency_id: None | Unset | UUID = UNSET
    agency_name: None | str | Unset = UNSET
    is_suspended: bool | Unset = UNSET
    has_workspace_role: bool | Unset = UNSET
    termination_reason: None | str | Unset = UNSET
    close_reason: None | str | Unset = UNSET
    date_of_hire: datetime.date | None | Unset = UNSET
    last_day_worked: datetime.date | None | Unset = UNSET
    probation_end_date: datetime.date | None | Unset = UNSET
    scheduled_termination: EmployeeProfileCompanyScheduledTerminationType0 | None | Unset = UNSET
    suspension: EmployeeProfileCompanySuspensionType0 | None | Unset = UNSET
    positions: list[EmployeePosition] | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.employee_profile_company_scheduled_termination_type_0 import (
            EmployeeProfileCompanyScheduledTerminationType0,  # noqa: PLC0415
        )
        from ..models.employee_profile_company_suspension_type_0 import (
            EmployeeProfileCompanySuspensionType0,  # noqa: PLC0415
        )

        employee_company_id = self.employee_company_id

        company_id: str | Unset = UNSET
        if not isinstance(self.company_id, Unset):
            company_id = str(self.company_id)

        company_name = self.company_name

        status: str | Unset = UNSET
        if not isinstance(self.status, Unset):
            status = self.status.value

        rehire_flag = self.rehire_flag

        is_primary = self.is_primary

        agency_id: None | str | Unset
        if isinstance(self.agency_id, Unset):
            agency_id = UNSET
        elif isinstance(self.agency_id, UUID):
            agency_id = str(self.agency_id)
        else:
            agency_id = self.agency_id

        agency_name: None | str | Unset
        if isinstance(self.agency_name, Unset):
            agency_name = UNSET
        else:
            agency_name = self.agency_name

        is_suspended = self.is_suspended

        has_workspace_role = self.has_workspace_role

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

        date_of_hire: None | str | Unset
        if isinstance(self.date_of_hire, Unset):
            date_of_hire = UNSET
        elif isinstance(self.date_of_hire, datetime.date):
            date_of_hire = self.date_of_hire.isoformat()
        else:
            date_of_hire = self.date_of_hire

        last_day_worked: None | str | Unset
        if isinstance(self.last_day_worked, Unset):
            last_day_worked = UNSET
        elif isinstance(self.last_day_worked, datetime.date):
            last_day_worked = self.last_day_worked.isoformat()
        else:
            last_day_worked = self.last_day_worked

        probation_end_date: None | str | Unset
        if isinstance(self.probation_end_date, Unset):
            probation_end_date = UNSET
        elif isinstance(self.probation_end_date, datetime.date):
            probation_end_date = self.probation_end_date.isoformat()
        else:
            probation_end_date = self.probation_end_date

        scheduled_termination: dict[str, Any] | None | Unset
        if isinstance(self.scheduled_termination, Unset):
            scheduled_termination = UNSET
        elif isinstance(self.scheduled_termination, EmployeeProfileCompanyScheduledTerminationType0):
            scheduled_termination = self.scheduled_termination.to_dict()
        else:
            scheduled_termination = self.scheduled_termination

        suspension: dict[str, Any] | None | Unset
        if isinstance(self.suspension, Unset):
            suspension = UNSET
        elif isinstance(self.suspension, EmployeeProfileCompanySuspensionType0):
            suspension = self.suspension.to_dict()
        else:
            suspension = self.suspension

        positions: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.positions, Unset):
            positions = []
            for positions_item_data in self.positions:
                positions_item = positions_item_data.to_dict()
                positions.append(positions_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if employee_company_id is not UNSET:
            field_dict["employee_company_id"] = employee_company_id
        if company_id is not UNSET:
            field_dict["company_id"] = company_id
        if company_name is not UNSET:
            field_dict["company_name"] = company_name
        if status is not UNSET:
            field_dict["status"] = status
        if rehire_flag is not UNSET:
            field_dict["rehire_flag"] = rehire_flag
        if is_primary is not UNSET:
            field_dict["is_primary"] = is_primary
        if agency_id is not UNSET:
            field_dict["agency_id"] = agency_id
        if agency_name is not UNSET:
            field_dict["agency_name"] = agency_name
        if is_suspended is not UNSET:
            field_dict["is_suspended"] = is_suspended
        if has_workspace_role is not UNSET:
            field_dict["has_workspace_role"] = has_workspace_role
        if termination_reason is not UNSET:
            field_dict["termination_reason"] = termination_reason
        if close_reason is not UNSET:
            field_dict["close_reason"] = close_reason
        if date_of_hire is not UNSET:
            field_dict["date_of_hire"] = date_of_hire
        if last_day_worked is not UNSET:
            field_dict["last_day_worked"] = last_day_worked
        if probation_end_date is not UNSET:
            field_dict["probation_end_date"] = probation_end_date
        if scheduled_termination is not UNSET:
            field_dict["scheduled_termination"] = scheduled_termination
        if suspension is not UNSET:
            field_dict["suspension"] = suspension
        if positions is not UNSET:
            field_dict["positions"] = positions

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.employee_position import EmployeePosition  # noqa: PLC0415
        from ..models.employee_profile_company_scheduled_termination_type_0 import (
            EmployeeProfileCompanyScheduledTerminationType0,  # noqa: PLC0415
        )
        from ..models.employee_profile_company_suspension_type_0 import (
            EmployeeProfileCompanySuspensionType0,  # noqa: PLC0415
        )

        d = dict(src_dict)
        employee_company_id = d.pop("employee_company_id", UNSET)

        _company_id = d.pop("company_id", UNSET)
        company_id: UUID | Unset
        if isinstance(_company_id, Unset):
            company_id = UNSET
        else:
            company_id = UUID(_company_id)

        company_name = d.pop("company_name", UNSET)

        _status = d.pop("status", UNSET)
        status: EmployeeProfileCompanyStatus | Unset
        if isinstance(_status, Unset):
            status = UNSET
        else:
            status = EmployeeProfileCompanyStatus(_status)

        rehire_flag = d.pop("rehire_flag", UNSET)

        is_primary = d.pop("is_primary", UNSET)

        def _parse_agency_id(data: object) -> None | Unset | UUID:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                agency_id_type_0 = UUID(data)

                return agency_id_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(None | Unset | UUID, data)

        agency_id = _parse_agency_id(d.pop("agency_id", UNSET))

        def _parse_agency_name(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        agency_name = _parse_agency_name(d.pop("agency_name", UNSET))

        is_suspended = d.pop("is_suspended", UNSET)

        has_workspace_role = d.pop("has_workspace_role", UNSET)

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

        def _parse_last_day_worked(data: object) -> datetime.date | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                last_day_worked_type_0 = datetime.date.fromisoformat(data)

                return last_day_worked_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(datetime.date | None | Unset, data)

        last_day_worked = _parse_last_day_worked(d.pop("last_day_worked", UNSET))

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

        def _parse_scheduled_termination(
            data: object,
        ) -> EmployeeProfileCompanyScheduledTerminationType0 | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                scheduled_termination_type_0 = EmployeeProfileCompanyScheduledTerminationType0.from_dict(data)

                return scheduled_termination_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(EmployeeProfileCompanyScheduledTerminationType0 | None | Unset, data)

        scheduled_termination = _parse_scheduled_termination(d.pop("scheduled_termination", UNSET))

        def _parse_suspension(data: object) -> EmployeeProfileCompanySuspensionType0 | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                suspension_type_0 = EmployeeProfileCompanySuspensionType0.from_dict(data)

                return suspension_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(EmployeeProfileCompanySuspensionType0 | None | Unset, data)

        suspension = _parse_suspension(d.pop("suspension", UNSET))

        _positions = d.pop("positions", UNSET)
        positions: list[EmployeePosition] | Unset = UNSET
        if _positions is not UNSET:
            positions = []
            for positions_item_data in _positions:
                positions_item = EmployeePosition.from_dict(positions_item_data)

                positions.append(positions_item)

        employee_profile_company = cls(
            employee_company_id=employee_company_id,
            company_id=company_id,
            company_name=company_name,
            status=status,
            rehire_flag=rehire_flag,
            is_primary=is_primary,
            agency_id=agency_id,
            agency_name=agency_name,
            is_suspended=is_suspended,
            has_workspace_role=has_workspace_role,
            termination_reason=termination_reason,
            close_reason=close_reason,
            date_of_hire=date_of_hire,
            last_day_worked=last_day_worked,
            probation_end_date=probation_end_date,
            scheduled_termination=scheduled_termination,
            suspension=suspension,
            positions=positions,
        )

        employee_profile_company.additional_properties = d
        return employee_profile_company

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

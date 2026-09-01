from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.employee_index_position_company_position_status import EmployeeIndexPositionCompanyPositionStatus
from ..types import UNSET, Unset

T = TypeVar("T", bound="EmployeeIndexPosition")


@_attrs_define
class EmployeeIndexPosition:
    """Position row for the Employees table, nested under an employee company.

    Attributes:
        employee_position_id (int):  Example: 1.
        company_position_name (str): Name of the assigned company position. Example: Registered Nurse.
        company_position_status (EmployeeIndexPositionCompanyPositionStatus): Status of the assigned company position;
            the table flags assignments to an inactive position. Example: active.
        department_name (None | str | Unset): Name of the department the company position belongs to. Example: Nursing.
        job_title (None | str | Unset):  Example: Charge Nurse.
        paid_by_company_name (None | str | Unset):  Example: Acme Corp.
        employment_classification (None | str | Unset):  Example: Full Time.
        pay_classification (None | str | Unset):  Example: hourly.
        flsa_status (None | str | Unset):  Example: non_exempt.
        payroll_frequency (None | str | Unset):  Example: bi_weekly.
    """

    employee_position_id: int
    company_position_name: str
    company_position_status: EmployeeIndexPositionCompanyPositionStatus
    department_name: None | str | Unset = UNSET
    job_title: None | str | Unset = UNSET
    paid_by_company_name: None | str | Unset = UNSET
    employment_classification: None | str | Unset = UNSET
    pay_classification: None | str | Unset = UNSET
    flsa_status: None | str | Unset = UNSET
    payroll_frequency: None | str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        employee_position_id = self.employee_position_id

        company_position_name = self.company_position_name

        company_position_status = self.company_position_status.value

        department_name: None | str | Unset
        if isinstance(self.department_name, Unset):
            department_name = UNSET
        else:
            department_name = self.department_name

        job_title: None | str | Unset
        if isinstance(self.job_title, Unset):
            job_title = UNSET
        else:
            job_title = self.job_title

        paid_by_company_name: None | str | Unset
        if isinstance(self.paid_by_company_name, Unset):
            paid_by_company_name = UNSET
        else:
            paid_by_company_name = self.paid_by_company_name

        employment_classification: None | str | Unset
        if isinstance(self.employment_classification, Unset):
            employment_classification = UNSET
        else:
            employment_classification = self.employment_classification

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

        payroll_frequency: None | str | Unset
        if isinstance(self.payroll_frequency, Unset):
            payroll_frequency = UNSET
        else:
            payroll_frequency = self.payroll_frequency

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "employee_position_id": employee_position_id,
                "company_position_name": company_position_name,
                "company_position_status": company_position_status,
            }
        )
        if department_name is not UNSET:
            field_dict["department_name"] = department_name
        if job_title is not UNSET:
            field_dict["job_title"] = job_title
        if paid_by_company_name is not UNSET:
            field_dict["paid_by_company_name"] = paid_by_company_name
        if employment_classification is not UNSET:
            field_dict["employment_classification"] = employment_classification
        if pay_classification is not UNSET:
            field_dict["pay_classification"] = pay_classification
        if flsa_status is not UNSET:
            field_dict["flsa_status"] = flsa_status
        if payroll_frequency is not UNSET:
            field_dict["payroll_frequency"] = payroll_frequency

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        employee_position_id = d.pop("employee_position_id")

        company_position_name = d.pop("company_position_name")

        company_position_status = EmployeeIndexPositionCompanyPositionStatus(d.pop("company_position_status"))

        def _parse_department_name(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        department_name = _parse_department_name(d.pop("department_name", UNSET))

        def _parse_job_title(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        job_title = _parse_job_title(d.pop("job_title", UNSET))

        def _parse_paid_by_company_name(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        paid_by_company_name = _parse_paid_by_company_name(d.pop("paid_by_company_name", UNSET))

        def _parse_employment_classification(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        employment_classification = _parse_employment_classification(d.pop("employment_classification", UNSET))

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

        def _parse_payroll_frequency(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        payroll_frequency = _parse_payroll_frequency(d.pop("payroll_frequency", UNSET))

        employee_index_position = cls(
            employee_position_id=employee_position_id,
            company_position_name=company_position_name,
            company_position_status=company_position_status,
            department_name=department_name,
            job_title=job_title,
            paid_by_company_name=paid_by_company_name,
            employment_classification=employment_classification,
            pay_classification=pay_classification,
            flsa_status=flsa_status,
            payroll_frequency=payroll_frequency,
        )

        employee_index_position.additional_properties = d
        return employee_index_position

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

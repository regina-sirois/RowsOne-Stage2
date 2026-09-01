from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast
from uuid import UUID

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.login_company_summary import LoginCompanySummary


T = TypeVar("T", bound="LoginUserContext")


@_attrs_define
class LoginUserContext:
    """Authenticated user with organization context and nested company summaries

    Attributes:
        id (UUID):  Example: 123e4567-e89b-12d3-a456-426614174000.
        first_name (str):  Example: John.
        last_name (str):  Example: Doe.
        email (str):  Example: johndoe@example.com.
        companies (list[LoginCompanySummary]):
        organization_id (UUID | Unset):  Example: 123e4567-e89b-12d3-a456-426614174000.
        organization_name (str | Unset):  Example: RowsOne Inc..
        organization_logo (None | str | Unset):  Example: https://example.com/logo.png.
    """

    id: UUID
    first_name: str
    last_name: str
    email: str
    companies: list[LoginCompanySummary]
    organization_id: UUID | Unset = UNSET
    organization_name: str | Unset = UNSET
    organization_logo: None | str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id = str(self.id)

        first_name = self.first_name

        last_name = self.last_name

        email = self.email

        companies = []
        for companies_item_data in self.companies:
            companies_item = companies_item_data.to_dict()
            companies.append(companies_item)

        organization_id: str | Unset = UNSET
        if not isinstance(self.organization_id, Unset):
            organization_id = str(self.organization_id)

        organization_name = self.organization_name

        organization_logo: None | str | Unset
        if isinstance(self.organization_logo, Unset):
            organization_logo = UNSET
        else:
            organization_logo = self.organization_logo

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id": id,
                "first_name": first_name,
                "last_name": last_name,
                "email": email,
                "companies": companies,
            }
        )
        if organization_id is not UNSET:
            field_dict["organization_id"] = organization_id
        if organization_name is not UNSET:
            field_dict["organization_name"] = organization_name
        if organization_logo is not UNSET:
            field_dict["organization_logo"] = organization_logo

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.login_company_summary import LoginCompanySummary  # noqa: PLC0415

        d = dict(src_dict)
        id = UUID(d.pop("id"))

        first_name = d.pop("first_name")

        last_name = d.pop("last_name")

        email = d.pop("email")

        companies = []
        _companies = d.pop("companies")
        for companies_item_data in _companies:
            companies_item = LoginCompanySummary.from_dict(companies_item_data)

            companies.append(companies_item)

        _organization_id = d.pop("organization_id", UNSET)
        organization_id: UUID | Unset
        if isinstance(_organization_id, Unset):
            organization_id = UNSET
        else:
            organization_id = UUID(_organization_id)

        organization_name = d.pop("organization_name", UNSET)

        def _parse_organization_logo(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        organization_logo = _parse_organization_logo(d.pop("organization_logo", UNSET))

        login_user_context = cls(
            id=id,
            first_name=first_name,
            last_name=last_name,
            email=email,
            companies=companies,
            organization_id=organization_id,
            organization_name=organization_name,
            organization_logo=organization_logo,
        )

        login_user_context.additional_properties = d
        return login_user_context

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

from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast
from uuid import UUID

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.user_resource_preferred_language import UserResourcePreferredLanguage
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.phone_number_resource import PhoneNumberResource


T = TypeVar("T", bound="UserResource")


@_attrs_define
class UserResource:
    """User representation for API responses

    Attributes:
        id (UUID): Unique identifier for the user Example: 550e8400-e29b-41d4-a716-446655440000.
        email (str): Email address of the user. Masked (e.g. u*****@example.com) without
            VIEW_USER_PERSONAL_PROFILE_PRIMARY_EMAIL unless the viewer is the user. Example: user@example.com.
        first_name (str): First name of the user Example: John.
        last_name (str): Last name of the user Example: Doe.
        full_name (str): Full name of the user Example: John Middle Doe.
        profile_picture_base64 (None | str | Unset): Base64 encoded profile picture, if available Example:
            data:image/jpeg;base64,/9j/4AAQSkZJRgABAQAAAQ....
        middle_name (None | str | Unset): Middle name of the user Example: Middle.
        name (str | Unset): @deprecated Use full_name instead. Full name of the user Example: John Middle Doe.
        preferred_name (None | str | Unset): Preferred name of the user Example: Johnny.
        preferred_language (UserResourcePreferredLanguage | Unset): ISO 639-1 language code. English, Spanish, Chinese,
            Vietnamese, Tagalog, Korean, French, Arabic, Russian, Portuguese, or Other. Example: en.
        prior_last_name (None | str | Unset): Prior/maiden last name of the user Example: Smith.
        phone_numbers (list[PhoneNumberResource] | Unset): User's phone numbers
    """

    id: UUID
    email: str
    first_name: str
    last_name: str
    full_name: str
    profile_picture_base64: None | str | Unset = UNSET
    middle_name: None | str | Unset = UNSET
    name: str | Unset = UNSET
    preferred_name: None | str | Unset = UNSET
    preferred_language: UserResourcePreferredLanguage | Unset = UNSET
    prior_last_name: None | str | Unset = UNSET
    phone_numbers: list[PhoneNumberResource] | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id = str(self.id)

        email = self.email

        first_name = self.first_name

        last_name = self.last_name

        full_name = self.full_name

        profile_picture_base64: None | str | Unset
        if isinstance(self.profile_picture_base64, Unset):
            profile_picture_base64 = UNSET
        else:
            profile_picture_base64 = self.profile_picture_base64

        middle_name: None | str | Unset
        if isinstance(self.middle_name, Unset):
            middle_name = UNSET
        else:
            middle_name = self.middle_name

        name = self.name

        preferred_name: None | str | Unset
        if isinstance(self.preferred_name, Unset):
            preferred_name = UNSET
        else:
            preferred_name = self.preferred_name

        preferred_language: str | Unset = UNSET
        if not isinstance(self.preferred_language, Unset):
            preferred_language = self.preferred_language.value

        prior_last_name: None | str | Unset
        if isinstance(self.prior_last_name, Unset):
            prior_last_name = UNSET
        else:
            prior_last_name = self.prior_last_name

        phone_numbers: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.phone_numbers, Unset):
            phone_numbers = []
            for phone_numbers_item_data in self.phone_numbers:
                phone_numbers_item = phone_numbers_item_data.to_dict()
                phone_numbers.append(phone_numbers_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id": id,
                "email": email,
                "first_name": first_name,
                "last_name": last_name,
                "full_name": full_name,
            }
        )
        if profile_picture_base64 is not UNSET:
            field_dict["profile_picture_base64"] = profile_picture_base64
        if middle_name is not UNSET:
            field_dict["middle_name"] = middle_name
        if name is not UNSET:
            field_dict["name"] = name
        if preferred_name is not UNSET:
            field_dict["preferred_name"] = preferred_name
        if preferred_language is not UNSET:
            field_dict["preferred_language"] = preferred_language
        if prior_last_name is not UNSET:
            field_dict["prior_last_name"] = prior_last_name
        if phone_numbers is not UNSET:
            field_dict["phone_numbers"] = phone_numbers

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.phone_number_resource import PhoneNumberResource  # noqa: PLC0415

        d = dict(src_dict)
        id = UUID(d.pop("id"))

        email = d.pop("email")

        first_name = d.pop("first_name")

        last_name = d.pop("last_name")

        full_name = d.pop("full_name")

        def _parse_profile_picture_base64(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        profile_picture_base64 = _parse_profile_picture_base64(d.pop("profile_picture_base64", UNSET))

        def _parse_middle_name(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        middle_name = _parse_middle_name(d.pop("middle_name", UNSET))

        name = d.pop("name", UNSET)

        def _parse_preferred_name(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        preferred_name = _parse_preferred_name(d.pop("preferred_name", UNSET))

        _preferred_language = d.pop("preferred_language", UNSET)
        preferred_language: UserResourcePreferredLanguage | Unset
        if isinstance(_preferred_language, Unset):
            preferred_language = UNSET
        else:
            preferred_language = UserResourcePreferredLanguage(_preferred_language)

        def _parse_prior_last_name(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        prior_last_name = _parse_prior_last_name(d.pop("prior_last_name", UNSET))

        _phone_numbers = d.pop("phone_numbers", UNSET)
        phone_numbers: list[PhoneNumberResource] | Unset = UNSET
        if _phone_numbers is not UNSET:
            phone_numbers = []
            for phone_numbers_item_data in _phone_numbers:
                phone_numbers_item = PhoneNumberResource.from_dict(phone_numbers_item_data)

                phone_numbers.append(phone_numbers_item)

        user_resource = cls(
            id=id,
            email=email,
            first_name=first_name,
            last_name=last_name,
            full_name=full_name,
            profile_picture_base64=profile_picture_base64,
            middle_name=middle_name,
            name=name,
            preferred_name=preferred_name,
            preferred_language=preferred_language,
            prior_last_name=prior_last_name,
            phone_numbers=phone_numbers,
        )

        user_resource.additional_properties = d
        return user_resource

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

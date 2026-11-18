from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import Any, TypeVar, cast
from uuid import UUID

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="PersonOut")


@_attrs_define
class PersonOut:
    """
    Attributes:
        person_id (int):
        record_time_stamp (datetime.datetime):
        laboratory_id (int | None | Unset):
        site_id (int | None | Unset):
        person_uuid (None | str | Unset):
        family_name (None | str | Unset):
        given_name (None | str | Unset):
        title (None | str | Unset):
        email_address (None | str | Unset):
        phone_number (None | str | Unset):
        login (None | str | Unset):
        fax_number (None | str | Unset):
        external_id (None | Unset | UUID):
    """

    person_id: int
    record_time_stamp: datetime.datetime
    laboratory_id: int | None | Unset = UNSET
    site_id: int | None | Unset = UNSET
    person_uuid: None | str | Unset = UNSET
    family_name: None | str | Unset = UNSET
    given_name: None | str | Unset = UNSET
    title: None | str | Unset = UNSET
    email_address: None | str | Unset = UNSET
    phone_number: None | str | Unset = UNSET
    login: None | str | Unset = UNSET
    fax_number: None | str | Unset = UNSET
    external_id: None | Unset | UUID = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        person_id = self.person_id

        record_time_stamp = self.record_time_stamp.isoformat()

        laboratory_id: int | None | Unset
        if isinstance(self.laboratory_id, Unset):
            laboratory_id = UNSET
        else:
            laboratory_id = self.laboratory_id

        site_id: int | None | Unset
        if isinstance(self.site_id, Unset):
            site_id = UNSET
        else:
            site_id = self.site_id

        person_uuid: None | str | Unset
        if isinstance(self.person_uuid, Unset):
            person_uuid = UNSET
        else:
            person_uuid = self.person_uuid

        family_name: None | str | Unset
        if isinstance(self.family_name, Unset):
            family_name = UNSET
        else:
            family_name = self.family_name

        given_name: None | str | Unset
        if isinstance(self.given_name, Unset):
            given_name = UNSET
        else:
            given_name = self.given_name

        title: None | str | Unset
        if isinstance(self.title, Unset):
            title = UNSET
        else:
            title = self.title

        email_address: None | str | Unset
        if isinstance(self.email_address, Unset):
            email_address = UNSET
        else:
            email_address = self.email_address

        phone_number: None | str | Unset
        if isinstance(self.phone_number, Unset):
            phone_number = UNSET
        else:
            phone_number = self.phone_number

        login: None | str | Unset
        if isinstance(self.login, Unset):
            login = UNSET
        else:
            login = self.login

        fax_number: None | str | Unset
        if isinstance(self.fax_number, Unset):
            fax_number = UNSET
        else:
            fax_number = self.fax_number

        external_id: None | str | Unset
        if isinstance(self.external_id, Unset):
            external_id = UNSET
        elif isinstance(self.external_id, UUID):
            external_id = str(self.external_id)
        else:
            external_id = self.external_id

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "personId": person_id,
                "recordTimeStamp": record_time_stamp,
            }
        )
        if laboratory_id is not UNSET:
            field_dict["laboratoryId"] = laboratory_id
        if site_id is not UNSET:
            field_dict["siteId"] = site_id
        if person_uuid is not UNSET:
            field_dict["personUUID"] = person_uuid
        if family_name is not UNSET:
            field_dict["familyName"] = family_name
        if given_name is not UNSET:
            field_dict["givenName"] = given_name
        if title is not UNSET:
            field_dict["title"] = title
        if email_address is not UNSET:
            field_dict["emailAddress"] = email_address
        if phone_number is not UNSET:
            field_dict["phoneNumber"] = phone_number
        if login is not UNSET:
            field_dict["login"] = login
        if fax_number is not UNSET:
            field_dict["faxNumber"] = fax_number
        if external_id is not UNSET:
            field_dict["externalId"] = external_id

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        person_id = d.pop("personId")

        record_time_stamp = datetime.datetime.fromisoformat(d.pop("recordTimeStamp"))

        def _parse_laboratory_id(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        laboratory_id = _parse_laboratory_id(d.pop("laboratoryId", UNSET))

        def _parse_site_id(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        site_id = _parse_site_id(d.pop("siteId", UNSET))

        def _parse_person_uuid(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        person_uuid = _parse_person_uuid(d.pop("personUUID", UNSET))

        def _parse_family_name(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        family_name = _parse_family_name(d.pop("familyName", UNSET))

        def _parse_given_name(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        given_name = _parse_given_name(d.pop("givenName", UNSET))

        def _parse_title(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        title = _parse_title(d.pop("title", UNSET))

        def _parse_email_address(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        email_address = _parse_email_address(d.pop("emailAddress", UNSET))

        def _parse_phone_number(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        phone_number = _parse_phone_number(d.pop("phoneNumber", UNSET))

        def _parse_login(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        login = _parse_login(d.pop("login", UNSET))

        def _parse_fax_number(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        fax_number = _parse_fax_number(d.pop("faxNumber", UNSET))

        def _parse_external_id(data: object) -> None | Unset | UUID:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                external_id_type_0 = UUID(data)

                return external_id_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(None | Unset | UUID, data)

        external_id = _parse_external_id(d.pop("externalId", UNSET))

        person_out = cls(
            person_id=person_id,
            record_time_stamp=record_time_stamp,
            laboratory_id=laboratory_id,
            site_id=site_id,
            person_uuid=person_uuid,
            family_name=family_name,
            given_name=given_name,
            title=title,
            email_address=email_address,
            phone_number=phone_number,
            login=login,
            fax_number=fax_number,
            external_id=external_id,
        )

        person_out.additional_properties = d
        return person_out

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

from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="DataCollectionCommentOut")


@_attrs_define
class DataCollectionCommentOut:
    """
    Attributes:
        comments (str):
        data_collection_comment_id (int):
        create_time (datetime.datetime):
        person_id (int):
        mod_time (datetime.datetime | None | Unset):
        data_collection_id (int | None | Unset):
        person_given_name (None | str | Unset):
        person_family_name (None | str | Unset):
        person_fed_id (None | str | Unset):
    """

    comments: str
    data_collection_comment_id: int
    create_time: datetime.datetime
    person_id: int
    mod_time: datetime.datetime | None | Unset = UNSET
    data_collection_id: int | None | Unset = UNSET
    person_given_name: None | str | Unset = UNSET
    person_family_name: None | str | Unset = UNSET
    person_fed_id: None | str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        comments = self.comments

        data_collection_comment_id = self.data_collection_comment_id

        create_time = self.create_time.isoformat()

        person_id = self.person_id

        mod_time: None | str | Unset
        if isinstance(self.mod_time, Unset):
            mod_time = UNSET
        elif isinstance(self.mod_time, datetime.datetime):
            mod_time = self.mod_time.isoformat()
        else:
            mod_time = self.mod_time

        data_collection_id: int | None | Unset
        if isinstance(self.data_collection_id, Unset):
            data_collection_id = UNSET
        else:
            data_collection_id = self.data_collection_id

        person_given_name: None | str | Unset
        if isinstance(self.person_given_name, Unset):
            person_given_name = UNSET
        else:
            person_given_name = self.person_given_name

        person_family_name: None | str | Unset
        if isinstance(self.person_family_name, Unset):
            person_family_name = UNSET
        else:
            person_family_name = self.person_family_name

        person_fed_id: None | str | Unset
        if isinstance(self.person_fed_id, Unset):
            person_fed_id = UNSET
        else:
            person_fed_id = self.person_fed_id

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "comments": comments,
                "dataCollectionCommentId": data_collection_comment_id,
                "createTime": create_time,
                "personId": person_id,
            }
        )
        if mod_time is not UNSET:
            field_dict["modTime"] = mod_time
        if data_collection_id is not UNSET:
            field_dict["dataCollectionId"] = data_collection_id
        if person_given_name is not UNSET:
            field_dict["personGivenName"] = person_given_name
        if person_family_name is not UNSET:
            field_dict["personFamilyName"] = person_family_name
        if person_fed_id is not UNSET:
            field_dict["personFedID"] = person_fed_id

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        comments = d.pop("comments")

        data_collection_comment_id = d.pop("dataCollectionCommentId")

        create_time = datetime.datetime.fromisoformat(d.pop("createTime"))

        person_id = d.pop("personId")

        def _parse_mod_time(data: object) -> datetime.datetime | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                mod_time_type_0 = datetime.datetime.fromisoformat(data)

                return mod_time_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(datetime.datetime | None | Unset, data)

        mod_time = _parse_mod_time(d.pop("modTime", UNSET))

        def _parse_data_collection_id(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        data_collection_id = _parse_data_collection_id(d.pop("dataCollectionId", UNSET))

        def _parse_person_given_name(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        person_given_name = _parse_person_given_name(d.pop("personGivenName", UNSET))

        def _parse_person_family_name(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        person_family_name = _parse_person_family_name(d.pop("personFamilyName", UNSET))

        def _parse_person_fed_id(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        person_fed_id = _parse_person_fed_id(d.pop("personFedID", UNSET))

        data_collection_comment_out = cls(
            comments=comments,
            data_collection_comment_id=data_collection_comment_id,
            create_time=create_time,
            person_id=person_id,
            mod_time=mod_time,
            data_collection_id=data_collection_id,
            person_given_name=person_given_name,
            person_family_name=person_family_name,
            person_fed_id=person_fed_id,
        )

        data_collection_comment_out.additional_properties = d
        return data_collection_comment_out

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

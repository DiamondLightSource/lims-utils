from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="ContainerQueueIn")


@_attrs_define
class ContainerQueueIn:
    """
    Attributes:
        person_id (int | None | Unset):
        completed_time_stamp (datetime.datetime | None | Unset):
    """

    person_id: int | None | Unset = UNSET
    completed_time_stamp: datetime.datetime | None | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        person_id: int | None | Unset
        if isinstance(self.person_id, Unset):
            person_id = UNSET
        else:
            person_id = self.person_id

        completed_time_stamp: None | str | Unset
        if isinstance(self.completed_time_stamp, Unset):
            completed_time_stamp = UNSET
        elif isinstance(self.completed_time_stamp, datetime.datetime):
            completed_time_stamp = self.completed_time_stamp.isoformat()
        else:
            completed_time_stamp = self.completed_time_stamp

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if person_id is not UNSET:
            field_dict["personId"] = person_id
        if completed_time_stamp is not UNSET:
            field_dict["completedTimeStamp"] = completed_time_stamp

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)

        def _parse_person_id(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        person_id = _parse_person_id(d.pop("personId", UNSET))

        def _parse_completed_time_stamp(data: object) -> datetime.datetime | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                completed_time_stamp_type_0 = datetime.datetime.fromisoformat(data)

                return completed_time_stamp_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(datetime.datetime | None | Unset, data)

        completed_time_stamp = _parse_completed_time_stamp(d.pop("completedTimeStamp", UNSET))

        container_queue_in = cls(
            person_id=person_id,
            completed_time_stamp=completed_time_stamp,
        )

        container_queue_in.additional_properties = d
        return container_queue_in

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

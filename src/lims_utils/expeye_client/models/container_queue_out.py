from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="ContainerQueueOut")


@_attrs_define
class ContainerQueueOut:
    """
    Attributes:
        person_id (int | None | Unset):
        completed_time_stamp (datetime.datetime | None | Unset):
        container_id (int | None | Unset):
        container_queue_id (int | None | Unset):
        created_time_stamp (datetime.datetime | None | Unset):
    """

    person_id: int | None | Unset = UNSET
    completed_time_stamp: datetime.datetime | None | Unset = UNSET
    container_id: int | None | Unset = UNSET
    container_queue_id: int | None | Unset = UNSET
    created_time_stamp: datetime.datetime | None | Unset = UNSET
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

        container_id: int | None | Unset
        if isinstance(self.container_id, Unset):
            container_id = UNSET
        else:
            container_id = self.container_id

        container_queue_id: int | None | Unset
        if isinstance(self.container_queue_id, Unset):
            container_queue_id = UNSET
        else:
            container_queue_id = self.container_queue_id

        created_time_stamp: None | str | Unset
        if isinstance(self.created_time_stamp, Unset):
            created_time_stamp = UNSET
        elif isinstance(self.created_time_stamp, datetime.datetime):
            created_time_stamp = self.created_time_stamp.isoformat()
        else:
            created_time_stamp = self.created_time_stamp

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if person_id is not UNSET:
            field_dict["personId"] = person_id
        if completed_time_stamp is not UNSET:
            field_dict["completedTimeStamp"] = completed_time_stamp
        if container_id is not UNSET:
            field_dict["containerId"] = container_id
        if container_queue_id is not UNSET:
            field_dict["containerQueueId"] = container_queue_id
        if created_time_stamp is not UNSET:
            field_dict["createdTimeStamp"] = created_time_stamp

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

        def _parse_container_id(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        container_id = _parse_container_id(d.pop("containerId", UNSET))

        def _parse_container_queue_id(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        container_queue_id = _parse_container_queue_id(d.pop("containerQueueId", UNSET))

        def _parse_created_time_stamp(data: object) -> datetime.datetime | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                created_time_stamp_type_0 = datetime.datetime.fromisoformat(data)

                return created_time_stamp_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(datetime.datetime | None | Unset, data)

        created_time_stamp = _parse_created_time_stamp(d.pop("createdTimeStamp", UNSET))

        container_queue_out = cls(
            person_id=person_id,
            completed_time_stamp=completed_time_stamp,
            container_id=container_id,
            container_queue_id=container_queue_id,
            created_time_stamp=created_time_stamp,
        )

        container_queue_out.additional_properties = d
        return container_queue_out

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

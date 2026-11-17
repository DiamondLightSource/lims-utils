from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="SessionEventOut")


@_attrs_define
class SessionEventOut:
    """
    Attributes:
        type_ (str):
        start_timestamp (datetime.datetime | None):
        end_timestamp (datetime.datetime | None):
        id (int):
    """

    type_: str
    start_timestamp: datetime.datetime | None
    end_timestamp: datetime.datetime | None
    id: int
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        type_ = self.type_

        start_timestamp: None | str
        if isinstance(self.start_timestamp, datetime.datetime):
            start_timestamp = self.start_timestamp.isoformat()
        else:
            start_timestamp = self.start_timestamp

        end_timestamp: None | str
        if isinstance(self.end_timestamp, datetime.datetime):
            end_timestamp = self.end_timestamp.isoformat()
        else:
            end_timestamp = self.end_timestamp

        id = self.id

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "type": type_,
                "startTimestamp": start_timestamp,
                "endTimestamp": end_timestamp,
                "id": id,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        type_ = d.pop("type")

        def _parse_start_timestamp(data: object) -> datetime.datetime | None:
            if data is None:
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                start_timestamp_type_0 = datetime.datetime.fromisoformat(data)

                return start_timestamp_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(datetime.datetime | None, data)

        start_timestamp = _parse_start_timestamp(d.pop("startTimestamp"))

        def _parse_end_timestamp(data: object) -> datetime.datetime | None:
            if data is None:
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                end_timestamp_type_0 = datetime.datetime.fromisoformat(data)

                return end_timestamp_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(datetime.datetime | None, data)

        end_timestamp = _parse_end_timestamp(d.pop("endTimestamp"))

        id = d.pop("id")

        session_event_out = cls(
            type_=type_,
            start_timestamp=start_timestamp,
            end_timestamp=end_timestamp,
            id=id,
        )

        session_event_out.additional_properties = d
        return session_event_out

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

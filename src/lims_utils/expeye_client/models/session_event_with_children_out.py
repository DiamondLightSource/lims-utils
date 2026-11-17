from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.auto_proc_program_scaling_out import AutoProcProgramScalingOut
    from ..models.session_event_out import SessionEventOut


T = TypeVar("T", bound="SessionEventWithChildrenOut")


@_attrs_define
class SessionEventWithChildrenOut:
    """
    Attributes:
        type_ (str):
        start_timestamp (datetime.datetime | None):
        end_timestamp (datetime.datetime | None):
        id (int):
        events (list[SessionEventOut] | Unset):
        scaling (list[AutoProcProgramScalingOut] | Unset):
    """

    type_: str
    start_timestamp: datetime.datetime | None
    end_timestamp: datetime.datetime | None
    id: int
    events: list[SessionEventOut] | Unset = UNSET
    scaling: list[AutoProcProgramScalingOut] | Unset = UNSET
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

        events: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.events, Unset):
            events = []
            for events_item_data in self.events:
                events_item = events_item_data.to_dict()
                events.append(events_item)

        scaling: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.scaling, Unset):
            scaling = []
            for scaling_item_data in self.scaling:
                scaling_item = scaling_item_data.to_dict()
                scaling.append(scaling_item)

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
        if events is not UNSET:
            field_dict["events"] = events
        if scaling is not UNSET:
            field_dict["scaling"] = scaling

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.auto_proc_program_scaling_out import AutoProcProgramScalingOut  # noqa: PLC0415
        from ..models.session_event_out import SessionEventOut  # noqa: PLC0415

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

        _events = d.pop("events", UNSET)
        events: list[SessionEventOut] | Unset = UNSET
        if _events is not UNSET:
            events = []
            for events_item_data in _events:
                events_item = SessionEventOut.from_dict(events_item_data)

                events.append(events_item)

        _scaling = d.pop("scaling", UNSET)
        scaling: list[AutoProcProgramScalingOut] | Unset = UNSET
        if _scaling is not UNSET:
            scaling = []
            for scaling_item_data in _scaling:
                scaling_item = AutoProcProgramScalingOut.from_dict(scaling_item_data)

                scaling.append(scaling_item)

        session_event_with_children_out = cls(
            type_=type_,
            start_timestamp=start_timestamp,
            end_timestamp=end_timestamp,
            id=id,
            events=events,
            scaling=scaling,
        )

        session_event_with_children_out.additional_properties = d
        return session_event_with_children_out

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

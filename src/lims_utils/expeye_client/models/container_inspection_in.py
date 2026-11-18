from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="ContainerInspectionIn")


@_attrs_define
class ContainerInspectionIn:
    """
    Attributes:
        inspection_type_id (int):
        temperature (float | None | Unset):
        state (None | str | Unset):
        priority (int | None | Unset):
        manual (bool | None | Unset):
        scheduled_time_stamp (datetime.datetime | None | Unset):
        completed_time_stamp (datetime.datetime | None | Unset):
        schedule_component_id (int | None | Unset):
        bl_time_stamp (datetime.datetime | None | Unset):
        imager_id (int | None | Unset):
    """

    inspection_type_id: int
    temperature: float | None | Unset = UNSET
    state: None | str | Unset = UNSET
    priority: int | None | Unset = UNSET
    manual: bool | None | Unset = UNSET
    scheduled_time_stamp: datetime.datetime | None | Unset = UNSET
    completed_time_stamp: datetime.datetime | None | Unset = UNSET
    schedule_component_id: int | None | Unset = UNSET
    bl_time_stamp: datetime.datetime | None | Unset = UNSET
    imager_id: int | None | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        inspection_type_id = self.inspection_type_id

        temperature: float | None | Unset
        if isinstance(self.temperature, Unset):
            temperature = UNSET
        else:
            temperature = self.temperature

        state: None | str | Unset
        if isinstance(self.state, Unset):
            state = UNSET
        else:
            state = self.state

        priority: int | None | Unset
        if isinstance(self.priority, Unset):
            priority = UNSET
        else:
            priority = self.priority

        manual: bool | None | Unset
        if isinstance(self.manual, Unset):
            manual = UNSET
        else:
            manual = self.manual

        scheduled_time_stamp: None | str | Unset
        if isinstance(self.scheduled_time_stamp, Unset):
            scheduled_time_stamp = UNSET
        elif isinstance(self.scheduled_time_stamp, datetime.datetime):
            scheduled_time_stamp = self.scheduled_time_stamp.isoformat()
        else:
            scheduled_time_stamp = self.scheduled_time_stamp

        completed_time_stamp: None | str | Unset
        if isinstance(self.completed_time_stamp, Unset):
            completed_time_stamp = UNSET
        elif isinstance(self.completed_time_stamp, datetime.datetime):
            completed_time_stamp = self.completed_time_stamp.isoformat()
        else:
            completed_time_stamp = self.completed_time_stamp

        schedule_component_id: int | None | Unset
        if isinstance(self.schedule_component_id, Unset):
            schedule_component_id = UNSET
        else:
            schedule_component_id = self.schedule_component_id

        bl_time_stamp: None | str | Unset
        if isinstance(self.bl_time_stamp, Unset):
            bl_time_stamp = UNSET
        elif isinstance(self.bl_time_stamp, datetime.datetime):
            bl_time_stamp = self.bl_time_stamp.isoformat()
        else:
            bl_time_stamp = self.bl_time_stamp

        imager_id: int | None | Unset
        if isinstance(self.imager_id, Unset):
            imager_id = UNSET
        else:
            imager_id = self.imager_id

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "inspectionTypeId": inspection_type_id,
            }
        )
        if temperature is not UNSET:
            field_dict["temperature"] = temperature
        if state is not UNSET:
            field_dict["state"] = state
        if priority is not UNSET:
            field_dict["priority"] = priority
        if manual is not UNSET:
            field_dict["manual"] = manual
        if scheduled_time_stamp is not UNSET:
            field_dict["scheduledTimeStamp"] = scheduled_time_stamp
        if completed_time_stamp is not UNSET:
            field_dict["completedTimeStamp"] = completed_time_stamp
        if schedule_component_id is not UNSET:
            field_dict["scheduleComponentId"] = schedule_component_id
        if bl_time_stamp is not UNSET:
            field_dict["blTimeStamp"] = bl_time_stamp
        if imager_id is not UNSET:
            field_dict["imagerId"] = imager_id

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        inspection_type_id = d.pop("inspectionTypeId")

        def _parse_temperature(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        temperature = _parse_temperature(d.pop("temperature", UNSET))

        def _parse_state(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        state = _parse_state(d.pop("state", UNSET))

        def _parse_priority(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        priority = _parse_priority(d.pop("priority", UNSET))

        def _parse_manual(data: object) -> bool | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(bool | None | Unset, data)

        manual = _parse_manual(d.pop("manual", UNSET))

        def _parse_scheduled_time_stamp(data: object) -> datetime.datetime | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                scheduled_time_stamp_type_0 = datetime.datetime.fromisoformat(data)

                return scheduled_time_stamp_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(datetime.datetime | None | Unset, data)

        scheduled_time_stamp = _parse_scheduled_time_stamp(d.pop("scheduledTimeStamp", UNSET))

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

        def _parse_schedule_component_id(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        schedule_component_id = _parse_schedule_component_id(d.pop("scheduleComponentId", UNSET))

        def _parse_bl_time_stamp(data: object) -> datetime.datetime | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                bl_time_stamp_type_0 = datetime.datetime.fromisoformat(data)

                return bl_time_stamp_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(datetime.datetime | None | Unset, data)

        bl_time_stamp = _parse_bl_time_stamp(d.pop("blTimeStamp", UNSET))

        def _parse_imager_id(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        imager_id = _parse_imager_id(d.pop("imagerId", UNSET))

        container_inspection_in = cls(
            inspection_type_id=inspection_type_id,
            temperature=temperature,
            state=state,
            priority=priority,
            manual=manual,
            scheduled_time_stamp=scheduled_time_stamp,
            completed_time_stamp=completed_time_stamp,
            schedule_component_id=schedule_component_id,
            bl_time_stamp=bl_time_stamp,
            imager_id=imager_id,
        )

        container_inspection_in.additional_properties = d
        return container_inspection_in

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

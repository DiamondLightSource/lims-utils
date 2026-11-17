from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="ContainerHistoryOut")


@_attrs_define
class ContainerHistoryOut:
    """
    Attributes:
        container_history_id (int):
        bl_time_stamp (datetime.datetime):
        container_id (int | None | Unset):
        location (None | str | Unset):
        status (None | str | Unset):
        beamline_name (None | str | Unset):
        current_dewar_id (int | None | Unset):
    """

    container_history_id: int
    bl_time_stamp: datetime.datetime
    container_id: int | None | Unset = UNSET
    location: None | str | Unset = UNSET
    status: None | str | Unset = UNSET
    beamline_name: None | str | Unset = UNSET
    current_dewar_id: int | None | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        container_history_id = self.container_history_id

        bl_time_stamp = self.bl_time_stamp.isoformat()

        container_id: int | None | Unset
        if isinstance(self.container_id, Unset):
            container_id = UNSET
        else:
            container_id = self.container_id

        location: None | str | Unset
        if isinstance(self.location, Unset):
            location = UNSET
        else:
            location = self.location

        status: None | str | Unset
        if isinstance(self.status, Unset):
            status = UNSET
        else:
            status = self.status

        beamline_name: None | str | Unset
        if isinstance(self.beamline_name, Unset):
            beamline_name = UNSET
        else:
            beamline_name = self.beamline_name

        current_dewar_id: int | None | Unset
        if isinstance(self.current_dewar_id, Unset):
            current_dewar_id = UNSET
        else:
            current_dewar_id = self.current_dewar_id

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "containerHistoryId": container_history_id,
                "blTimeStamp": bl_time_stamp,
            }
        )
        if container_id is not UNSET:
            field_dict["containerId"] = container_id
        if location is not UNSET:
            field_dict["location"] = location
        if status is not UNSET:
            field_dict["status"] = status
        if beamline_name is not UNSET:
            field_dict["beamlineName"] = beamline_name
        if current_dewar_id is not UNSET:
            field_dict["currentDewarId"] = current_dewar_id

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        container_history_id = d.pop("containerHistoryId")

        bl_time_stamp = datetime.datetime.fromisoformat(d.pop("blTimeStamp"))

        def _parse_container_id(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        container_id = _parse_container_id(d.pop("containerId", UNSET))

        def _parse_location(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        location = _parse_location(d.pop("location", UNSET))

        def _parse_status(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        status = _parse_status(d.pop("status", UNSET))

        def _parse_beamline_name(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        beamline_name = _parse_beamline_name(d.pop("beamlineName", UNSET))

        def _parse_current_dewar_id(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        current_dewar_id = _parse_current_dewar_id(d.pop("currentDewarId", UNSET))

        container_history_out = cls(
            container_history_id=container_history_id,
            bl_time_stamp=bl_time_stamp,
            container_id=container_id,
            location=location,
            status=status,
            beamline_name=beamline_name,
            current_dewar_id=current_dewar_id,
        )

        container_history_out.additional_properties = d
        return container_history_out

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

from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="PositionOut")


@_attrs_define
class PositionOut:
    """
    Attributes:
        position_id (int):
        record_time_stamp (datetime.datetime | None):
        relative_position_id (int | None | Unset): Relative position, pointing to another existing position
        pos_x (float | None | Unset):
        pos_y (float | None | Unset):
        pos_z (float | None | Unset):
        scale (float | None | Unset):
    """

    position_id: int
    record_time_stamp: datetime.datetime | None
    relative_position_id: int | None | Unset = UNSET
    pos_x: float | None | Unset = UNSET
    pos_y: float | None | Unset = UNSET
    pos_z: float | None | Unset = UNSET
    scale: float | None | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        position_id = self.position_id

        record_time_stamp: None | str
        if isinstance(self.record_time_stamp, datetime.datetime):
            record_time_stamp = self.record_time_stamp.isoformat()
        else:
            record_time_stamp = self.record_time_stamp

        relative_position_id: int | None | Unset
        if isinstance(self.relative_position_id, Unset):
            relative_position_id = UNSET
        else:
            relative_position_id = self.relative_position_id

        pos_x: float | None | Unset
        if isinstance(self.pos_x, Unset):
            pos_x = UNSET
        else:
            pos_x = self.pos_x

        pos_y: float | None | Unset
        if isinstance(self.pos_y, Unset):
            pos_y = UNSET
        else:
            pos_y = self.pos_y

        pos_z: float | None | Unset
        if isinstance(self.pos_z, Unset):
            pos_z = UNSET
        else:
            pos_z = self.pos_z

        scale: float | None | Unset
        if isinstance(self.scale, Unset):
            scale = UNSET
        else:
            scale = self.scale

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "positionId": position_id,
                "recordTimeStamp": record_time_stamp,
            }
        )
        if relative_position_id is not UNSET:
            field_dict["relativePositionId"] = relative_position_id
        if pos_x is not UNSET:
            field_dict["posX"] = pos_x
        if pos_y is not UNSET:
            field_dict["posY"] = pos_y
        if pos_z is not UNSET:
            field_dict["posZ"] = pos_z
        if scale is not UNSET:
            field_dict["scale"] = scale

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        position_id = d.pop("positionId")

        def _parse_record_time_stamp(data: object) -> datetime.datetime | None:
            if data is None:
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                record_time_stamp_type_0 = datetime.datetime.fromisoformat(data)

                return record_time_stamp_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(datetime.datetime | None, data)

        record_time_stamp = _parse_record_time_stamp(d.pop("recordTimeStamp"))

        def _parse_relative_position_id(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        relative_position_id = _parse_relative_position_id(d.pop("relativePositionId", UNSET))

        def _parse_pos_x(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        pos_x = _parse_pos_x(d.pop("posX", UNSET))

        def _parse_pos_y(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        pos_y = _parse_pos_y(d.pop("posY", UNSET))

        def _parse_pos_z(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        pos_z = _parse_pos_z(d.pop("posZ", UNSET))

        def _parse_scale(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        scale = _parse_scale(d.pop("scale", UNSET))

        position_out = cls(
            position_id=position_id,
            record_time_stamp=record_time_stamp,
            relative_position_id=relative_position_id,
            pos_x=pos_x,
            pos_y=pos_y,
            pos_z=pos_z,
            scale=scale,
        )

        position_out.additional_properties = d
        return position_out

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

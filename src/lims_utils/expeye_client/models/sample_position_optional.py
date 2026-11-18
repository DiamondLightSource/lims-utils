from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import Any, Literal, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="SamplePositionOptional")


@_attrs_define
class SamplePositionOptional:
    """
    Attributes:
        pos_x (float | None | Unset):
        pos_y (float | None | Unset):
        pos_z (float | None | Unset):
        position_type (Literal['dispensing'] | None | Unset): Type of marked position (e.g.: dispensing location)
        record_time_stamp (datetime.datetime | None | Unset):
    """

    pos_x: float | None | Unset = UNSET
    pos_y: float | None | Unset = UNSET
    pos_z: float | None | Unset = UNSET
    position_type: Literal["dispensing"] | None | Unset = UNSET
    record_time_stamp: datetime.datetime | None | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
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

        position_type: Literal["dispensing"] | None | Unset
        if isinstance(self.position_type, Unset):
            position_type = UNSET
        else:
            position_type = self.position_type

        record_time_stamp: None | str | Unset
        if isinstance(self.record_time_stamp, Unset):
            record_time_stamp = UNSET
        elif isinstance(self.record_time_stamp, datetime.datetime):
            record_time_stamp = self.record_time_stamp.isoformat()
        else:
            record_time_stamp = self.record_time_stamp

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if pos_x is not UNSET:
            field_dict["posX"] = pos_x
        if pos_y is not UNSET:
            field_dict["posY"] = pos_y
        if pos_z is not UNSET:
            field_dict["posZ"] = pos_z
        if position_type is not UNSET:
            field_dict["positionType"] = position_type
        if record_time_stamp is not UNSET:
            field_dict["recordTimeStamp"] = record_time_stamp

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)

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

        def _parse_position_type(data: object) -> Literal["dispensing"] | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            position_type_type_0 = cast(Literal["dispensing"], data)
            if position_type_type_0 != "dispensing":
                raise ValueError(f"positionType_type_0 must match const 'dispensing', got '{position_type_type_0}'")
            return position_type_type_0
            return cast(Literal["dispensing"] | None | Unset, data)

        position_type = _parse_position_type(d.pop("positionType", UNSET))

        def _parse_record_time_stamp(data: object) -> datetime.datetime | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                record_time_stamp_type_0 = datetime.datetime.fromisoformat(data)

                return record_time_stamp_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(datetime.datetime | None | Unset, data)

        record_time_stamp = _parse_record_time_stamp(d.pop("recordTimeStamp", UNSET))

        sample_position_optional = cls(
            pos_x=pos_x,
            pos_y=pos_y,
            pos_z=pos_z,
            position_type=position_type,
            record_time_stamp=record_time_stamp,
        )

        sample_position_optional.additional_properties = d
        return sample_position_optional

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

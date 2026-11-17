from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="LaserParametersOut")


@_attrs_define
class LaserParametersOut:
    """
    Attributes:
        laser_parameters_id (int):
        laser_repetition_rate (float | None | Unset): Laser repetition rate in kHz
        scanhead_move_speed (float | None | Unset): Scanhead move speed in m/s
        number_of_passes (int | None | Unset):
        gonio_rotation_speed (int | None | Unset): Goniometer rotation speed in degrees/s
        total_marking_time (float | None | Unset): Total marking time in seconds
        laser_transmission (float | None | Unset): Laser transmission in %
    """

    laser_parameters_id: int
    laser_repetition_rate: float | None | Unset = UNSET
    scanhead_move_speed: float | None | Unset = UNSET
    number_of_passes: int | None | Unset = UNSET
    gonio_rotation_speed: int | None | Unset = UNSET
    total_marking_time: float | None | Unset = UNSET
    laser_transmission: float | None | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        laser_parameters_id = self.laser_parameters_id

        laser_repetition_rate: float | None | Unset
        if isinstance(self.laser_repetition_rate, Unset):
            laser_repetition_rate = UNSET
        else:
            laser_repetition_rate = self.laser_repetition_rate

        scanhead_move_speed: float | None | Unset
        if isinstance(self.scanhead_move_speed, Unset):
            scanhead_move_speed = UNSET
        else:
            scanhead_move_speed = self.scanhead_move_speed

        number_of_passes: int | None | Unset
        if isinstance(self.number_of_passes, Unset):
            number_of_passes = UNSET
        else:
            number_of_passes = self.number_of_passes

        gonio_rotation_speed: int | None | Unset
        if isinstance(self.gonio_rotation_speed, Unset):
            gonio_rotation_speed = UNSET
        else:
            gonio_rotation_speed = self.gonio_rotation_speed

        total_marking_time: float | None | Unset
        if isinstance(self.total_marking_time, Unset):
            total_marking_time = UNSET
        else:
            total_marking_time = self.total_marking_time

        laser_transmission: float | None | Unset
        if isinstance(self.laser_transmission, Unset):
            laser_transmission = UNSET
        else:
            laser_transmission = self.laser_transmission

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "laserParametersId": laser_parameters_id,
            }
        )
        if laser_repetition_rate is not UNSET:
            field_dict["laserRepetitionRate"] = laser_repetition_rate
        if scanhead_move_speed is not UNSET:
            field_dict["scanheadMoveSpeed"] = scanhead_move_speed
        if number_of_passes is not UNSET:
            field_dict["numberOfPasses"] = number_of_passes
        if gonio_rotation_speed is not UNSET:
            field_dict["gonioRotationSpeed"] = gonio_rotation_speed
        if total_marking_time is not UNSET:
            field_dict["totalMarkingTime"] = total_marking_time
        if laser_transmission is not UNSET:
            field_dict["laserTransmission"] = laser_transmission

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        laser_parameters_id = d.pop("laserParametersId")

        def _parse_laser_repetition_rate(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        laser_repetition_rate = _parse_laser_repetition_rate(d.pop("laserRepetitionRate", UNSET))

        def _parse_scanhead_move_speed(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        scanhead_move_speed = _parse_scanhead_move_speed(d.pop("scanheadMoveSpeed", UNSET))

        def _parse_number_of_passes(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        number_of_passes = _parse_number_of_passes(d.pop("numberOfPasses", UNSET))

        def _parse_gonio_rotation_speed(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        gonio_rotation_speed = _parse_gonio_rotation_speed(d.pop("gonioRotationSpeed", UNSET))

        def _parse_total_marking_time(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        total_marking_time = _parse_total_marking_time(d.pop("totalMarkingTime", UNSET))

        def _parse_laser_transmission(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        laser_transmission = _parse_laser_transmission(d.pop("laserTransmission", UNSET))

        laser_parameters_out = cls(
            laser_parameters_id=laser_parameters_id,
            laser_repetition_rate=laser_repetition_rate,
            scanhead_move_speed=scanhead_move_speed,
            number_of_passes=number_of_passes,
            gonio_rotation_speed=gonio_rotation_speed,
            total_marking_time=total_marking_time,
            laser_transmission=laser_transmission,
        )

        laser_parameters_out.additional_properties = d
        return laser_parameters_out

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

from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="LaserPointIn")


@_attrs_define
class LaserPointIn:
    """
    Attributes:
        radius (int): Radius of point, in microns
        x (int): X coordinate of point, in microns
        y (int): Y coordinate of point, in microns
        point_index (int): Index of point, expresses ordinality
        laser_on (bool | None | Unset): Whether the laser is on for this point
    """

    radius: int
    x: int
    y: int
    point_index: int
    laser_on: bool | None | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        radius = self.radius

        x = self.x

        y = self.y

        point_index = self.point_index

        laser_on: bool | None | Unset
        if isinstance(self.laser_on, Unset):
            laser_on = UNSET
        else:
            laser_on = self.laser_on

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "radius": radius,
                "x": x,
                "y": y,
                "pointIndex": point_index,
            }
        )
        if laser_on is not UNSET:
            field_dict["laserOn"] = laser_on

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        radius = d.pop("radius")

        x = d.pop("x")

        y = d.pop("y")

        point_index = d.pop("pointIndex")

        def _parse_laser_on(data: object) -> bool | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(bool | None | Unset, data)

        laser_on = _parse_laser_on(d.pop("laserOn", UNSET))

        laser_point_in = cls(
            radius=radius,
            x=x,
            y=y,
            point_index=point_index,
            laser_on=laser_on,
        )

        laser_point_in.additional_properties = d
        return laser_point_in

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

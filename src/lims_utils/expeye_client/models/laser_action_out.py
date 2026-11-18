from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.laser_parameters_out import LaserParametersOut
    from ..models.laser_point_out import LaserPointOut


T = TypeVar("T", bound="LaserActionOut")


@_attrs_define
class LaserActionOut:
    """
    Attributes:
        parameters (LaserParametersOut):
        points (list[LaserPointOut]):
    """

    parameters: LaserParametersOut
    points: list[LaserPointOut]
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        parameters = self.parameters.to_dict()

        points = []
        for points_item_data in self.points:
            points_item = points_item_data.to_dict()
            points.append(points_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "parameters": parameters,
                "points": points,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.laser_parameters_out import LaserParametersOut
        from ..models.laser_point_out import LaserPointOut

        d = dict(src_dict)
        parameters = LaserParametersOut.from_dict(d.pop("parameters"))

        points = []
        _points = d.pop("points")
        for points_item_data in _points:
            points_item = LaserPointOut.from_dict(points_item_data)

            points.append(points_item)

        laser_action_out = cls(
            parameters=parameters,
            points=points,
        )

        laser_action_out.additional_properties = d
        return laser_action_out

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

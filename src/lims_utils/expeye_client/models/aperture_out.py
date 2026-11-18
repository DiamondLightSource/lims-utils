from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="ApertureOut")


@_attrs_define
class ApertureOut:
    """
    Attributes:
        aperture_id (int):
        size_x (float | None | Unset):
    """

    aperture_id: int
    size_x: float | None | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        aperture_id = self.aperture_id

        size_x: float | None | Unset
        if isinstance(self.size_x, Unset):
            size_x = UNSET
        else:
            size_x = self.size_x

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "apertureId": aperture_id,
            }
        )
        if size_x is not UNSET:
            field_dict["sizeX"] = size_x

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        aperture_id = d.pop("apertureId")

        def _parse_size_x(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        size_x = _parse_size_x(d.pop("sizeX", UNSET))

        aperture_out = cls(
            aperture_id=aperture_id,
            size_x=size_x,
        )

        aperture_out.additional_properties = d
        return aperture_out

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

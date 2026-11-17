from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="ImageQualityIndicatorOut")


@_attrs_define
class ImageQualityIndicatorOut:
    """
    Attributes:
        image (int):
        res (float | None | Unset): Estimated resolution
        spots (int | None | Unset): Total number of spots
        bragg (int | None | Unset): Number of good bragg candidates
        signal (float | None | Unset): Total integrated signal
        dozor (float | None | Unset): Dozor score
    """

    image: int
    res: float | None | Unset = UNSET
    spots: int | None | Unset = UNSET
    bragg: int | None | Unset = UNSET
    signal: float | None | Unset = UNSET
    dozor: float | None | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        image = self.image

        res: float | None | Unset
        if isinstance(self.res, Unset):
            res = UNSET
        else:
            res = self.res

        spots: int | None | Unset
        if isinstance(self.spots, Unset):
            spots = UNSET
        else:
            spots = self.spots

        bragg: int | None | Unset
        if isinstance(self.bragg, Unset):
            bragg = UNSET
        else:
            bragg = self.bragg

        signal: float | None | Unset
        if isinstance(self.signal, Unset):
            signal = UNSET
        else:
            signal = self.signal

        dozor: float | None | Unset
        if isinstance(self.dozor, Unset):
            dozor = UNSET
        else:
            dozor = self.dozor

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "image": image,
            }
        )
        if res is not UNSET:
            field_dict["res"] = res
        if spots is not UNSET:
            field_dict["spots"] = spots
        if bragg is not UNSET:
            field_dict["bragg"] = bragg
        if signal is not UNSET:
            field_dict["signal"] = signal
        if dozor is not UNSET:
            field_dict["dozor"] = dozor

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        image = d.pop("image")

        def _parse_res(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        res = _parse_res(d.pop("res", UNSET))

        def _parse_spots(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        spots = _parse_spots(d.pop("spots", UNSET))

        def _parse_bragg(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        bragg = _parse_bragg(d.pop("bragg", UNSET))

        def _parse_signal(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        signal = _parse_signal(d.pop("signal", UNSET))

        def _parse_dozor(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        dozor = _parse_dozor(d.pop("dozor", UNSET))

        image_quality_indicator_out = cls(
            image=image,
            res=res,
            spots=spots,
            bragg=bragg,
            signal=signal,
            dozor=dozor,
        )

        image_quality_indicator_out.additional_properties = d
        return image_quality_indicator_out

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

from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.strategy_option_screen_type_0 import StrategyOptionScreenType0
from ..types import UNSET, Unset

T = TypeVar("T", bound="StrategyOption")


@_attrs_define
class StrategyOption:
    """
    Attributes:
        screen (None | StrategyOptionScreenType0 | Unset):
        collect_samples (int | None | Unset):
        sample_group (None | str | Unset):
    """

    screen: None | StrategyOptionScreenType0 | Unset = UNSET
    collect_samples: int | None | Unset = UNSET
    sample_group: None | str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        screen: None | str | Unset
        if isinstance(self.screen, Unset):
            screen = UNSET
        elif isinstance(self.screen, StrategyOptionScreenType0):
            screen = self.screen.value
        else:
            screen = self.screen

        collect_samples: int | None | Unset
        if isinstance(self.collect_samples, Unset):
            collect_samples = UNSET
        else:
            collect_samples = self.collect_samples

        sample_group: None | str | Unset
        if isinstance(self.sample_group, Unset):
            sample_group = UNSET
        else:
            sample_group = self.sample_group

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if screen is not UNSET:
            field_dict["screen"] = screen
        if collect_samples is not UNSET:
            field_dict["collect_samples"] = collect_samples
        if sample_group is not UNSET:
            field_dict["sample_group"] = sample_group

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)

        def _parse_screen(data: object) -> None | StrategyOptionScreenType0 | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                screen_type_0 = StrategyOptionScreenType0(data)

                return screen_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(None | StrategyOptionScreenType0 | Unset, data)

        screen = _parse_screen(d.pop("screen", UNSET))

        def _parse_collect_samples(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        collect_samples = _parse_collect_samples(d.pop("collect_samples", UNSET))

        def _parse_sample_group(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        sample_group = _parse_sample_group(d.pop("sample_group", UNSET))

        strategy_option = cls(
            screen=screen,
            collect_samples=collect_samples,
            sample_group=sample_group,
        )

        strategy_option.additional_properties = d
        return strategy_option

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

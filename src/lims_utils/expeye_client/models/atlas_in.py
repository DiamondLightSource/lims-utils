from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define

from ..models.atlas_type import AtlasType
from ..models.grid_square_mode import GridSquareMode
from ..types import UNSET, Unset

T = TypeVar("T", bound="AtlasIn")


@_attrs_define
class AtlasIn:
    """
    Attributes:
        atlas_image (str):
        pixel_size (float):
        cassette_slot (int | None | Unset):
        has_red (bool | Unset):  Default: False.
        has_green (bool | Unset):  Default: False.
        has_blue (bool | Unset):  Default: False.
        has_cyan (bool | Unset):  Default: False.
        has_magenta (bool | Unset):  Default: False.
        has_yellow (bool | Unset):  Default: False.
        has_grey (bool | Unset):  Default: False.
        mode (GridSquareMode | None | Unset):
        atlas_type (AtlasType | Unset):
    """

    atlas_image: str
    pixel_size: float
    cassette_slot: int | None | Unset = UNSET
    has_red: bool | Unset = False
    has_green: bool | Unset = False
    has_blue: bool | Unset = False
    has_cyan: bool | Unset = False
    has_magenta: bool | Unset = False
    has_yellow: bool | Unset = False
    has_grey: bool | Unset = False
    mode: GridSquareMode | None | Unset = UNSET
    atlas_type: AtlasType | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        atlas_image = self.atlas_image

        pixel_size = self.pixel_size

        cassette_slot: int | None | Unset
        if isinstance(self.cassette_slot, Unset):
            cassette_slot = UNSET
        else:
            cassette_slot = self.cassette_slot

        has_red = self.has_red

        has_green = self.has_green

        has_blue = self.has_blue

        has_cyan = self.has_cyan

        has_magenta = self.has_magenta

        has_yellow = self.has_yellow

        has_grey = self.has_grey

        mode: None | str | Unset
        if isinstance(self.mode, Unset):
            mode = UNSET
        elif isinstance(self.mode, GridSquareMode):
            mode = self.mode.value
        else:
            mode = self.mode

        atlas_type: str | Unset = UNSET
        if not isinstance(self.atlas_type, Unset):
            atlas_type = self.atlas_type.value

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "atlasImage": atlas_image,
                "pixelSize": pixel_size,
            }
        )
        if cassette_slot is not UNSET:
            field_dict["cassetteSlot"] = cassette_slot
        if has_red is not UNSET:
            field_dict["hasRed"] = has_red
        if has_green is not UNSET:
            field_dict["hasGreen"] = has_green
        if has_blue is not UNSET:
            field_dict["hasBlue"] = has_blue
        if has_cyan is not UNSET:
            field_dict["hasCyan"] = has_cyan
        if has_magenta is not UNSET:
            field_dict["hasMagenta"] = has_magenta
        if has_yellow is not UNSET:
            field_dict["hasYellow"] = has_yellow
        if has_grey is not UNSET:
            field_dict["hasGrey"] = has_grey
        if mode is not UNSET:
            field_dict["mode"] = mode
        if atlas_type is not UNSET:
            field_dict["atlasType"] = atlas_type

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        atlas_image = d.pop("atlasImage")

        pixel_size = d.pop("pixelSize")

        def _parse_cassette_slot(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        cassette_slot = _parse_cassette_slot(d.pop("cassetteSlot", UNSET))

        has_red = d.pop("hasRed", UNSET)

        has_green = d.pop("hasGreen", UNSET)

        has_blue = d.pop("hasBlue", UNSET)

        has_cyan = d.pop("hasCyan", UNSET)

        has_magenta = d.pop("hasMagenta", UNSET)

        has_yellow = d.pop("hasYellow", UNSET)

        has_grey = d.pop("hasGrey", UNSET)

        def _parse_mode(data: object) -> GridSquareMode | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                mode_type_0 = GridSquareMode(data)

                return mode_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(GridSquareMode | None | Unset, data)

        mode = _parse_mode(d.pop("mode", UNSET))

        _atlas_type = d.pop("atlasType", UNSET)
        atlas_type: AtlasType | Unset
        if isinstance(_atlas_type, Unset):
            atlas_type = UNSET
        else:
            atlas_type = AtlasType(_atlas_type)

        atlas_in = cls(
            atlas_image=atlas_image,
            pixel_size=pixel_size,
            cassette_slot=cassette_slot,
            has_red=has_red,
            has_green=has_green,
            has_blue=has_blue,
            has_cyan=has_cyan,
            has_magenta=has_magenta,
            has_yellow=has_yellow,
            has_grey=has_grey,
            mode=mode,
            atlas_type=atlas_type,
        )

        return atlas_in

from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define

from ..models.atlas_type import AtlasType
from ..models.grid_square_mode import GridSquareMode
from ..types import UNSET, Unset

T = TypeVar("T", bound="AtlasOptional")


@_attrs_define
class AtlasOptional:
    """
    Attributes:
        atlas_image (str):
        cassette_slot (int | None | Unset):
        has_red (bool | Unset):  Default: False.
        has_green (bool | Unset):  Default: False.
        has_blue (bool | Unset):  Default: False.
        has_cyan (bool | Unset):  Default: False.
        has_magenta (bool | Unset):  Default: False.
        has_yellow (bool | Unset):  Default: False.
        has_grey (bool | Unset):  Default: False.
        mode (GridSquareMode | None | Unset):
        pixel_size (float | None | Unset):
        atlas_type (AtlasType | None | Unset):
    """

    atlas_image: str
    cassette_slot: int | None | Unset = UNSET
    has_red: bool | Unset = False
    has_green: bool | Unset = False
    has_blue: bool | Unset = False
    has_cyan: bool | Unset = False
    has_magenta: bool | Unset = False
    has_yellow: bool | Unset = False
    has_grey: bool | Unset = False
    mode: GridSquareMode | None | Unset = UNSET
    pixel_size: float | None | Unset = UNSET
    atlas_type: AtlasType | None | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        atlas_image = self.atlas_image

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

        pixel_size: float | None | Unset
        if isinstance(self.pixel_size, Unset):
            pixel_size = UNSET
        else:
            pixel_size = self.pixel_size

        atlas_type: None | str | Unset
        if isinstance(self.atlas_type, Unset):
            atlas_type = UNSET
        elif isinstance(self.atlas_type, AtlasType):
            atlas_type = self.atlas_type.value
        else:
            atlas_type = self.atlas_type

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "atlasImage": atlas_image,
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
        if pixel_size is not UNSET:
            field_dict["pixelSize"] = pixel_size
        if atlas_type is not UNSET:
            field_dict["atlasType"] = atlas_type

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        atlas_image = d.pop("atlasImage")

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

        def _parse_pixel_size(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        pixel_size = _parse_pixel_size(d.pop("pixelSize", UNSET))

        def _parse_atlas_type(data: object) -> AtlasType | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                atlas_type_type_0 = AtlasType(data)

                return atlas_type_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(AtlasType | None | Unset, data)

        atlas_type = _parse_atlas_type(d.pop("atlasType", UNSET))

        atlas_optional = cls(
            atlas_image=atlas_image,
            cassette_slot=cassette_slot,
            has_red=has_red,
            has_green=has_green,
            has_blue=has_blue,
            has_cyan=has_cyan,
            has_magenta=has_magenta,
            has_yellow=has_yellow,
            has_grey=has_grey,
            mode=mode,
            pixel_size=pixel_size,
            atlas_type=atlas_type,
        )

        return atlas_optional

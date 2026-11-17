from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define

from ..models.grid_square_mode import GridSquareMode
from ..types import UNSET, Unset

T = TypeVar("T", bound="GridSquareOut")


@_attrs_define
class GridSquareOut:
    """
    Attributes:
        pixel_location_x (int):
        pixel_location_y (int):
        height (int):
        width (int):
        angle (float):
        grid_square_image (None | str | Unset):
        has_red (bool | Unset):  Default: False.
        has_green (bool | Unset):  Default: False.
        has_blue (bool | Unset):  Default: False.
        has_cyan (bool | Unset):  Default: False.
        has_magenta (bool | Unset):  Default: False.
        has_yellow (bool | Unset):  Default: False.
        has_grey (bool | Unset):  Default: False.
        mode (GridSquareMode | None | Unset):
        grid_square_id (int | None | Unset):
        atlas_id (int | None | Unset):
    """

    pixel_location_x: int
    pixel_location_y: int
    height: int
    width: int
    angle: float
    grid_square_image: None | str | Unset = UNSET
    has_red: bool | Unset = False
    has_green: bool | Unset = False
    has_blue: bool | Unset = False
    has_cyan: bool | Unset = False
    has_magenta: bool | Unset = False
    has_yellow: bool | Unset = False
    has_grey: bool | Unset = False
    mode: GridSquareMode | None | Unset = UNSET
    grid_square_id: int | None | Unset = UNSET
    atlas_id: int | None | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        pixel_location_x = self.pixel_location_x

        pixel_location_y = self.pixel_location_y

        height = self.height

        width = self.width

        angle = self.angle

        grid_square_image: None | str | Unset
        if isinstance(self.grid_square_image, Unset):
            grid_square_image = UNSET
        else:
            grid_square_image = self.grid_square_image

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

        grid_square_id: int | None | Unset
        if isinstance(self.grid_square_id, Unset):
            grid_square_id = UNSET
        else:
            grid_square_id = self.grid_square_id

        atlas_id: int | None | Unset
        if isinstance(self.atlas_id, Unset):
            atlas_id = UNSET
        else:
            atlas_id = self.atlas_id

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "pixelLocationX": pixel_location_x,
                "pixelLocationY": pixel_location_y,
                "height": height,
                "width": width,
                "angle": angle,
            }
        )
        if grid_square_image is not UNSET:
            field_dict["gridSquareImage"] = grid_square_image
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
        if grid_square_id is not UNSET:
            field_dict["gridSquareId"] = grid_square_id
        if atlas_id is not UNSET:
            field_dict["atlasId"] = atlas_id

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        pixel_location_x = d.pop("pixelLocationX")

        pixel_location_y = d.pop("pixelLocationY")

        height = d.pop("height")

        width = d.pop("width")

        angle = d.pop("angle")

        def _parse_grid_square_image(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        grid_square_image = _parse_grid_square_image(d.pop("gridSquareImage", UNSET))

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

        def _parse_grid_square_id(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        grid_square_id = _parse_grid_square_id(d.pop("gridSquareId", UNSET))

        def _parse_atlas_id(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        atlas_id = _parse_atlas_id(d.pop("atlasId", UNSET))

        grid_square_out = cls(
            pixel_location_x=pixel_location_x,
            pixel_location_y=pixel_location_y,
            height=height,
            width=width,
            angle=angle,
            grid_square_image=grid_square_image,
            has_red=has_red,
            has_green=has_green,
            has_blue=has_blue,
            has_cyan=has_cyan,
            has_magenta=has_magenta,
            has_yellow=has_yellow,
            has_grey=has_grey,
            mode=mode,
            grid_square_id=grid_square_id,
            atlas_id=atlas_id,
        )

        return grid_square_out

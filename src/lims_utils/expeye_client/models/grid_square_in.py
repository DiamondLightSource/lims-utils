from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define

from ..models.grid_square_mode import GridSquareMode
from ..types import UNSET, Unset

T = TypeVar("T", bound="GridSquareIn")


@_attrs_define
class GridSquareIn:
    """
    Attributes:
        pixel_location_x (int):
        pixel_location_y (int):
        height (int):
        width (int):
        angle (float):
        mode (GridSquareMode):
        grid_square_image (None | str | Unset):
        has_red (bool | Unset):  Default: False.
        has_green (bool | Unset):  Default: False.
        has_blue (bool | Unset):  Default: False.
        has_cyan (bool | Unset):  Default: False.
        has_magenta (bool | Unset):  Default: False.
        has_yellow (bool | Unset):  Default: False.
        has_grey (bool | Unset):  Default: False.
    """

    pixel_location_x: int
    pixel_location_y: int
    height: int
    width: int
    angle: float
    mode: GridSquareMode
    grid_square_image: None | str | Unset = UNSET
    has_red: bool | Unset = False
    has_green: bool | Unset = False
    has_blue: bool | Unset = False
    has_cyan: bool | Unset = False
    has_magenta: bool | Unset = False
    has_yellow: bool | Unset = False
    has_grey: bool | Unset = False

    def to_dict(self) -> dict[str, Any]:
        pixel_location_x = self.pixel_location_x

        pixel_location_y = self.pixel_location_y

        height = self.height

        width = self.width

        angle = self.angle

        mode = self.mode.value

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

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "pixelLocationX": pixel_location_x,
                "pixelLocationY": pixel_location_y,
                "height": height,
                "width": width,
                "angle": angle,
                "mode": mode,
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

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        pixel_location_x = d.pop("pixelLocationX")

        pixel_location_y = d.pop("pixelLocationY")

        height = d.pop("height")

        width = d.pop("width")

        angle = d.pop("angle")

        mode = GridSquareMode(d.pop("mode"))

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

        grid_square_in = cls(
            pixel_location_x=pixel_location_x,
            pixel_location_y=pixel_location_y,
            height=height,
            width=width,
            angle=angle,
            mode=mode,
            grid_square_image=grid_square_image,
            has_red=has_red,
            has_green=has_green,
            has_blue=has_blue,
            has_cyan=has_cyan,
            has_magenta=has_magenta,
            has_yellow=has_yellow,
            has_grey=has_grey,
        )

        return grid_square_in

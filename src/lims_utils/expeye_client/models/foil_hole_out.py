from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define

from ..types import UNSET, Unset

T = TypeVar("T", bound="FoilHoleOut")


@_attrs_define
class FoilHoleOut:
    """
    Attributes:
        foil_hole_label (str):
        foil_hole_image (None | str | Unset):
        pixel_location_x (int | None | Unset):
        pixel_location_y (int | None | Unset):
        diameter (int | None | Unset):
        stage_location_x (float | None | Unset):
        stage_location_y (float | None | Unset):
        quality_indicator (float | None | Unset):
        pixel_size (float | None | Unset):
        foil_hole_id (int | None | Unset):
        grid_square_id (int | None | Unset):
        movie_count (int | None | Unset):  Default: 0.
        particle_count (float | None | Unset):
        resolution (float | None | Unset):
        astigmatism (float | None | Unset):
    """

    foil_hole_label: str
    foil_hole_image: None | str | Unset = UNSET
    pixel_location_x: int | None | Unset = UNSET
    pixel_location_y: int | None | Unset = UNSET
    diameter: int | None | Unset = UNSET
    stage_location_x: float | None | Unset = UNSET
    stage_location_y: float | None | Unset = UNSET
    quality_indicator: float | None | Unset = UNSET
    pixel_size: float | None | Unset = UNSET
    foil_hole_id: int | None | Unset = UNSET
    grid_square_id: int | None | Unset = UNSET
    movie_count: int | None | Unset = 0
    particle_count: float | None | Unset = UNSET
    resolution: float | None | Unset = UNSET
    astigmatism: float | None | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        foil_hole_label = self.foil_hole_label

        foil_hole_image: None | str | Unset
        if isinstance(self.foil_hole_image, Unset):
            foil_hole_image = UNSET
        else:
            foil_hole_image = self.foil_hole_image

        pixel_location_x: int | None | Unset
        if isinstance(self.pixel_location_x, Unset):
            pixel_location_x = UNSET
        else:
            pixel_location_x = self.pixel_location_x

        pixel_location_y: int | None | Unset
        if isinstance(self.pixel_location_y, Unset):
            pixel_location_y = UNSET
        else:
            pixel_location_y = self.pixel_location_y

        diameter: int | None | Unset
        if isinstance(self.diameter, Unset):
            diameter = UNSET
        else:
            diameter = self.diameter

        stage_location_x: float | None | Unset
        if isinstance(self.stage_location_x, Unset):
            stage_location_x = UNSET
        else:
            stage_location_x = self.stage_location_x

        stage_location_y: float | None | Unset
        if isinstance(self.stage_location_y, Unset):
            stage_location_y = UNSET
        else:
            stage_location_y = self.stage_location_y

        quality_indicator: float | None | Unset
        if isinstance(self.quality_indicator, Unset):
            quality_indicator = UNSET
        else:
            quality_indicator = self.quality_indicator

        pixel_size: float | None | Unset
        if isinstance(self.pixel_size, Unset):
            pixel_size = UNSET
        else:
            pixel_size = self.pixel_size

        foil_hole_id: int | None | Unset
        if isinstance(self.foil_hole_id, Unset):
            foil_hole_id = UNSET
        else:
            foil_hole_id = self.foil_hole_id

        grid_square_id: int | None | Unset
        if isinstance(self.grid_square_id, Unset):
            grid_square_id = UNSET
        else:
            grid_square_id = self.grid_square_id

        movie_count: int | None | Unset
        if isinstance(self.movie_count, Unset):
            movie_count = UNSET
        else:
            movie_count = self.movie_count

        particle_count: float | None | Unset
        if isinstance(self.particle_count, Unset):
            particle_count = UNSET
        else:
            particle_count = self.particle_count

        resolution: float | None | Unset
        if isinstance(self.resolution, Unset):
            resolution = UNSET
        else:
            resolution = self.resolution

        astigmatism: float | None | Unset
        if isinstance(self.astigmatism, Unset):
            astigmatism = UNSET
        else:
            astigmatism = self.astigmatism

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "foilHoleLabel": foil_hole_label,
            }
        )
        if foil_hole_image is not UNSET:
            field_dict["foilHoleImage"] = foil_hole_image
        if pixel_location_x is not UNSET:
            field_dict["pixelLocationX"] = pixel_location_x
        if pixel_location_y is not UNSET:
            field_dict["pixelLocationY"] = pixel_location_y
        if diameter is not UNSET:
            field_dict["diameter"] = diameter
        if stage_location_x is not UNSET:
            field_dict["stageLocationX"] = stage_location_x
        if stage_location_y is not UNSET:
            field_dict["stageLocationY"] = stage_location_y
        if quality_indicator is not UNSET:
            field_dict["qualityIndicator"] = quality_indicator
        if pixel_size is not UNSET:
            field_dict["pixelSize"] = pixel_size
        if foil_hole_id is not UNSET:
            field_dict["foilHoleId"] = foil_hole_id
        if grid_square_id is not UNSET:
            field_dict["gridSquareId"] = grid_square_id
        if movie_count is not UNSET:
            field_dict["movieCount"] = movie_count
        if particle_count is not UNSET:
            field_dict["particleCount"] = particle_count
        if resolution is not UNSET:
            field_dict["resolution"] = resolution
        if astigmatism is not UNSET:
            field_dict["astigmatism"] = astigmatism

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        foil_hole_label = d.pop("foilHoleLabel")

        def _parse_foil_hole_image(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        foil_hole_image = _parse_foil_hole_image(d.pop("foilHoleImage", UNSET))

        def _parse_pixel_location_x(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        pixel_location_x = _parse_pixel_location_x(d.pop("pixelLocationX", UNSET))

        def _parse_pixel_location_y(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        pixel_location_y = _parse_pixel_location_y(d.pop("pixelLocationY", UNSET))

        def _parse_diameter(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        diameter = _parse_diameter(d.pop("diameter", UNSET))

        def _parse_stage_location_x(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        stage_location_x = _parse_stage_location_x(d.pop("stageLocationX", UNSET))

        def _parse_stage_location_y(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        stage_location_y = _parse_stage_location_y(d.pop("stageLocationY", UNSET))

        def _parse_quality_indicator(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        quality_indicator = _parse_quality_indicator(d.pop("qualityIndicator", UNSET))

        def _parse_pixel_size(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        pixel_size = _parse_pixel_size(d.pop("pixelSize", UNSET))

        def _parse_foil_hole_id(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        foil_hole_id = _parse_foil_hole_id(d.pop("foilHoleId", UNSET))

        def _parse_grid_square_id(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        grid_square_id = _parse_grid_square_id(d.pop("gridSquareId", UNSET))

        def _parse_movie_count(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        movie_count = _parse_movie_count(d.pop("movieCount", UNSET))

        def _parse_particle_count(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        particle_count = _parse_particle_count(d.pop("particleCount", UNSET))

        def _parse_resolution(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        resolution = _parse_resolution(d.pop("resolution", UNSET))

        def _parse_astigmatism(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        astigmatism = _parse_astigmatism(d.pop("astigmatism", UNSET))

        foil_hole_out = cls(
            foil_hole_label=foil_hole_label,
            foil_hole_image=foil_hole_image,
            pixel_location_x=pixel_location_x,
            pixel_location_y=pixel_location_y,
            diameter=diameter,
            stage_location_x=stage_location_x,
            stage_location_y=stage_location_y,
            quality_indicator=quality_indicator,
            pixel_size=pixel_size,
            foil_hole_id=foil_hole_id,
            grid_square_id=grid_square_id,
            movie_count=movie_count,
            particle_count=particle_count,
            resolution=resolution,
            astigmatism=astigmatism,
        )

        return foil_hole_out

from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define

from ..types import UNSET, Unset

T = TypeVar("T", bound="MovieOut")


@_attrs_define
class MovieOut:
    """
    Attributes:
        movie_id (int):
        movie_number (int | None | Unset):
        movie_full_path (None | str | Unset):
        created_time_stamp (datetime.datetime | Unset):
        position_x (float | None | Unset):
        position_y (float | None | Unset):
        nominal_defocus (float | None | Unset):
        angle (float | None | Unset):
        fluence (float | None | Unset):
        number_of_frames (int | None | Unset):
        foil_hole_id (int | None | Unset):
    """

    movie_id: int
    movie_number: int | None | Unset = UNSET
    movie_full_path: None | str | Unset = UNSET
    created_time_stamp: datetime.datetime | Unset = UNSET
    position_x: float | None | Unset = UNSET
    position_y: float | None | Unset = UNSET
    nominal_defocus: float | None | Unset = UNSET
    angle: float | None | Unset = UNSET
    fluence: float | None | Unset = UNSET
    number_of_frames: int | None | Unset = UNSET
    foil_hole_id: int | None | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        movie_id = self.movie_id

        movie_number: int | None | Unset
        if isinstance(self.movie_number, Unset):
            movie_number = UNSET
        else:
            movie_number = self.movie_number

        movie_full_path: None | str | Unset
        if isinstance(self.movie_full_path, Unset):
            movie_full_path = UNSET
        else:
            movie_full_path = self.movie_full_path

        created_time_stamp: str | Unset = UNSET
        if not isinstance(self.created_time_stamp, Unset):
            created_time_stamp = self.created_time_stamp.isoformat()

        position_x: float | None | Unset
        if isinstance(self.position_x, Unset):
            position_x = UNSET
        else:
            position_x = self.position_x

        position_y: float | None | Unset
        if isinstance(self.position_y, Unset):
            position_y = UNSET
        else:
            position_y = self.position_y

        nominal_defocus: float | None | Unset
        if isinstance(self.nominal_defocus, Unset):
            nominal_defocus = UNSET
        else:
            nominal_defocus = self.nominal_defocus

        angle: float | None | Unset
        if isinstance(self.angle, Unset):
            angle = UNSET
        else:
            angle = self.angle

        fluence: float | None | Unset
        if isinstance(self.fluence, Unset):
            fluence = UNSET
        else:
            fluence = self.fluence

        number_of_frames: int | None | Unset
        if isinstance(self.number_of_frames, Unset):
            number_of_frames = UNSET
        else:
            number_of_frames = self.number_of_frames

        foil_hole_id: int | None | Unset
        if isinstance(self.foil_hole_id, Unset):
            foil_hole_id = UNSET
        else:
            foil_hole_id = self.foil_hole_id

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "movieId": movie_id,
            }
        )
        if movie_number is not UNSET:
            field_dict["movieNumber"] = movie_number
        if movie_full_path is not UNSET:
            field_dict["movieFullPath"] = movie_full_path
        if created_time_stamp is not UNSET:
            field_dict["createdTimeStamp"] = created_time_stamp
        if position_x is not UNSET:
            field_dict["positionX"] = position_x
        if position_y is not UNSET:
            field_dict["positionY"] = position_y
        if nominal_defocus is not UNSET:
            field_dict["nominalDefocus"] = nominal_defocus
        if angle is not UNSET:
            field_dict["angle"] = angle
        if fluence is not UNSET:
            field_dict["fluence"] = fluence
        if number_of_frames is not UNSET:
            field_dict["numberOfFrames"] = number_of_frames
        if foil_hole_id is not UNSET:
            field_dict["foilHoleId"] = foil_hole_id

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        movie_id = d.pop("movieId")

        def _parse_movie_number(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        movie_number = _parse_movie_number(d.pop("movieNumber", UNSET))

        def _parse_movie_full_path(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        movie_full_path = _parse_movie_full_path(d.pop("movieFullPath", UNSET))

        _created_time_stamp = d.pop("createdTimeStamp", UNSET)
        created_time_stamp: datetime.datetime | Unset
        if isinstance(_created_time_stamp, Unset):
            created_time_stamp = UNSET
        else:
            created_time_stamp = datetime.datetime.fromisoformat(_created_time_stamp)

        def _parse_position_x(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        position_x = _parse_position_x(d.pop("positionX", UNSET))

        def _parse_position_y(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        position_y = _parse_position_y(d.pop("positionY", UNSET))

        def _parse_nominal_defocus(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        nominal_defocus = _parse_nominal_defocus(d.pop("nominalDefocus", UNSET))

        def _parse_angle(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        angle = _parse_angle(d.pop("angle", UNSET))

        def _parse_fluence(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        fluence = _parse_fluence(d.pop("fluence", UNSET))

        def _parse_number_of_frames(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        number_of_frames = _parse_number_of_frames(d.pop("numberOfFrames", UNSET))

        def _parse_foil_hole_id(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        foil_hole_id = _parse_foil_hole_id(d.pop("foilHoleId", UNSET))

        movie_out = cls(
            movie_id=movie_id,
            movie_number=movie_number,
            movie_full_path=movie_full_path,
            created_time_stamp=created_time_stamp,
            position_x=position_x,
            position_y=position_y,
            nominal_defocus=nominal_defocus,
            angle=angle,
            fluence=fluence,
            number_of_frames=number_of_frames,
            foil_hole_id=foil_hole_id,
        )

        return movie_out

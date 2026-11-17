from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define

if TYPE_CHECKING:
    from ..models.ctf_out import CTFOut
    from ..models.motion_correction_out import MotionCorrectionOut
    from ..models.movie_out import MovieOut
    from ..models.tilt_image_alignment_out import TiltImageAlignmentOut


T = TypeVar("T", bound="FullMovieOut")


@_attrs_define
class FullMovieOut:
    """
    Attributes:
        ctf (CTFOut):
        movie (MovieOut):
        motion_correction (MotionCorrectionOut):
        tilt_image_alignment (None | TiltImageAlignmentOut):
    """

    ctf: CTFOut
    movie: MovieOut
    motion_correction: MotionCorrectionOut
    tilt_image_alignment: None | TiltImageAlignmentOut

    def to_dict(self) -> dict[str, Any]:
        from ..models.tilt_image_alignment_out import TiltImageAlignmentOut

        ctf = self.ctf.to_dict()

        movie = self.movie.to_dict()

        motion_correction = self.motion_correction.to_dict()

        tilt_image_alignment: dict[str, Any] | None
        if isinstance(self.tilt_image_alignment, TiltImageAlignmentOut):
            tilt_image_alignment = self.tilt_image_alignment.to_dict()
        else:
            tilt_image_alignment = self.tilt_image_alignment

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "CTF": ctf,
                "movie": movie,
                "motionCorrection": motion_correction,
                "tiltImageAlignment": tilt_image_alignment,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.ctf_out import CTFOut
        from ..models.motion_correction_out import MotionCorrectionOut
        from ..models.movie_out import MovieOut
        from ..models.tilt_image_alignment_out import TiltImageAlignmentOut

        d = dict(src_dict)
        ctf = CTFOut.from_dict(d.pop("CTF"))

        movie = MovieOut.from_dict(d.pop("movie"))

        motion_correction = MotionCorrectionOut.from_dict(d.pop("motionCorrection"))

        def _parse_tilt_image_alignment(data: object) -> None | TiltImageAlignmentOut:
            if data is None:
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                tilt_image_alignment_type_0 = TiltImageAlignmentOut.from_dict(data)

                return tilt_image_alignment_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(None | TiltImageAlignmentOut, data)

        tilt_image_alignment = _parse_tilt_image_alignment(d.pop("tiltImageAlignment"))

        full_movie_out = cls(
            ctf=ctf,
            movie=movie,
            motion_correction=motion_correction,
            tilt_image_alignment=tilt_image_alignment,
        )

        return full_movie_out

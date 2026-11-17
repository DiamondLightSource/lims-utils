from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.ctf_base import CTFBase
    from ..models.motion_correction_optional import MotionCorrectionOptional
    from ..models.movie_optional import MovieOptional
    from ..models.tilt_image_alignment_optional import TiltImageAlignmentOptional


T = TypeVar("T", bound="FullMovieOptional")


@_attrs_define
class FullMovieOptional:
    """
    Attributes:
        movie (MovieOptional | Unset):
        motion_correction (MotionCorrectionOptional | Unset):
        ctf (CTFBase | Unset):
        tilt_image_alignment (None | TiltImageAlignmentOptional | Unset):
    """

    movie: MovieOptional | Unset = UNSET
    motion_correction: MotionCorrectionOptional | Unset = UNSET
    ctf: CTFBase | Unset = UNSET
    tilt_image_alignment: None | TiltImageAlignmentOptional | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        from ..models.tilt_image_alignment_optional import TiltImageAlignmentOptional

        movie: dict[str, Any] | Unset = UNSET
        if not isinstance(self.movie, Unset):
            movie = self.movie.to_dict()

        motion_correction: dict[str, Any] | Unset = UNSET
        if not isinstance(self.motion_correction, Unset):
            motion_correction = self.motion_correction.to_dict()

        ctf: dict[str, Any] | Unset = UNSET
        if not isinstance(self.ctf, Unset):
            ctf = self.ctf.to_dict()

        tilt_image_alignment: dict[str, Any] | None | Unset
        if isinstance(self.tilt_image_alignment, Unset):
            tilt_image_alignment = UNSET
        elif isinstance(self.tilt_image_alignment, TiltImageAlignmentOptional):
            tilt_image_alignment = self.tilt_image_alignment.to_dict()
        else:
            tilt_image_alignment = self.tilt_image_alignment

        field_dict: dict[str, Any] = {}

        field_dict.update({})
        if movie is not UNSET:
            field_dict["movie"] = movie
        if motion_correction is not UNSET:
            field_dict["motionCorrection"] = motion_correction
        if ctf is not UNSET:
            field_dict["CTF"] = ctf
        if tilt_image_alignment is not UNSET:
            field_dict["tiltImageAlignment"] = tilt_image_alignment

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.ctf_base import CTFBase
        from ..models.motion_correction_optional import MotionCorrectionOptional
        from ..models.movie_optional import MovieOptional
        from ..models.tilt_image_alignment_optional import TiltImageAlignmentOptional

        d = dict(src_dict)
        _movie = d.pop("movie", UNSET)
        movie: MovieOptional | Unset
        if isinstance(_movie, Unset):
            movie = UNSET
        else:
            movie = MovieOptional.from_dict(_movie)

        _motion_correction = d.pop("motionCorrection", UNSET)
        motion_correction: MotionCorrectionOptional | Unset
        if isinstance(_motion_correction, Unset):
            motion_correction = UNSET
        else:
            motion_correction = MotionCorrectionOptional.from_dict(_motion_correction)

        _ctf = d.pop("CTF", UNSET)
        ctf: CTFBase | Unset
        if isinstance(_ctf, Unset):
            ctf = UNSET
        else:
            ctf = CTFBase.from_dict(_ctf)

        def _parse_tilt_image_alignment(data: object) -> None | TiltImageAlignmentOptional | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                tilt_image_alignment_type_0 = TiltImageAlignmentOptional.from_dict(data)

                return tilt_image_alignment_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(None | TiltImageAlignmentOptional | Unset, data)

        tilt_image_alignment = _parse_tilt_image_alignment(d.pop("tiltImageAlignment", UNSET))

        full_movie_optional = cls(
            movie=movie,
            motion_correction=motion_correction,
            ctf=ctf,
            tilt_image_alignment=tilt_image_alignment,
        )

        return full_movie_optional

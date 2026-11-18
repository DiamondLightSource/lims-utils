from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define

from ..types import UNSET, Unset

T = TypeVar("T", bound="TiltImageAlignmentOptional")


@_attrs_define
class TiltImageAlignmentOptional:
    """
    Attributes:
        tomogram_id (int | None | Unset):
        defocus_u (float | None | Unset):
        defocus_v (float | None | Unset):
        psd_file (None | str | Unset):
        resolution (float | None | Unset):
        fit_quality (float | None | Unset):
        refined_magnification (float | None | Unset):
        refined_tilt_angle (float | None | Unset):
        refined_tilt_axis (float | None | Unset):
        residual_error (float | None | Unset):
    """

    tomogram_id: int | None | Unset = UNSET
    defocus_u: float | None | Unset = UNSET
    defocus_v: float | None | Unset = UNSET
    psd_file: None | str | Unset = UNSET
    resolution: float | None | Unset = UNSET
    fit_quality: float | None | Unset = UNSET
    refined_magnification: float | None | Unset = UNSET
    refined_tilt_angle: float | None | Unset = UNSET
    refined_tilt_axis: float | None | Unset = UNSET
    residual_error: float | None | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        tomogram_id: int | None | Unset
        if isinstance(self.tomogram_id, Unset):
            tomogram_id = UNSET
        else:
            tomogram_id = self.tomogram_id

        defocus_u: float | None | Unset
        if isinstance(self.defocus_u, Unset):
            defocus_u = UNSET
        else:
            defocus_u = self.defocus_u

        defocus_v: float | None | Unset
        if isinstance(self.defocus_v, Unset):
            defocus_v = UNSET
        else:
            defocus_v = self.defocus_v

        psd_file: None | str | Unset
        if isinstance(self.psd_file, Unset):
            psd_file = UNSET
        else:
            psd_file = self.psd_file

        resolution: float | None | Unset
        if isinstance(self.resolution, Unset):
            resolution = UNSET
        else:
            resolution = self.resolution

        fit_quality: float | None | Unset
        if isinstance(self.fit_quality, Unset):
            fit_quality = UNSET
        else:
            fit_quality = self.fit_quality

        refined_magnification: float | None | Unset
        if isinstance(self.refined_magnification, Unset):
            refined_magnification = UNSET
        else:
            refined_magnification = self.refined_magnification

        refined_tilt_angle: float | None | Unset
        if isinstance(self.refined_tilt_angle, Unset):
            refined_tilt_angle = UNSET
        else:
            refined_tilt_angle = self.refined_tilt_angle

        refined_tilt_axis: float | None | Unset
        if isinstance(self.refined_tilt_axis, Unset):
            refined_tilt_axis = UNSET
        else:
            refined_tilt_axis = self.refined_tilt_axis

        residual_error: float | None | Unset
        if isinstance(self.residual_error, Unset):
            residual_error = UNSET
        else:
            residual_error = self.residual_error

        field_dict: dict[str, Any] = {}

        field_dict.update({})
        if tomogram_id is not UNSET:
            field_dict["tomogramId"] = tomogram_id
        if defocus_u is not UNSET:
            field_dict["defocusU"] = defocus_u
        if defocus_v is not UNSET:
            field_dict["defocusV"] = defocus_v
        if psd_file is not UNSET:
            field_dict["psdFile"] = psd_file
        if resolution is not UNSET:
            field_dict["resolution"] = resolution
        if fit_quality is not UNSET:
            field_dict["fitQuality"] = fit_quality
        if refined_magnification is not UNSET:
            field_dict["refinedMagnification"] = refined_magnification
        if refined_tilt_angle is not UNSET:
            field_dict["refinedTiltAngle"] = refined_tilt_angle
        if refined_tilt_axis is not UNSET:
            field_dict["refinedTiltAxis"] = refined_tilt_axis
        if residual_error is not UNSET:
            field_dict["residualError"] = residual_error

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)

        def _parse_tomogram_id(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        tomogram_id = _parse_tomogram_id(d.pop("tomogramId", UNSET))

        def _parse_defocus_u(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        defocus_u = _parse_defocus_u(d.pop("defocusU", UNSET))

        def _parse_defocus_v(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        defocus_v = _parse_defocus_v(d.pop("defocusV", UNSET))

        def _parse_psd_file(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        psd_file = _parse_psd_file(d.pop("psdFile", UNSET))

        def _parse_resolution(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        resolution = _parse_resolution(d.pop("resolution", UNSET))

        def _parse_fit_quality(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        fit_quality = _parse_fit_quality(d.pop("fitQuality", UNSET))

        def _parse_refined_magnification(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        refined_magnification = _parse_refined_magnification(d.pop("refinedMagnification", UNSET))

        def _parse_refined_tilt_angle(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        refined_tilt_angle = _parse_refined_tilt_angle(d.pop("refinedTiltAngle", UNSET))

        def _parse_refined_tilt_axis(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        refined_tilt_axis = _parse_refined_tilt_axis(d.pop("refinedTiltAxis", UNSET))

        def _parse_residual_error(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        residual_error = _parse_residual_error(d.pop("residualError", UNSET))

        tilt_image_alignment_optional = cls(
            tomogram_id=tomogram_id,
            defocus_u=defocus_u,
            defocus_v=defocus_v,
            psd_file=psd_file,
            resolution=resolution,
            fit_quality=fit_quality,
            refined_magnification=refined_magnification,
            refined_tilt_angle=refined_tilt_angle,
            refined_tilt_axis=refined_tilt_axis,
            residual_error=residual_error,
        )

        return tilt_image_alignment_optional

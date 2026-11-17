from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define

from ..types import UNSET, Unset

T = TypeVar("T", bound="CTFBase")


@_attrs_define
class CTFBase:
    """
    Attributes:
        auto_proc_program_id (int | None | Unset):
        box_size_x (float | None | Unset):
        box_size_y (float | None | Unset):
        min_resolution (float | None | Unset):
        max_resolution (float | None | Unset):
        min_defocus (float | None | Unset):
        max_defocus (float | None | Unset):
        defocus_step_size (float | None | Unset):
        astigmatism (float | None | Unset):
        astigmatism_angle (float | None | Unset):
        estimated_resolution (float | None | Unset):
        estimated_defocus (float | None | Unset):
        amplitude_contrast (float | None | Unset):
        cc_value (float | None | Unset):
        fft_theoretical_full_path (None | str | Unset):
        comments (None | str | Unset):
        ice_ring_density (float | None | Unset):
    """

    auto_proc_program_id: int | None | Unset = UNSET
    box_size_x: float | None | Unset = UNSET
    box_size_y: float | None | Unset = UNSET
    min_resolution: float | None | Unset = UNSET
    max_resolution: float | None | Unset = UNSET
    min_defocus: float | None | Unset = UNSET
    max_defocus: float | None | Unset = UNSET
    defocus_step_size: float | None | Unset = UNSET
    astigmatism: float | None | Unset = UNSET
    astigmatism_angle: float | None | Unset = UNSET
    estimated_resolution: float | None | Unset = UNSET
    estimated_defocus: float | None | Unset = UNSET
    amplitude_contrast: float | None | Unset = UNSET
    cc_value: float | None | Unset = UNSET
    fft_theoretical_full_path: None | str | Unset = UNSET
    comments: None | str | Unset = UNSET
    ice_ring_density: float | None | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        auto_proc_program_id: int | None | Unset
        if isinstance(self.auto_proc_program_id, Unset):
            auto_proc_program_id = UNSET
        else:
            auto_proc_program_id = self.auto_proc_program_id

        box_size_x: float | None | Unset
        if isinstance(self.box_size_x, Unset):
            box_size_x = UNSET
        else:
            box_size_x = self.box_size_x

        box_size_y: float | None | Unset
        if isinstance(self.box_size_y, Unset):
            box_size_y = UNSET
        else:
            box_size_y = self.box_size_y

        min_resolution: float | None | Unset
        if isinstance(self.min_resolution, Unset):
            min_resolution = UNSET
        else:
            min_resolution = self.min_resolution

        max_resolution: float | None | Unset
        if isinstance(self.max_resolution, Unset):
            max_resolution = UNSET
        else:
            max_resolution = self.max_resolution

        min_defocus: float | None | Unset
        if isinstance(self.min_defocus, Unset):
            min_defocus = UNSET
        else:
            min_defocus = self.min_defocus

        max_defocus: float | None | Unset
        if isinstance(self.max_defocus, Unset):
            max_defocus = UNSET
        else:
            max_defocus = self.max_defocus

        defocus_step_size: float | None | Unset
        if isinstance(self.defocus_step_size, Unset):
            defocus_step_size = UNSET
        else:
            defocus_step_size = self.defocus_step_size

        astigmatism: float | None | Unset
        if isinstance(self.astigmatism, Unset):
            astigmatism = UNSET
        else:
            astigmatism = self.astigmatism

        astigmatism_angle: float | None | Unset
        if isinstance(self.astigmatism_angle, Unset):
            astigmatism_angle = UNSET
        else:
            astigmatism_angle = self.astigmatism_angle

        estimated_resolution: float | None | Unset
        if isinstance(self.estimated_resolution, Unset):
            estimated_resolution = UNSET
        else:
            estimated_resolution = self.estimated_resolution

        estimated_defocus: float | None | Unset
        if isinstance(self.estimated_defocus, Unset):
            estimated_defocus = UNSET
        else:
            estimated_defocus = self.estimated_defocus

        amplitude_contrast: float | None | Unset
        if isinstance(self.amplitude_contrast, Unset):
            amplitude_contrast = UNSET
        else:
            amplitude_contrast = self.amplitude_contrast

        cc_value: float | None | Unset
        if isinstance(self.cc_value, Unset):
            cc_value = UNSET
        else:
            cc_value = self.cc_value

        fft_theoretical_full_path: None | str | Unset
        if isinstance(self.fft_theoretical_full_path, Unset):
            fft_theoretical_full_path = UNSET
        else:
            fft_theoretical_full_path = self.fft_theoretical_full_path

        comments: None | str | Unset
        if isinstance(self.comments, Unset):
            comments = UNSET
        else:
            comments = self.comments

        ice_ring_density: float | None | Unset
        if isinstance(self.ice_ring_density, Unset):
            ice_ring_density = UNSET
        else:
            ice_ring_density = self.ice_ring_density

        field_dict: dict[str, Any] = {}

        field_dict.update({})
        if auto_proc_program_id is not UNSET:
            field_dict["autoProcProgramId"] = auto_proc_program_id
        if box_size_x is not UNSET:
            field_dict["boxSizeX"] = box_size_x
        if box_size_y is not UNSET:
            field_dict["boxSizeY"] = box_size_y
        if min_resolution is not UNSET:
            field_dict["minResolution"] = min_resolution
        if max_resolution is not UNSET:
            field_dict["maxResolution"] = max_resolution
        if min_defocus is not UNSET:
            field_dict["minDefocus"] = min_defocus
        if max_defocus is not UNSET:
            field_dict["maxDefocus"] = max_defocus
        if defocus_step_size is not UNSET:
            field_dict["defocusStepSize"] = defocus_step_size
        if astigmatism is not UNSET:
            field_dict["astigmatism"] = astigmatism
        if astigmatism_angle is not UNSET:
            field_dict["astigmatismAngle"] = astigmatism_angle
        if estimated_resolution is not UNSET:
            field_dict["estimatedResolution"] = estimated_resolution
        if estimated_defocus is not UNSET:
            field_dict["estimatedDefocus"] = estimated_defocus
        if amplitude_contrast is not UNSET:
            field_dict["amplitudeContrast"] = amplitude_contrast
        if cc_value is not UNSET:
            field_dict["ccValue"] = cc_value
        if fft_theoretical_full_path is not UNSET:
            field_dict["fftTheoreticalFullPath"] = fft_theoretical_full_path
        if comments is not UNSET:
            field_dict["comments"] = comments
        if ice_ring_density is not UNSET:
            field_dict["iceRingDensity"] = ice_ring_density

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)

        def _parse_auto_proc_program_id(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        auto_proc_program_id = _parse_auto_proc_program_id(d.pop("autoProcProgramId", UNSET))

        def _parse_box_size_x(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        box_size_x = _parse_box_size_x(d.pop("boxSizeX", UNSET))

        def _parse_box_size_y(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        box_size_y = _parse_box_size_y(d.pop("boxSizeY", UNSET))

        def _parse_min_resolution(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        min_resolution = _parse_min_resolution(d.pop("minResolution", UNSET))

        def _parse_max_resolution(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        max_resolution = _parse_max_resolution(d.pop("maxResolution", UNSET))

        def _parse_min_defocus(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        min_defocus = _parse_min_defocus(d.pop("minDefocus", UNSET))

        def _parse_max_defocus(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        max_defocus = _parse_max_defocus(d.pop("maxDefocus", UNSET))

        def _parse_defocus_step_size(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        defocus_step_size = _parse_defocus_step_size(d.pop("defocusStepSize", UNSET))

        def _parse_astigmatism(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        astigmatism = _parse_astigmatism(d.pop("astigmatism", UNSET))

        def _parse_astigmatism_angle(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        astigmatism_angle = _parse_astigmatism_angle(d.pop("astigmatismAngle", UNSET))

        def _parse_estimated_resolution(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        estimated_resolution = _parse_estimated_resolution(d.pop("estimatedResolution", UNSET))

        def _parse_estimated_defocus(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        estimated_defocus = _parse_estimated_defocus(d.pop("estimatedDefocus", UNSET))

        def _parse_amplitude_contrast(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        amplitude_contrast = _parse_amplitude_contrast(d.pop("amplitudeContrast", UNSET))

        def _parse_cc_value(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        cc_value = _parse_cc_value(d.pop("ccValue", UNSET))

        def _parse_fft_theoretical_full_path(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        fft_theoretical_full_path = _parse_fft_theoretical_full_path(d.pop("fftTheoreticalFullPath", UNSET))

        def _parse_comments(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        comments = _parse_comments(d.pop("comments", UNSET))

        def _parse_ice_ring_density(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        ice_ring_density = _parse_ice_ring_density(d.pop("iceRingDensity", UNSET))

        ctf_base = cls(
            auto_proc_program_id=auto_proc_program_id,
            box_size_x=box_size_x,
            box_size_y=box_size_y,
            min_resolution=min_resolution,
            max_resolution=max_resolution,
            min_defocus=min_defocus,
            max_defocus=max_defocus,
            defocus_step_size=defocus_step_size,
            astigmatism=astigmatism,
            astigmatism_angle=astigmatism_angle,
            estimated_resolution=estimated_resolution,
            estimated_defocus=estimated_defocus,
            amplitude_contrast=amplitude_contrast,
            cc_value=cc_value,
            fft_theoretical_full_path=fft_theoretical_full_path,
            comments=comments,
            ice_ring_density=ice_ring_density,
        )

        return ctf_base

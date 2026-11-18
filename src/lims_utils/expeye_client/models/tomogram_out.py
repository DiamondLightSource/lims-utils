from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define

from ..types import UNSET, Unset

T = TypeVar("T", bound="TomogramOut")


@_attrs_define
class TomogramOut:
    """
    Attributes:
        data_collection_id (int):
        tomogram_id (int):
        grid_square_id (int | None | Unset):
        volume_file (None | str | Unset):
        stack_file (None | str | Unset):
        file_directory (None | str | Unset):
        central_slice_image (None | str | Unset):
        size_x (int | None | Unset):
        size_y (int | None | Unset):
        size_z (int | None | Unset):
        pixel_location_x (int | None | Unset):
        pixel_location_y (int | None | Unset):
        pixel_spacing (float | None | Unset):
        residual_error_mean (float | None | Unset):
        residual_error_sd (float | None | Unset):
        x_axis_correction (float | None | Unset):
        tilt_angle_offset (float | None | Unset):
        z_shift (float | None | Unset):
        refined_tilt_axis (float | None | Unset):
        global_alignment_quality (float | None | Unset):
        title (None | str | Unset):
    """

    data_collection_id: int
    tomogram_id: int
    grid_square_id: int | None | Unset = UNSET
    volume_file: None | str | Unset = UNSET
    stack_file: None | str | Unset = UNSET
    file_directory: None | str | Unset = UNSET
    central_slice_image: None | str | Unset = UNSET
    size_x: int | None | Unset = UNSET
    size_y: int | None | Unset = UNSET
    size_z: int | None | Unset = UNSET
    pixel_location_x: int | None | Unset = UNSET
    pixel_location_y: int | None | Unset = UNSET
    pixel_spacing: float | None | Unset = UNSET
    residual_error_mean: float | None | Unset = UNSET
    residual_error_sd: float | None | Unset = UNSET
    x_axis_correction: float | None | Unset = UNSET
    tilt_angle_offset: float | None | Unset = UNSET
    z_shift: float | None | Unset = UNSET
    refined_tilt_axis: float | None | Unset = UNSET
    global_alignment_quality: float | None | Unset = UNSET
    title: None | str | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        data_collection_id = self.data_collection_id

        tomogram_id = self.tomogram_id

        grid_square_id: int | None | Unset
        if isinstance(self.grid_square_id, Unset):
            grid_square_id = UNSET
        else:
            grid_square_id = self.grid_square_id

        volume_file: None | str | Unset
        if isinstance(self.volume_file, Unset):
            volume_file = UNSET
        else:
            volume_file = self.volume_file

        stack_file: None | str | Unset
        if isinstance(self.stack_file, Unset):
            stack_file = UNSET
        else:
            stack_file = self.stack_file

        file_directory: None | str | Unset
        if isinstance(self.file_directory, Unset):
            file_directory = UNSET
        else:
            file_directory = self.file_directory

        central_slice_image: None | str | Unset
        if isinstance(self.central_slice_image, Unset):
            central_slice_image = UNSET
        else:
            central_slice_image = self.central_slice_image

        size_x: int | None | Unset
        if isinstance(self.size_x, Unset):
            size_x = UNSET
        else:
            size_x = self.size_x

        size_y: int | None | Unset
        if isinstance(self.size_y, Unset):
            size_y = UNSET
        else:
            size_y = self.size_y

        size_z: int | None | Unset
        if isinstance(self.size_z, Unset):
            size_z = UNSET
        else:
            size_z = self.size_z

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

        pixel_spacing: float | None | Unset
        if isinstance(self.pixel_spacing, Unset):
            pixel_spacing = UNSET
        else:
            pixel_spacing = self.pixel_spacing

        residual_error_mean: float | None | Unset
        if isinstance(self.residual_error_mean, Unset):
            residual_error_mean = UNSET
        else:
            residual_error_mean = self.residual_error_mean

        residual_error_sd: float | None | Unset
        if isinstance(self.residual_error_sd, Unset):
            residual_error_sd = UNSET
        else:
            residual_error_sd = self.residual_error_sd

        x_axis_correction: float | None | Unset
        if isinstance(self.x_axis_correction, Unset):
            x_axis_correction = UNSET
        else:
            x_axis_correction = self.x_axis_correction

        tilt_angle_offset: float | None | Unset
        if isinstance(self.tilt_angle_offset, Unset):
            tilt_angle_offset = UNSET
        else:
            tilt_angle_offset = self.tilt_angle_offset

        z_shift: float | None | Unset
        if isinstance(self.z_shift, Unset):
            z_shift = UNSET
        else:
            z_shift = self.z_shift

        refined_tilt_axis: float | None | Unset
        if isinstance(self.refined_tilt_axis, Unset):
            refined_tilt_axis = UNSET
        else:
            refined_tilt_axis = self.refined_tilt_axis

        global_alignment_quality: float | None | Unset
        if isinstance(self.global_alignment_quality, Unset):
            global_alignment_quality = UNSET
        else:
            global_alignment_quality = self.global_alignment_quality

        title: None | str | Unset
        if isinstance(self.title, Unset):
            title = UNSET
        else:
            title = self.title

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "dataCollectionId": data_collection_id,
                "tomogramId": tomogram_id,
            }
        )
        if grid_square_id is not UNSET:
            field_dict["gridSquareId"] = grid_square_id
        if volume_file is not UNSET:
            field_dict["volumeFile"] = volume_file
        if stack_file is not UNSET:
            field_dict["stackFile"] = stack_file
        if file_directory is not UNSET:
            field_dict["fileDirectory"] = file_directory
        if central_slice_image is not UNSET:
            field_dict["centralSliceImage"] = central_slice_image
        if size_x is not UNSET:
            field_dict["sizeX"] = size_x
        if size_y is not UNSET:
            field_dict["sizeY"] = size_y
        if size_z is not UNSET:
            field_dict["sizeZ"] = size_z
        if pixel_location_x is not UNSET:
            field_dict["pixelLocationX"] = pixel_location_x
        if pixel_location_y is not UNSET:
            field_dict["pixelLocationY"] = pixel_location_y
        if pixel_spacing is not UNSET:
            field_dict["pixelSpacing"] = pixel_spacing
        if residual_error_mean is not UNSET:
            field_dict["residualErrorMean"] = residual_error_mean
        if residual_error_sd is not UNSET:
            field_dict["residualErrorSD"] = residual_error_sd
        if x_axis_correction is not UNSET:
            field_dict["xAxisCorrection"] = x_axis_correction
        if tilt_angle_offset is not UNSET:
            field_dict["tiltAngleOffset"] = tilt_angle_offset
        if z_shift is not UNSET:
            field_dict["zShift"] = z_shift
        if refined_tilt_axis is not UNSET:
            field_dict["refinedTiltAxis"] = refined_tilt_axis
        if global_alignment_quality is not UNSET:
            field_dict["globalAlignmentQuality"] = global_alignment_quality
        if title is not UNSET:
            field_dict["title"] = title

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        data_collection_id = d.pop("dataCollectionId")

        tomogram_id = d.pop("tomogramId")

        def _parse_grid_square_id(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        grid_square_id = _parse_grid_square_id(d.pop("gridSquareId", UNSET))

        def _parse_volume_file(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        volume_file = _parse_volume_file(d.pop("volumeFile", UNSET))

        def _parse_stack_file(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        stack_file = _parse_stack_file(d.pop("stackFile", UNSET))

        def _parse_file_directory(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        file_directory = _parse_file_directory(d.pop("fileDirectory", UNSET))

        def _parse_central_slice_image(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        central_slice_image = _parse_central_slice_image(d.pop("centralSliceImage", UNSET))

        def _parse_size_x(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        size_x = _parse_size_x(d.pop("sizeX", UNSET))

        def _parse_size_y(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        size_y = _parse_size_y(d.pop("sizeY", UNSET))

        def _parse_size_z(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        size_z = _parse_size_z(d.pop("sizeZ", UNSET))

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

        def _parse_pixel_spacing(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        pixel_spacing = _parse_pixel_spacing(d.pop("pixelSpacing", UNSET))

        def _parse_residual_error_mean(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        residual_error_mean = _parse_residual_error_mean(d.pop("residualErrorMean", UNSET))

        def _parse_residual_error_sd(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        residual_error_sd = _parse_residual_error_sd(d.pop("residualErrorSD", UNSET))

        def _parse_x_axis_correction(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        x_axis_correction = _parse_x_axis_correction(d.pop("xAxisCorrection", UNSET))

        def _parse_tilt_angle_offset(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        tilt_angle_offset = _parse_tilt_angle_offset(d.pop("tiltAngleOffset", UNSET))

        def _parse_z_shift(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        z_shift = _parse_z_shift(d.pop("zShift", UNSET))

        def _parse_refined_tilt_axis(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        refined_tilt_axis = _parse_refined_tilt_axis(d.pop("refinedTiltAxis", UNSET))

        def _parse_global_alignment_quality(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        global_alignment_quality = _parse_global_alignment_quality(d.pop("globalAlignmentQuality", UNSET))

        def _parse_title(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        title = _parse_title(d.pop("title", UNSET))

        tomogram_out = cls(
            data_collection_id=data_collection_id,
            tomogram_id=tomogram_id,
            grid_square_id=grid_square_id,
            volume_file=volume_file,
            stack_file=stack_file,
            file_directory=file_directory,
            central_slice_image=central_slice_image,
            size_x=size_x,
            size_y=size_y,
            size_z=size_z,
            pixel_location_x=pixel_location_x,
            pixel_location_y=pixel_location_y,
            pixel_spacing=pixel_spacing,
            residual_error_mean=residual_error_mean,
            residual_error_sd=residual_error_sd,
            x_axis_correction=x_axis_correction,
            tilt_angle_offset=tilt_angle_offset,
            z_shift=z_shift,
            refined_tilt_axis=refined_tilt_axis,
            global_alignment_quality=global_alignment_quality,
            title=title,
        )

        return tomogram_out

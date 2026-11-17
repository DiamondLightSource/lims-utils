from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define

from ..types import UNSET, Unset

T = TypeVar("T", bound="MotionCorrectionOut")


@_attrs_define
class MotionCorrectionOut:
    """
    Attributes:
        motion_correction_id (int):
        auto_proc_program_id (int | None | Unset):
        image_number (int | None | Unset):
        first_frame (int | None | Unset):
        last_frame (int | None | Unset):
        dose_per_frame (float | None | Unset):
        dose_weight (float | None | Unset):
        total_motion (float | None | Unset):
        average_motion_per_frame (float | None | Unset):
        drift_plot_full_path (None | str | Unset):
        micrograph_full_path (None | str | Unset):
        micrograph_snapshot_full_path (None | str | Unset):
        patches_used_x (int | None | Unset):
        patches_used_y (int | None | Unset):
        fft_full_path (None | str | Unset):
        fft_corrected_full_path (None | str | Unset):
        comments (None | str | Unset):
        movie_id (int | None | Unset):
        data_collection_id (int | None | Unset):
    """

    motion_correction_id: int
    auto_proc_program_id: int | None | Unset = UNSET
    image_number: int | None | Unset = UNSET
    first_frame: int | None | Unset = UNSET
    last_frame: int | None | Unset = UNSET
    dose_per_frame: float | None | Unset = UNSET
    dose_weight: float | None | Unset = UNSET
    total_motion: float | None | Unset = UNSET
    average_motion_per_frame: float | None | Unset = UNSET
    drift_plot_full_path: None | str | Unset = UNSET
    micrograph_full_path: None | str | Unset = UNSET
    micrograph_snapshot_full_path: None | str | Unset = UNSET
    patches_used_x: int | None | Unset = UNSET
    patches_used_y: int | None | Unset = UNSET
    fft_full_path: None | str | Unset = UNSET
    fft_corrected_full_path: None | str | Unset = UNSET
    comments: None | str | Unset = UNSET
    movie_id: int | None | Unset = UNSET
    data_collection_id: int | None | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        motion_correction_id = self.motion_correction_id

        auto_proc_program_id: int | None | Unset
        if isinstance(self.auto_proc_program_id, Unset):
            auto_proc_program_id = UNSET
        else:
            auto_proc_program_id = self.auto_proc_program_id

        image_number: int | None | Unset
        if isinstance(self.image_number, Unset):
            image_number = UNSET
        else:
            image_number = self.image_number

        first_frame: int | None | Unset
        if isinstance(self.first_frame, Unset):
            first_frame = UNSET
        else:
            first_frame = self.first_frame

        last_frame: int | None | Unset
        if isinstance(self.last_frame, Unset):
            last_frame = UNSET
        else:
            last_frame = self.last_frame

        dose_per_frame: float | None | Unset
        if isinstance(self.dose_per_frame, Unset):
            dose_per_frame = UNSET
        else:
            dose_per_frame = self.dose_per_frame

        dose_weight: float | None | Unset
        if isinstance(self.dose_weight, Unset):
            dose_weight = UNSET
        else:
            dose_weight = self.dose_weight

        total_motion: float | None | Unset
        if isinstance(self.total_motion, Unset):
            total_motion = UNSET
        else:
            total_motion = self.total_motion

        average_motion_per_frame: float | None | Unset
        if isinstance(self.average_motion_per_frame, Unset):
            average_motion_per_frame = UNSET
        else:
            average_motion_per_frame = self.average_motion_per_frame

        drift_plot_full_path: None | str | Unset
        if isinstance(self.drift_plot_full_path, Unset):
            drift_plot_full_path = UNSET
        else:
            drift_plot_full_path = self.drift_plot_full_path

        micrograph_full_path: None | str | Unset
        if isinstance(self.micrograph_full_path, Unset):
            micrograph_full_path = UNSET
        else:
            micrograph_full_path = self.micrograph_full_path

        micrograph_snapshot_full_path: None | str | Unset
        if isinstance(self.micrograph_snapshot_full_path, Unset):
            micrograph_snapshot_full_path = UNSET
        else:
            micrograph_snapshot_full_path = self.micrograph_snapshot_full_path

        patches_used_x: int | None | Unset
        if isinstance(self.patches_used_x, Unset):
            patches_used_x = UNSET
        else:
            patches_used_x = self.patches_used_x

        patches_used_y: int | None | Unset
        if isinstance(self.patches_used_y, Unset):
            patches_used_y = UNSET
        else:
            patches_used_y = self.patches_used_y

        fft_full_path: None | str | Unset
        if isinstance(self.fft_full_path, Unset):
            fft_full_path = UNSET
        else:
            fft_full_path = self.fft_full_path

        fft_corrected_full_path: None | str | Unset
        if isinstance(self.fft_corrected_full_path, Unset):
            fft_corrected_full_path = UNSET
        else:
            fft_corrected_full_path = self.fft_corrected_full_path

        comments: None | str | Unset
        if isinstance(self.comments, Unset):
            comments = UNSET
        else:
            comments = self.comments

        movie_id: int | None | Unset
        if isinstance(self.movie_id, Unset):
            movie_id = UNSET
        else:
            movie_id = self.movie_id

        data_collection_id: int | None | Unset
        if isinstance(self.data_collection_id, Unset):
            data_collection_id = UNSET
        else:
            data_collection_id = self.data_collection_id

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "motionCorrectionId": motion_correction_id,
            }
        )
        if auto_proc_program_id is not UNSET:
            field_dict["autoProcProgramId"] = auto_proc_program_id
        if image_number is not UNSET:
            field_dict["imageNumber"] = image_number
        if first_frame is not UNSET:
            field_dict["firstFrame"] = first_frame
        if last_frame is not UNSET:
            field_dict["lastFrame"] = last_frame
        if dose_per_frame is not UNSET:
            field_dict["dosePerFrame"] = dose_per_frame
        if dose_weight is not UNSET:
            field_dict["doseWeight"] = dose_weight
        if total_motion is not UNSET:
            field_dict["totalMotion"] = total_motion
        if average_motion_per_frame is not UNSET:
            field_dict["averageMotionPerFrame"] = average_motion_per_frame
        if drift_plot_full_path is not UNSET:
            field_dict["driftPlotFullPath"] = drift_plot_full_path
        if micrograph_full_path is not UNSET:
            field_dict["micrographFullPath"] = micrograph_full_path
        if micrograph_snapshot_full_path is not UNSET:
            field_dict["micrographSnapshotFullPath"] = micrograph_snapshot_full_path
        if patches_used_x is not UNSET:
            field_dict["patchesUsedX"] = patches_used_x
        if patches_used_y is not UNSET:
            field_dict["patchesUsedY"] = patches_used_y
        if fft_full_path is not UNSET:
            field_dict["fftFullPath"] = fft_full_path
        if fft_corrected_full_path is not UNSET:
            field_dict["fftCorrectedFullPath"] = fft_corrected_full_path
        if comments is not UNSET:
            field_dict["comments"] = comments
        if movie_id is not UNSET:
            field_dict["movieId"] = movie_id
        if data_collection_id is not UNSET:
            field_dict["dataCollectionId"] = data_collection_id

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        motion_correction_id = d.pop("motionCorrectionId")

        def _parse_auto_proc_program_id(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        auto_proc_program_id = _parse_auto_proc_program_id(d.pop("autoProcProgramId", UNSET))

        def _parse_image_number(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        image_number = _parse_image_number(d.pop("imageNumber", UNSET))

        def _parse_first_frame(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        first_frame = _parse_first_frame(d.pop("firstFrame", UNSET))

        def _parse_last_frame(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        last_frame = _parse_last_frame(d.pop("lastFrame", UNSET))

        def _parse_dose_per_frame(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        dose_per_frame = _parse_dose_per_frame(d.pop("dosePerFrame", UNSET))

        def _parse_dose_weight(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        dose_weight = _parse_dose_weight(d.pop("doseWeight", UNSET))

        def _parse_total_motion(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        total_motion = _parse_total_motion(d.pop("totalMotion", UNSET))

        def _parse_average_motion_per_frame(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        average_motion_per_frame = _parse_average_motion_per_frame(d.pop("averageMotionPerFrame", UNSET))

        def _parse_drift_plot_full_path(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        drift_plot_full_path = _parse_drift_plot_full_path(d.pop("driftPlotFullPath", UNSET))

        def _parse_micrograph_full_path(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        micrograph_full_path = _parse_micrograph_full_path(d.pop("micrographFullPath", UNSET))

        def _parse_micrograph_snapshot_full_path(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        micrograph_snapshot_full_path = _parse_micrograph_snapshot_full_path(d.pop("micrographSnapshotFullPath", UNSET))

        def _parse_patches_used_x(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        patches_used_x = _parse_patches_used_x(d.pop("patchesUsedX", UNSET))

        def _parse_patches_used_y(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        patches_used_y = _parse_patches_used_y(d.pop("patchesUsedY", UNSET))

        def _parse_fft_full_path(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        fft_full_path = _parse_fft_full_path(d.pop("fftFullPath", UNSET))

        def _parse_fft_corrected_full_path(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        fft_corrected_full_path = _parse_fft_corrected_full_path(d.pop("fftCorrectedFullPath", UNSET))

        def _parse_comments(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        comments = _parse_comments(d.pop("comments", UNSET))

        def _parse_movie_id(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        movie_id = _parse_movie_id(d.pop("movieId", UNSET))

        def _parse_data_collection_id(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        data_collection_id = _parse_data_collection_id(d.pop("dataCollectionId", UNSET))

        motion_correction_out = cls(
            motion_correction_id=motion_correction_id,
            auto_proc_program_id=auto_proc_program_id,
            image_number=image_number,
            first_frame=first_frame,
            last_frame=last_frame,
            dose_per_frame=dose_per_frame,
            dose_weight=dose_weight,
            total_motion=total_motion,
            average_motion_per_frame=average_motion_per_frame,
            drift_plot_full_path=drift_plot_full_path,
            micrograph_full_path=micrograph_full_path,
            micrograph_snapshot_full_path=micrograph_snapshot_full_path,
            patches_used_x=patches_used_x,
            patches_used_y=patches_used_y,
            fft_full_path=fft_full_path,
            fft_corrected_full_path=fft_corrected_full_path,
            comments=comments,
            movie_id=movie_id,
            data_collection_id=data_collection_id,
        )

        return motion_correction_out

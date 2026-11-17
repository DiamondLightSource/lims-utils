from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define

from ..models.milling_step_out_beam_type_type_0 import MillingStepOutBeamTypeType0
from ..models.milling_step_out_status_type_0 import MillingStepOutStatusType0
from ..types import UNSET, Unset

T = TypeVar("T", bound="MillingStepOut")


@_attrs_define
class MillingStepOut:
    """
    Attributes:
        milling_step_id (int):
        milling_step_name_id (int | None | Unset):
        is_enabled (int | None | Unset):
        status (MillingStepOutStatusType0 | None | Unset):
        execution_time (float | None | Unset):
        stage_x (float | None | Unset):
        stage_y (float | None | Unset):
        stage_z (float | None | Unset):
        rotation (float | None | Unset):
        alpha_tilt (float | None | Unset):
        beam_type (MillingStepOutBeamTypeType0 | None | Unset):
        beam_voltage (float | None | Unset):
        beam_current (float | None | Unset):
        milling_angle (float | None | Unset):
        depth_correction (float | None | Unset):
        lamella_offset (float | None | Unset):
        trench_height_front (float | None | Unset):
        trench_height_rear (float | None | Unset):
        width_overlap_front_left (float | None | Unset):
        width_overlap_front_right (float | None | Unset):
        width_overlap_rear_left (float | None | Unset):
        width_overlap_rear_right (float | None | Unset):
        step (None | str | Unset):
        recipe (None | str | Unset):
        grid_square_id (int | None | Unset):
    """

    milling_step_id: int
    milling_step_name_id: int | None | Unset = UNSET
    is_enabled: int | None | Unset = UNSET
    status: MillingStepOutStatusType0 | None | Unset = UNSET
    execution_time: float | None | Unset = UNSET
    stage_x: float | None | Unset = UNSET
    stage_y: float | None | Unset = UNSET
    stage_z: float | None | Unset = UNSET
    rotation: float | None | Unset = UNSET
    alpha_tilt: float | None | Unset = UNSET
    beam_type: MillingStepOutBeamTypeType0 | None | Unset = UNSET
    beam_voltage: float | None | Unset = UNSET
    beam_current: float | None | Unset = UNSET
    milling_angle: float | None | Unset = UNSET
    depth_correction: float | None | Unset = UNSET
    lamella_offset: float | None | Unset = UNSET
    trench_height_front: float | None | Unset = UNSET
    trench_height_rear: float | None | Unset = UNSET
    width_overlap_front_left: float | None | Unset = UNSET
    width_overlap_front_right: float | None | Unset = UNSET
    width_overlap_rear_left: float | None | Unset = UNSET
    width_overlap_rear_right: float | None | Unset = UNSET
    step: None | str | Unset = UNSET
    recipe: None | str | Unset = UNSET
    grid_square_id: int | None | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        milling_step_id = self.milling_step_id

        milling_step_name_id: int | None | Unset
        if isinstance(self.milling_step_name_id, Unset):
            milling_step_name_id = UNSET
        else:
            milling_step_name_id = self.milling_step_name_id

        is_enabled: int | None | Unset
        if isinstance(self.is_enabled, Unset):
            is_enabled = UNSET
        else:
            is_enabled = self.is_enabled

        status: None | str | Unset
        if isinstance(self.status, Unset):
            status = UNSET
        elif isinstance(self.status, MillingStepOutStatusType0):
            status = self.status.value
        else:
            status = self.status

        execution_time: float | None | Unset
        if isinstance(self.execution_time, Unset):
            execution_time = UNSET
        else:
            execution_time = self.execution_time

        stage_x: float | None | Unset
        if isinstance(self.stage_x, Unset):
            stage_x = UNSET
        else:
            stage_x = self.stage_x

        stage_y: float | None | Unset
        if isinstance(self.stage_y, Unset):
            stage_y = UNSET
        else:
            stage_y = self.stage_y

        stage_z: float | None | Unset
        if isinstance(self.stage_z, Unset):
            stage_z = UNSET
        else:
            stage_z = self.stage_z

        rotation: float | None | Unset
        if isinstance(self.rotation, Unset):
            rotation = UNSET
        else:
            rotation = self.rotation

        alpha_tilt: float | None | Unset
        if isinstance(self.alpha_tilt, Unset):
            alpha_tilt = UNSET
        else:
            alpha_tilt = self.alpha_tilt

        beam_type: None | str | Unset
        if isinstance(self.beam_type, Unset):
            beam_type = UNSET
        elif isinstance(self.beam_type, MillingStepOutBeamTypeType0):
            beam_type = self.beam_type.value
        else:
            beam_type = self.beam_type

        beam_voltage: float | None | Unset
        if isinstance(self.beam_voltage, Unset):
            beam_voltage = UNSET
        else:
            beam_voltage = self.beam_voltage

        beam_current: float | None | Unset
        if isinstance(self.beam_current, Unset):
            beam_current = UNSET
        else:
            beam_current = self.beam_current

        milling_angle: float | None | Unset
        if isinstance(self.milling_angle, Unset):
            milling_angle = UNSET
        else:
            milling_angle = self.milling_angle

        depth_correction: float | None | Unset
        if isinstance(self.depth_correction, Unset):
            depth_correction = UNSET
        else:
            depth_correction = self.depth_correction

        lamella_offset: float | None | Unset
        if isinstance(self.lamella_offset, Unset):
            lamella_offset = UNSET
        else:
            lamella_offset = self.lamella_offset

        trench_height_front: float | None | Unset
        if isinstance(self.trench_height_front, Unset):
            trench_height_front = UNSET
        else:
            trench_height_front = self.trench_height_front

        trench_height_rear: float | None | Unset
        if isinstance(self.trench_height_rear, Unset):
            trench_height_rear = UNSET
        else:
            trench_height_rear = self.trench_height_rear

        width_overlap_front_left: float | None | Unset
        if isinstance(self.width_overlap_front_left, Unset):
            width_overlap_front_left = UNSET
        else:
            width_overlap_front_left = self.width_overlap_front_left

        width_overlap_front_right: float | None | Unset
        if isinstance(self.width_overlap_front_right, Unset):
            width_overlap_front_right = UNSET
        else:
            width_overlap_front_right = self.width_overlap_front_right

        width_overlap_rear_left: float | None | Unset
        if isinstance(self.width_overlap_rear_left, Unset):
            width_overlap_rear_left = UNSET
        else:
            width_overlap_rear_left = self.width_overlap_rear_left

        width_overlap_rear_right: float | None | Unset
        if isinstance(self.width_overlap_rear_right, Unset):
            width_overlap_rear_right = UNSET
        else:
            width_overlap_rear_right = self.width_overlap_rear_right

        step: None | str | Unset
        if isinstance(self.step, Unset):
            step = UNSET
        else:
            step = self.step

        recipe: None | str | Unset
        if isinstance(self.recipe, Unset):
            recipe = UNSET
        else:
            recipe = self.recipe

        grid_square_id: int | None | Unset
        if isinstance(self.grid_square_id, Unset):
            grid_square_id = UNSET
        else:
            grid_square_id = self.grid_square_id

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "millingStepId": milling_step_id,
            }
        )
        if milling_step_name_id is not UNSET:
            field_dict["millingStepNameId"] = milling_step_name_id
        if is_enabled is not UNSET:
            field_dict["isEnabled"] = is_enabled
        if status is not UNSET:
            field_dict["status"] = status
        if execution_time is not UNSET:
            field_dict["executionTime"] = execution_time
        if stage_x is not UNSET:
            field_dict["stageX"] = stage_x
        if stage_y is not UNSET:
            field_dict["stageY"] = stage_y
        if stage_z is not UNSET:
            field_dict["stageZ"] = stage_z
        if rotation is not UNSET:
            field_dict["rotation"] = rotation
        if alpha_tilt is not UNSET:
            field_dict["alphaTilt"] = alpha_tilt
        if beam_type is not UNSET:
            field_dict["beamType"] = beam_type
        if beam_voltage is not UNSET:
            field_dict["beamVoltage"] = beam_voltage
        if beam_current is not UNSET:
            field_dict["beamCurrent"] = beam_current
        if milling_angle is not UNSET:
            field_dict["millingAngle"] = milling_angle
        if depth_correction is not UNSET:
            field_dict["depthCorrection"] = depth_correction
        if lamella_offset is not UNSET:
            field_dict["lamellaOffset"] = lamella_offset
        if trench_height_front is not UNSET:
            field_dict["trenchHeightFront"] = trench_height_front
        if trench_height_rear is not UNSET:
            field_dict["trenchHeightRear"] = trench_height_rear
        if width_overlap_front_left is not UNSET:
            field_dict["widthOverlapFrontLeft"] = width_overlap_front_left
        if width_overlap_front_right is not UNSET:
            field_dict["widthOverlapFrontRight"] = width_overlap_front_right
        if width_overlap_rear_left is not UNSET:
            field_dict["widthOverlapRearLeft"] = width_overlap_rear_left
        if width_overlap_rear_right is not UNSET:
            field_dict["widthOverlapRearRight"] = width_overlap_rear_right
        if step is not UNSET:
            field_dict["step"] = step
        if recipe is not UNSET:
            field_dict["recipe"] = recipe
        if grid_square_id is not UNSET:
            field_dict["gridSquareId"] = grid_square_id

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        milling_step_id = d.pop("millingStepId")

        def _parse_milling_step_name_id(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        milling_step_name_id = _parse_milling_step_name_id(d.pop("millingStepNameId", UNSET))

        def _parse_is_enabled(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        is_enabled = _parse_is_enabled(d.pop("isEnabled", UNSET))

        def _parse_status(data: object) -> MillingStepOutStatusType0 | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                status_type_0 = MillingStepOutStatusType0(data)

                return status_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(MillingStepOutStatusType0 | None | Unset, data)

        status = _parse_status(d.pop("status", UNSET))

        def _parse_execution_time(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        execution_time = _parse_execution_time(d.pop("executionTime", UNSET))

        def _parse_stage_x(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        stage_x = _parse_stage_x(d.pop("stageX", UNSET))

        def _parse_stage_y(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        stage_y = _parse_stage_y(d.pop("stageY", UNSET))

        def _parse_stage_z(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        stage_z = _parse_stage_z(d.pop("stageZ", UNSET))

        def _parse_rotation(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        rotation = _parse_rotation(d.pop("rotation", UNSET))

        def _parse_alpha_tilt(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        alpha_tilt = _parse_alpha_tilt(d.pop("alphaTilt", UNSET))

        def _parse_beam_type(data: object) -> MillingStepOutBeamTypeType0 | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                beam_type_type_0 = MillingStepOutBeamTypeType0(data)

                return beam_type_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(MillingStepOutBeamTypeType0 | None | Unset, data)

        beam_type = _parse_beam_type(d.pop("beamType", UNSET))

        def _parse_beam_voltage(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        beam_voltage = _parse_beam_voltage(d.pop("beamVoltage", UNSET))

        def _parse_beam_current(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        beam_current = _parse_beam_current(d.pop("beamCurrent", UNSET))

        def _parse_milling_angle(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        milling_angle = _parse_milling_angle(d.pop("millingAngle", UNSET))

        def _parse_depth_correction(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        depth_correction = _parse_depth_correction(d.pop("depthCorrection", UNSET))

        def _parse_lamella_offset(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        lamella_offset = _parse_lamella_offset(d.pop("lamellaOffset", UNSET))

        def _parse_trench_height_front(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        trench_height_front = _parse_trench_height_front(d.pop("trenchHeightFront", UNSET))

        def _parse_trench_height_rear(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        trench_height_rear = _parse_trench_height_rear(d.pop("trenchHeightRear", UNSET))

        def _parse_width_overlap_front_left(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        width_overlap_front_left = _parse_width_overlap_front_left(d.pop("widthOverlapFrontLeft", UNSET))

        def _parse_width_overlap_front_right(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        width_overlap_front_right = _parse_width_overlap_front_right(d.pop("widthOverlapFrontRight", UNSET))

        def _parse_width_overlap_rear_left(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        width_overlap_rear_left = _parse_width_overlap_rear_left(d.pop("widthOverlapRearLeft", UNSET))

        def _parse_width_overlap_rear_right(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        width_overlap_rear_right = _parse_width_overlap_rear_right(d.pop("widthOverlapRearRight", UNSET))

        def _parse_step(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        step = _parse_step(d.pop("step", UNSET))

        def _parse_recipe(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        recipe = _parse_recipe(d.pop("recipe", UNSET))

        def _parse_grid_square_id(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        grid_square_id = _parse_grid_square_id(d.pop("gridSquareId", UNSET))

        milling_step_out = cls(
            milling_step_id=milling_step_id,
            milling_step_name_id=milling_step_name_id,
            is_enabled=is_enabled,
            status=status,
            execution_time=execution_time,
            stage_x=stage_x,
            stage_y=stage_y,
            stage_z=stage_z,
            rotation=rotation,
            alpha_tilt=alpha_tilt,
            beam_type=beam_type,
            beam_voltage=beam_voltage,
            beam_current=beam_current,
            milling_angle=milling_angle,
            depth_correction=depth_correction,
            lamella_offset=lamella_offset,
            trench_height_front=trench_height_front,
            trench_height_rear=trench_height_rear,
            width_overlap_front_left=width_overlap_front_left,
            width_overlap_front_right=width_overlap_front_right,
            width_overlap_rear_left=width_overlap_rear_left,
            width_overlap_rear_right=width_overlap_rear_right,
            step=step,
            recipe=recipe,
            grid_square_id=grid_square_id,
        )

        return milling_step_out

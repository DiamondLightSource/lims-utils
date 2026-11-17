from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.grid_info_out_orientation_type_0 import GridInfoOutOrientationType0
from ..types import UNSET, Unset

T = TypeVar("T", bound="GridInfoOut")


@_attrs_define
class GridInfoOut:
    """
    Attributes:
        grid_info_id (int):
        x_offset (float | None | Unset):
        y_offset (float | None | Unset):
        snapshot_offset_x_pixel (float | None | Unset):
        snapshot_offset_y_pixel (float | None | Unset):
        dx (float | None | Unset):
        dy (float | None | Unset):
        steps_x (float | None | Unset):
        steps_y (float | None | Unset):
        mesh_angle (float | None | Unset):
        record_time_stamp (datetime.datetime | None | Unset):
        workflow_mesh_id (int | None | Unset):
        orientation (GridInfoOutOrientationType0 | None | Unset):
        data_collection_group_id (int | None | Unset):
        microns_per_pixel_x (float | None | Unset):
        microns_per_pixel_y (float | None | Unset):
        snaked (bool | None | Unset):
        patches_x (int | None | Unset):
        patches_y (int | None | Unset):
    """

    grid_info_id: int
    x_offset: float | None | Unset = UNSET
    y_offset: float | None | Unset = UNSET
    snapshot_offset_x_pixel: float | None | Unset = UNSET
    snapshot_offset_y_pixel: float | None | Unset = UNSET
    dx: float | None | Unset = UNSET
    dy: float | None | Unset = UNSET
    steps_x: float | None | Unset = UNSET
    steps_y: float | None | Unset = UNSET
    mesh_angle: float | None | Unset = UNSET
    record_time_stamp: datetime.datetime | None | Unset = UNSET
    workflow_mesh_id: int | None | Unset = UNSET
    orientation: GridInfoOutOrientationType0 | None | Unset = UNSET
    data_collection_group_id: int | None | Unset = UNSET
    microns_per_pixel_x: float | None | Unset = UNSET
    microns_per_pixel_y: float | None | Unset = UNSET
    snaked: bool | None | Unset = UNSET
    patches_x: int | None | Unset = UNSET
    patches_y: int | None | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        grid_info_id = self.grid_info_id

        x_offset: float | None | Unset
        if isinstance(self.x_offset, Unset):
            x_offset = UNSET
        else:
            x_offset = self.x_offset

        y_offset: float | None | Unset
        if isinstance(self.y_offset, Unset):
            y_offset = UNSET
        else:
            y_offset = self.y_offset

        snapshot_offset_x_pixel: float | None | Unset
        if isinstance(self.snapshot_offset_x_pixel, Unset):
            snapshot_offset_x_pixel = UNSET
        else:
            snapshot_offset_x_pixel = self.snapshot_offset_x_pixel

        snapshot_offset_y_pixel: float | None | Unset
        if isinstance(self.snapshot_offset_y_pixel, Unset):
            snapshot_offset_y_pixel = UNSET
        else:
            snapshot_offset_y_pixel = self.snapshot_offset_y_pixel

        dx: float | None | Unset
        if isinstance(self.dx, Unset):
            dx = UNSET
        else:
            dx = self.dx

        dy: float | None | Unset
        if isinstance(self.dy, Unset):
            dy = UNSET
        else:
            dy = self.dy

        steps_x: float | None | Unset
        if isinstance(self.steps_x, Unset):
            steps_x = UNSET
        else:
            steps_x = self.steps_x

        steps_y: float | None | Unset
        if isinstance(self.steps_y, Unset):
            steps_y = UNSET
        else:
            steps_y = self.steps_y

        mesh_angle: float | None | Unset
        if isinstance(self.mesh_angle, Unset):
            mesh_angle = UNSET
        else:
            mesh_angle = self.mesh_angle

        record_time_stamp: None | str | Unset
        if isinstance(self.record_time_stamp, Unset):
            record_time_stamp = UNSET
        elif isinstance(self.record_time_stamp, datetime.datetime):
            record_time_stamp = self.record_time_stamp.isoformat()
        else:
            record_time_stamp = self.record_time_stamp

        workflow_mesh_id: int | None | Unset
        if isinstance(self.workflow_mesh_id, Unset):
            workflow_mesh_id = UNSET
        else:
            workflow_mesh_id = self.workflow_mesh_id

        orientation: None | str | Unset
        if isinstance(self.orientation, Unset):
            orientation = UNSET
        elif isinstance(self.orientation, GridInfoOutOrientationType0):
            orientation = self.orientation.value
        else:
            orientation = self.orientation

        data_collection_group_id: int | None | Unset
        if isinstance(self.data_collection_group_id, Unset):
            data_collection_group_id = UNSET
        else:
            data_collection_group_id = self.data_collection_group_id

        microns_per_pixel_x: float | None | Unset
        if isinstance(self.microns_per_pixel_x, Unset):
            microns_per_pixel_x = UNSET
        else:
            microns_per_pixel_x = self.microns_per_pixel_x

        microns_per_pixel_y: float | None | Unset
        if isinstance(self.microns_per_pixel_y, Unset):
            microns_per_pixel_y = UNSET
        else:
            microns_per_pixel_y = self.microns_per_pixel_y

        snaked: bool | None | Unset
        if isinstance(self.snaked, Unset):
            snaked = UNSET
        else:
            snaked = self.snaked

        patches_x: int | None | Unset
        if isinstance(self.patches_x, Unset):
            patches_x = UNSET
        else:
            patches_x = self.patches_x

        patches_y: int | None | Unset
        if isinstance(self.patches_y, Unset):
            patches_y = UNSET
        else:
            patches_y = self.patches_y

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "gridInfoId": grid_info_id,
            }
        )
        if x_offset is not UNSET:
            field_dict["xOffset"] = x_offset
        if y_offset is not UNSET:
            field_dict["yOffset"] = y_offset
        if snapshot_offset_x_pixel is not UNSET:
            field_dict["snapshotOffsetXPixel"] = snapshot_offset_x_pixel
        if snapshot_offset_y_pixel is not UNSET:
            field_dict["snapshotOffsetYPixel"] = snapshot_offset_y_pixel
        if dx is not UNSET:
            field_dict["dx"] = dx
        if dy is not UNSET:
            field_dict["dy"] = dy
        if steps_x is not UNSET:
            field_dict["stepsX"] = steps_x
        if steps_y is not UNSET:
            field_dict["stepsY"] = steps_y
        if mesh_angle is not UNSET:
            field_dict["meshAngle"] = mesh_angle
        if record_time_stamp is not UNSET:
            field_dict["recordTimeStamp"] = record_time_stamp
        if workflow_mesh_id is not UNSET:
            field_dict["workflowMeshId"] = workflow_mesh_id
        if orientation is not UNSET:
            field_dict["orientation"] = orientation
        if data_collection_group_id is not UNSET:
            field_dict["dataCollectionGroupId"] = data_collection_group_id
        if microns_per_pixel_x is not UNSET:
            field_dict["micronsPerPixelX"] = microns_per_pixel_x
        if microns_per_pixel_y is not UNSET:
            field_dict["micronsPerPixelY"] = microns_per_pixel_y
        if snaked is not UNSET:
            field_dict["snaked"] = snaked
        if patches_x is not UNSET:
            field_dict["patchesX"] = patches_x
        if patches_y is not UNSET:
            field_dict["patchesY"] = patches_y

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        grid_info_id = d.pop("gridInfoId")

        def _parse_x_offset(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        x_offset = _parse_x_offset(d.pop("xOffset", UNSET))

        def _parse_y_offset(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        y_offset = _parse_y_offset(d.pop("yOffset", UNSET))

        def _parse_snapshot_offset_x_pixel(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        snapshot_offset_x_pixel = _parse_snapshot_offset_x_pixel(d.pop("snapshotOffsetXPixel", UNSET))

        def _parse_snapshot_offset_y_pixel(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        snapshot_offset_y_pixel = _parse_snapshot_offset_y_pixel(d.pop("snapshotOffsetYPixel", UNSET))

        def _parse_dx(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        dx = _parse_dx(d.pop("dx", UNSET))

        def _parse_dy(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        dy = _parse_dy(d.pop("dy", UNSET))

        def _parse_steps_x(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        steps_x = _parse_steps_x(d.pop("stepsX", UNSET))

        def _parse_steps_y(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        steps_y = _parse_steps_y(d.pop("stepsY", UNSET))

        def _parse_mesh_angle(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        mesh_angle = _parse_mesh_angle(d.pop("meshAngle", UNSET))

        def _parse_record_time_stamp(data: object) -> datetime.datetime | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                record_time_stamp_type_0 = datetime.datetime.fromisoformat(data)

                return record_time_stamp_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(datetime.datetime | None | Unset, data)

        record_time_stamp = _parse_record_time_stamp(d.pop("recordTimeStamp", UNSET))

        def _parse_workflow_mesh_id(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        workflow_mesh_id = _parse_workflow_mesh_id(d.pop("workflowMeshId", UNSET))

        def _parse_orientation(data: object) -> GridInfoOutOrientationType0 | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                orientation_type_0 = GridInfoOutOrientationType0(data)

                return orientation_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(GridInfoOutOrientationType0 | None | Unset, data)

        orientation = _parse_orientation(d.pop("orientation", UNSET))

        def _parse_data_collection_group_id(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        data_collection_group_id = _parse_data_collection_group_id(d.pop("dataCollectionGroupId", UNSET))

        def _parse_microns_per_pixel_x(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        microns_per_pixel_x = _parse_microns_per_pixel_x(d.pop("micronsPerPixelX", UNSET))

        def _parse_microns_per_pixel_y(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        microns_per_pixel_y = _parse_microns_per_pixel_y(d.pop("micronsPerPixelY", UNSET))

        def _parse_snaked(data: object) -> bool | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(bool | None | Unset, data)

        snaked = _parse_snaked(d.pop("snaked", UNSET))

        def _parse_patches_x(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        patches_x = _parse_patches_x(d.pop("patchesX", UNSET))

        def _parse_patches_y(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        patches_y = _parse_patches_y(d.pop("patchesY", UNSET))

        grid_info_out = cls(
            grid_info_id=grid_info_id,
            x_offset=x_offset,
            y_offset=y_offset,
            snapshot_offset_x_pixel=snapshot_offset_x_pixel,
            snapshot_offset_y_pixel=snapshot_offset_y_pixel,
            dx=dx,
            dy=dy,
            steps_x=steps_x,
            steps_y=steps_y,
            mesh_angle=mesh_angle,
            record_time_stamp=record_time_stamp,
            workflow_mesh_id=workflow_mesh_id,
            orientation=orientation,
            data_collection_group_id=data_collection_group_id,
            microns_per_pixel_x=microns_per_pixel_x,
            microns_per_pixel_y=microns_per_pixel_y,
            snaked=snaked,
            patches_x=patches_x,
            patches_y=patches_y,
        )

        grid_info_out.additional_properties = d
        return grid_info_out

    @property
    def additional_keys(self) -> list[str]:
        return list(self.additional_properties.keys())

    def __getitem__(self, key: str) -> Any:
        return self.additional_properties[key]

    def __setitem__(self, key: str, value: Any) -> None:
        self.additional_properties[key] = value

    def __delitem__(self, key: str) -> None:
        del self.additional_properties[key]

    def __contains__(self, key: str) -> bool:
        return key in self.additional_properties

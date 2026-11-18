from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="SampleImageOptional")


@_attrs_define
class SampleImageOptional:
    """
    Attributes:
        container_inspection_id (int | None | Unset):
        bl_sample_image_score_id (int | None | Unset):
        microns_per_pixel_x (float | None | Unset):
        microns_per_pixel_y (float | None | Unset):
        image_full_path (None | str | Unset):
        comments (None | str | Unset):
        modified_time_stamp (datetime.datetime | None | Unset):
        offset_x (int | Unset):  Default: 0.
        offset_y (int | Unset):  Default: 0.
    """

    container_inspection_id: int | None | Unset = UNSET
    bl_sample_image_score_id: int | None | Unset = UNSET
    microns_per_pixel_x: float | None | Unset = UNSET
    microns_per_pixel_y: float | None | Unset = UNSET
    image_full_path: None | str | Unset = UNSET
    comments: None | str | Unset = UNSET
    modified_time_stamp: datetime.datetime | None | Unset = UNSET
    offset_x: int | Unset = 0
    offset_y: int | Unset = 0
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        container_inspection_id: int | None | Unset
        if isinstance(self.container_inspection_id, Unset):
            container_inspection_id = UNSET
        else:
            container_inspection_id = self.container_inspection_id

        bl_sample_image_score_id: int | None | Unset
        if isinstance(self.bl_sample_image_score_id, Unset):
            bl_sample_image_score_id = UNSET
        else:
            bl_sample_image_score_id = self.bl_sample_image_score_id

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

        image_full_path: None | str | Unset
        if isinstance(self.image_full_path, Unset):
            image_full_path = UNSET
        else:
            image_full_path = self.image_full_path

        comments: None | str | Unset
        if isinstance(self.comments, Unset):
            comments = UNSET
        else:
            comments = self.comments

        modified_time_stamp: None | str | Unset
        if isinstance(self.modified_time_stamp, Unset):
            modified_time_stamp = UNSET
        elif isinstance(self.modified_time_stamp, datetime.datetime):
            modified_time_stamp = self.modified_time_stamp.isoformat()
        else:
            modified_time_stamp = self.modified_time_stamp

        offset_x = self.offset_x

        offset_y = self.offset_y

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if container_inspection_id is not UNSET:
            field_dict["containerInspectionId"] = container_inspection_id
        if bl_sample_image_score_id is not UNSET:
            field_dict["blSampleImageScoreId"] = bl_sample_image_score_id
        if microns_per_pixel_x is not UNSET:
            field_dict["micronsPerPixelX"] = microns_per_pixel_x
        if microns_per_pixel_y is not UNSET:
            field_dict["micronsPerPixelY"] = microns_per_pixel_y
        if image_full_path is not UNSET:
            field_dict["imageFullPath"] = image_full_path
        if comments is not UNSET:
            field_dict["comments"] = comments
        if modified_time_stamp is not UNSET:
            field_dict["modifiedTimeStamp"] = modified_time_stamp
        if offset_x is not UNSET:
            field_dict["offsetX"] = offset_x
        if offset_y is not UNSET:
            field_dict["offsetY"] = offset_y

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)

        def _parse_container_inspection_id(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        container_inspection_id = _parse_container_inspection_id(d.pop("containerInspectionId", UNSET))

        def _parse_bl_sample_image_score_id(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        bl_sample_image_score_id = _parse_bl_sample_image_score_id(d.pop("blSampleImageScoreId", UNSET))

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

        def _parse_image_full_path(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        image_full_path = _parse_image_full_path(d.pop("imageFullPath", UNSET))

        def _parse_comments(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        comments = _parse_comments(d.pop("comments", UNSET))

        def _parse_modified_time_stamp(data: object) -> datetime.datetime | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                modified_time_stamp_type_0 = datetime.datetime.fromisoformat(data)

                return modified_time_stamp_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(datetime.datetime | None | Unset, data)

        modified_time_stamp = _parse_modified_time_stamp(d.pop("modifiedTimeStamp", UNSET))

        offset_x = d.pop("offsetX", UNSET)

        offset_y = d.pop("offsetY", UNSET)

        sample_image_optional = cls(
            container_inspection_id=container_inspection_id,
            bl_sample_image_score_id=bl_sample_image_score_id,
            microns_per_pixel_x=microns_per_pixel_x,
            microns_per_pixel_y=microns_per_pixel_y,
            image_full_path=image_full_path,
            comments=comments,
            modified_time_stamp=modified_time_stamp,
            offset_x=offset_x,
            offset_y=offset_y,
        )

        sample_image_optional.additional_properties = d
        return sample_image_optional

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

from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.robot_action_out_action_type_type_0 import RobotActionOutActionTypeType0
from ..models.robot_action_out_status_type_0 import RobotActionOutStatusType0
from ..types import UNSET, Unset

T = TypeVar("T", bound="RobotActionOut")


@_attrs_define
class RobotActionOut:
    """
    Attributes:
        robot_action_id (int):
        session_id (int):
        start_timestamp (datetime.datetime | None | Unset):
        end_timestamp (datetime.datetime | None | Unset):
        sample_id (int | None | Unset):
        action_type (None | RobotActionOutActionTypeType0 | Unset):
        status (None | RobotActionOutStatusType0 | Unset):
        message (None | str | Unset):
        container_location (int | None | Unset):
        dewar_location (int | None | Unset):
        sample_barcode (None | str | Unset):
        xtal_snapshot_before (None | str | Unset):
        xtal_snapshot_after (None | str | Unset):
    """

    robot_action_id: int
    session_id: int
    start_timestamp: datetime.datetime | None | Unset = UNSET
    end_timestamp: datetime.datetime | None | Unset = UNSET
    sample_id: int | None | Unset = UNSET
    action_type: None | RobotActionOutActionTypeType0 | Unset = UNSET
    status: None | RobotActionOutStatusType0 | Unset = UNSET
    message: None | str | Unset = UNSET
    container_location: int | None | Unset = UNSET
    dewar_location: int | None | Unset = UNSET
    sample_barcode: None | str | Unset = UNSET
    xtal_snapshot_before: None | str | Unset = UNSET
    xtal_snapshot_after: None | str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        robot_action_id = self.robot_action_id

        session_id = self.session_id

        start_timestamp: None | str | Unset
        if isinstance(self.start_timestamp, Unset):
            start_timestamp = UNSET
        elif isinstance(self.start_timestamp, datetime.datetime):
            start_timestamp = self.start_timestamp.isoformat()
        else:
            start_timestamp = self.start_timestamp

        end_timestamp: None | str | Unset
        if isinstance(self.end_timestamp, Unset):
            end_timestamp = UNSET
        elif isinstance(self.end_timestamp, datetime.datetime):
            end_timestamp = self.end_timestamp.isoformat()
        else:
            end_timestamp = self.end_timestamp

        sample_id: int | None | Unset
        if isinstance(self.sample_id, Unset):
            sample_id = UNSET
        else:
            sample_id = self.sample_id

        action_type: None | str | Unset
        if isinstance(self.action_type, Unset):
            action_type = UNSET
        elif isinstance(self.action_type, RobotActionOutActionTypeType0):
            action_type = self.action_type.value
        else:
            action_type = self.action_type

        status: None | str | Unset
        if isinstance(self.status, Unset):
            status = UNSET
        elif isinstance(self.status, RobotActionOutStatusType0):
            status = self.status.value
        else:
            status = self.status

        message: None | str | Unset
        if isinstance(self.message, Unset):
            message = UNSET
        else:
            message = self.message

        container_location: int | None | Unset
        if isinstance(self.container_location, Unset):
            container_location = UNSET
        else:
            container_location = self.container_location

        dewar_location: int | None | Unset
        if isinstance(self.dewar_location, Unset):
            dewar_location = UNSET
        else:
            dewar_location = self.dewar_location

        sample_barcode: None | str | Unset
        if isinstance(self.sample_barcode, Unset):
            sample_barcode = UNSET
        else:
            sample_barcode = self.sample_barcode

        xtal_snapshot_before: None | str | Unset
        if isinstance(self.xtal_snapshot_before, Unset):
            xtal_snapshot_before = UNSET
        else:
            xtal_snapshot_before = self.xtal_snapshot_before

        xtal_snapshot_after: None | str | Unset
        if isinstance(self.xtal_snapshot_after, Unset):
            xtal_snapshot_after = UNSET
        else:
            xtal_snapshot_after = self.xtal_snapshot_after

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "robotActionId": robot_action_id,
                "sessionId": session_id,
            }
        )
        if start_timestamp is not UNSET:
            field_dict["startTimestamp"] = start_timestamp
        if end_timestamp is not UNSET:
            field_dict["endTimestamp"] = end_timestamp
        if sample_id is not UNSET:
            field_dict["sampleId"] = sample_id
        if action_type is not UNSET:
            field_dict["actionType"] = action_type
        if status is not UNSET:
            field_dict["status"] = status
        if message is not UNSET:
            field_dict["message"] = message
        if container_location is not UNSET:
            field_dict["containerLocation"] = container_location
        if dewar_location is not UNSET:
            field_dict["dewarLocation"] = dewar_location
        if sample_barcode is not UNSET:
            field_dict["sampleBarcode"] = sample_barcode
        if xtal_snapshot_before is not UNSET:
            field_dict["xtalSnapshotBefore"] = xtal_snapshot_before
        if xtal_snapshot_after is not UNSET:
            field_dict["xtalSnapshotAfter"] = xtal_snapshot_after

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        robot_action_id = d.pop("robotActionId")

        session_id = d.pop("sessionId")

        def _parse_start_timestamp(data: object) -> datetime.datetime | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                start_timestamp_type_0 = datetime.datetime.fromisoformat(data)

                return start_timestamp_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(datetime.datetime | None | Unset, data)

        start_timestamp = _parse_start_timestamp(d.pop("startTimestamp", UNSET))

        def _parse_end_timestamp(data: object) -> datetime.datetime | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                end_timestamp_type_0 = datetime.datetime.fromisoformat(data)

                return end_timestamp_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(datetime.datetime | None | Unset, data)

        end_timestamp = _parse_end_timestamp(d.pop("endTimestamp", UNSET))

        def _parse_sample_id(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        sample_id = _parse_sample_id(d.pop("sampleId", UNSET))

        def _parse_action_type(data: object) -> None | RobotActionOutActionTypeType0 | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                action_type_type_0 = RobotActionOutActionTypeType0(data)

                return action_type_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(None | RobotActionOutActionTypeType0 | Unset, data)

        action_type = _parse_action_type(d.pop("actionType", UNSET))

        def _parse_status(data: object) -> None | RobotActionOutStatusType0 | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                status_type_0 = RobotActionOutStatusType0(data)

                return status_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(None | RobotActionOutStatusType0 | Unset, data)

        status = _parse_status(d.pop("status", UNSET))

        def _parse_message(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        message = _parse_message(d.pop("message", UNSET))

        def _parse_container_location(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        container_location = _parse_container_location(d.pop("containerLocation", UNSET))

        def _parse_dewar_location(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        dewar_location = _parse_dewar_location(d.pop("dewarLocation", UNSET))

        def _parse_sample_barcode(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        sample_barcode = _parse_sample_barcode(d.pop("sampleBarcode", UNSET))

        def _parse_xtal_snapshot_before(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        xtal_snapshot_before = _parse_xtal_snapshot_before(d.pop("xtalSnapshotBefore", UNSET))

        def _parse_xtal_snapshot_after(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        xtal_snapshot_after = _parse_xtal_snapshot_after(d.pop("xtalSnapshotAfter", UNSET))

        robot_action_out = cls(
            robot_action_id=robot_action_id,
            session_id=session_id,
            start_timestamp=start_timestamp,
            end_timestamp=end_timestamp,
            sample_id=sample_id,
            action_type=action_type,
            status=status,
            message=message,
            container_location=container_location,
            dewar_location=dewar_location,
            sample_barcode=sample_barcode,
            xtal_snapshot_before=xtal_snapshot_before,
            xtal_snapshot_after=xtal_snapshot_after,
        )

        robot_action_out.additional_properties = d
        return robot_action_out

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

from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast
from uuid import UUID

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.processing_status import ProcessingStatus
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.auto_proc_integration_out import AutoProcIntegrationOut
    from ..models.auto_proc_with_scaling_out import AutoProcWithScalingOut


T = TypeVar("T", bound="AutoProcProgramWithAutoProcOut")


@_attrs_define
class AutoProcProgramWithAutoProcOut:
    """
    Attributes:
        auto_proc_program_id (int):
        processing_job_id (int):
        status (ProcessingStatus):
        parent_auto_proc_program_id (int | None | Unset):
        processing_command_line (None | str | Unset):
        processing_programs (None | str | Unset):
        processing_status (int | None | Unset):
        processing_message (None | str | Unset):
        processing_start_time (datetime.datetime | None | Unset):
        processing_end_time (datetime.datetime | None | Unset):
        processing_environment (None | str | Unset):
        record_time_stamp (datetime.datetime | None | Unset):
        job_uuid (None | Unset | UUID):
        auto_proc (list[AutoProcWithScalingOut] | Unset):
        auto_proc_integration (list[AutoProcIntegrationOut] | Unset):
    """

    auto_proc_program_id: int
    processing_job_id: int
    status: ProcessingStatus
    parent_auto_proc_program_id: int | None | Unset = UNSET
    processing_command_line: None | str | Unset = UNSET
    processing_programs: None | str | Unset = UNSET
    processing_status: int | None | Unset = UNSET
    processing_message: None | str | Unset = UNSET
    processing_start_time: datetime.datetime | None | Unset = UNSET
    processing_end_time: datetime.datetime | None | Unset = UNSET
    processing_environment: None | str | Unset = UNSET
    record_time_stamp: datetime.datetime | None | Unset = UNSET
    job_uuid: None | Unset | UUID = UNSET
    auto_proc: list[AutoProcWithScalingOut] | Unset = UNSET
    auto_proc_integration: list[AutoProcIntegrationOut] | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        auto_proc_program_id = self.auto_proc_program_id

        processing_job_id = self.processing_job_id

        status = self.status.value

        parent_auto_proc_program_id: int | None | Unset
        if isinstance(self.parent_auto_proc_program_id, Unset):
            parent_auto_proc_program_id = UNSET
        else:
            parent_auto_proc_program_id = self.parent_auto_proc_program_id

        processing_command_line: None | str | Unset
        if isinstance(self.processing_command_line, Unset):
            processing_command_line = UNSET
        else:
            processing_command_line = self.processing_command_line

        processing_programs: None | str | Unset
        if isinstance(self.processing_programs, Unset):
            processing_programs = UNSET
        else:
            processing_programs = self.processing_programs

        processing_status: int | None | Unset
        if isinstance(self.processing_status, Unset):
            processing_status = UNSET
        else:
            processing_status = self.processing_status

        processing_message: None | str | Unset
        if isinstance(self.processing_message, Unset):
            processing_message = UNSET
        else:
            processing_message = self.processing_message

        processing_start_time: None | str | Unset
        if isinstance(self.processing_start_time, Unset):
            processing_start_time = UNSET
        elif isinstance(self.processing_start_time, datetime.datetime):
            processing_start_time = self.processing_start_time.isoformat()
        else:
            processing_start_time = self.processing_start_time

        processing_end_time: None | str | Unset
        if isinstance(self.processing_end_time, Unset):
            processing_end_time = UNSET
        elif isinstance(self.processing_end_time, datetime.datetime):
            processing_end_time = self.processing_end_time.isoformat()
        else:
            processing_end_time = self.processing_end_time

        processing_environment: None | str | Unset
        if isinstance(self.processing_environment, Unset):
            processing_environment = UNSET
        else:
            processing_environment = self.processing_environment

        record_time_stamp: None | str | Unset
        if isinstance(self.record_time_stamp, Unset):
            record_time_stamp = UNSET
        elif isinstance(self.record_time_stamp, datetime.datetime):
            record_time_stamp = self.record_time_stamp.isoformat()
        else:
            record_time_stamp = self.record_time_stamp

        job_uuid: None | str | Unset
        if isinstance(self.job_uuid, Unset):
            job_uuid = UNSET
        elif isinstance(self.job_uuid, UUID):
            job_uuid = str(self.job_uuid)
        else:
            job_uuid = self.job_uuid

        auto_proc: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.auto_proc, Unset):
            auto_proc = []
            for auto_proc_item_data in self.auto_proc:
                auto_proc_item = auto_proc_item_data.to_dict()
                auto_proc.append(auto_proc_item)

        auto_proc_integration: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.auto_proc_integration, Unset):
            auto_proc_integration = []
            for auto_proc_integration_item_data in self.auto_proc_integration:
                auto_proc_integration_item = auto_proc_integration_item_data.to_dict()
                auto_proc_integration.append(auto_proc_integration_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "autoProcProgramId": auto_proc_program_id,
                "processingJobId": processing_job_id,
                "status": status,
            }
        )
        if parent_auto_proc_program_id is not UNSET:
            field_dict["parentAutoProcProgramId"] = parent_auto_proc_program_id
        if processing_command_line is not UNSET:
            field_dict["processingCommandLine"] = processing_command_line
        if processing_programs is not UNSET:
            field_dict["processingPrograms"] = processing_programs
        if processing_status is not UNSET:
            field_dict["processingStatus"] = processing_status
        if processing_message is not UNSET:
            field_dict["processingMessage"] = processing_message
        if processing_start_time is not UNSET:
            field_dict["processingStartTime"] = processing_start_time
        if processing_end_time is not UNSET:
            field_dict["processingEndTime"] = processing_end_time
        if processing_environment is not UNSET:
            field_dict["processingEnvironment"] = processing_environment
        if record_time_stamp is not UNSET:
            field_dict["recordTimeStamp"] = record_time_stamp
        if job_uuid is not UNSET:
            field_dict["jobUuid"] = job_uuid
        if auto_proc is not UNSET:
            field_dict["autoProc"] = auto_proc
        if auto_proc_integration is not UNSET:
            field_dict["autoProcIntegration"] = auto_proc_integration

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.auto_proc_integration_out import AutoProcIntegrationOut
        from ..models.auto_proc_with_scaling_out import AutoProcWithScalingOut

        d = dict(src_dict)
        auto_proc_program_id = d.pop("autoProcProgramId")

        processing_job_id = d.pop("processingJobId")

        status = ProcessingStatus(d.pop("status"))

        def _parse_parent_auto_proc_program_id(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        parent_auto_proc_program_id = _parse_parent_auto_proc_program_id(d.pop("parentAutoProcProgramId", UNSET))

        def _parse_processing_command_line(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        processing_command_line = _parse_processing_command_line(d.pop("processingCommandLine", UNSET))

        def _parse_processing_programs(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        processing_programs = _parse_processing_programs(d.pop("processingPrograms", UNSET))

        def _parse_processing_status(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        processing_status = _parse_processing_status(d.pop("processingStatus", UNSET))

        def _parse_processing_message(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        processing_message = _parse_processing_message(d.pop("processingMessage", UNSET))

        def _parse_processing_start_time(data: object) -> datetime.datetime | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                processing_start_time_type_0 = datetime.datetime.fromisoformat(data)

                return processing_start_time_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(datetime.datetime | None | Unset, data)

        processing_start_time = _parse_processing_start_time(d.pop("processingStartTime", UNSET))

        def _parse_processing_end_time(data: object) -> datetime.datetime | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                processing_end_time_type_0 = datetime.datetime.fromisoformat(data)

                return processing_end_time_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(datetime.datetime | None | Unset, data)

        processing_end_time = _parse_processing_end_time(d.pop("processingEndTime", UNSET))

        def _parse_processing_environment(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        processing_environment = _parse_processing_environment(d.pop("processingEnvironment", UNSET))

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

        def _parse_job_uuid(data: object) -> None | Unset | UUID:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                job_uuid_type_0 = UUID(data)

                return job_uuid_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(None | Unset | UUID, data)

        job_uuid = _parse_job_uuid(d.pop("jobUuid", UNSET))

        _auto_proc = d.pop("autoProc", UNSET)
        auto_proc: list[AutoProcWithScalingOut] | Unset = UNSET
        if _auto_proc is not UNSET:
            auto_proc = []
            for auto_proc_item_data in _auto_proc:
                auto_proc_item = AutoProcWithScalingOut.from_dict(auto_proc_item_data)

                auto_proc.append(auto_proc_item)

        _auto_proc_integration = d.pop("autoProcIntegration", UNSET)
        auto_proc_integration: list[AutoProcIntegrationOut] | Unset = UNSET
        if _auto_proc_integration is not UNSET:
            auto_proc_integration = []
            for auto_proc_integration_item_data in _auto_proc_integration:
                auto_proc_integration_item = AutoProcIntegrationOut.from_dict(auto_proc_integration_item_data)

                auto_proc_integration.append(auto_proc_integration_item)

        auto_proc_program_with_auto_proc_out = cls(
            auto_proc_program_id=auto_proc_program_id,
            processing_job_id=processing_job_id,
            status=status,
            parent_auto_proc_program_id=parent_auto_proc_program_id,
            processing_command_line=processing_command_line,
            processing_programs=processing_programs,
            processing_status=processing_status,
            processing_message=processing_message,
            processing_start_time=processing_start_time,
            processing_end_time=processing_end_time,
            processing_environment=processing_environment,
            record_time_stamp=record_time_stamp,
            job_uuid=job_uuid,
            auto_proc=auto_proc,
            auto_proc_integration=auto_proc_integration,
        )

        auto_proc_program_with_auto_proc_out.additional_properties = d
        return auto_proc_program_with_auto_proc_out

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

from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.processing_status import ProcessingStatus
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.auto_proc_program_with_auto_proc_out import AutoProcProgramWithAutoProcOut


T = TypeVar("T", bound="ProcessingJobWithAutoProcProgramOut")


@_attrs_define
class ProcessingJobWithAutoProcProgramOut:
    """
    Attributes:
        processing_job_id (int):
        display_name (None | str):
        recipe (None | str):
        status (ProcessingStatus):
        comments (None | str | Unset):
        record_timestamp (datetime.datetime | None | Unset):
        automatic (int | None | Unset):
        auto_proc_program (list[AutoProcProgramWithAutoProcOut] | Unset):
    """

    processing_job_id: int
    display_name: None | str
    recipe: None | str
    status: ProcessingStatus
    comments: None | str | Unset = UNSET
    record_timestamp: datetime.datetime | None | Unset = UNSET
    automatic: int | None | Unset = UNSET
    auto_proc_program: list[AutoProcProgramWithAutoProcOut] | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        processing_job_id = self.processing_job_id

        display_name: None | str
        display_name = self.display_name

        recipe: None | str
        recipe = self.recipe

        status = self.status.value

        comments: None | str | Unset
        if isinstance(self.comments, Unset):
            comments = UNSET
        else:
            comments = self.comments

        record_timestamp: None | str | Unset
        if isinstance(self.record_timestamp, Unset):
            record_timestamp = UNSET
        elif isinstance(self.record_timestamp, datetime.datetime):
            record_timestamp = self.record_timestamp.isoformat()
        else:
            record_timestamp = self.record_timestamp

        automatic: int | None | Unset
        if isinstance(self.automatic, Unset):
            automatic = UNSET
        else:
            automatic = self.automatic

        auto_proc_program: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.auto_proc_program, Unset):
            auto_proc_program = []
            for auto_proc_program_item_data in self.auto_proc_program:
                auto_proc_program_item = auto_proc_program_item_data.to_dict()
                auto_proc_program.append(auto_proc_program_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "processingJobId": processing_job_id,
                "displayName": display_name,
                "recipe": recipe,
                "status": status,
            }
        )
        if comments is not UNSET:
            field_dict["comments"] = comments
        if record_timestamp is not UNSET:
            field_dict["recordTimestamp"] = record_timestamp
        if automatic is not UNSET:
            field_dict["automatic"] = automatic
        if auto_proc_program is not UNSET:
            field_dict["autoProcProgram"] = auto_proc_program

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.auto_proc_program_with_auto_proc_out import AutoProcProgramWithAutoProcOut

        d = dict(src_dict)
        processing_job_id = d.pop("processingJobId")

        def _parse_display_name(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        display_name = _parse_display_name(d.pop("displayName"))

        def _parse_recipe(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        recipe = _parse_recipe(d.pop("recipe"))

        status = ProcessingStatus(d.pop("status"))

        def _parse_comments(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        comments = _parse_comments(d.pop("comments", UNSET))

        def _parse_record_timestamp(data: object) -> datetime.datetime | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                record_timestamp_type_0 = datetime.datetime.fromisoformat(data)

                return record_timestamp_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(datetime.datetime | None | Unset, data)

        record_timestamp = _parse_record_timestamp(d.pop("recordTimestamp", UNSET))

        def _parse_automatic(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        automatic = _parse_automatic(d.pop("automatic", UNSET))

        _auto_proc_program = d.pop("autoProcProgram", UNSET)
        auto_proc_program: list[AutoProcProgramWithAutoProcOut] | Unset = UNSET
        if _auto_proc_program is not UNSET:
            auto_proc_program = []
            for auto_proc_program_item_data in _auto_proc_program:
                auto_proc_program_item = AutoProcProgramWithAutoProcOut.from_dict(auto_proc_program_item_data)

                auto_proc_program.append(auto_proc_program_item)

        processing_job_with_auto_proc_program_out = cls(
            processing_job_id=processing_job_id,
            display_name=display_name,
            recipe=recipe,
            status=status,
            comments=comments,
            record_timestamp=record_timestamp,
            automatic=automatic,
            auto_proc_program=auto_proc_program,
        )

        processing_job_with_auto_proc_program_out.additional_properties = d
        return processing_job_with_auto_proc_program_out

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

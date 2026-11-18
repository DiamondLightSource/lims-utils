from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.file_type import FileType
from ..types import UNSET, Unset

T = TypeVar("T", bound="AutoProcProgramAttachmentOut")


@_attrs_define
class AutoProcProgramAttachmentOut:
    """
    Attributes:
        auto_proc_program_attachment_id (int):
        auto_proc_program_id (int):
        file_type (FileType | None | Unset):
        file_name (None | str | Unset):
        file_path (None | str | Unset):
        record_time_stamp (datetime.datetime | None | Unset):
        importance_rank (int | None | Unset):
        deleted (bool | None | Unset):  Default: False.
    """

    auto_proc_program_attachment_id: int
    auto_proc_program_id: int
    file_type: FileType | None | Unset = UNSET
    file_name: None | str | Unset = UNSET
    file_path: None | str | Unset = UNSET
    record_time_stamp: datetime.datetime | None | Unset = UNSET
    importance_rank: int | None | Unset = UNSET
    deleted: bool | None | Unset = False
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        auto_proc_program_attachment_id = self.auto_proc_program_attachment_id

        auto_proc_program_id = self.auto_proc_program_id

        file_type: None | str | Unset
        if isinstance(self.file_type, Unset):
            file_type = UNSET
        elif isinstance(self.file_type, FileType):
            file_type = self.file_type.value
        else:
            file_type = self.file_type

        file_name: None | str | Unset
        if isinstance(self.file_name, Unset):
            file_name = UNSET
        else:
            file_name = self.file_name

        file_path: None | str | Unset
        if isinstance(self.file_path, Unset):
            file_path = UNSET
        else:
            file_path = self.file_path

        record_time_stamp: None | str | Unset
        if isinstance(self.record_time_stamp, Unset):
            record_time_stamp = UNSET
        elif isinstance(self.record_time_stamp, datetime.datetime):
            record_time_stamp = self.record_time_stamp.isoformat()
        else:
            record_time_stamp = self.record_time_stamp

        importance_rank: int | None | Unset
        if isinstance(self.importance_rank, Unset):
            importance_rank = UNSET
        else:
            importance_rank = self.importance_rank

        deleted: bool | None | Unset
        if isinstance(self.deleted, Unset):
            deleted = UNSET
        else:
            deleted = self.deleted

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "autoProcProgramAttachmentId": auto_proc_program_attachment_id,
                "autoProcProgramId": auto_proc_program_id,
            }
        )
        if file_type is not UNSET:
            field_dict["fileType"] = file_type
        if file_name is not UNSET:
            field_dict["fileName"] = file_name
        if file_path is not UNSET:
            field_dict["filePath"] = file_path
        if record_time_stamp is not UNSET:
            field_dict["recordTimeStamp"] = record_time_stamp
        if importance_rank is not UNSET:
            field_dict["importanceRank"] = importance_rank
        if deleted is not UNSET:
            field_dict["deleted"] = deleted

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        auto_proc_program_attachment_id = d.pop("autoProcProgramAttachmentId")

        auto_proc_program_id = d.pop("autoProcProgramId")

        def _parse_file_type(data: object) -> FileType | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                file_type_type_0 = FileType(data)

                return file_type_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(FileType | None | Unset, data)

        file_type = _parse_file_type(d.pop("fileType", UNSET))

        def _parse_file_name(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        file_name = _parse_file_name(d.pop("fileName", UNSET))

        def _parse_file_path(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        file_path = _parse_file_path(d.pop("filePath", UNSET))

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

        def _parse_importance_rank(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        importance_rank = _parse_importance_rank(d.pop("importanceRank", UNSET))

        def _parse_deleted(data: object) -> bool | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(bool | None | Unset, data)

        deleted = _parse_deleted(d.pop("deleted", UNSET))

        auto_proc_program_attachment_out = cls(
            auto_proc_program_attachment_id=auto_proc_program_attachment_id,
            auto_proc_program_id=auto_proc_program_id,
            file_type=file_type,
            file_name=file_name,
            file_path=file_path,
            record_time_stamp=record_time_stamp,
            importance_rank=importance_rank,
            deleted=deleted,
        )

        auto_proc_program_attachment_out.additional_properties = d
        return auto_proc_program_attachment_out

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

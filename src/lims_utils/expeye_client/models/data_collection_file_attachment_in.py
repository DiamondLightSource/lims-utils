from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.file_attachment_type import FileAttachmentType
from ..types import UNSET, Unset

T = TypeVar("T", bound="DataCollectionFileAttachmentIn")


@_attrs_define
class DataCollectionFileAttachmentIn:
    """
    Attributes:
        file_full_path (None | str):
        file_type (FileAttachmentType | None | Unset):
    """

    file_full_path: None | str
    file_type: FileAttachmentType | None | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        file_full_path: None | str
        file_full_path = self.file_full_path

        file_type: None | str | Unset
        if isinstance(self.file_type, Unset):
            file_type = UNSET
        elif isinstance(self.file_type, FileAttachmentType):
            file_type = self.file_type.value
        else:
            file_type = self.file_type

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "fileFullPath": file_full_path,
            }
        )
        if file_type is not UNSET:
            field_dict["fileType"] = file_type

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)

        def _parse_file_full_path(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        file_full_path = _parse_file_full_path(d.pop("fileFullPath"))

        def _parse_file_type(data: object) -> FileAttachmentType | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                file_type_type_0 = FileAttachmentType(data)

                return file_type_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(FileAttachmentType | None | Unset, data)

        file_type = _parse_file_type(d.pop("fileType", UNSET))

        data_collection_file_attachment_in = cls(
            file_full_path=file_full_path,
            file_type=file_type,
        )

        data_collection_file_attachment_in.additional_properties = d
        return data_collection_file_attachment_in

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

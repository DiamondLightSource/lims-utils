from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.file_attachment_type import FileAttachmentType
from ..types import UNSET, Unset

T = TypeVar("T", bound="DataCollectionFileAttachmentOptional")


@_attrs_define
class DataCollectionFileAttachmentOptional:
    """
    Attributes:
        file_type (FileAttachmentType | None | Unset):
        file_full_path (None | str | Unset):
    """

    file_type: FileAttachmentType | None | Unset = UNSET
    file_full_path: None | str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        file_type: None | str | Unset
        if isinstance(self.file_type, Unset):
            file_type = UNSET
        elif isinstance(self.file_type, FileAttachmentType):
            file_type = self.file_type.value
        else:
            file_type = self.file_type

        file_full_path: None | str | Unset
        if isinstance(self.file_full_path, Unset):
            file_full_path = UNSET
        else:
            file_full_path = self.file_full_path

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if file_type is not UNSET:
            field_dict["fileType"] = file_type
        if file_full_path is not UNSET:
            field_dict["fileFullPath"] = file_full_path

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)

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

        def _parse_file_full_path(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        file_full_path = _parse_file_full_path(d.pop("fileFullPath", UNSET))

        data_collection_file_attachment_optional = cls(
            file_type=file_type,
            file_full_path=file_full_path,
        )

        data_collection_file_attachment_optional.additional_properties = d
        return data_collection_file_attachment_optional

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

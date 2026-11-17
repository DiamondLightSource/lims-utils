from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="DataCollectionCommentIn")


@_attrs_define
class DataCollectionCommentIn:
    """
    Attributes:
        comments (str):
        mod_time (datetime.datetime | None | Unset):
    """

    comments: str
    mod_time: datetime.datetime | None | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        comments = self.comments

        mod_time: None | str | Unset
        if isinstance(self.mod_time, Unset):
            mod_time = UNSET
        elif isinstance(self.mod_time, datetime.datetime):
            mod_time = self.mod_time.isoformat()
        else:
            mod_time = self.mod_time

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "comments": comments,
            }
        )
        if mod_time is not UNSET:
            field_dict["modTime"] = mod_time

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        comments = d.pop("comments")

        def _parse_mod_time(data: object) -> datetime.datetime | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                mod_time_type_0 = datetime.datetime.fromisoformat(data)

                return mod_time_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(datetime.datetime | None | Unset, data)

        mod_time = _parse_mod_time(d.pop("modTime", UNSET))

        data_collection_comment_in = cls(
            comments=comments,
            mod_time=mod_time,
        )

        data_collection_comment_in.additional_properties = d
        return data_collection_comment_in

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

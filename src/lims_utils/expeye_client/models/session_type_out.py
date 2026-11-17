from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="SessionTypeOut")


@_attrs_define
class SessionTypeOut:
    """
    Attributes:
        type_name (str):
        session_id (int):
        session_type_id (int):
    """

    type_name: str
    session_id: int
    session_type_id: int
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        type_name = self.type_name

        session_id = self.session_id

        session_type_id = self.session_type_id

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "typeName": type_name,
                "sessionId": session_id,
                "sessionTypeId": session_type_id,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        type_name = d.pop("typeName")

        session_id = d.pop("sessionId")

        session_type_id = d.pop("sessionTypeId")

        session_type_out = cls(
            type_name=type_name,
            session_id=session_id,
            session_type_id=session_type_id,
        )

        session_type_out.additional_properties = d
        return session_type_out

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

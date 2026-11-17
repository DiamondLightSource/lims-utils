from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="UserGroupHasPersonOut")


@_attrs_define
class UserGroupHasPersonOut:
    """
    Attributes:
        user_group_id (int):
        person_id (int):
    """

    user_group_id: int
    person_id: int
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        user_group_id = self.user_group_id

        person_id = self.person_id

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "userGroupId": user_group_id,
                "personId": person_id,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        user_group_id = d.pop("userGroupId")

        person_id = d.pop("personId")

        user_group_has_person_out = cls(
            user_group_id=user_group_id,
            person_id=person_id,
        )

        user_group_has_person_out.additional_properties = d
        return user_group_has_person_out

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

from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.person_id_with_role_role_type_0 import PersonIdWithRoleRoleType0
from ..types import UNSET, Unset

T = TypeVar("T", bound="PersonIdWithRole")


@_attrs_define
class PersonIdWithRole:
    """
    Attributes:
        person (int):
        role (None | PersonIdWithRoleRoleType0 | Unset):
        is_remote (bool | Unset):  Default: False.
    """

    person: int
    role: None | PersonIdWithRoleRoleType0 | Unset = UNSET
    is_remote: bool | Unset = False
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        person = self.person

        role: None | str | Unset
        if isinstance(self.role, Unset):
            role = UNSET
        elif isinstance(self.role, PersonIdWithRoleRoleType0):
            role = self.role.value
        else:
            role = self.role

        is_remote = self.is_remote

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "person": person,
            }
        )
        if role is not UNSET:
            field_dict["role"] = role
        if is_remote is not UNSET:
            field_dict["isRemote"] = is_remote

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        person = d.pop("person")

        def _parse_role(data: object) -> None | PersonIdWithRoleRoleType0 | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                role_type_0 = PersonIdWithRoleRoleType0(data)

                return role_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(None | PersonIdWithRoleRoleType0 | Unset, data)

        role = _parse_role(d.pop("role", UNSET))

        is_remote = d.pop("isRemote", UNSET)

        person_id_with_role = cls(
            person=person,
            role=role,
            is_remote=is_remote,
        )

        person_id_with_role.additional_properties = d
        return person_id_with_role

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

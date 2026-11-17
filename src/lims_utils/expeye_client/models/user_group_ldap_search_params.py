from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.ldap_search_params import LDAPSearchParams


T = TypeVar("T", bound="UserGroupLDAPSearchParams")


@_attrs_define
class UserGroupLDAPSearchParams:
    """
    Attributes:
        user_group_id (int):
        name (str):
        parameters (list[LDAPSearchParams]):
    """

    user_group_id: int
    name: str
    parameters: list[LDAPSearchParams]
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        user_group_id = self.user_group_id

        name = self.name

        parameters = []
        for parameters_item_data in self.parameters:
            parameters_item = parameters_item_data.to_dict()
            parameters.append(parameters_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "userGroupId": user_group_id,
                "name": name,
                "parameters": parameters,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.ldap_search_params import LDAPSearchParams

        d = dict(src_dict)
        user_group_id = d.pop("userGroupId")

        name = d.pop("name")

        parameters = []
        _parameters = d.pop("parameters")
        for parameters_item_data in _parameters:
            parameters_item = LDAPSearchParams.from_dict(parameters_item_data)

            parameters.append(parameters_item)

        user_group_ldap_search_params = cls(
            user_group_id=user_group_id,
            name=name,
            parameters=parameters,
        )

        user_group_ldap_search_params.additional_properties = d
        return user_group_ldap_search_params

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

from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="LDAPSearchParams")


@_attrs_define
class LDAPSearchParams:
    """
    Attributes:
        name (str):
        host_url (str):
        filter_ (str):
        attributes (str):
        sequence_number (int):
        search_base (str):
    """

    name: str
    host_url: str
    filter_: str
    attributes: str
    sequence_number: int
    search_base: str
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        name = self.name

        host_url = self.host_url

        filter_ = self.filter_

        attributes = self.attributes

        sequence_number = self.sequence_number

        search_base = self.search_base

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "name": name,
                "hostURL": host_url,
                "filter": filter_,
                "attributes": attributes,
                "sequenceNumber": sequence_number,
                "searchBase": search_base,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        name = d.pop("name")

        host_url = d.pop("hostURL")

        filter_ = d.pop("filter")

        attributes = d.pop("attributes")

        sequence_number = d.pop("sequenceNumber")

        search_base = d.pop("searchBase")

        ldap_search_params = cls(
            name=name,
            host_url=host_url,
            filter_=filter_,
            attributes=attributes,
            sequence_number=sequence_number,
            search_base=search_base,
        )

        ldap_search_params.additional_properties = d
        return ldap_search_params

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

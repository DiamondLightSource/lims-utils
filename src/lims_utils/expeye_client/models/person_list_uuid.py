from __future__ import annotations

from collections.abc import Mapping
from typing import Any, Literal, TypeVar, cast
from uuid import UUID

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="PersonListUuid")


@_attrs_define
class PersonListUuid:
    """
    Attributes:
        persons (list[UUID]):
        person_as (Literal['uuid']):
    """

    persons: list[UUID]
    person_as: Literal["uuid"]
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        persons = []
        for persons_item_data in self.persons:
            persons_item = str(persons_item_data)
            persons.append(persons_item)

        person_as = self.person_as

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "persons": persons,
                "personAs": person_as,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        persons = []
        _persons = d.pop("persons")
        for persons_item_data in _persons:
            persons_item = UUID(persons_item_data)

            persons.append(persons_item)

        person_as = cast(Literal["uuid"], d.pop("personAs"))
        if person_as != "uuid":
            raise ValueError(f"personAs must match const 'uuid', got '{person_as}'")

        person_list_uuid = cls(
            persons=persons,
            person_as=person_as,
        )

        person_list_uuid.additional_properties = d
        return person_list_uuid

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

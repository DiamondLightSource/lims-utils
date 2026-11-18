from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="LabContactOut")


@_attrs_define
class LabContactOut:
    """
    Attributes:
        lab_contact_id (int):
        card_name (str):
    """

    lab_contact_id: int
    card_name: str
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        lab_contact_id = self.lab_contact_id

        card_name = self.card_name

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "labContactId": lab_contact_id,
                "cardName": card_name,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        lab_contact_id = d.pop("labContactId")

        card_name = d.pop("cardName")

        lab_contact_out = cls(
            lab_contact_id=lab_contact_id,
            card_name=card_name,
        )

        lab_contact_out.additional_properties = d
        return lab_contact_out

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

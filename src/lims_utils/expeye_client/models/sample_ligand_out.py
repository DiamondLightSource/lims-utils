from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="SampleLigandOut")


@_attrs_define
class SampleLigandOut:
    """
    Attributes:
        ligand_id (int):
        bl_sample_id (int):
    """

    ligand_id: int
    bl_sample_id: int
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        ligand_id = self.ligand_id

        bl_sample_id = self.bl_sample_id

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "ligandId": ligand_id,
                "blSampleId": bl_sample_id,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        ligand_id = d.pop("ligandId")

        bl_sample_id = d.pop("blSampleId")

        sample_ligand_out = cls(
            ligand_id=ligand_id,
            bl_sample_id=bl_sample_id,
        )

        sample_ligand_out.additional_properties = d
        return sample_ligand_out

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

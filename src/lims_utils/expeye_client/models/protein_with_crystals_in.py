from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.crystal_in import CrystalIn


T = TypeVar("T", bound="ProteinWithCrystalsIn")


@_attrs_define
class ProteinWithCrystalsIn:
    """
    Attributes:
        protein (int | str):
        crystals (list[CrystalIn]):
    """

    protein: int | str
    crystals: list[CrystalIn]
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        protein: int | str
        protein = self.protein

        crystals = []
        for crystals_item_data in self.crystals:
            crystals_item = crystals_item_data.to_dict()
            crystals.append(crystals_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "protein": protein,
                "crystals": crystals,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.crystal_in import CrystalIn

        d = dict(src_dict)

        def _parse_protein(data: object) -> int | str:
            return cast(int | str, data)

        protein = _parse_protein(d.pop("protein"))

        crystals = []
        _crystals = d.pop("crystals")
        for crystals_item_data in _crystals:
            crystals_item = CrystalIn.from_dict(crystals_item_data)

            crystals.append(crystals_item)

        protein_with_crystals_in = cls(
            protein=protein,
            crystals=crystals,
        )

        protein_with_crystals_in.additional_properties = d
        return protein_with_crystals_in

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

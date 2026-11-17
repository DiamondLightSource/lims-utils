from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="LigandIn")


@_attrs_define
class LigandIn:
    """
    Attributes:
        name (None | str | Unset):
        smiles (None | str | Unset):
        library_name (None | str | Unset):
        library_batch_number (None | str | Unset):
        plate_barcode (None | str | Unset):
        source_well (None | str | Unset):
    """

    name: None | str | Unset = UNSET
    smiles: None | str | Unset = UNSET
    library_name: None | str | Unset = UNSET
    library_batch_number: None | str | Unset = UNSET
    plate_barcode: None | str | Unset = UNSET
    source_well: None | str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        name: None | str | Unset
        if isinstance(self.name, Unset):
            name = UNSET
        else:
            name = self.name

        smiles: None | str | Unset
        if isinstance(self.smiles, Unset):
            smiles = UNSET
        else:
            smiles = self.smiles

        library_name: None | str | Unset
        if isinstance(self.library_name, Unset):
            library_name = UNSET
        else:
            library_name = self.library_name

        library_batch_number: None | str | Unset
        if isinstance(self.library_batch_number, Unset):
            library_batch_number = UNSET
        else:
            library_batch_number = self.library_batch_number

        plate_barcode: None | str | Unset
        if isinstance(self.plate_barcode, Unset):
            plate_barcode = UNSET
        else:
            plate_barcode = self.plate_barcode

        source_well: None | str | Unset
        if isinstance(self.source_well, Unset):
            source_well = UNSET
        else:
            source_well = self.source_well

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if name is not UNSET:
            field_dict["name"] = name
        if smiles is not UNSET:
            field_dict["SMILES"] = smiles
        if library_name is not UNSET:
            field_dict["libraryName"] = library_name
        if library_batch_number is not UNSET:
            field_dict["libraryBatchNumber"] = library_batch_number
        if plate_barcode is not UNSET:
            field_dict["plateBarcode"] = plate_barcode
        if source_well is not UNSET:
            field_dict["sourceWell"] = source_well

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)

        def _parse_name(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        name = _parse_name(d.pop("name", UNSET))

        def _parse_smiles(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        smiles = _parse_smiles(d.pop("SMILES", UNSET))

        def _parse_library_name(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        library_name = _parse_library_name(d.pop("libraryName", UNSET))

        def _parse_library_batch_number(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        library_batch_number = _parse_library_batch_number(d.pop("libraryBatchNumber", UNSET))

        def _parse_plate_barcode(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        plate_barcode = _parse_plate_barcode(d.pop("plateBarcode", UNSET))

        def _parse_source_well(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        source_well = _parse_source_well(d.pop("sourceWell", UNSET))

        ligand_in = cls(
            name=name,
            smiles=smiles,
            library_name=library_name,
            library_batch_number=library_batch_number,
            plate_barcode=plate_barcode,
            source_well=source_well,
        )

        ligand_in.additional_properties = d
        return ligand_in

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

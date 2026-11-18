from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="PDBOut")


@_attrs_define
class PDBOut:
    """
    Attributes:
        pdb_id (int):
        name (None | str | Unset):
        code (None | str | Unset):
        source (None | str | Unset):
        contents (None | str | Unset):
    """

    pdb_id: int
    name: None | str | Unset = UNSET
    code: None | str | Unset = UNSET
    source: None | str | Unset = UNSET
    contents: None | str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        pdb_id = self.pdb_id

        name: None | str | Unset
        if isinstance(self.name, Unset):
            name = UNSET
        else:
            name = self.name

        code: None | str | Unset
        if isinstance(self.code, Unset):
            code = UNSET
        else:
            code = self.code

        source: None | str | Unset
        if isinstance(self.source, Unset):
            source = UNSET
        else:
            source = self.source

        contents: None | str | Unset
        if isinstance(self.contents, Unset):
            contents = UNSET
        else:
            contents = self.contents

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "pdbId": pdb_id,
            }
        )
        if name is not UNSET:
            field_dict["name"] = name
        if code is not UNSET:
            field_dict["code"] = code
        if source is not UNSET:
            field_dict["source"] = source
        if contents is not UNSET:
            field_dict["contents"] = contents

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        pdb_id = d.pop("pdbId")

        def _parse_name(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        name = _parse_name(d.pop("name", UNSET))

        def _parse_code(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        code = _parse_code(d.pop("code", UNSET))

        def _parse_source(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        source = _parse_source(d.pop("source", UNSET))

        def _parse_contents(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        contents = _parse_contents(d.pop("contents", UNSET))

        pdb_out = cls(
            pdb_id=pdb_id,
            name=name,
            code=code,
            source=source,
            contents=contents,
        )

        pdb_out.additional_properties = d
        return pdb_out

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

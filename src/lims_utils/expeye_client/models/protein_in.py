from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast
from uuid import UUID

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.safety_levels import SafetyLevels
from ..types import UNSET, Unset

T = TypeVar("T", bound="ProteinIn")


@_attrs_define
class ProteinIn:
    """
    Attributes:
        name (None | str | Unset):
        acronym (None | str | Unset):
        description (None | str | Unset):
        hazard_group (int | None | Unset):
        containment_level (int | None | Unset):
        safety_level (None | SafetyLevels | Unset):
        protein_type (None | str | Unset):
        abundance (float | None | Unset):
        density (float | None | Unset):
        sequence (None | str | Unset):
        external_id (None | Unset | UUID):
    """

    name: None | str | Unset = UNSET
    acronym: None | str | Unset = UNSET
    description: None | str | Unset = UNSET
    hazard_group: int | None | Unset = UNSET
    containment_level: int | None | Unset = UNSET
    safety_level: None | SafetyLevels | Unset = UNSET
    protein_type: None | str | Unset = UNSET
    abundance: float | None | Unset = UNSET
    density: float | None | Unset = UNSET
    sequence: None | str | Unset = UNSET
    external_id: None | Unset | UUID = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        name: None | str | Unset
        if isinstance(self.name, Unset):
            name = UNSET
        else:
            name = self.name

        acronym: None | str | Unset
        if isinstance(self.acronym, Unset):
            acronym = UNSET
        else:
            acronym = self.acronym

        description: None | str | Unset
        if isinstance(self.description, Unset):
            description = UNSET
        else:
            description = self.description

        hazard_group: int | None | Unset
        if isinstance(self.hazard_group, Unset):
            hazard_group = UNSET
        else:
            hazard_group = self.hazard_group

        containment_level: int | None | Unset
        if isinstance(self.containment_level, Unset):
            containment_level = UNSET
        else:
            containment_level = self.containment_level

        safety_level: None | str | Unset
        if isinstance(self.safety_level, Unset):
            safety_level = UNSET
        elif isinstance(self.safety_level, SafetyLevels):
            safety_level = self.safety_level.value
        else:
            safety_level = self.safety_level

        protein_type: None | str | Unset
        if isinstance(self.protein_type, Unset):
            protein_type = UNSET
        else:
            protein_type = self.protein_type

        abundance: float | None | Unset
        if isinstance(self.abundance, Unset):
            abundance = UNSET
        else:
            abundance = self.abundance

        density: float | None | Unset
        if isinstance(self.density, Unset):
            density = UNSET
        else:
            density = self.density

        sequence: None | str | Unset
        if isinstance(self.sequence, Unset):
            sequence = UNSET
        else:
            sequence = self.sequence

        external_id: None | str | Unset
        if isinstance(self.external_id, Unset):
            external_id = UNSET
        elif isinstance(self.external_id, UUID):
            external_id = str(self.external_id)
        else:
            external_id = self.external_id

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if name is not UNSET:
            field_dict["name"] = name
        if acronym is not UNSET:
            field_dict["acronym"] = acronym
        if description is not UNSET:
            field_dict["description"] = description
        if hazard_group is not UNSET:
            field_dict["hazardGroup"] = hazard_group
        if containment_level is not UNSET:
            field_dict["containmentLevel"] = containment_level
        if safety_level is not UNSET:
            field_dict["safetyLevel"] = safety_level
        if protein_type is not UNSET:
            field_dict["proteinType"] = protein_type
        if abundance is not UNSET:
            field_dict["abundance"] = abundance
        if density is not UNSET:
            field_dict["density"] = density
        if sequence is not UNSET:
            field_dict["sequence"] = sequence
        if external_id is not UNSET:
            field_dict["externalId"] = external_id

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

        def _parse_acronym(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        acronym = _parse_acronym(d.pop("acronym", UNSET))

        def _parse_description(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        description = _parse_description(d.pop("description", UNSET))

        def _parse_hazard_group(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        hazard_group = _parse_hazard_group(d.pop("hazardGroup", UNSET))

        def _parse_containment_level(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        containment_level = _parse_containment_level(d.pop("containmentLevel", UNSET))

        def _parse_safety_level(data: object) -> None | SafetyLevels | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                safety_level_type_0 = SafetyLevels(data)

                return safety_level_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(None | SafetyLevels | Unset, data)

        safety_level = _parse_safety_level(d.pop("safetyLevel", UNSET))

        def _parse_protein_type(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        protein_type = _parse_protein_type(d.pop("proteinType", UNSET))

        def _parse_abundance(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        abundance = _parse_abundance(d.pop("abundance", UNSET))

        def _parse_density(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        density = _parse_density(d.pop("density", UNSET))

        def _parse_sequence(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        sequence = _parse_sequence(d.pop("sequence", UNSET))

        def _parse_external_id(data: object) -> None | Unset | UUID:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                external_id_type_0 = UUID(data)

                return external_id_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(None | Unset | UUID, data)

        external_id = _parse_external_id(d.pop("externalId", UNSET))

        protein_in = cls(
            name=name,
            acronym=acronym,
            description=description,
            hazard_group=hazard_group,
            containment_level=containment_level,
            safety_level=safety_level,
            protein_type=protein_type,
            abundance=abundance,
            density=density,
            sequence=sequence,
            external_id=external_id,
        )

        protein_in.additional_properties = d
        return protein_in

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

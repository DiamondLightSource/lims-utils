from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="CrystalOut")


@_attrs_define
class CrystalOut:
    """
    Attributes:
        crystal_id (int):
        record_time_stamp (datetime.datetime):
        name (None | str | Unset):
        morphology (None | str | Unset):
        color (None | str | Unset):
        space_group (None | str | Unset):
        comments (None | str | Unset):
        pdb_file_name (None | str | Unset):
        pdb_file_path (None | str | Unset):
        abundance (float | None | Unset):
        theoretical_density (float | None | Unset):
        diffraction_plan_id (int | None | Unset):
        crystal_uuid (None | str | Unset):
        size_x (float | None | Unset):
        size_y (float | None | Unset):
        size_z (float | None | Unset):
        cell_a (float | None | Unset):
        cell_b (float | None | Unset):
        cell_c (float | None | Unset):
        cell_alpha (float | None | Unset):
        cell_beta (float | None | Unset):
        cell_gamma (float | None | Unset):
    """

    crystal_id: int
    record_time_stamp: datetime.datetime
    name: None | str | Unset = UNSET
    morphology: None | str | Unset = UNSET
    color: None | str | Unset = UNSET
    space_group: None | str | Unset = UNSET
    comments: None | str | Unset = UNSET
    pdb_file_name: None | str | Unset = UNSET
    pdb_file_path: None | str | Unset = UNSET
    abundance: float | None | Unset = UNSET
    theoretical_density: float | None | Unset = UNSET
    diffraction_plan_id: int | None | Unset = UNSET
    crystal_uuid: None | str | Unset = UNSET
    size_x: float | None | Unset = UNSET
    size_y: float | None | Unset = UNSET
    size_z: float | None | Unset = UNSET
    cell_a: float | None | Unset = UNSET
    cell_b: float | None | Unset = UNSET
    cell_c: float | None | Unset = UNSET
    cell_alpha: float | None | Unset = UNSET
    cell_beta: float | None | Unset = UNSET
    cell_gamma: float | None | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        crystal_id = self.crystal_id

        record_time_stamp = self.record_time_stamp.isoformat()

        name: None | str | Unset
        if isinstance(self.name, Unset):
            name = UNSET
        else:
            name = self.name

        morphology: None | str | Unset
        if isinstance(self.morphology, Unset):
            morphology = UNSET
        else:
            morphology = self.morphology

        color: None | str | Unset
        if isinstance(self.color, Unset):
            color = UNSET
        else:
            color = self.color

        space_group: None | str | Unset
        if isinstance(self.space_group, Unset):
            space_group = UNSET
        else:
            space_group = self.space_group

        comments: None | str | Unset
        if isinstance(self.comments, Unset):
            comments = UNSET
        else:
            comments = self.comments

        pdb_file_name: None | str | Unset
        if isinstance(self.pdb_file_name, Unset):
            pdb_file_name = UNSET
        else:
            pdb_file_name = self.pdb_file_name

        pdb_file_path: None | str | Unset
        if isinstance(self.pdb_file_path, Unset):
            pdb_file_path = UNSET
        else:
            pdb_file_path = self.pdb_file_path

        abundance: float | None | Unset
        if isinstance(self.abundance, Unset):
            abundance = UNSET
        else:
            abundance = self.abundance

        theoretical_density: float | None | Unset
        if isinstance(self.theoretical_density, Unset):
            theoretical_density = UNSET
        else:
            theoretical_density = self.theoretical_density

        diffraction_plan_id: int | None | Unset
        if isinstance(self.diffraction_plan_id, Unset):
            diffraction_plan_id = UNSET
        else:
            diffraction_plan_id = self.diffraction_plan_id

        crystal_uuid: None | str | Unset
        if isinstance(self.crystal_uuid, Unset):
            crystal_uuid = UNSET
        else:
            crystal_uuid = self.crystal_uuid

        size_x: float | None | Unset
        if isinstance(self.size_x, Unset):
            size_x = UNSET
        else:
            size_x = self.size_x

        size_y: float | None | Unset
        if isinstance(self.size_y, Unset):
            size_y = UNSET
        else:
            size_y = self.size_y

        size_z: float | None | Unset
        if isinstance(self.size_z, Unset):
            size_z = UNSET
        else:
            size_z = self.size_z

        cell_a: float | None | Unset
        if isinstance(self.cell_a, Unset):
            cell_a = UNSET
        else:
            cell_a = self.cell_a

        cell_b: float | None | Unset
        if isinstance(self.cell_b, Unset):
            cell_b = UNSET
        else:
            cell_b = self.cell_b

        cell_c: float | None | Unset
        if isinstance(self.cell_c, Unset):
            cell_c = UNSET
        else:
            cell_c = self.cell_c

        cell_alpha: float | None | Unset
        if isinstance(self.cell_alpha, Unset):
            cell_alpha = UNSET
        else:
            cell_alpha = self.cell_alpha

        cell_beta: float | None | Unset
        if isinstance(self.cell_beta, Unset):
            cell_beta = UNSET
        else:
            cell_beta = self.cell_beta

        cell_gamma: float | None | Unset
        if isinstance(self.cell_gamma, Unset):
            cell_gamma = UNSET
        else:
            cell_gamma = self.cell_gamma

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "crystalId": crystal_id,
                "recordTimeStamp": record_time_stamp,
            }
        )
        if name is not UNSET:
            field_dict["name"] = name
        if morphology is not UNSET:
            field_dict["morphology"] = morphology
        if color is not UNSET:
            field_dict["color"] = color
        if space_group is not UNSET:
            field_dict["spaceGroup"] = space_group
        if comments is not UNSET:
            field_dict["comments"] = comments
        if pdb_file_name is not UNSET:
            field_dict["pdbFileName"] = pdb_file_name
        if pdb_file_path is not UNSET:
            field_dict["pdbFilePath"] = pdb_file_path
        if abundance is not UNSET:
            field_dict["abundance"] = abundance
        if theoretical_density is not UNSET:
            field_dict["theoreticalDensity"] = theoretical_density
        if diffraction_plan_id is not UNSET:
            field_dict["diffractionPlanId"] = diffraction_plan_id
        if crystal_uuid is not UNSET:
            field_dict["crystalUUID"] = crystal_uuid
        if size_x is not UNSET:
            field_dict["sizeX"] = size_x
        if size_y is not UNSET:
            field_dict["sizeY"] = size_y
        if size_z is not UNSET:
            field_dict["sizeZ"] = size_z
        if cell_a is not UNSET:
            field_dict["cellA"] = cell_a
        if cell_b is not UNSET:
            field_dict["cellB"] = cell_b
        if cell_c is not UNSET:
            field_dict["cellC"] = cell_c
        if cell_alpha is not UNSET:
            field_dict["cellAlpha"] = cell_alpha
        if cell_beta is not UNSET:
            field_dict["cellBeta"] = cell_beta
        if cell_gamma is not UNSET:
            field_dict["cellGamma"] = cell_gamma

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        crystal_id = d.pop("crystalId")

        record_time_stamp = datetime.datetime.fromisoformat(d.pop("recordTimeStamp"))

        def _parse_name(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        name = _parse_name(d.pop("name", UNSET))

        def _parse_morphology(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        morphology = _parse_morphology(d.pop("morphology", UNSET))

        def _parse_color(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        color = _parse_color(d.pop("color", UNSET))

        def _parse_space_group(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        space_group = _parse_space_group(d.pop("spaceGroup", UNSET))

        def _parse_comments(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        comments = _parse_comments(d.pop("comments", UNSET))

        def _parse_pdb_file_name(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        pdb_file_name = _parse_pdb_file_name(d.pop("pdbFileName", UNSET))

        def _parse_pdb_file_path(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        pdb_file_path = _parse_pdb_file_path(d.pop("pdbFilePath", UNSET))

        def _parse_abundance(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        abundance = _parse_abundance(d.pop("abundance", UNSET))

        def _parse_theoretical_density(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        theoretical_density = _parse_theoretical_density(d.pop("theoreticalDensity", UNSET))

        def _parse_diffraction_plan_id(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        diffraction_plan_id = _parse_diffraction_plan_id(d.pop("diffractionPlanId", UNSET))

        def _parse_crystal_uuid(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        crystal_uuid = _parse_crystal_uuid(d.pop("crystalUUID", UNSET))

        def _parse_size_x(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        size_x = _parse_size_x(d.pop("sizeX", UNSET))

        def _parse_size_y(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        size_y = _parse_size_y(d.pop("sizeY", UNSET))

        def _parse_size_z(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        size_z = _parse_size_z(d.pop("sizeZ", UNSET))

        def _parse_cell_a(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        cell_a = _parse_cell_a(d.pop("cellA", UNSET))

        def _parse_cell_b(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        cell_b = _parse_cell_b(d.pop("cellB", UNSET))

        def _parse_cell_c(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        cell_c = _parse_cell_c(d.pop("cellC", UNSET))

        def _parse_cell_alpha(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        cell_alpha = _parse_cell_alpha(d.pop("cellAlpha", UNSET))

        def _parse_cell_beta(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        cell_beta = _parse_cell_beta(d.pop("cellBeta", UNSET))

        def _parse_cell_gamma(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        cell_gamma = _parse_cell_gamma(d.pop("cellGamma", UNSET))

        crystal_out = cls(
            crystal_id=crystal_id,
            record_time_stamp=record_time_stamp,
            name=name,
            morphology=morphology,
            color=color,
            space_group=space_group,
            comments=comments,
            pdb_file_name=pdb_file_name,
            pdb_file_path=pdb_file_path,
            abundance=abundance,
            theoretical_density=theoretical_density,
            diffraction_plan_id=diffraction_plan_id,
            crystal_uuid=crystal_uuid,
            size_x=size_x,
            size_y=size_y,
            size_z=size_z,
            cell_a=cell_a,
            cell_b=cell_b,
            cell_c=cell_c,
            cell_alpha=cell_alpha,
            cell_beta=cell_beta,
            cell_gamma=cell_gamma,
        )

        crystal_out.additional_properties = d
        return crystal_out

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

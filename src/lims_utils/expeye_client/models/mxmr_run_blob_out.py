from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.mxmr_run_blob_out_map_type_type_0 import MXMRRunBlobOutMapTypeType0
from ..types import UNSET, Unset

T = TypeVar("T", bound="MXMRRunBlobOut")


@_attrs_define
class MXMRRunBlobOut:
    """
    Attributes:
        mx_mr_run_blob_id (int):
        mx_mr_run_id (int):
        file_path (None | str | Unset):
        view1 (None | str | Unset):
        view2 (None | str | Unset):
        view3 (None | str | Unset):
        x (float | None | Unset):
        y (float | None | Unset):
        z (float | None | Unset):
        height (float | None | Unset):
        occupancy (float | None | Unset):
        nearest_atom_name (None | str | Unset):
        nearest_atom_chain_id (None | str | Unset):
        nearest_atom_res_name (None | str | Unset):
        nearest_atom_res_seq (int | None | Unset):
        nearest_atom_distance (float | None | Unset):
        map_type (MXMRRunBlobOutMapTypeType0 | None | Unset):
    """

    mx_mr_run_blob_id: int
    mx_mr_run_id: int
    file_path: None | str | Unset = UNSET
    view1: None | str | Unset = UNSET
    view2: None | str | Unset = UNSET
    view3: None | str | Unset = UNSET
    x: float | None | Unset = UNSET
    y: float | None | Unset = UNSET
    z: float | None | Unset = UNSET
    height: float | None | Unset = UNSET
    occupancy: float | None | Unset = UNSET
    nearest_atom_name: None | str | Unset = UNSET
    nearest_atom_chain_id: None | str | Unset = UNSET
    nearest_atom_res_name: None | str | Unset = UNSET
    nearest_atom_res_seq: int | None | Unset = UNSET
    nearest_atom_distance: float | None | Unset = UNSET
    map_type: MXMRRunBlobOutMapTypeType0 | None | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        mx_mr_run_blob_id = self.mx_mr_run_blob_id

        mx_mr_run_id = self.mx_mr_run_id

        file_path: None | str | Unset
        if isinstance(self.file_path, Unset):
            file_path = UNSET
        else:
            file_path = self.file_path

        view1: None | str | Unset
        if isinstance(self.view1, Unset):
            view1 = UNSET
        else:
            view1 = self.view1

        view2: None | str | Unset
        if isinstance(self.view2, Unset):
            view2 = UNSET
        else:
            view2 = self.view2

        view3: None | str | Unset
        if isinstance(self.view3, Unset):
            view3 = UNSET
        else:
            view3 = self.view3

        x: float | None | Unset
        if isinstance(self.x, Unset):
            x = UNSET
        else:
            x = self.x

        y: float | None | Unset
        if isinstance(self.y, Unset):
            y = UNSET
        else:
            y = self.y

        z: float | None | Unset
        if isinstance(self.z, Unset):
            z = UNSET
        else:
            z = self.z

        height: float | None | Unset
        if isinstance(self.height, Unset):
            height = UNSET
        else:
            height = self.height

        occupancy: float | None | Unset
        if isinstance(self.occupancy, Unset):
            occupancy = UNSET
        else:
            occupancy = self.occupancy

        nearest_atom_name: None | str | Unset
        if isinstance(self.nearest_atom_name, Unset):
            nearest_atom_name = UNSET
        else:
            nearest_atom_name = self.nearest_atom_name

        nearest_atom_chain_id: None | str | Unset
        if isinstance(self.nearest_atom_chain_id, Unset):
            nearest_atom_chain_id = UNSET
        else:
            nearest_atom_chain_id = self.nearest_atom_chain_id

        nearest_atom_res_name: None | str | Unset
        if isinstance(self.nearest_atom_res_name, Unset):
            nearest_atom_res_name = UNSET
        else:
            nearest_atom_res_name = self.nearest_atom_res_name

        nearest_atom_res_seq: int | None | Unset
        if isinstance(self.nearest_atom_res_seq, Unset):
            nearest_atom_res_seq = UNSET
        else:
            nearest_atom_res_seq = self.nearest_atom_res_seq

        nearest_atom_distance: float | None | Unset
        if isinstance(self.nearest_atom_distance, Unset):
            nearest_atom_distance = UNSET
        else:
            nearest_atom_distance = self.nearest_atom_distance

        map_type: None | str | Unset
        if isinstance(self.map_type, Unset):
            map_type = UNSET
        elif isinstance(self.map_type, MXMRRunBlobOutMapTypeType0):
            map_type = self.map_type.value
        else:
            map_type = self.map_type

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "mxMRRunBlobId": mx_mr_run_blob_id,
                "mxMRRunId": mx_mr_run_id,
            }
        )
        if file_path is not UNSET:
            field_dict["filePath"] = file_path
        if view1 is not UNSET:
            field_dict["view1"] = view1
        if view2 is not UNSET:
            field_dict["view2"] = view2
        if view3 is not UNSET:
            field_dict["view3"] = view3
        if x is not UNSET:
            field_dict["x"] = x
        if y is not UNSET:
            field_dict["y"] = y
        if z is not UNSET:
            field_dict["z"] = z
        if height is not UNSET:
            field_dict["height"] = height
        if occupancy is not UNSET:
            field_dict["occupancy"] = occupancy
        if nearest_atom_name is not UNSET:
            field_dict["nearestAtomName"] = nearest_atom_name
        if nearest_atom_chain_id is not UNSET:
            field_dict["nearestAtomChainId"] = nearest_atom_chain_id
        if nearest_atom_res_name is not UNSET:
            field_dict["nearestAtomResName"] = nearest_atom_res_name
        if nearest_atom_res_seq is not UNSET:
            field_dict["nearestAtomResSeq"] = nearest_atom_res_seq
        if nearest_atom_distance is not UNSET:
            field_dict["nearestAtomDistance"] = nearest_atom_distance
        if map_type is not UNSET:
            field_dict["mapType"] = map_type

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        mx_mr_run_blob_id = d.pop("mxMRRunBlobId")

        mx_mr_run_id = d.pop("mxMRRunId")

        def _parse_file_path(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        file_path = _parse_file_path(d.pop("filePath", UNSET))

        def _parse_view1(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        view1 = _parse_view1(d.pop("view1", UNSET))

        def _parse_view2(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        view2 = _parse_view2(d.pop("view2", UNSET))

        def _parse_view3(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        view3 = _parse_view3(d.pop("view3", UNSET))

        def _parse_x(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        x = _parse_x(d.pop("x", UNSET))

        def _parse_y(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        y = _parse_y(d.pop("y", UNSET))

        def _parse_z(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        z = _parse_z(d.pop("z", UNSET))

        def _parse_height(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        height = _parse_height(d.pop("height", UNSET))

        def _parse_occupancy(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        occupancy = _parse_occupancy(d.pop("occupancy", UNSET))

        def _parse_nearest_atom_name(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        nearest_atom_name = _parse_nearest_atom_name(d.pop("nearestAtomName", UNSET))

        def _parse_nearest_atom_chain_id(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        nearest_atom_chain_id = _parse_nearest_atom_chain_id(d.pop("nearestAtomChainId", UNSET))

        def _parse_nearest_atom_res_name(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        nearest_atom_res_name = _parse_nearest_atom_res_name(d.pop("nearestAtomResName", UNSET))

        def _parse_nearest_atom_res_seq(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        nearest_atom_res_seq = _parse_nearest_atom_res_seq(d.pop("nearestAtomResSeq", UNSET))

        def _parse_nearest_atom_distance(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        nearest_atom_distance = _parse_nearest_atom_distance(d.pop("nearestAtomDistance", UNSET))

        def _parse_map_type(data: object) -> MXMRRunBlobOutMapTypeType0 | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                map_type_type_0 = MXMRRunBlobOutMapTypeType0(data)

                return map_type_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(MXMRRunBlobOutMapTypeType0 | None | Unset, data)

        map_type = _parse_map_type(d.pop("mapType", UNSET))

        mxmr_run_blob_out = cls(
            mx_mr_run_blob_id=mx_mr_run_blob_id,
            mx_mr_run_id=mx_mr_run_id,
            file_path=file_path,
            view1=view1,
            view2=view2,
            view3=view3,
            x=x,
            y=y,
            z=z,
            height=height,
            occupancy=occupancy,
            nearest_atom_name=nearest_atom_name,
            nearest_atom_chain_id=nearest_atom_chain_id,
            nearest_atom_res_name=nearest_atom_res_name,
            nearest_atom_res_seq=nearest_atom_res_seq,
            nearest_atom_distance=nearest_atom_distance,
            map_type=map_type,
        )

        mxmr_run_blob_out.additional_properties = d
        return mxmr_run_blob_out

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

from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="AutoProcIntegrationOut")


@_attrs_define
class AutoProcIntegrationOut:
    """
    Attributes:
        auto_proc_integration_id (int):
        cell_a (float | None):
        cell_b (float | None):
        cell_c (float | None):
        cell_alpha (float | None):
        cell_beta (float | None):
        cell_gamma (float | None):
        start_image_number (int | None | Unset):
        end_image_number (int | None | Unset):
        refined_detector_distance (float | None | Unset):
        refined_x_beam (float | None | Unset):
        refined_y_beam (float | None | Unset):
        rotation_axis_x (float | None | Unset):
        rotation_axis_y (float | None | Unset):
        rotation_axis_z (float | None | Unset):
        beam_vector_x (float | None | Unset):
        beam_vector_y (float | None | Unset):
        beam_vector_z (float | None | Unset):
        record_time_stamp (datetime.datetime | None | Unset):
        anomalous (bool | None | Unset):
    """

    auto_proc_integration_id: int
    cell_a: float | None
    cell_b: float | None
    cell_c: float | None
    cell_alpha: float | None
    cell_beta: float | None
    cell_gamma: float | None
    start_image_number: int | None | Unset = UNSET
    end_image_number: int | None | Unset = UNSET
    refined_detector_distance: float | None | Unset = UNSET
    refined_x_beam: float | None | Unset = UNSET
    refined_y_beam: float | None | Unset = UNSET
    rotation_axis_x: float | None | Unset = UNSET
    rotation_axis_y: float | None | Unset = UNSET
    rotation_axis_z: float | None | Unset = UNSET
    beam_vector_x: float | None | Unset = UNSET
    beam_vector_y: float | None | Unset = UNSET
    beam_vector_z: float | None | Unset = UNSET
    record_time_stamp: datetime.datetime | None | Unset = UNSET
    anomalous: bool | None | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        auto_proc_integration_id = self.auto_proc_integration_id

        cell_a: float | None
        cell_a = self.cell_a

        cell_b: float | None
        cell_b = self.cell_b

        cell_c: float | None
        cell_c = self.cell_c

        cell_alpha: float | None
        cell_alpha = self.cell_alpha

        cell_beta: float | None
        cell_beta = self.cell_beta

        cell_gamma: float | None
        cell_gamma = self.cell_gamma

        start_image_number: int | None | Unset
        if isinstance(self.start_image_number, Unset):
            start_image_number = UNSET
        else:
            start_image_number = self.start_image_number

        end_image_number: int | None | Unset
        if isinstance(self.end_image_number, Unset):
            end_image_number = UNSET
        else:
            end_image_number = self.end_image_number

        refined_detector_distance: float | None | Unset
        if isinstance(self.refined_detector_distance, Unset):
            refined_detector_distance = UNSET
        else:
            refined_detector_distance = self.refined_detector_distance

        refined_x_beam: float | None | Unset
        if isinstance(self.refined_x_beam, Unset):
            refined_x_beam = UNSET
        else:
            refined_x_beam = self.refined_x_beam

        refined_y_beam: float | None | Unset
        if isinstance(self.refined_y_beam, Unset):
            refined_y_beam = UNSET
        else:
            refined_y_beam = self.refined_y_beam

        rotation_axis_x: float | None | Unset
        if isinstance(self.rotation_axis_x, Unset):
            rotation_axis_x = UNSET
        else:
            rotation_axis_x = self.rotation_axis_x

        rotation_axis_y: float | None | Unset
        if isinstance(self.rotation_axis_y, Unset):
            rotation_axis_y = UNSET
        else:
            rotation_axis_y = self.rotation_axis_y

        rotation_axis_z: float | None | Unset
        if isinstance(self.rotation_axis_z, Unset):
            rotation_axis_z = UNSET
        else:
            rotation_axis_z = self.rotation_axis_z

        beam_vector_x: float | None | Unset
        if isinstance(self.beam_vector_x, Unset):
            beam_vector_x = UNSET
        else:
            beam_vector_x = self.beam_vector_x

        beam_vector_y: float | None | Unset
        if isinstance(self.beam_vector_y, Unset):
            beam_vector_y = UNSET
        else:
            beam_vector_y = self.beam_vector_y

        beam_vector_z: float | None | Unset
        if isinstance(self.beam_vector_z, Unset):
            beam_vector_z = UNSET
        else:
            beam_vector_z = self.beam_vector_z

        record_time_stamp: None | str | Unset
        if isinstance(self.record_time_stamp, Unset):
            record_time_stamp = UNSET
        elif isinstance(self.record_time_stamp, datetime.datetime):
            record_time_stamp = self.record_time_stamp.isoformat()
        else:
            record_time_stamp = self.record_time_stamp

        anomalous: bool | None | Unset
        if isinstance(self.anomalous, Unset):
            anomalous = UNSET
        else:
            anomalous = self.anomalous

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "autoProcIntegrationId": auto_proc_integration_id,
                "cellA": cell_a,
                "cellB": cell_b,
                "cellC": cell_c,
                "cellAlpha": cell_alpha,
                "cellBeta": cell_beta,
                "cellGamma": cell_gamma,
            }
        )
        if start_image_number is not UNSET:
            field_dict["startImageNumber"] = start_image_number
        if end_image_number is not UNSET:
            field_dict["endImageNumber"] = end_image_number
        if refined_detector_distance is not UNSET:
            field_dict["refinedDetectorDistance"] = refined_detector_distance
        if refined_x_beam is not UNSET:
            field_dict["refinedXBeam"] = refined_x_beam
        if refined_y_beam is not UNSET:
            field_dict["refinedYBeam"] = refined_y_beam
        if rotation_axis_x is not UNSET:
            field_dict["rotationAxisX"] = rotation_axis_x
        if rotation_axis_y is not UNSET:
            field_dict["rotationAxisY"] = rotation_axis_y
        if rotation_axis_z is not UNSET:
            field_dict["rotationAxisZ"] = rotation_axis_z
        if beam_vector_x is not UNSET:
            field_dict["beamVectorX"] = beam_vector_x
        if beam_vector_y is not UNSET:
            field_dict["beamVectorY"] = beam_vector_y
        if beam_vector_z is not UNSET:
            field_dict["beamVectorZ"] = beam_vector_z
        if record_time_stamp is not UNSET:
            field_dict["recordTimeStamp"] = record_time_stamp
        if anomalous is not UNSET:
            field_dict["anomalous"] = anomalous

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        auto_proc_integration_id = d.pop("autoProcIntegrationId")

        def _parse_cell_a(data: object) -> float | None:
            if data is None:
                return data
            return cast(float | None, data)

        cell_a = _parse_cell_a(d.pop("cellA"))

        def _parse_cell_b(data: object) -> float | None:
            if data is None:
                return data
            return cast(float | None, data)

        cell_b = _parse_cell_b(d.pop("cellB"))

        def _parse_cell_c(data: object) -> float | None:
            if data is None:
                return data
            return cast(float | None, data)

        cell_c = _parse_cell_c(d.pop("cellC"))

        def _parse_cell_alpha(data: object) -> float | None:
            if data is None:
                return data
            return cast(float | None, data)

        cell_alpha = _parse_cell_alpha(d.pop("cellAlpha"))

        def _parse_cell_beta(data: object) -> float | None:
            if data is None:
                return data
            return cast(float | None, data)

        cell_beta = _parse_cell_beta(d.pop("cellBeta"))

        def _parse_cell_gamma(data: object) -> float | None:
            if data is None:
                return data
            return cast(float | None, data)

        cell_gamma = _parse_cell_gamma(d.pop("cellGamma"))

        def _parse_start_image_number(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        start_image_number = _parse_start_image_number(d.pop("startImageNumber", UNSET))

        def _parse_end_image_number(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        end_image_number = _parse_end_image_number(d.pop("endImageNumber", UNSET))

        def _parse_refined_detector_distance(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        refined_detector_distance = _parse_refined_detector_distance(d.pop("refinedDetectorDistance", UNSET))

        def _parse_refined_x_beam(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        refined_x_beam = _parse_refined_x_beam(d.pop("refinedXBeam", UNSET))

        def _parse_refined_y_beam(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        refined_y_beam = _parse_refined_y_beam(d.pop("refinedYBeam", UNSET))

        def _parse_rotation_axis_x(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        rotation_axis_x = _parse_rotation_axis_x(d.pop("rotationAxisX", UNSET))

        def _parse_rotation_axis_y(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        rotation_axis_y = _parse_rotation_axis_y(d.pop("rotationAxisY", UNSET))

        def _parse_rotation_axis_z(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        rotation_axis_z = _parse_rotation_axis_z(d.pop("rotationAxisZ", UNSET))

        def _parse_beam_vector_x(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        beam_vector_x = _parse_beam_vector_x(d.pop("beamVectorX", UNSET))

        def _parse_beam_vector_y(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        beam_vector_y = _parse_beam_vector_y(d.pop("beamVectorY", UNSET))

        def _parse_beam_vector_z(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        beam_vector_z = _parse_beam_vector_z(d.pop("beamVectorZ", UNSET))

        def _parse_record_time_stamp(data: object) -> datetime.datetime | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                record_time_stamp_type_0 = datetime.datetime.fromisoformat(data)

                return record_time_stamp_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(datetime.datetime | None | Unset, data)

        record_time_stamp = _parse_record_time_stamp(d.pop("recordTimeStamp", UNSET))

        def _parse_anomalous(data: object) -> bool | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(bool | None | Unset, data)

        anomalous = _parse_anomalous(d.pop("anomalous", UNSET))

        auto_proc_integration_out = cls(
            auto_proc_integration_id=auto_proc_integration_id,
            cell_a=cell_a,
            cell_b=cell_b,
            cell_c=cell_c,
            cell_alpha=cell_alpha,
            cell_beta=cell_beta,
            cell_gamma=cell_gamma,
            start_image_number=start_image_number,
            end_image_number=end_image_number,
            refined_detector_distance=refined_detector_distance,
            refined_x_beam=refined_x_beam,
            refined_y_beam=refined_y_beam,
            rotation_axis_x=rotation_axis_x,
            rotation_axis_y=rotation_axis_y,
            rotation_axis_z=rotation_axis_z,
            beam_vector_x=beam_vector_x,
            beam_vector_y=beam_vector_y,
            beam_vector_z=beam_vector_z,
            record_time_stamp=record_time_stamp,
            anomalous=anomalous,
        )

        auto_proc_integration_out.additional_properties = d
        return auto_proc_integration_out

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

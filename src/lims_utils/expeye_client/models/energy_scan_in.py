from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="EnergyScanIn")


@_attrs_define
class EnergyScanIn:
    """
    Attributes:
        fluorescence_detector (None | str | Unset):
        scan_file_full_path (None | str | Unset):
        jpeg_chooch_file_full_path (None | str | Unset):
        element (None | str | Unset):
        start_energy (float | None | Unset):
        end_energy (float | None | Unset):
        transmission_factor (float | None | Unset):
        exposure_time (float | None | Unset):
        axis_postion (float | None | Unset):
        synchrotron_current (float | None | Unset):
        temperature (float | None | Unset):
        peak_energy (float | None | Unset):
        peak_f_prime (float | None | Unset):
        peak_f_double_prime (float | None | Unset):
        inflection_energy (float | None | Unset):
        inflection_f_prime (float | None | Unset):
        inflection_f_double_prime (float | None | Unset):
        xray_dose (float | None | Unset):
        start_time (datetime.datetime | None | Unset):
        end_time (datetime.datetime | None | Unset):
        edge_energy (None | str | Unset):
        beam_size_vertical (float | None | Unset):
        beam_size_horizontal (float | None | Unset):
        comments (None | str | Unset):
        sample_id (int | None | Unset):
    """

    fluorescence_detector: None | str | Unset = UNSET
    scan_file_full_path: None | str | Unset = UNSET
    jpeg_chooch_file_full_path: None | str | Unset = UNSET
    element: None | str | Unset = UNSET
    start_energy: float | None | Unset = UNSET
    end_energy: float | None | Unset = UNSET
    transmission_factor: float | None | Unset = UNSET
    exposure_time: float | None | Unset = UNSET
    axis_postion: float | None | Unset = UNSET
    synchrotron_current: float | None | Unset = UNSET
    temperature: float | None | Unset = UNSET
    peak_energy: float | None | Unset = UNSET
    peak_f_prime: float | None | Unset = UNSET
    peak_f_double_prime: float | None | Unset = UNSET
    inflection_energy: float | None | Unset = UNSET
    inflection_f_prime: float | None | Unset = UNSET
    inflection_f_double_prime: float | None | Unset = UNSET
    xray_dose: float | None | Unset = UNSET
    start_time: datetime.datetime | None | Unset = UNSET
    end_time: datetime.datetime | None | Unset = UNSET
    edge_energy: None | str | Unset = UNSET
    beam_size_vertical: float | None | Unset = UNSET
    beam_size_horizontal: float | None | Unset = UNSET
    comments: None | str | Unset = UNSET
    sample_id: int | None | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        fluorescence_detector: None | str | Unset
        if isinstance(self.fluorescence_detector, Unset):
            fluorescence_detector = UNSET
        else:
            fluorescence_detector = self.fluorescence_detector

        scan_file_full_path: None | str | Unset
        if isinstance(self.scan_file_full_path, Unset):
            scan_file_full_path = UNSET
        else:
            scan_file_full_path = self.scan_file_full_path

        jpeg_chooch_file_full_path: None | str | Unset
        if isinstance(self.jpeg_chooch_file_full_path, Unset):
            jpeg_chooch_file_full_path = UNSET
        else:
            jpeg_chooch_file_full_path = self.jpeg_chooch_file_full_path

        element: None | str | Unset
        if isinstance(self.element, Unset):
            element = UNSET
        else:
            element = self.element

        start_energy: float | None | Unset
        if isinstance(self.start_energy, Unset):
            start_energy = UNSET
        else:
            start_energy = self.start_energy

        end_energy: float | None | Unset
        if isinstance(self.end_energy, Unset):
            end_energy = UNSET
        else:
            end_energy = self.end_energy

        transmission_factor: float | None | Unset
        if isinstance(self.transmission_factor, Unset):
            transmission_factor = UNSET
        else:
            transmission_factor = self.transmission_factor

        exposure_time: float | None | Unset
        if isinstance(self.exposure_time, Unset):
            exposure_time = UNSET
        else:
            exposure_time = self.exposure_time

        axis_postion: float | None | Unset
        if isinstance(self.axis_postion, Unset):
            axis_postion = UNSET
        else:
            axis_postion = self.axis_postion

        synchrotron_current: float | None | Unset
        if isinstance(self.synchrotron_current, Unset):
            synchrotron_current = UNSET
        else:
            synchrotron_current = self.synchrotron_current

        temperature: float | None | Unset
        if isinstance(self.temperature, Unset):
            temperature = UNSET
        else:
            temperature = self.temperature

        peak_energy: float | None | Unset
        if isinstance(self.peak_energy, Unset):
            peak_energy = UNSET
        else:
            peak_energy = self.peak_energy

        peak_f_prime: float | None | Unset
        if isinstance(self.peak_f_prime, Unset):
            peak_f_prime = UNSET
        else:
            peak_f_prime = self.peak_f_prime

        peak_f_double_prime: float | None | Unset
        if isinstance(self.peak_f_double_prime, Unset):
            peak_f_double_prime = UNSET
        else:
            peak_f_double_prime = self.peak_f_double_prime

        inflection_energy: float | None | Unset
        if isinstance(self.inflection_energy, Unset):
            inflection_energy = UNSET
        else:
            inflection_energy = self.inflection_energy

        inflection_f_prime: float | None | Unset
        if isinstance(self.inflection_f_prime, Unset):
            inflection_f_prime = UNSET
        else:
            inflection_f_prime = self.inflection_f_prime

        inflection_f_double_prime: float | None | Unset
        if isinstance(self.inflection_f_double_prime, Unset):
            inflection_f_double_prime = UNSET
        else:
            inflection_f_double_prime = self.inflection_f_double_prime

        xray_dose: float | None | Unset
        if isinstance(self.xray_dose, Unset):
            xray_dose = UNSET
        else:
            xray_dose = self.xray_dose

        start_time: None | str | Unset
        if isinstance(self.start_time, Unset):
            start_time = UNSET
        elif isinstance(self.start_time, datetime.datetime):
            start_time = self.start_time.isoformat()
        else:
            start_time = self.start_time

        end_time: None | str | Unset
        if isinstance(self.end_time, Unset):
            end_time = UNSET
        elif isinstance(self.end_time, datetime.datetime):
            end_time = self.end_time.isoformat()
        else:
            end_time = self.end_time

        edge_energy: None | str | Unset
        if isinstance(self.edge_energy, Unset):
            edge_energy = UNSET
        else:
            edge_energy = self.edge_energy

        beam_size_vertical: float | None | Unset
        if isinstance(self.beam_size_vertical, Unset):
            beam_size_vertical = UNSET
        else:
            beam_size_vertical = self.beam_size_vertical

        beam_size_horizontal: float | None | Unset
        if isinstance(self.beam_size_horizontal, Unset):
            beam_size_horizontal = UNSET
        else:
            beam_size_horizontal = self.beam_size_horizontal

        comments: None | str | Unset
        if isinstance(self.comments, Unset):
            comments = UNSET
        else:
            comments = self.comments

        sample_id: int | None | Unset
        if isinstance(self.sample_id, Unset):
            sample_id = UNSET
        else:
            sample_id = self.sample_id

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if fluorescence_detector is not UNSET:
            field_dict["fluorescenceDetector"] = fluorescence_detector
        if scan_file_full_path is not UNSET:
            field_dict["scanFileFullPath"] = scan_file_full_path
        if jpeg_chooch_file_full_path is not UNSET:
            field_dict["jpegChoochFileFullPath"] = jpeg_chooch_file_full_path
        if element is not UNSET:
            field_dict["element"] = element
        if start_energy is not UNSET:
            field_dict["startEnergy"] = start_energy
        if end_energy is not UNSET:
            field_dict["endEnergy"] = end_energy
        if transmission_factor is not UNSET:
            field_dict["transmissionFactor"] = transmission_factor
        if exposure_time is not UNSET:
            field_dict["exposureTime"] = exposure_time
        if axis_postion is not UNSET:
            field_dict["axisPostion"] = axis_postion
        if synchrotron_current is not UNSET:
            field_dict["synchrotronCurrent"] = synchrotron_current
        if temperature is not UNSET:
            field_dict["temperature"] = temperature
        if peak_energy is not UNSET:
            field_dict["peakEnergy"] = peak_energy
        if peak_f_prime is not UNSET:
            field_dict["peakFPrime"] = peak_f_prime
        if peak_f_double_prime is not UNSET:
            field_dict["peakFDoublePrime"] = peak_f_double_prime
        if inflection_energy is not UNSET:
            field_dict["inflectionEnergy"] = inflection_energy
        if inflection_f_prime is not UNSET:
            field_dict["inflectionFPrime"] = inflection_f_prime
        if inflection_f_double_prime is not UNSET:
            field_dict["inflectionFDoublePrime"] = inflection_f_double_prime
        if xray_dose is not UNSET:
            field_dict["xrayDose"] = xray_dose
        if start_time is not UNSET:
            field_dict["startTime"] = start_time
        if end_time is not UNSET:
            field_dict["endTime"] = end_time
        if edge_energy is not UNSET:
            field_dict["edgeEnergy"] = edge_energy
        if beam_size_vertical is not UNSET:
            field_dict["beamSizeVertical"] = beam_size_vertical
        if beam_size_horizontal is not UNSET:
            field_dict["beamSizeHorizontal"] = beam_size_horizontal
        if comments is not UNSET:
            field_dict["comments"] = comments
        if sample_id is not UNSET:
            field_dict["sampleId"] = sample_id

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)

        def _parse_fluorescence_detector(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        fluorescence_detector = _parse_fluorescence_detector(d.pop("fluorescenceDetector", UNSET))

        def _parse_scan_file_full_path(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        scan_file_full_path = _parse_scan_file_full_path(d.pop("scanFileFullPath", UNSET))

        def _parse_jpeg_chooch_file_full_path(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        jpeg_chooch_file_full_path = _parse_jpeg_chooch_file_full_path(d.pop("jpegChoochFileFullPath", UNSET))

        def _parse_element(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        element = _parse_element(d.pop("element", UNSET))

        def _parse_start_energy(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        start_energy = _parse_start_energy(d.pop("startEnergy", UNSET))

        def _parse_end_energy(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        end_energy = _parse_end_energy(d.pop("endEnergy", UNSET))

        def _parse_transmission_factor(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        transmission_factor = _parse_transmission_factor(d.pop("transmissionFactor", UNSET))

        def _parse_exposure_time(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        exposure_time = _parse_exposure_time(d.pop("exposureTime", UNSET))

        def _parse_axis_postion(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        axis_postion = _parse_axis_postion(d.pop("axisPostion", UNSET))

        def _parse_synchrotron_current(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        synchrotron_current = _parse_synchrotron_current(d.pop("synchrotronCurrent", UNSET))

        def _parse_temperature(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        temperature = _parse_temperature(d.pop("temperature", UNSET))

        def _parse_peak_energy(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        peak_energy = _parse_peak_energy(d.pop("peakEnergy", UNSET))

        def _parse_peak_f_prime(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        peak_f_prime = _parse_peak_f_prime(d.pop("peakFPrime", UNSET))

        def _parse_peak_f_double_prime(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        peak_f_double_prime = _parse_peak_f_double_prime(d.pop("peakFDoublePrime", UNSET))

        def _parse_inflection_energy(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        inflection_energy = _parse_inflection_energy(d.pop("inflectionEnergy", UNSET))

        def _parse_inflection_f_prime(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        inflection_f_prime = _parse_inflection_f_prime(d.pop("inflectionFPrime", UNSET))

        def _parse_inflection_f_double_prime(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        inflection_f_double_prime = _parse_inflection_f_double_prime(d.pop("inflectionFDoublePrime", UNSET))

        def _parse_xray_dose(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        xray_dose = _parse_xray_dose(d.pop("xrayDose", UNSET))

        def _parse_start_time(data: object) -> datetime.datetime | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                start_time_type_0 = datetime.datetime.fromisoformat(data)

                return start_time_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(datetime.datetime | None | Unset, data)

        start_time = _parse_start_time(d.pop("startTime", UNSET))

        def _parse_end_time(data: object) -> datetime.datetime | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                end_time_type_0 = datetime.datetime.fromisoformat(data)

                return end_time_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(datetime.datetime | None | Unset, data)

        end_time = _parse_end_time(d.pop("endTime", UNSET))

        def _parse_edge_energy(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        edge_energy = _parse_edge_energy(d.pop("edgeEnergy", UNSET))

        def _parse_beam_size_vertical(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        beam_size_vertical = _parse_beam_size_vertical(d.pop("beamSizeVertical", UNSET))

        def _parse_beam_size_horizontal(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        beam_size_horizontal = _parse_beam_size_horizontal(d.pop("beamSizeHorizontal", UNSET))

        def _parse_comments(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        comments = _parse_comments(d.pop("comments", UNSET))

        def _parse_sample_id(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        sample_id = _parse_sample_id(d.pop("sampleId", UNSET))

        energy_scan_in = cls(
            fluorescence_detector=fluorescence_detector,
            scan_file_full_path=scan_file_full_path,
            jpeg_chooch_file_full_path=jpeg_chooch_file_full_path,
            element=element,
            start_energy=start_energy,
            end_energy=end_energy,
            transmission_factor=transmission_factor,
            exposure_time=exposure_time,
            axis_postion=axis_postion,
            synchrotron_current=synchrotron_current,
            temperature=temperature,
            peak_energy=peak_energy,
            peak_f_prime=peak_f_prime,
            peak_f_double_prime=peak_f_double_prime,
            inflection_energy=inflection_energy,
            inflection_f_prime=inflection_f_prime,
            inflection_f_double_prime=inflection_f_double_prime,
            xray_dose=xray_dose,
            start_time=start_time,
            end_time=end_time,
            edge_energy=edge_energy,
            beam_size_vertical=beam_size_vertical,
            beam_size_horizontal=beam_size_horizontal,
            comments=comments,
            sample_id=sample_id,
        )

        energy_scan_in.additional_properties = d
        return energy_scan_in

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

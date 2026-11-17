from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="FluorescenceSpectrumOptional")


@_attrs_define
class FluorescenceSpectrumOptional:
    """
    Attributes:
        start_time (datetime.datetime | None | Unset):
        end_time (datetime.datetime | None | Unset):
        sample_id (int | None | Unset):
        jpeg_scan_file_full_path (None | str | Unset):
        filename (None | str | Unset):
        exposure_time (float | None | Unset):
        axis_position (float | None | Unset):
        beam_transmission (float | None | Unset):
        annotated_pymca_xfe_spectrum (None | str | Unset):
        fitted_data_file_full_path (None | str | Unset):
        scan_file_full_path (None | str | Unset):
        energy (float | None | Unset):
        beam_size_vertical (float | None | Unset):
        beam_size_horizontal (float | None | Unset):
        crystal_class (None | str | Unset):
        comments (None | str | Unset):
        bl_sub_sample_id (int | None | Unset):
        flux (float | None | Unset):
        flux_end (float | None | Unset):
        working_directory (None | str | Unset):
        session_id (int | None | Unset):
    """

    start_time: datetime.datetime | None | Unset = UNSET
    end_time: datetime.datetime | None | Unset = UNSET
    sample_id: int | None | Unset = UNSET
    jpeg_scan_file_full_path: None | str | Unset = UNSET
    filename: None | str | Unset = UNSET
    exposure_time: float | None | Unset = UNSET
    axis_position: float | None | Unset = UNSET
    beam_transmission: float | None | Unset = UNSET
    annotated_pymca_xfe_spectrum: None | str | Unset = UNSET
    fitted_data_file_full_path: None | str | Unset = UNSET
    scan_file_full_path: None | str | Unset = UNSET
    energy: float | None | Unset = UNSET
    beam_size_vertical: float | None | Unset = UNSET
    beam_size_horizontal: float | None | Unset = UNSET
    crystal_class: None | str | Unset = UNSET
    comments: None | str | Unset = UNSET
    bl_sub_sample_id: int | None | Unset = UNSET
    flux: float | None | Unset = UNSET
    flux_end: float | None | Unset = UNSET
    working_directory: None | str | Unset = UNSET
    session_id: int | None | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
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

        sample_id: int | None | Unset
        if isinstance(self.sample_id, Unset):
            sample_id = UNSET
        else:
            sample_id = self.sample_id

        jpeg_scan_file_full_path: None | str | Unset
        if isinstance(self.jpeg_scan_file_full_path, Unset):
            jpeg_scan_file_full_path = UNSET
        else:
            jpeg_scan_file_full_path = self.jpeg_scan_file_full_path

        filename: None | str | Unset
        if isinstance(self.filename, Unset):
            filename = UNSET
        else:
            filename = self.filename

        exposure_time: float | None | Unset
        if isinstance(self.exposure_time, Unset):
            exposure_time = UNSET
        else:
            exposure_time = self.exposure_time

        axis_position: float | None | Unset
        if isinstance(self.axis_position, Unset):
            axis_position = UNSET
        else:
            axis_position = self.axis_position

        beam_transmission: float | None | Unset
        if isinstance(self.beam_transmission, Unset):
            beam_transmission = UNSET
        else:
            beam_transmission = self.beam_transmission

        annotated_pymca_xfe_spectrum: None | str | Unset
        if isinstance(self.annotated_pymca_xfe_spectrum, Unset):
            annotated_pymca_xfe_spectrum = UNSET
        else:
            annotated_pymca_xfe_spectrum = self.annotated_pymca_xfe_spectrum

        fitted_data_file_full_path: None | str | Unset
        if isinstance(self.fitted_data_file_full_path, Unset):
            fitted_data_file_full_path = UNSET
        else:
            fitted_data_file_full_path = self.fitted_data_file_full_path

        scan_file_full_path: None | str | Unset
        if isinstance(self.scan_file_full_path, Unset):
            scan_file_full_path = UNSET
        else:
            scan_file_full_path = self.scan_file_full_path

        energy: float | None | Unset
        if isinstance(self.energy, Unset):
            energy = UNSET
        else:
            energy = self.energy

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

        crystal_class: None | str | Unset
        if isinstance(self.crystal_class, Unset):
            crystal_class = UNSET
        else:
            crystal_class = self.crystal_class

        comments: None | str | Unset
        if isinstance(self.comments, Unset):
            comments = UNSET
        else:
            comments = self.comments

        bl_sub_sample_id: int | None | Unset
        if isinstance(self.bl_sub_sample_id, Unset):
            bl_sub_sample_id = UNSET
        else:
            bl_sub_sample_id = self.bl_sub_sample_id

        flux: float | None | Unset
        if isinstance(self.flux, Unset):
            flux = UNSET
        else:
            flux = self.flux

        flux_end: float | None | Unset
        if isinstance(self.flux_end, Unset):
            flux_end = UNSET
        else:
            flux_end = self.flux_end

        working_directory: None | str | Unset
        if isinstance(self.working_directory, Unset):
            working_directory = UNSET
        else:
            working_directory = self.working_directory

        session_id: int | None | Unset
        if isinstance(self.session_id, Unset):
            session_id = UNSET
        else:
            session_id = self.session_id

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if start_time is not UNSET:
            field_dict["startTime"] = start_time
        if end_time is not UNSET:
            field_dict["endTime"] = end_time
        if sample_id is not UNSET:
            field_dict["sampleId"] = sample_id
        if jpeg_scan_file_full_path is not UNSET:
            field_dict["jpegScanFileFullPath"] = jpeg_scan_file_full_path
        if filename is not UNSET:
            field_dict["filename"] = filename
        if exposure_time is not UNSET:
            field_dict["exposureTime"] = exposure_time
        if axis_position is not UNSET:
            field_dict["axisPosition"] = axis_position
        if beam_transmission is not UNSET:
            field_dict["beamTransmission"] = beam_transmission
        if annotated_pymca_xfe_spectrum is not UNSET:
            field_dict["annotatedPymcaXfeSpectrum"] = annotated_pymca_xfe_spectrum
        if fitted_data_file_full_path is not UNSET:
            field_dict["fittedDataFileFullPath"] = fitted_data_file_full_path
        if scan_file_full_path is not UNSET:
            field_dict["scanFileFullPath"] = scan_file_full_path
        if energy is not UNSET:
            field_dict["energy"] = energy
        if beam_size_vertical is not UNSET:
            field_dict["beamSizeVertical"] = beam_size_vertical
        if beam_size_horizontal is not UNSET:
            field_dict["beamSizeHorizontal"] = beam_size_horizontal
        if crystal_class is not UNSET:
            field_dict["crystalClass"] = crystal_class
        if comments is not UNSET:
            field_dict["comments"] = comments
        if bl_sub_sample_id is not UNSET:
            field_dict["blSubSampleId"] = bl_sub_sample_id
        if flux is not UNSET:
            field_dict["flux"] = flux
        if flux_end is not UNSET:
            field_dict["fluxEnd"] = flux_end
        if working_directory is not UNSET:
            field_dict["workingDirectory"] = working_directory
        if session_id is not UNSET:
            field_dict["sessionId"] = session_id

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)

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

        def _parse_sample_id(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        sample_id = _parse_sample_id(d.pop("sampleId", UNSET))

        def _parse_jpeg_scan_file_full_path(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        jpeg_scan_file_full_path = _parse_jpeg_scan_file_full_path(d.pop("jpegScanFileFullPath", UNSET))

        def _parse_filename(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        filename = _parse_filename(d.pop("filename", UNSET))

        def _parse_exposure_time(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        exposure_time = _parse_exposure_time(d.pop("exposureTime", UNSET))

        def _parse_axis_position(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        axis_position = _parse_axis_position(d.pop("axisPosition", UNSET))

        def _parse_beam_transmission(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        beam_transmission = _parse_beam_transmission(d.pop("beamTransmission", UNSET))

        def _parse_annotated_pymca_xfe_spectrum(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        annotated_pymca_xfe_spectrum = _parse_annotated_pymca_xfe_spectrum(d.pop("annotatedPymcaXfeSpectrum", UNSET))

        def _parse_fitted_data_file_full_path(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        fitted_data_file_full_path = _parse_fitted_data_file_full_path(d.pop("fittedDataFileFullPath", UNSET))

        def _parse_scan_file_full_path(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        scan_file_full_path = _parse_scan_file_full_path(d.pop("scanFileFullPath", UNSET))

        def _parse_energy(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        energy = _parse_energy(d.pop("energy", UNSET))

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

        def _parse_crystal_class(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        crystal_class = _parse_crystal_class(d.pop("crystalClass", UNSET))

        def _parse_comments(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        comments = _parse_comments(d.pop("comments", UNSET))

        def _parse_bl_sub_sample_id(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        bl_sub_sample_id = _parse_bl_sub_sample_id(d.pop("blSubSampleId", UNSET))

        def _parse_flux(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        flux = _parse_flux(d.pop("flux", UNSET))

        def _parse_flux_end(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        flux_end = _parse_flux_end(d.pop("fluxEnd", UNSET))

        def _parse_working_directory(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        working_directory = _parse_working_directory(d.pop("workingDirectory", UNSET))

        def _parse_session_id(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        session_id = _parse_session_id(d.pop("sessionId", UNSET))

        fluorescence_spectrum_optional = cls(
            start_time=start_time,
            end_time=end_time,
            sample_id=sample_id,
            jpeg_scan_file_full_path=jpeg_scan_file_full_path,
            filename=filename,
            exposure_time=exposure_time,
            axis_position=axis_position,
            beam_transmission=beam_transmission,
            annotated_pymca_xfe_spectrum=annotated_pymca_xfe_spectrum,
            fitted_data_file_full_path=fitted_data_file_full_path,
            scan_file_full_path=scan_file_full_path,
            energy=energy,
            beam_size_vertical=beam_size_vertical,
            beam_size_horizontal=beam_size_horizontal,
            crystal_class=crystal_class,
            comments=comments,
            bl_sub_sample_id=bl_sub_sample_id,
            flux=flux,
            flux_end=flux_end,
            working_directory=working_directory,
            session_id=session_id,
        )

        fluorescence_spectrum_optional.additional_properties = d
        return fluorescence_spectrum_optional

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

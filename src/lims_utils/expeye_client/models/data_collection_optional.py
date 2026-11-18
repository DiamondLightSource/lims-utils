from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.rotation_axis_enum import RotationAxisEnum
from ..types import UNSET, Unset

T = TypeVar("T", bound="DataCollectionOptional")


@_attrs_define
class DataCollectionOptional:
    """
    Attributes:
        comments (None | str | Unset):
        start_time (datetime.datetime | None | Unset): Start time of the dataCollection
        pixel_size_on_image (float | None | Unset): Pixel size on image, calculated from magnification
        voltage (float | None | Unset): Unit: kV
        image_size_x (int | None | Unset): Image size in x, in case crop has been used.
        image_size_y (int | None | Unset): Image size in y, in case crop has been used.
        experimenttype (None | str | Unset):
        end_time (datetime.datetime | None | Unset): End time of the dataCollection
        run_status (None | str | Unset):
        axis_start (float | None | Unset):
        axis_end (float | None | Unset):
        axis_range (float | None | Unset):
        overlap (float | None | Unset):
        number_of_images (int | None | Unset):
        start_image_number (int | None | Unset):
        number_of_passes (int | None | Unset):
        exposure_time (float | None | Unset):
        image_directory (None | str | Unset): The directory where files reside - should end with a slash
        image_prefix (None | str | Unset):
        image_suffix (None | str | Unset):
        image_container_sub_path (None | str | Unset): Internal path of a HDF5 file pointing to the data
                    for this data collection
        file_template (None | str | Unset):
        wavelength (float | None | Unset):
        resolution (float | None | Unset):
        detector_distance (float | None | Unset):
        x_beam (float | None | Unset):
        y_beam (float | None | Unset):
        printable_for_report (int | None | Unset):
        slit_gap_vertical (float | None | Unset):
        slit_gap_horizontal (float | None | Unset):
        transmission (float | None | Unset):
        synchrotron_mode (None | str | Unset):
        xtal_snapshot_full_path_1 (None | str | Unset):
        xtal_snapshot_full_path_2 (None | str | Unset):
        xtal_snapshot_full_path_3 (None | str | Unset):
        xtal_snapshot_full_path_4 (None | str | Unset):
        rotation_axis (None | RotationAxisEnum | Unset):
        phi_start (float | None | Unset):
        kappa_start (float | None | Unset):
        omega_start (float | None | Unset):
        chi_start (float | None | Unset):
        detector_2_theta (float | None | Unset):
        detector_mode (None | str | Unset):
        sample_id (int | None | Unset):
        undulator_gap_1 (float | None | Unset):
        undulator_gap_2 (float | None | Unset):
        undulator_gap_3 (float | None | Unset):
        beam_size_at_sample_x (float | None | Unset):
        beam_size_at_sample_y (float | None | Unset):
        centering_method (None | str | Unset):
        detector_id (int | None | Unset):
        flux (float | None | Unset):
        bl_sub_sample_id (int | None | Unset):
        flux_end (float | None | Unset):
        dat_full_path (None | str | Unset):
        magnification (float | None | Unset):
        total_absorbed_dose (float | None | Unset):
        binning (int | None | Unset):
        particle_diameter (float | None | Unset):
        min_resolution (float | None | Unset):
        min_defocus (float | None | Unset):
        max_defocus (float | None | Unset):
        c2aperture (float | None | Unset):
        total_exposed_dose (float | None | Unset):
        phase_plate (int | None | Unset):
        data_collection_plan_id (int | None | Unset):
        data_collection_number (int | None | Unset):
        data_collection_group_id (int | None | Unset):
    """

    comments: None | str | Unset = UNSET
    start_time: datetime.datetime | None | Unset = UNSET
    pixel_size_on_image: float | None | Unset = UNSET
    voltage: float | None | Unset = UNSET
    image_size_x: int | None | Unset = UNSET
    image_size_y: int | None | Unset = UNSET
    experimenttype: None | str | Unset = UNSET
    end_time: datetime.datetime | None | Unset = UNSET
    run_status: None | str | Unset = UNSET
    axis_start: float | None | Unset = UNSET
    axis_end: float | None | Unset = UNSET
    axis_range: float | None | Unset = UNSET
    overlap: float | None | Unset = UNSET
    number_of_images: int | None | Unset = UNSET
    start_image_number: int | None | Unset = UNSET
    number_of_passes: int | None | Unset = UNSET
    exposure_time: float | None | Unset = UNSET
    image_directory: None | str | Unset = UNSET
    image_prefix: None | str | Unset = UNSET
    image_suffix: None | str | Unset = UNSET
    image_container_sub_path: None | str | Unset = UNSET
    file_template: None | str | Unset = UNSET
    wavelength: float | None | Unset = UNSET
    resolution: float | None | Unset = UNSET
    detector_distance: float | None | Unset = UNSET
    x_beam: float | None | Unset = UNSET
    y_beam: float | None | Unset = UNSET
    printable_for_report: int | None | Unset = UNSET
    slit_gap_vertical: float | None | Unset = UNSET
    slit_gap_horizontal: float | None | Unset = UNSET
    transmission: float | None | Unset = UNSET
    synchrotron_mode: None | str | Unset = UNSET
    xtal_snapshot_full_path_1: None | str | Unset = UNSET
    xtal_snapshot_full_path_2: None | str | Unset = UNSET
    xtal_snapshot_full_path_3: None | str | Unset = UNSET
    xtal_snapshot_full_path_4: None | str | Unset = UNSET
    rotation_axis: None | RotationAxisEnum | Unset = UNSET
    phi_start: float | None | Unset = UNSET
    kappa_start: float | None | Unset = UNSET
    omega_start: float | None | Unset = UNSET
    chi_start: float | None | Unset = UNSET
    detector_2_theta: float | None | Unset = UNSET
    detector_mode: None | str | Unset = UNSET
    sample_id: int | None | Unset = UNSET
    undulator_gap_1: float | None | Unset = UNSET
    undulator_gap_2: float | None | Unset = UNSET
    undulator_gap_3: float | None | Unset = UNSET
    beam_size_at_sample_x: float | None | Unset = UNSET
    beam_size_at_sample_y: float | None | Unset = UNSET
    centering_method: None | str | Unset = UNSET
    detector_id: int | None | Unset = UNSET
    flux: float | None | Unset = UNSET
    bl_sub_sample_id: int | None | Unset = UNSET
    flux_end: float | None | Unset = UNSET
    dat_full_path: None | str | Unset = UNSET
    magnification: float | None | Unset = UNSET
    total_absorbed_dose: float | None | Unset = UNSET
    binning: int | None | Unset = UNSET
    particle_diameter: float | None | Unset = UNSET
    min_resolution: float | None | Unset = UNSET
    min_defocus: float | None | Unset = UNSET
    max_defocus: float | None | Unset = UNSET
    c2aperture: float | None | Unset = UNSET
    total_exposed_dose: float | None | Unset = UNSET
    phase_plate: int | None | Unset = UNSET
    data_collection_plan_id: int | None | Unset = UNSET
    data_collection_number: int | None | Unset = UNSET
    data_collection_group_id: int | None | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        comments: None | str | Unset
        if isinstance(self.comments, Unset):
            comments = UNSET
        else:
            comments = self.comments

        start_time: None | str | Unset
        if isinstance(self.start_time, Unset):
            start_time = UNSET
        elif isinstance(self.start_time, datetime.datetime):
            start_time = self.start_time.isoformat()
        else:
            start_time = self.start_time

        pixel_size_on_image: float | None | Unset
        if isinstance(self.pixel_size_on_image, Unset):
            pixel_size_on_image = UNSET
        else:
            pixel_size_on_image = self.pixel_size_on_image

        voltage: float | None | Unset
        if isinstance(self.voltage, Unset):
            voltage = UNSET
        else:
            voltage = self.voltage

        image_size_x: int | None | Unset
        if isinstance(self.image_size_x, Unset):
            image_size_x = UNSET
        else:
            image_size_x = self.image_size_x

        image_size_y: int | None | Unset
        if isinstance(self.image_size_y, Unset):
            image_size_y = UNSET
        else:
            image_size_y = self.image_size_y

        experimenttype: None | str | Unset
        if isinstance(self.experimenttype, Unset):
            experimenttype = UNSET
        else:
            experimenttype = self.experimenttype

        end_time: None | str | Unset
        if isinstance(self.end_time, Unset):
            end_time = UNSET
        elif isinstance(self.end_time, datetime.datetime):
            end_time = self.end_time.isoformat()
        else:
            end_time = self.end_time

        run_status: None | str | Unset
        if isinstance(self.run_status, Unset):
            run_status = UNSET
        else:
            run_status = self.run_status

        axis_start: float | None | Unset
        if isinstance(self.axis_start, Unset):
            axis_start = UNSET
        else:
            axis_start = self.axis_start

        axis_end: float | None | Unset
        if isinstance(self.axis_end, Unset):
            axis_end = UNSET
        else:
            axis_end = self.axis_end

        axis_range: float | None | Unset
        if isinstance(self.axis_range, Unset):
            axis_range = UNSET
        else:
            axis_range = self.axis_range

        overlap: float | None | Unset
        if isinstance(self.overlap, Unset):
            overlap = UNSET
        else:
            overlap = self.overlap

        number_of_images: int | None | Unset
        if isinstance(self.number_of_images, Unset):
            number_of_images = UNSET
        else:
            number_of_images = self.number_of_images

        start_image_number: int | None | Unset
        if isinstance(self.start_image_number, Unset):
            start_image_number = UNSET
        else:
            start_image_number = self.start_image_number

        number_of_passes: int | None | Unset
        if isinstance(self.number_of_passes, Unset):
            number_of_passes = UNSET
        else:
            number_of_passes = self.number_of_passes

        exposure_time: float | None | Unset
        if isinstance(self.exposure_time, Unset):
            exposure_time = UNSET
        else:
            exposure_time = self.exposure_time

        image_directory: None | str | Unset
        if isinstance(self.image_directory, Unset):
            image_directory = UNSET
        else:
            image_directory = self.image_directory

        image_prefix: None | str | Unset
        if isinstance(self.image_prefix, Unset):
            image_prefix = UNSET
        else:
            image_prefix = self.image_prefix

        image_suffix: None | str | Unset
        if isinstance(self.image_suffix, Unset):
            image_suffix = UNSET
        else:
            image_suffix = self.image_suffix

        image_container_sub_path: None | str | Unset
        if isinstance(self.image_container_sub_path, Unset):
            image_container_sub_path = UNSET
        else:
            image_container_sub_path = self.image_container_sub_path

        file_template: None | str | Unset
        if isinstance(self.file_template, Unset):
            file_template = UNSET
        else:
            file_template = self.file_template

        wavelength: float | None | Unset
        if isinstance(self.wavelength, Unset):
            wavelength = UNSET
        else:
            wavelength = self.wavelength

        resolution: float | None | Unset
        if isinstance(self.resolution, Unset):
            resolution = UNSET
        else:
            resolution = self.resolution

        detector_distance: float | None | Unset
        if isinstance(self.detector_distance, Unset):
            detector_distance = UNSET
        else:
            detector_distance = self.detector_distance

        x_beam: float | None | Unset
        if isinstance(self.x_beam, Unset):
            x_beam = UNSET
        else:
            x_beam = self.x_beam

        y_beam: float | None | Unset
        if isinstance(self.y_beam, Unset):
            y_beam = UNSET
        else:
            y_beam = self.y_beam

        printable_for_report: int | None | Unset
        if isinstance(self.printable_for_report, Unset):
            printable_for_report = UNSET
        else:
            printable_for_report = self.printable_for_report

        slit_gap_vertical: float | None | Unset
        if isinstance(self.slit_gap_vertical, Unset):
            slit_gap_vertical = UNSET
        else:
            slit_gap_vertical = self.slit_gap_vertical

        slit_gap_horizontal: float | None | Unset
        if isinstance(self.slit_gap_horizontal, Unset):
            slit_gap_horizontal = UNSET
        else:
            slit_gap_horizontal = self.slit_gap_horizontal

        transmission: float | None | Unset
        if isinstance(self.transmission, Unset):
            transmission = UNSET
        else:
            transmission = self.transmission

        synchrotron_mode: None | str | Unset
        if isinstance(self.synchrotron_mode, Unset):
            synchrotron_mode = UNSET
        else:
            synchrotron_mode = self.synchrotron_mode

        xtal_snapshot_full_path_1: None | str | Unset
        if isinstance(self.xtal_snapshot_full_path_1, Unset):
            xtal_snapshot_full_path_1 = UNSET
        else:
            xtal_snapshot_full_path_1 = self.xtal_snapshot_full_path_1

        xtal_snapshot_full_path_2: None | str | Unset
        if isinstance(self.xtal_snapshot_full_path_2, Unset):
            xtal_snapshot_full_path_2 = UNSET
        else:
            xtal_snapshot_full_path_2 = self.xtal_snapshot_full_path_2

        xtal_snapshot_full_path_3: None | str | Unset
        if isinstance(self.xtal_snapshot_full_path_3, Unset):
            xtal_snapshot_full_path_3 = UNSET
        else:
            xtal_snapshot_full_path_3 = self.xtal_snapshot_full_path_3

        xtal_snapshot_full_path_4: None | str | Unset
        if isinstance(self.xtal_snapshot_full_path_4, Unset):
            xtal_snapshot_full_path_4 = UNSET
        else:
            xtal_snapshot_full_path_4 = self.xtal_snapshot_full_path_4

        rotation_axis: None | str | Unset
        if isinstance(self.rotation_axis, Unset):
            rotation_axis = UNSET
        elif isinstance(self.rotation_axis, RotationAxisEnum):
            rotation_axis = self.rotation_axis.value
        else:
            rotation_axis = self.rotation_axis

        phi_start: float | None | Unset
        if isinstance(self.phi_start, Unset):
            phi_start = UNSET
        else:
            phi_start = self.phi_start

        kappa_start: float | None | Unset
        if isinstance(self.kappa_start, Unset):
            kappa_start = UNSET
        else:
            kappa_start = self.kappa_start

        omega_start: float | None | Unset
        if isinstance(self.omega_start, Unset):
            omega_start = UNSET
        else:
            omega_start = self.omega_start

        chi_start: float | None | Unset
        if isinstance(self.chi_start, Unset):
            chi_start = UNSET
        else:
            chi_start = self.chi_start

        detector_2_theta: float | None | Unset
        if isinstance(self.detector_2_theta, Unset):
            detector_2_theta = UNSET
        else:
            detector_2_theta = self.detector_2_theta

        detector_mode: None | str | Unset
        if isinstance(self.detector_mode, Unset):
            detector_mode = UNSET
        else:
            detector_mode = self.detector_mode

        sample_id: int | None | Unset
        if isinstance(self.sample_id, Unset):
            sample_id = UNSET
        else:
            sample_id = self.sample_id

        undulator_gap_1: float | None | Unset
        if isinstance(self.undulator_gap_1, Unset):
            undulator_gap_1 = UNSET
        else:
            undulator_gap_1 = self.undulator_gap_1

        undulator_gap_2: float | None | Unset
        if isinstance(self.undulator_gap_2, Unset):
            undulator_gap_2 = UNSET
        else:
            undulator_gap_2 = self.undulator_gap_2

        undulator_gap_3: float | None | Unset
        if isinstance(self.undulator_gap_3, Unset):
            undulator_gap_3 = UNSET
        else:
            undulator_gap_3 = self.undulator_gap_3

        beam_size_at_sample_x: float | None | Unset
        if isinstance(self.beam_size_at_sample_x, Unset):
            beam_size_at_sample_x = UNSET
        else:
            beam_size_at_sample_x = self.beam_size_at_sample_x

        beam_size_at_sample_y: float | None | Unset
        if isinstance(self.beam_size_at_sample_y, Unset):
            beam_size_at_sample_y = UNSET
        else:
            beam_size_at_sample_y = self.beam_size_at_sample_y

        centering_method: None | str | Unset
        if isinstance(self.centering_method, Unset):
            centering_method = UNSET
        else:
            centering_method = self.centering_method

        detector_id: int | None | Unset
        if isinstance(self.detector_id, Unset):
            detector_id = UNSET
        else:
            detector_id = self.detector_id

        flux: float | None | Unset
        if isinstance(self.flux, Unset):
            flux = UNSET
        else:
            flux = self.flux

        bl_sub_sample_id: int | None | Unset
        if isinstance(self.bl_sub_sample_id, Unset):
            bl_sub_sample_id = UNSET
        else:
            bl_sub_sample_id = self.bl_sub_sample_id

        flux_end: float | None | Unset
        if isinstance(self.flux_end, Unset):
            flux_end = UNSET
        else:
            flux_end = self.flux_end

        dat_full_path: None | str | Unset
        if isinstance(self.dat_full_path, Unset):
            dat_full_path = UNSET
        else:
            dat_full_path = self.dat_full_path

        magnification: float | None | Unset
        if isinstance(self.magnification, Unset):
            magnification = UNSET
        else:
            magnification = self.magnification

        total_absorbed_dose: float | None | Unset
        if isinstance(self.total_absorbed_dose, Unset):
            total_absorbed_dose = UNSET
        else:
            total_absorbed_dose = self.total_absorbed_dose

        binning: int | None | Unset
        if isinstance(self.binning, Unset):
            binning = UNSET
        else:
            binning = self.binning

        particle_diameter: float | None | Unset
        if isinstance(self.particle_diameter, Unset):
            particle_diameter = UNSET
        else:
            particle_diameter = self.particle_diameter

        min_resolution: float | None | Unset
        if isinstance(self.min_resolution, Unset):
            min_resolution = UNSET
        else:
            min_resolution = self.min_resolution

        min_defocus: float | None | Unset
        if isinstance(self.min_defocus, Unset):
            min_defocus = UNSET
        else:
            min_defocus = self.min_defocus

        max_defocus: float | None | Unset
        if isinstance(self.max_defocus, Unset):
            max_defocus = UNSET
        else:
            max_defocus = self.max_defocus

        c2aperture: float | None | Unset
        if isinstance(self.c2aperture, Unset):
            c2aperture = UNSET
        else:
            c2aperture = self.c2aperture

        total_exposed_dose: float | None | Unset
        if isinstance(self.total_exposed_dose, Unset):
            total_exposed_dose = UNSET
        else:
            total_exposed_dose = self.total_exposed_dose

        phase_plate: int | None | Unset
        if isinstance(self.phase_plate, Unset):
            phase_plate = UNSET
        else:
            phase_plate = self.phase_plate

        data_collection_plan_id: int | None | Unset
        if isinstance(self.data_collection_plan_id, Unset):
            data_collection_plan_id = UNSET
        else:
            data_collection_plan_id = self.data_collection_plan_id

        data_collection_number: int | None | Unset
        if isinstance(self.data_collection_number, Unset):
            data_collection_number = UNSET
        else:
            data_collection_number = self.data_collection_number

        data_collection_group_id: int | None | Unset
        if isinstance(self.data_collection_group_id, Unset):
            data_collection_group_id = UNSET
        else:
            data_collection_group_id = self.data_collection_group_id

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if comments is not UNSET:
            field_dict["comments"] = comments
        if start_time is not UNSET:
            field_dict["startTime"] = start_time
        if pixel_size_on_image is not UNSET:
            field_dict["pixelSizeOnImage"] = pixel_size_on_image
        if voltage is not UNSET:
            field_dict["voltage"] = voltage
        if image_size_x is not UNSET:
            field_dict["imageSizeX"] = image_size_x
        if image_size_y is not UNSET:
            field_dict["imageSizeY"] = image_size_y
        if experimenttype is not UNSET:
            field_dict["experimenttype"] = experimenttype
        if end_time is not UNSET:
            field_dict["endTime"] = end_time
        if run_status is not UNSET:
            field_dict["runStatus"] = run_status
        if axis_start is not UNSET:
            field_dict["axisStart"] = axis_start
        if axis_end is not UNSET:
            field_dict["axisEnd"] = axis_end
        if axis_range is not UNSET:
            field_dict["axisRange"] = axis_range
        if overlap is not UNSET:
            field_dict["overlap"] = overlap
        if number_of_images is not UNSET:
            field_dict["numberOfImages"] = number_of_images
        if start_image_number is not UNSET:
            field_dict["startImageNumber"] = start_image_number
        if number_of_passes is not UNSET:
            field_dict["numberOfPasses"] = number_of_passes
        if exposure_time is not UNSET:
            field_dict["exposureTime"] = exposure_time
        if image_directory is not UNSET:
            field_dict["imageDirectory"] = image_directory
        if image_prefix is not UNSET:
            field_dict["imagePrefix"] = image_prefix
        if image_suffix is not UNSET:
            field_dict["imageSuffix"] = image_suffix
        if image_container_sub_path is not UNSET:
            field_dict["imageContainerSubPath"] = image_container_sub_path
        if file_template is not UNSET:
            field_dict["fileTemplate"] = file_template
        if wavelength is not UNSET:
            field_dict["wavelength"] = wavelength
        if resolution is not UNSET:
            field_dict["resolution"] = resolution
        if detector_distance is not UNSET:
            field_dict["detectorDistance"] = detector_distance
        if x_beam is not UNSET:
            field_dict["xBeam"] = x_beam
        if y_beam is not UNSET:
            field_dict["yBeam"] = y_beam
        if printable_for_report is not UNSET:
            field_dict["printableForReport"] = printable_for_report
        if slit_gap_vertical is not UNSET:
            field_dict["slitGapVertical"] = slit_gap_vertical
        if slit_gap_horizontal is not UNSET:
            field_dict["slitGapHorizontal"] = slit_gap_horizontal
        if transmission is not UNSET:
            field_dict["transmission"] = transmission
        if synchrotron_mode is not UNSET:
            field_dict["synchrotronMode"] = synchrotron_mode
        if xtal_snapshot_full_path_1 is not UNSET:
            field_dict["xtalSnapshotFullPath1"] = xtal_snapshot_full_path_1
        if xtal_snapshot_full_path_2 is not UNSET:
            field_dict["xtalSnapshotFullPath2"] = xtal_snapshot_full_path_2
        if xtal_snapshot_full_path_3 is not UNSET:
            field_dict["xtalSnapshotFullPath3"] = xtal_snapshot_full_path_3
        if xtal_snapshot_full_path_4 is not UNSET:
            field_dict["xtalSnapshotFullPath4"] = xtal_snapshot_full_path_4
        if rotation_axis is not UNSET:
            field_dict["rotationAxis"] = rotation_axis
        if phi_start is not UNSET:
            field_dict["phiStart"] = phi_start
        if kappa_start is not UNSET:
            field_dict["kappaStart"] = kappa_start
        if omega_start is not UNSET:
            field_dict["omegaStart"] = omega_start
        if chi_start is not UNSET:
            field_dict["chiStart"] = chi_start
        if detector_2_theta is not UNSET:
            field_dict["detector2Theta"] = detector_2_theta
        if detector_mode is not UNSET:
            field_dict["detectorMode"] = detector_mode
        if sample_id is not UNSET:
            field_dict["sampleId"] = sample_id
        if undulator_gap_1 is not UNSET:
            field_dict["undulatorGap1"] = undulator_gap_1
        if undulator_gap_2 is not UNSET:
            field_dict["undulatorGap2"] = undulator_gap_2
        if undulator_gap_3 is not UNSET:
            field_dict["undulatorGap3"] = undulator_gap_3
        if beam_size_at_sample_x is not UNSET:
            field_dict["beamSizeAtSampleX"] = beam_size_at_sample_x
        if beam_size_at_sample_y is not UNSET:
            field_dict["beamSizeAtSampleY"] = beam_size_at_sample_y
        if centering_method is not UNSET:
            field_dict["centeringMethod"] = centering_method
        if detector_id is not UNSET:
            field_dict["detectorId"] = detector_id
        if flux is not UNSET:
            field_dict["flux"] = flux
        if bl_sub_sample_id is not UNSET:
            field_dict["blSubSampleId"] = bl_sub_sample_id
        if flux_end is not UNSET:
            field_dict["flux_end"] = flux_end
        if dat_full_path is not UNSET:
            field_dict["datFullPath"] = dat_full_path
        if magnification is not UNSET:
            field_dict["magnification"] = magnification
        if total_absorbed_dose is not UNSET:
            field_dict["totalAbsorbedDose"] = total_absorbed_dose
        if binning is not UNSET:
            field_dict["binning"] = binning
        if particle_diameter is not UNSET:
            field_dict["particleDiameter"] = particle_diameter
        if min_resolution is not UNSET:
            field_dict["minResolution"] = min_resolution
        if min_defocus is not UNSET:
            field_dict["minDefocus"] = min_defocus
        if max_defocus is not UNSET:
            field_dict["maxDefocus"] = max_defocus
        if c2aperture is not UNSET:
            field_dict["c2aperture"] = c2aperture
        if total_exposed_dose is not UNSET:
            field_dict["totalExposedDose"] = total_exposed_dose
        if phase_plate is not UNSET:
            field_dict["phasePlate"] = phase_plate
        if data_collection_plan_id is not UNSET:
            field_dict["dataCollectionPlanId"] = data_collection_plan_id
        if data_collection_number is not UNSET:
            field_dict["dataCollectionNumber"] = data_collection_number
        if data_collection_group_id is not UNSET:
            field_dict["dataCollectionGroupId"] = data_collection_group_id

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)

        def _parse_comments(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        comments = _parse_comments(d.pop("comments", UNSET))

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

        def _parse_pixel_size_on_image(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        pixel_size_on_image = _parse_pixel_size_on_image(d.pop("pixelSizeOnImage", UNSET))

        def _parse_voltage(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        voltage = _parse_voltage(d.pop("voltage", UNSET))

        def _parse_image_size_x(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        image_size_x = _parse_image_size_x(d.pop("imageSizeX", UNSET))

        def _parse_image_size_y(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        image_size_y = _parse_image_size_y(d.pop("imageSizeY", UNSET))

        def _parse_experimenttype(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        experimenttype = _parse_experimenttype(d.pop("experimenttype", UNSET))

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

        def _parse_run_status(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        run_status = _parse_run_status(d.pop("runStatus", UNSET))

        def _parse_axis_start(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        axis_start = _parse_axis_start(d.pop("axisStart", UNSET))

        def _parse_axis_end(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        axis_end = _parse_axis_end(d.pop("axisEnd", UNSET))

        def _parse_axis_range(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        axis_range = _parse_axis_range(d.pop("axisRange", UNSET))

        def _parse_overlap(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        overlap = _parse_overlap(d.pop("overlap", UNSET))

        def _parse_number_of_images(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        number_of_images = _parse_number_of_images(d.pop("numberOfImages", UNSET))

        def _parse_start_image_number(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        start_image_number = _parse_start_image_number(d.pop("startImageNumber", UNSET))

        def _parse_number_of_passes(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        number_of_passes = _parse_number_of_passes(d.pop("numberOfPasses", UNSET))

        def _parse_exposure_time(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        exposure_time = _parse_exposure_time(d.pop("exposureTime", UNSET))

        def _parse_image_directory(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        image_directory = _parse_image_directory(d.pop("imageDirectory", UNSET))

        def _parse_image_prefix(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        image_prefix = _parse_image_prefix(d.pop("imagePrefix", UNSET))

        def _parse_image_suffix(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        image_suffix = _parse_image_suffix(d.pop("imageSuffix", UNSET))

        def _parse_image_container_sub_path(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        image_container_sub_path = _parse_image_container_sub_path(d.pop("imageContainerSubPath", UNSET))

        def _parse_file_template(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        file_template = _parse_file_template(d.pop("fileTemplate", UNSET))

        def _parse_wavelength(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        wavelength = _parse_wavelength(d.pop("wavelength", UNSET))

        def _parse_resolution(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        resolution = _parse_resolution(d.pop("resolution", UNSET))

        def _parse_detector_distance(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        detector_distance = _parse_detector_distance(d.pop("detectorDistance", UNSET))

        def _parse_x_beam(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        x_beam = _parse_x_beam(d.pop("xBeam", UNSET))

        def _parse_y_beam(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        y_beam = _parse_y_beam(d.pop("yBeam", UNSET))

        def _parse_printable_for_report(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        printable_for_report = _parse_printable_for_report(d.pop("printableForReport", UNSET))

        def _parse_slit_gap_vertical(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        slit_gap_vertical = _parse_slit_gap_vertical(d.pop("slitGapVertical", UNSET))

        def _parse_slit_gap_horizontal(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        slit_gap_horizontal = _parse_slit_gap_horizontal(d.pop("slitGapHorizontal", UNSET))

        def _parse_transmission(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        transmission = _parse_transmission(d.pop("transmission", UNSET))

        def _parse_synchrotron_mode(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        synchrotron_mode = _parse_synchrotron_mode(d.pop("synchrotronMode", UNSET))

        def _parse_xtal_snapshot_full_path_1(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        xtal_snapshot_full_path_1 = _parse_xtal_snapshot_full_path_1(d.pop("xtalSnapshotFullPath1", UNSET))

        def _parse_xtal_snapshot_full_path_2(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        xtal_snapshot_full_path_2 = _parse_xtal_snapshot_full_path_2(d.pop("xtalSnapshotFullPath2", UNSET))

        def _parse_xtal_snapshot_full_path_3(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        xtal_snapshot_full_path_3 = _parse_xtal_snapshot_full_path_3(d.pop("xtalSnapshotFullPath3", UNSET))

        def _parse_xtal_snapshot_full_path_4(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        xtal_snapshot_full_path_4 = _parse_xtal_snapshot_full_path_4(d.pop("xtalSnapshotFullPath4", UNSET))

        def _parse_rotation_axis(data: object) -> None | RotationAxisEnum | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                rotation_axis_type_0 = RotationAxisEnum(data)

                return rotation_axis_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(None | RotationAxisEnum | Unset, data)

        rotation_axis = _parse_rotation_axis(d.pop("rotationAxis", UNSET))

        def _parse_phi_start(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        phi_start = _parse_phi_start(d.pop("phiStart", UNSET))

        def _parse_kappa_start(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        kappa_start = _parse_kappa_start(d.pop("kappaStart", UNSET))

        def _parse_omega_start(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        omega_start = _parse_omega_start(d.pop("omegaStart", UNSET))

        def _parse_chi_start(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        chi_start = _parse_chi_start(d.pop("chiStart", UNSET))

        def _parse_detector_2_theta(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        detector_2_theta = _parse_detector_2_theta(d.pop("detector2Theta", UNSET))

        def _parse_detector_mode(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        detector_mode = _parse_detector_mode(d.pop("detectorMode", UNSET))

        def _parse_sample_id(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        sample_id = _parse_sample_id(d.pop("sampleId", UNSET))

        def _parse_undulator_gap_1(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        undulator_gap_1 = _parse_undulator_gap_1(d.pop("undulatorGap1", UNSET))

        def _parse_undulator_gap_2(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        undulator_gap_2 = _parse_undulator_gap_2(d.pop("undulatorGap2", UNSET))

        def _parse_undulator_gap_3(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        undulator_gap_3 = _parse_undulator_gap_3(d.pop("undulatorGap3", UNSET))

        def _parse_beam_size_at_sample_x(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        beam_size_at_sample_x = _parse_beam_size_at_sample_x(d.pop("beamSizeAtSampleX", UNSET))

        def _parse_beam_size_at_sample_y(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        beam_size_at_sample_y = _parse_beam_size_at_sample_y(d.pop("beamSizeAtSampleY", UNSET))

        def _parse_centering_method(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        centering_method = _parse_centering_method(d.pop("centeringMethod", UNSET))

        def _parse_detector_id(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        detector_id = _parse_detector_id(d.pop("detectorId", UNSET))

        def _parse_flux(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        flux = _parse_flux(d.pop("flux", UNSET))

        def _parse_bl_sub_sample_id(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        bl_sub_sample_id = _parse_bl_sub_sample_id(d.pop("blSubSampleId", UNSET))

        def _parse_flux_end(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        flux_end = _parse_flux_end(d.pop("flux_end", UNSET))

        def _parse_dat_full_path(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        dat_full_path = _parse_dat_full_path(d.pop("datFullPath", UNSET))

        def _parse_magnification(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        magnification = _parse_magnification(d.pop("magnification", UNSET))

        def _parse_total_absorbed_dose(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        total_absorbed_dose = _parse_total_absorbed_dose(d.pop("totalAbsorbedDose", UNSET))

        def _parse_binning(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        binning = _parse_binning(d.pop("binning", UNSET))

        def _parse_particle_diameter(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        particle_diameter = _parse_particle_diameter(d.pop("particleDiameter", UNSET))

        def _parse_min_resolution(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        min_resolution = _parse_min_resolution(d.pop("minResolution", UNSET))

        def _parse_min_defocus(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        min_defocus = _parse_min_defocus(d.pop("minDefocus", UNSET))

        def _parse_max_defocus(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        max_defocus = _parse_max_defocus(d.pop("maxDefocus", UNSET))

        def _parse_c2aperture(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        c2aperture = _parse_c2aperture(d.pop("c2aperture", UNSET))

        def _parse_total_exposed_dose(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        total_exposed_dose = _parse_total_exposed_dose(d.pop("totalExposedDose", UNSET))

        def _parse_phase_plate(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        phase_plate = _parse_phase_plate(d.pop("phasePlate", UNSET))

        def _parse_data_collection_plan_id(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        data_collection_plan_id = _parse_data_collection_plan_id(d.pop("dataCollectionPlanId", UNSET))

        def _parse_data_collection_number(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        data_collection_number = _parse_data_collection_number(d.pop("dataCollectionNumber", UNSET))

        def _parse_data_collection_group_id(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        data_collection_group_id = _parse_data_collection_group_id(d.pop("dataCollectionGroupId", UNSET))

        data_collection_optional = cls(
            comments=comments,
            start_time=start_time,
            pixel_size_on_image=pixel_size_on_image,
            voltage=voltage,
            image_size_x=image_size_x,
            image_size_y=image_size_y,
            experimenttype=experimenttype,
            end_time=end_time,
            run_status=run_status,
            axis_start=axis_start,
            axis_end=axis_end,
            axis_range=axis_range,
            overlap=overlap,
            number_of_images=number_of_images,
            start_image_number=start_image_number,
            number_of_passes=number_of_passes,
            exposure_time=exposure_time,
            image_directory=image_directory,
            image_prefix=image_prefix,
            image_suffix=image_suffix,
            image_container_sub_path=image_container_sub_path,
            file_template=file_template,
            wavelength=wavelength,
            resolution=resolution,
            detector_distance=detector_distance,
            x_beam=x_beam,
            y_beam=y_beam,
            printable_for_report=printable_for_report,
            slit_gap_vertical=slit_gap_vertical,
            slit_gap_horizontal=slit_gap_horizontal,
            transmission=transmission,
            synchrotron_mode=synchrotron_mode,
            xtal_snapshot_full_path_1=xtal_snapshot_full_path_1,
            xtal_snapshot_full_path_2=xtal_snapshot_full_path_2,
            xtal_snapshot_full_path_3=xtal_snapshot_full_path_3,
            xtal_snapshot_full_path_4=xtal_snapshot_full_path_4,
            rotation_axis=rotation_axis,
            phi_start=phi_start,
            kappa_start=kappa_start,
            omega_start=omega_start,
            chi_start=chi_start,
            detector_2_theta=detector_2_theta,
            detector_mode=detector_mode,
            sample_id=sample_id,
            undulator_gap_1=undulator_gap_1,
            undulator_gap_2=undulator_gap_2,
            undulator_gap_3=undulator_gap_3,
            beam_size_at_sample_x=beam_size_at_sample_x,
            beam_size_at_sample_y=beam_size_at_sample_y,
            centering_method=centering_method,
            detector_id=detector_id,
            flux=flux,
            bl_sub_sample_id=bl_sub_sample_id,
            flux_end=flux_end,
            dat_full_path=dat_full_path,
            magnification=magnification,
            total_absorbed_dose=total_absorbed_dose,
            binning=binning,
            particle_diameter=particle_diameter,
            min_resolution=min_resolution,
            min_defocus=min_defocus,
            max_defocus=max_defocus,
            c2aperture=c2aperture,
            total_exposed_dose=total_exposed_dose,
            phase_plate=phase_plate,
            data_collection_plan_id=data_collection_plan_id,
            data_collection_number=data_collection_number,
            data_collection_group_id=data_collection_group_id,
        )

        data_collection_optional.additional_properties = d
        return data_collection_optional

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

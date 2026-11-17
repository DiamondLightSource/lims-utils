from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.centring_method import CentringMethod
from ..models.collection_mode import CollectionMode
from ..models.diffraction_plan_experiment_type import DiffractionPlanExperimentType
from ..models.reduction_parameters import ReductionParameters
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.diffraction_plan_optional_scan_parameters_type_0_type_0 import (
        DiffractionPlanOptionalScanParametersType0Type0,
    )
    from ..models.string_serialised_strategy_option_type_0 import StringSerialisedStrategyOptionType0


T = TypeVar("T", bound="DiffractionPlanOptional")


@_attrs_define
class DiffractionPlanOptional:
    """
    Attributes:
        name (None | str | Unset):
        experiment_kind (DiffractionPlanExperimentType | None | Unset):
        observed_resolution (float | None | Unset):
        minimal_resolution (float | None | Unset):
        exposure_time (float | None | Unset):
        oscillation_range (float | None | Unset):
        maximal_resolution (float | None | Unset):
        screening_resolution (float | None | Unset):
        radiation_sensitivity (float | None | Unset):
        anomalous_scatterer (None | str | Unset):
        preferred_beam_size_x (float | None | Unset):
        preferred_beam_size_y (float | None | Unset):
        preferred_beam_diameter (float | None | Unset):
        comments (None | str | Unset):
        aimed_completeness (float | None | Unset):
        aimed_i_over_sigma_at_highest_res (float | None | Unset):
        aimed_multiplicity (float | None | Unset):
        aimed_resolution (float | None | Unset):
        anomalous_data (bool | None | Unset):
        complexity (None | str | Unset):
        estimate_radiation_damage (bool | None | Unset):
        forced_space_group (None | str | Unset):
        required_completeness (float | None | Unset):
        required_multiplicity (float | None | Unset):
        required_resolution (float | None | Unset):
        kappa_strategy_option (None | str | Unset):
        number_of_positions (int | None | Unset):
        min_dim_accross_spindle_axis (float | None | Unset):
        max_dim_accross_spindle_axis (float | None | Unset):
        radiation_sensitivity_beta (float | None | Unset):
        radiation_sensitivity_gamma (float | None | Unset):
        min_osc_width (float | None | Unset):
        detector_id (int | None | Unset):
        distance (float | None | Unset):
        orientation (float | None | Unset):
        mono_bandwidth (float | None | Unset):
        monochromator (None | str | Unset):
        energy (float | None | Unset):
        transmission (float | None | Unset):
        box_size_x (float | None | Unset):
        box_size_y (float | None | Unset):
        kappa_start (float | None | Unset):
        axis_start (float | None | Unset):
        axis_range (float | None | Unset):
        number_of_images (int | None | Unset):
        preset_for_proposal_id (int | None | Unset):
        beam_line_name (None | str | Unset):
        centring_method (CentringMethod | None | Unset):
        user_path (None | str | Unset):
        robot_plate_temperature (float | None | Unset):
        exposure_temperature (float | None | Unset):
        purification_column_id (int | None | Unset):
        experiment_type_id (int | None | Unset):
        collection_mode (CollectionMode | None | Unset):
        priority (int | None | Unset):
        q_min (float | None | Unset):
        q_max (float | None | Unset):
        reduction_parameters_averaging (None | ReductionParameters | Unset):
        scan_parameters (DiffractionPlanOptionalScanParametersType0Type0 | None | str | Unset):
        strategy_option (None | str | StringSerialisedStrategyOptionType0 | Unset):
    """

    name: None | str | Unset = UNSET
    experiment_kind: DiffractionPlanExperimentType | None | Unset = UNSET
    observed_resolution: float | None | Unset = UNSET
    minimal_resolution: float | None | Unset = UNSET
    exposure_time: float | None | Unset = UNSET
    oscillation_range: float | None | Unset = UNSET
    maximal_resolution: float | None | Unset = UNSET
    screening_resolution: float | None | Unset = UNSET
    radiation_sensitivity: float | None | Unset = UNSET
    anomalous_scatterer: None | str | Unset = UNSET
    preferred_beam_size_x: float | None | Unset = UNSET
    preferred_beam_size_y: float | None | Unset = UNSET
    preferred_beam_diameter: float | None | Unset = UNSET
    comments: None | str | Unset = UNSET
    aimed_completeness: float | None | Unset = UNSET
    aimed_i_over_sigma_at_highest_res: float | None | Unset = UNSET
    aimed_multiplicity: float | None | Unset = UNSET
    aimed_resolution: float | None | Unset = UNSET
    anomalous_data: bool | None | Unset = UNSET
    complexity: None | str | Unset = UNSET
    estimate_radiation_damage: bool | None | Unset = UNSET
    forced_space_group: None | str | Unset = UNSET
    required_completeness: float | None | Unset = UNSET
    required_multiplicity: float | None | Unset = UNSET
    required_resolution: float | None | Unset = UNSET
    kappa_strategy_option: None | str | Unset = UNSET
    number_of_positions: int | None | Unset = UNSET
    min_dim_accross_spindle_axis: float | None | Unset = UNSET
    max_dim_accross_spindle_axis: float | None | Unset = UNSET
    radiation_sensitivity_beta: float | None | Unset = UNSET
    radiation_sensitivity_gamma: float | None | Unset = UNSET
    min_osc_width: float | None | Unset = UNSET
    detector_id: int | None | Unset = UNSET
    distance: float | None | Unset = UNSET
    orientation: float | None | Unset = UNSET
    mono_bandwidth: float | None | Unset = UNSET
    monochromator: None | str | Unset = UNSET
    energy: float | None | Unset = UNSET
    transmission: float | None | Unset = UNSET
    box_size_x: float | None | Unset = UNSET
    box_size_y: float | None | Unset = UNSET
    kappa_start: float | None | Unset = UNSET
    axis_start: float | None | Unset = UNSET
    axis_range: float | None | Unset = UNSET
    number_of_images: int | None | Unset = UNSET
    preset_for_proposal_id: int | None | Unset = UNSET
    beam_line_name: None | str | Unset = UNSET
    centring_method: CentringMethod | None | Unset = UNSET
    user_path: None | str | Unset = UNSET
    robot_plate_temperature: float | None | Unset = UNSET
    exposure_temperature: float | None | Unset = UNSET
    purification_column_id: int | None | Unset = UNSET
    experiment_type_id: int | None | Unset = UNSET
    collection_mode: CollectionMode | None | Unset = UNSET
    priority: int | None | Unset = UNSET
    q_min: float | None | Unset = UNSET
    q_max: float | None | Unset = UNSET
    reduction_parameters_averaging: None | ReductionParameters | Unset = UNSET
    scan_parameters: DiffractionPlanOptionalScanParametersType0Type0 | None | str | Unset = UNSET
    strategy_option: None | str | StringSerialisedStrategyOptionType0 | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.diffraction_plan_optional_scan_parameters_type_0_type_0 import (
            DiffractionPlanOptionalScanParametersType0Type0,  # noqa: PLC0415
        )
        from ..models.string_serialised_strategy_option_type_0 import StringSerialisedStrategyOptionType0  # noqa: PLC0415

        name: None | str | Unset
        if isinstance(self.name, Unset):
            name = UNSET
        else:
            name = self.name

        experiment_kind: None | str | Unset
        if isinstance(self.experiment_kind, Unset):
            experiment_kind = UNSET
        elif isinstance(self.experiment_kind, DiffractionPlanExperimentType):
            experiment_kind = self.experiment_kind.value
        else:
            experiment_kind = self.experiment_kind

        observed_resolution: float | None | Unset
        if isinstance(self.observed_resolution, Unset):
            observed_resolution = UNSET
        else:
            observed_resolution = self.observed_resolution

        minimal_resolution: float | None | Unset
        if isinstance(self.minimal_resolution, Unset):
            minimal_resolution = UNSET
        else:
            minimal_resolution = self.minimal_resolution

        exposure_time: float | None | Unset
        if isinstance(self.exposure_time, Unset):
            exposure_time = UNSET
        else:
            exposure_time = self.exposure_time

        oscillation_range: float | None | Unset
        if isinstance(self.oscillation_range, Unset):
            oscillation_range = UNSET
        else:
            oscillation_range = self.oscillation_range

        maximal_resolution: float | None | Unset
        if isinstance(self.maximal_resolution, Unset):
            maximal_resolution = UNSET
        else:
            maximal_resolution = self.maximal_resolution

        screening_resolution: float | None | Unset
        if isinstance(self.screening_resolution, Unset):
            screening_resolution = UNSET
        else:
            screening_resolution = self.screening_resolution

        radiation_sensitivity: float | None | Unset
        if isinstance(self.radiation_sensitivity, Unset):
            radiation_sensitivity = UNSET
        else:
            radiation_sensitivity = self.radiation_sensitivity

        anomalous_scatterer: None | str | Unset
        if isinstance(self.anomalous_scatterer, Unset):
            anomalous_scatterer = UNSET
        else:
            anomalous_scatterer = self.anomalous_scatterer

        preferred_beam_size_x: float | None | Unset
        if isinstance(self.preferred_beam_size_x, Unset):
            preferred_beam_size_x = UNSET
        else:
            preferred_beam_size_x = self.preferred_beam_size_x

        preferred_beam_size_y: float | None | Unset
        if isinstance(self.preferred_beam_size_y, Unset):
            preferred_beam_size_y = UNSET
        else:
            preferred_beam_size_y = self.preferred_beam_size_y

        preferred_beam_diameter: float | None | Unset
        if isinstance(self.preferred_beam_diameter, Unset):
            preferred_beam_diameter = UNSET
        else:
            preferred_beam_diameter = self.preferred_beam_diameter

        comments: None | str | Unset
        if isinstance(self.comments, Unset):
            comments = UNSET
        else:
            comments = self.comments

        aimed_completeness: float | None | Unset
        if isinstance(self.aimed_completeness, Unset):
            aimed_completeness = UNSET
        else:
            aimed_completeness = self.aimed_completeness

        aimed_i_over_sigma_at_highest_res: float | None | Unset
        if isinstance(self.aimed_i_over_sigma_at_highest_res, Unset):
            aimed_i_over_sigma_at_highest_res = UNSET
        else:
            aimed_i_over_sigma_at_highest_res = self.aimed_i_over_sigma_at_highest_res

        aimed_multiplicity: float | None | Unset
        if isinstance(self.aimed_multiplicity, Unset):
            aimed_multiplicity = UNSET
        else:
            aimed_multiplicity = self.aimed_multiplicity

        aimed_resolution: float | None | Unset
        if isinstance(self.aimed_resolution, Unset):
            aimed_resolution = UNSET
        else:
            aimed_resolution = self.aimed_resolution

        anomalous_data: bool | None | Unset
        if isinstance(self.anomalous_data, Unset):
            anomalous_data = UNSET
        else:
            anomalous_data = self.anomalous_data

        complexity: None | str | Unset
        if isinstance(self.complexity, Unset):
            complexity = UNSET
        else:
            complexity = self.complexity

        estimate_radiation_damage: bool | None | Unset
        if isinstance(self.estimate_radiation_damage, Unset):
            estimate_radiation_damage = UNSET
        else:
            estimate_radiation_damage = self.estimate_radiation_damage

        forced_space_group: None | str | Unset
        if isinstance(self.forced_space_group, Unset):
            forced_space_group = UNSET
        else:
            forced_space_group = self.forced_space_group

        required_completeness: float | None | Unset
        if isinstance(self.required_completeness, Unset):
            required_completeness = UNSET
        else:
            required_completeness = self.required_completeness

        required_multiplicity: float | None | Unset
        if isinstance(self.required_multiplicity, Unset):
            required_multiplicity = UNSET
        else:
            required_multiplicity = self.required_multiplicity

        required_resolution: float | None | Unset
        if isinstance(self.required_resolution, Unset):
            required_resolution = UNSET
        else:
            required_resolution = self.required_resolution

        kappa_strategy_option: None | str | Unset
        if isinstance(self.kappa_strategy_option, Unset):
            kappa_strategy_option = UNSET
        else:
            kappa_strategy_option = self.kappa_strategy_option

        number_of_positions: int | None | Unset
        if isinstance(self.number_of_positions, Unset):
            number_of_positions = UNSET
        else:
            number_of_positions = self.number_of_positions

        min_dim_accross_spindle_axis: float | None | Unset
        if isinstance(self.min_dim_accross_spindle_axis, Unset):
            min_dim_accross_spindle_axis = UNSET
        else:
            min_dim_accross_spindle_axis = self.min_dim_accross_spindle_axis

        max_dim_accross_spindle_axis: float | None | Unset
        if isinstance(self.max_dim_accross_spindle_axis, Unset):
            max_dim_accross_spindle_axis = UNSET
        else:
            max_dim_accross_spindle_axis = self.max_dim_accross_spindle_axis

        radiation_sensitivity_beta: float | None | Unset
        if isinstance(self.radiation_sensitivity_beta, Unset):
            radiation_sensitivity_beta = UNSET
        else:
            radiation_sensitivity_beta = self.radiation_sensitivity_beta

        radiation_sensitivity_gamma: float | None | Unset
        if isinstance(self.radiation_sensitivity_gamma, Unset):
            radiation_sensitivity_gamma = UNSET
        else:
            radiation_sensitivity_gamma = self.radiation_sensitivity_gamma

        min_osc_width: float | None | Unset
        if isinstance(self.min_osc_width, Unset):
            min_osc_width = UNSET
        else:
            min_osc_width = self.min_osc_width

        detector_id: int | None | Unset
        if isinstance(self.detector_id, Unset):
            detector_id = UNSET
        else:
            detector_id = self.detector_id

        distance: float | None | Unset
        if isinstance(self.distance, Unset):
            distance = UNSET
        else:
            distance = self.distance

        orientation: float | None | Unset
        if isinstance(self.orientation, Unset):
            orientation = UNSET
        else:
            orientation = self.orientation

        mono_bandwidth: float | None | Unset
        if isinstance(self.mono_bandwidth, Unset):
            mono_bandwidth = UNSET
        else:
            mono_bandwidth = self.mono_bandwidth

        monochromator: None | str | Unset
        if isinstance(self.monochromator, Unset):
            monochromator = UNSET
        else:
            monochromator = self.monochromator

        energy: float | None | Unset
        if isinstance(self.energy, Unset):
            energy = UNSET
        else:
            energy = self.energy

        transmission: float | None | Unset
        if isinstance(self.transmission, Unset):
            transmission = UNSET
        else:
            transmission = self.transmission

        box_size_x: float | None | Unset
        if isinstance(self.box_size_x, Unset):
            box_size_x = UNSET
        else:
            box_size_x = self.box_size_x

        box_size_y: float | None | Unset
        if isinstance(self.box_size_y, Unset):
            box_size_y = UNSET
        else:
            box_size_y = self.box_size_y

        kappa_start: float | None | Unset
        if isinstance(self.kappa_start, Unset):
            kappa_start = UNSET
        else:
            kappa_start = self.kappa_start

        axis_start: float | None | Unset
        if isinstance(self.axis_start, Unset):
            axis_start = UNSET
        else:
            axis_start = self.axis_start

        axis_range: float | None | Unset
        if isinstance(self.axis_range, Unset):
            axis_range = UNSET
        else:
            axis_range = self.axis_range

        number_of_images: int | None | Unset
        if isinstance(self.number_of_images, Unset):
            number_of_images = UNSET
        else:
            number_of_images = self.number_of_images

        preset_for_proposal_id: int | None | Unset
        if isinstance(self.preset_for_proposal_id, Unset):
            preset_for_proposal_id = UNSET
        else:
            preset_for_proposal_id = self.preset_for_proposal_id

        beam_line_name: None | str | Unset
        if isinstance(self.beam_line_name, Unset):
            beam_line_name = UNSET
        else:
            beam_line_name = self.beam_line_name

        centring_method: None | str | Unset
        if isinstance(self.centring_method, Unset):
            centring_method = UNSET
        elif isinstance(self.centring_method, CentringMethod):
            centring_method = self.centring_method.value
        else:
            centring_method = self.centring_method

        user_path: None | str | Unset
        if isinstance(self.user_path, Unset):
            user_path = UNSET
        else:
            user_path = self.user_path

        robot_plate_temperature: float | None | Unset
        if isinstance(self.robot_plate_temperature, Unset):
            robot_plate_temperature = UNSET
        else:
            robot_plate_temperature = self.robot_plate_temperature

        exposure_temperature: float | None | Unset
        if isinstance(self.exposure_temperature, Unset):
            exposure_temperature = UNSET
        else:
            exposure_temperature = self.exposure_temperature

        purification_column_id: int | None | Unset
        if isinstance(self.purification_column_id, Unset):
            purification_column_id = UNSET
        else:
            purification_column_id = self.purification_column_id

        experiment_type_id: int | None | Unset
        if isinstance(self.experiment_type_id, Unset):
            experiment_type_id = UNSET
        else:
            experiment_type_id = self.experiment_type_id

        collection_mode: None | str | Unset
        if isinstance(self.collection_mode, Unset):
            collection_mode = UNSET
        elif isinstance(self.collection_mode, CollectionMode):
            collection_mode = self.collection_mode.value
        else:
            collection_mode = self.collection_mode

        priority: int | None | Unset
        if isinstance(self.priority, Unset):
            priority = UNSET
        else:
            priority = self.priority

        q_min: float | None | Unset
        if isinstance(self.q_min, Unset):
            q_min = UNSET
        else:
            q_min = self.q_min

        q_max: float | None | Unset
        if isinstance(self.q_max, Unset):
            q_max = UNSET
        else:
            q_max = self.q_max

        reduction_parameters_averaging: None | str | Unset
        if isinstance(self.reduction_parameters_averaging, Unset):
            reduction_parameters_averaging = UNSET
        elif isinstance(self.reduction_parameters_averaging, ReductionParameters):
            reduction_parameters_averaging = self.reduction_parameters_averaging.value
        else:
            reduction_parameters_averaging = self.reduction_parameters_averaging

        scan_parameters: dict[str, Any] | None | str | Unset
        if isinstance(self.scan_parameters, Unset):
            scan_parameters = UNSET
        elif isinstance(self.scan_parameters, DiffractionPlanOptionalScanParametersType0Type0):
            scan_parameters = self.scan_parameters.to_dict()
        else:
            scan_parameters = self.scan_parameters

        strategy_option: dict[str, Any] | None | str | Unset
        if isinstance(self.strategy_option, Unset):
            strategy_option = UNSET
        elif isinstance(self.strategy_option, StringSerialisedStrategyOptionType0):
            strategy_option = self.strategy_option.to_dict()
        else:
            strategy_option = self.strategy_option

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if name is not UNSET:
            field_dict["name"] = name
        if experiment_kind is not UNSET:
            field_dict["experimentKind"] = experiment_kind
        if observed_resolution is not UNSET:
            field_dict["observedResolution"] = observed_resolution
        if minimal_resolution is not UNSET:
            field_dict["minimalResolution"] = minimal_resolution
        if exposure_time is not UNSET:
            field_dict["exposureTime"] = exposure_time
        if oscillation_range is not UNSET:
            field_dict["oscillationRange"] = oscillation_range
        if maximal_resolution is not UNSET:
            field_dict["maximalResolution"] = maximal_resolution
        if screening_resolution is not UNSET:
            field_dict["screeningResolution"] = screening_resolution
        if radiation_sensitivity is not UNSET:
            field_dict["radiationSensitivity"] = radiation_sensitivity
        if anomalous_scatterer is not UNSET:
            field_dict["anomalousScatterer"] = anomalous_scatterer
        if preferred_beam_size_x is not UNSET:
            field_dict["preferredBeamSizeX"] = preferred_beam_size_x
        if preferred_beam_size_y is not UNSET:
            field_dict["preferredBeamSizeY"] = preferred_beam_size_y
        if preferred_beam_diameter is not UNSET:
            field_dict["preferredBeamDiameter"] = preferred_beam_diameter
        if comments is not UNSET:
            field_dict["comments"] = comments
        if aimed_completeness is not UNSET:
            field_dict["aimedCompleteness"] = aimed_completeness
        if aimed_i_over_sigma_at_highest_res is not UNSET:
            field_dict["aimedIOverSigmaAtHighestRes"] = aimed_i_over_sigma_at_highest_res
        if aimed_multiplicity is not UNSET:
            field_dict["aimedMultiplicity"] = aimed_multiplicity
        if aimed_resolution is not UNSET:
            field_dict["aimedResolution"] = aimed_resolution
        if anomalous_data is not UNSET:
            field_dict["anomalousData"] = anomalous_data
        if complexity is not UNSET:
            field_dict["complexity"] = complexity
        if estimate_radiation_damage is not UNSET:
            field_dict["estimateRadiationDamage"] = estimate_radiation_damage
        if forced_space_group is not UNSET:
            field_dict["forcedSpaceGroup"] = forced_space_group
        if required_completeness is not UNSET:
            field_dict["requiredCompleteness"] = required_completeness
        if required_multiplicity is not UNSET:
            field_dict["requiredMultiplicity"] = required_multiplicity
        if required_resolution is not UNSET:
            field_dict["requiredResolution"] = required_resolution
        if kappa_strategy_option is not UNSET:
            field_dict["kappaStrategyOption"] = kappa_strategy_option
        if number_of_positions is not UNSET:
            field_dict["numberOfPositions"] = number_of_positions
        if min_dim_accross_spindle_axis is not UNSET:
            field_dict["minDimAccrossSpindleAxis"] = min_dim_accross_spindle_axis
        if max_dim_accross_spindle_axis is not UNSET:
            field_dict["maxDimAccrossSpindleAxis"] = max_dim_accross_spindle_axis
        if radiation_sensitivity_beta is not UNSET:
            field_dict["radiationSensitivityBeta"] = radiation_sensitivity_beta
        if radiation_sensitivity_gamma is not UNSET:
            field_dict["radiationSensitivityGamma"] = radiation_sensitivity_gamma
        if min_osc_width is not UNSET:
            field_dict["minOscWidth"] = min_osc_width
        if detector_id is not UNSET:
            field_dict["detectorId"] = detector_id
        if distance is not UNSET:
            field_dict["distance"] = distance
        if orientation is not UNSET:
            field_dict["orientation"] = orientation
        if mono_bandwidth is not UNSET:
            field_dict["monoBandwidth"] = mono_bandwidth
        if monochromator is not UNSET:
            field_dict["monochromator"] = monochromator
        if energy is not UNSET:
            field_dict["energy"] = energy
        if transmission is not UNSET:
            field_dict["transmission"] = transmission
        if box_size_x is not UNSET:
            field_dict["boxSizeX"] = box_size_x
        if box_size_y is not UNSET:
            field_dict["boxSizeY"] = box_size_y
        if kappa_start is not UNSET:
            field_dict["kappaStart"] = kappa_start
        if axis_start is not UNSET:
            field_dict["axisStart"] = axis_start
        if axis_range is not UNSET:
            field_dict["axisRange"] = axis_range
        if number_of_images is not UNSET:
            field_dict["numberOfImages"] = number_of_images
        if preset_for_proposal_id is not UNSET:
            field_dict["presetForProposalId"] = preset_for_proposal_id
        if beam_line_name is not UNSET:
            field_dict["beamLineName"] = beam_line_name
        if centring_method is not UNSET:
            field_dict["centringMethod"] = centring_method
        if user_path is not UNSET:
            field_dict["userPath"] = user_path
        if robot_plate_temperature is not UNSET:
            field_dict["robotPlateTemperature"] = robot_plate_temperature
        if exposure_temperature is not UNSET:
            field_dict["exposureTemperature"] = exposure_temperature
        if purification_column_id is not UNSET:
            field_dict["purificationColumnId"] = purification_column_id
        if experiment_type_id is not UNSET:
            field_dict["experimentTypeId"] = experiment_type_id
        if collection_mode is not UNSET:
            field_dict["collectionMode"] = collection_mode
        if priority is not UNSET:
            field_dict["priority"] = priority
        if q_min is not UNSET:
            field_dict["qMin"] = q_min
        if q_max is not UNSET:
            field_dict["qMax"] = q_max
        if reduction_parameters_averaging is not UNSET:
            field_dict["reductionParametersAveraging"] = reduction_parameters_averaging
        if scan_parameters is not UNSET:
            field_dict["scanParameters"] = scan_parameters
        if strategy_option is not UNSET:
            field_dict["strategyOption"] = strategy_option

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.diffraction_plan_optional_scan_parameters_type_0_type_0 import (
            DiffractionPlanOptionalScanParametersType0Type0,  # noqa: PLC0415
        )
        from ..models.string_serialised_strategy_option_type_0 import StringSerialisedStrategyOptionType0  # noqa: PLC0415

        d = dict(src_dict)

        def _parse_name(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        name = _parse_name(d.pop("name", UNSET))

        def _parse_experiment_kind(data: object) -> DiffractionPlanExperimentType | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                experiment_kind_type_0 = DiffractionPlanExperimentType(data)

                return experiment_kind_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(DiffractionPlanExperimentType | None | Unset, data)

        experiment_kind = _parse_experiment_kind(d.pop("experimentKind", UNSET))

        def _parse_observed_resolution(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        observed_resolution = _parse_observed_resolution(d.pop("observedResolution", UNSET))

        def _parse_minimal_resolution(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        minimal_resolution = _parse_minimal_resolution(d.pop("minimalResolution", UNSET))

        def _parse_exposure_time(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        exposure_time = _parse_exposure_time(d.pop("exposureTime", UNSET))

        def _parse_oscillation_range(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        oscillation_range = _parse_oscillation_range(d.pop("oscillationRange", UNSET))

        def _parse_maximal_resolution(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        maximal_resolution = _parse_maximal_resolution(d.pop("maximalResolution", UNSET))

        def _parse_screening_resolution(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        screening_resolution = _parse_screening_resolution(d.pop("screeningResolution", UNSET))

        def _parse_radiation_sensitivity(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        radiation_sensitivity = _parse_radiation_sensitivity(d.pop("radiationSensitivity", UNSET))

        def _parse_anomalous_scatterer(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        anomalous_scatterer = _parse_anomalous_scatterer(d.pop("anomalousScatterer", UNSET))

        def _parse_preferred_beam_size_x(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        preferred_beam_size_x = _parse_preferred_beam_size_x(d.pop("preferredBeamSizeX", UNSET))

        def _parse_preferred_beam_size_y(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        preferred_beam_size_y = _parse_preferred_beam_size_y(d.pop("preferredBeamSizeY", UNSET))

        def _parse_preferred_beam_diameter(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        preferred_beam_diameter = _parse_preferred_beam_diameter(d.pop("preferredBeamDiameter", UNSET))

        def _parse_comments(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        comments = _parse_comments(d.pop("comments", UNSET))

        def _parse_aimed_completeness(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        aimed_completeness = _parse_aimed_completeness(d.pop("aimedCompleteness", UNSET))

        def _parse_aimed_i_over_sigma_at_highest_res(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        aimed_i_over_sigma_at_highest_res = _parse_aimed_i_over_sigma_at_highest_res(
            d.pop("aimedIOverSigmaAtHighestRes", UNSET)
        )

        def _parse_aimed_multiplicity(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        aimed_multiplicity = _parse_aimed_multiplicity(d.pop("aimedMultiplicity", UNSET))

        def _parse_aimed_resolution(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        aimed_resolution = _parse_aimed_resolution(d.pop("aimedResolution", UNSET))

        def _parse_anomalous_data(data: object) -> bool | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(bool | None | Unset, data)

        anomalous_data = _parse_anomalous_data(d.pop("anomalousData", UNSET))

        def _parse_complexity(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        complexity = _parse_complexity(d.pop("complexity", UNSET))

        def _parse_estimate_radiation_damage(data: object) -> bool | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(bool | None | Unset, data)

        estimate_radiation_damage = _parse_estimate_radiation_damage(d.pop("estimateRadiationDamage", UNSET))

        def _parse_forced_space_group(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        forced_space_group = _parse_forced_space_group(d.pop("forcedSpaceGroup", UNSET))

        def _parse_required_completeness(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        required_completeness = _parse_required_completeness(d.pop("requiredCompleteness", UNSET))

        def _parse_required_multiplicity(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        required_multiplicity = _parse_required_multiplicity(d.pop("requiredMultiplicity", UNSET))

        def _parse_required_resolution(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        required_resolution = _parse_required_resolution(d.pop("requiredResolution", UNSET))

        def _parse_kappa_strategy_option(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        kappa_strategy_option = _parse_kappa_strategy_option(d.pop("kappaStrategyOption", UNSET))

        def _parse_number_of_positions(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        number_of_positions = _parse_number_of_positions(d.pop("numberOfPositions", UNSET))

        def _parse_min_dim_accross_spindle_axis(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        min_dim_accross_spindle_axis = _parse_min_dim_accross_spindle_axis(d.pop("minDimAccrossSpindleAxis", UNSET))

        def _parse_max_dim_accross_spindle_axis(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        max_dim_accross_spindle_axis = _parse_max_dim_accross_spindle_axis(d.pop("maxDimAccrossSpindleAxis", UNSET))

        def _parse_radiation_sensitivity_beta(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        radiation_sensitivity_beta = _parse_radiation_sensitivity_beta(d.pop("radiationSensitivityBeta", UNSET))

        def _parse_radiation_sensitivity_gamma(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        radiation_sensitivity_gamma = _parse_radiation_sensitivity_gamma(d.pop("radiationSensitivityGamma", UNSET))

        def _parse_min_osc_width(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        min_osc_width = _parse_min_osc_width(d.pop("minOscWidth", UNSET))

        def _parse_detector_id(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        detector_id = _parse_detector_id(d.pop("detectorId", UNSET))

        def _parse_distance(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        distance = _parse_distance(d.pop("distance", UNSET))

        def _parse_orientation(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        orientation = _parse_orientation(d.pop("orientation", UNSET))

        def _parse_mono_bandwidth(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        mono_bandwidth = _parse_mono_bandwidth(d.pop("monoBandwidth", UNSET))

        def _parse_monochromator(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        monochromator = _parse_monochromator(d.pop("monochromator", UNSET))

        def _parse_energy(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        energy = _parse_energy(d.pop("energy", UNSET))

        def _parse_transmission(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        transmission = _parse_transmission(d.pop("transmission", UNSET))

        def _parse_box_size_x(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        box_size_x = _parse_box_size_x(d.pop("boxSizeX", UNSET))

        def _parse_box_size_y(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        box_size_y = _parse_box_size_y(d.pop("boxSizeY", UNSET))

        def _parse_kappa_start(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        kappa_start = _parse_kappa_start(d.pop("kappaStart", UNSET))

        def _parse_axis_start(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        axis_start = _parse_axis_start(d.pop("axisStart", UNSET))

        def _parse_axis_range(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        axis_range = _parse_axis_range(d.pop("axisRange", UNSET))

        def _parse_number_of_images(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        number_of_images = _parse_number_of_images(d.pop("numberOfImages", UNSET))

        def _parse_preset_for_proposal_id(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        preset_for_proposal_id = _parse_preset_for_proposal_id(d.pop("presetForProposalId", UNSET))

        def _parse_beam_line_name(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        beam_line_name = _parse_beam_line_name(d.pop("beamLineName", UNSET))

        def _parse_centring_method(data: object) -> CentringMethod | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                centring_method_type_0 = CentringMethod(data)

                return centring_method_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(CentringMethod | None | Unset, data)

        centring_method = _parse_centring_method(d.pop("centringMethod", UNSET))

        def _parse_user_path(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        user_path = _parse_user_path(d.pop("userPath", UNSET))

        def _parse_robot_plate_temperature(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        robot_plate_temperature = _parse_robot_plate_temperature(d.pop("robotPlateTemperature", UNSET))

        def _parse_exposure_temperature(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        exposure_temperature = _parse_exposure_temperature(d.pop("exposureTemperature", UNSET))

        def _parse_purification_column_id(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        purification_column_id = _parse_purification_column_id(d.pop("purificationColumnId", UNSET))

        def _parse_experiment_type_id(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        experiment_type_id = _parse_experiment_type_id(d.pop("experimentTypeId", UNSET))

        def _parse_collection_mode(data: object) -> CollectionMode | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                collection_mode_type_0 = CollectionMode(data)

                return collection_mode_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(CollectionMode | None | Unset, data)

        collection_mode = _parse_collection_mode(d.pop("collectionMode", UNSET))

        def _parse_priority(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        priority = _parse_priority(d.pop("priority", UNSET))

        def _parse_q_min(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        q_min = _parse_q_min(d.pop("qMin", UNSET))

        def _parse_q_max(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        q_max = _parse_q_max(d.pop("qMax", UNSET))

        def _parse_reduction_parameters_averaging(data: object) -> None | ReductionParameters | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                reduction_parameters_averaging_type_0 = ReductionParameters(data)

                return reduction_parameters_averaging_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(None | ReductionParameters | Unset, data)

        reduction_parameters_averaging = _parse_reduction_parameters_averaging(
            d.pop("reductionParametersAveraging", UNSET)
        )

        def _parse_scan_parameters(
            data: object,
        ) -> DiffractionPlanOptionalScanParametersType0Type0 | None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                scan_parameters_type_0_type_0 = DiffractionPlanOptionalScanParametersType0Type0.from_dict(data)

                return scan_parameters_type_0_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(DiffractionPlanOptionalScanParametersType0Type0 | None | str | Unset, data)

        scan_parameters = _parse_scan_parameters(d.pop("scanParameters", UNSET))

        def _parse_strategy_option(data: object) -> None | str | StringSerialisedStrategyOptionType0 | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                componentsschemas_string_serialised_strategy_option_type_0 = (
                    StringSerialisedStrategyOptionType0.from_dict(data)
                )

                return componentsschemas_string_serialised_strategy_option_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(None | str | StringSerialisedStrategyOptionType0 | Unset, data)

        strategy_option = _parse_strategy_option(d.pop("strategyOption", UNSET))

        diffraction_plan_optional = cls(
            name=name,
            experiment_kind=experiment_kind,
            observed_resolution=observed_resolution,
            minimal_resolution=minimal_resolution,
            exposure_time=exposure_time,
            oscillation_range=oscillation_range,
            maximal_resolution=maximal_resolution,
            screening_resolution=screening_resolution,
            radiation_sensitivity=radiation_sensitivity,
            anomalous_scatterer=anomalous_scatterer,
            preferred_beam_size_x=preferred_beam_size_x,
            preferred_beam_size_y=preferred_beam_size_y,
            preferred_beam_diameter=preferred_beam_diameter,
            comments=comments,
            aimed_completeness=aimed_completeness,
            aimed_i_over_sigma_at_highest_res=aimed_i_over_sigma_at_highest_res,
            aimed_multiplicity=aimed_multiplicity,
            aimed_resolution=aimed_resolution,
            anomalous_data=anomalous_data,
            complexity=complexity,
            estimate_radiation_damage=estimate_radiation_damage,
            forced_space_group=forced_space_group,
            required_completeness=required_completeness,
            required_multiplicity=required_multiplicity,
            required_resolution=required_resolution,
            kappa_strategy_option=kappa_strategy_option,
            number_of_positions=number_of_positions,
            min_dim_accross_spindle_axis=min_dim_accross_spindle_axis,
            max_dim_accross_spindle_axis=max_dim_accross_spindle_axis,
            radiation_sensitivity_beta=radiation_sensitivity_beta,
            radiation_sensitivity_gamma=radiation_sensitivity_gamma,
            min_osc_width=min_osc_width,
            detector_id=detector_id,
            distance=distance,
            orientation=orientation,
            mono_bandwidth=mono_bandwidth,
            monochromator=monochromator,
            energy=energy,
            transmission=transmission,
            box_size_x=box_size_x,
            box_size_y=box_size_y,
            kappa_start=kappa_start,
            axis_start=axis_start,
            axis_range=axis_range,
            number_of_images=number_of_images,
            preset_for_proposal_id=preset_for_proposal_id,
            beam_line_name=beam_line_name,
            centring_method=centring_method,
            user_path=user_path,
            robot_plate_temperature=robot_plate_temperature,
            exposure_temperature=exposure_temperature,
            purification_column_id=purification_column_id,
            experiment_type_id=experiment_type_id,
            collection_mode=collection_mode,
            priority=priority,
            q_min=q_min,
            q_max=q_max,
            reduction_parameters_averaging=reduction_parameters_averaging,
            scan_parameters=scan_parameters,
            strategy_option=strategy_option,
        )

        diffraction_plan_optional.additional_properties = d
        return diffraction_plan_optional

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

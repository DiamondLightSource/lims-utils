from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.auto_proc_scaling_statistics_out_scalingstatisticstype import (
    AutoProcScalingStatisticsOutScalingstatisticstype,
)
from ..types import UNSET, Unset

T = TypeVar("T", bound="AutoProcScalingStatisticsOut")


@_attrs_define
class AutoProcScalingStatisticsOut:
    """
    Attributes:
        auto_proc_scaling_statistics_id (int):
        scaling_statistics_type (AutoProcScalingStatisticsOutScalingstatisticstype):
        r_merge (float | None | Unset):
        comments (None | str | Unset):
        fractional_partial_bias (float | None | Unset):
        resolution_limit_high (float | None | Unset):
        resolution_limit_low (float | None | Unset):
        r_meas_within_i_plus_i_minus (float | None | Unset):
        r_meas_all_i_plus_i_minus (float | None | Unset):
        r_pim_within_i_plus_i_minus (float | None | Unset):
        r_pim_all_i_plus_i_minus (float | None | Unset):
        cc_half (float | None | Unset):
        cc_anomalous (float | None | Unset):
        mean_i_over_sig_i (float | None | Unset):
        n_total_observations (int | None | Unset):
        res_i_over_sig_i2 (float | None | Unset):
        n_total_unique_observations (int | None | Unset):
        multiplicity (float | None | Unset):
        completeness (float | None | Unset):
        anomalous_completeness (float | None | Unset):
        anomalous_multiplicity (float | None | Unset):
    """

    auto_proc_scaling_statistics_id: int
    scaling_statistics_type: AutoProcScalingStatisticsOutScalingstatisticstype
    r_merge: float | None | Unset = UNSET
    comments: None | str | Unset = UNSET
    fractional_partial_bias: float | None | Unset = UNSET
    resolution_limit_high: float | None | Unset = UNSET
    resolution_limit_low: float | None | Unset = UNSET
    r_meas_within_i_plus_i_minus: float | None | Unset = UNSET
    r_meas_all_i_plus_i_minus: float | None | Unset = UNSET
    r_pim_within_i_plus_i_minus: float | None | Unset = UNSET
    r_pim_all_i_plus_i_minus: float | None | Unset = UNSET
    cc_half: float | None | Unset = UNSET
    cc_anomalous: float | None | Unset = UNSET
    mean_i_over_sig_i: float | None | Unset = UNSET
    n_total_observations: int | None | Unset = UNSET
    res_i_over_sig_i2: float | None | Unset = UNSET
    n_total_unique_observations: int | None | Unset = UNSET
    multiplicity: float | None | Unset = UNSET
    completeness: float | None | Unset = UNSET
    anomalous_completeness: float | None | Unset = UNSET
    anomalous_multiplicity: float | None | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        auto_proc_scaling_statistics_id = self.auto_proc_scaling_statistics_id

        scaling_statistics_type = self.scaling_statistics_type.value

        r_merge: float | None | Unset
        if isinstance(self.r_merge, Unset):
            r_merge = UNSET
        else:
            r_merge = self.r_merge

        comments: None | str | Unset
        if isinstance(self.comments, Unset):
            comments = UNSET
        else:
            comments = self.comments

        fractional_partial_bias: float | None | Unset
        if isinstance(self.fractional_partial_bias, Unset):
            fractional_partial_bias = UNSET
        else:
            fractional_partial_bias = self.fractional_partial_bias

        resolution_limit_high: float | None | Unset
        if isinstance(self.resolution_limit_high, Unset):
            resolution_limit_high = UNSET
        else:
            resolution_limit_high = self.resolution_limit_high

        resolution_limit_low: float | None | Unset
        if isinstance(self.resolution_limit_low, Unset):
            resolution_limit_low = UNSET
        else:
            resolution_limit_low = self.resolution_limit_low

        r_meas_within_i_plus_i_minus: float | None | Unset
        if isinstance(self.r_meas_within_i_plus_i_minus, Unset):
            r_meas_within_i_plus_i_minus = UNSET
        else:
            r_meas_within_i_plus_i_minus = self.r_meas_within_i_plus_i_minus

        r_meas_all_i_plus_i_minus: float | None | Unset
        if isinstance(self.r_meas_all_i_plus_i_minus, Unset):
            r_meas_all_i_plus_i_minus = UNSET
        else:
            r_meas_all_i_plus_i_minus = self.r_meas_all_i_plus_i_minus

        r_pim_within_i_plus_i_minus: float | None | Unset
        if isinstance(self.r_pim_within_i_plus_i_minus, Unset):
            r_pim_within_i_plus_i_minus = UNSET
        else:
            r_pim_within_i_plus_i_minus = self.r_pim_within_i_plus_i_minus

        r_pim_all_i_plus_i_minus: float | None | Unset
        if isinstance(self.r_pim_all_i_plus_i_minus, Unset):
            r_pim_all_i_plus_i_minus = UNSET
        else:
            r_pim_all_i_plus_i_minus = self.r_pim_all_i_plus_i_minus

        cc_half: float | None | Unset
        if isinstance(self.cc_half, Unset):
            cc_half = UNSET
        else:
            cc_half = self.cc_half

        cc_anomalous: float | None | Unset
        if isinstance(self.cc_anomalous, Unset):
            cc_anomalous = UNSET
        else:
            cc_anomalous = self.cc_anomalous

        mean_i_over_sig_i: float | None | Unset
        if isinstance(self.mean_i_over_sig_i, Unset):
            mean_i_over_sig_i = UNSET
        else:
            mean_i_over_sig_i = self.mean_i_over_sig_i

        n_total_observations: int | None | Unset
        if isinstance(self.n_total_observations, Unset):
            n_total_observations = UNSET
        else:
            n_total_observations = self.n_total_observations

        res_i_over_sig_i2: float | None | Unset
        if isinstance(self.res_i_over_sig_i2, Unset):
            res_i_over_sig_i2 = UNSET
        else:
            res_i_over_sig_i2 = self.res_i_over_sig_i2

        n_total_unique_observations: int | None | Unset
        if isinstance(self.n_total_unique_observations, Unset):
            n_total_unique_observations = UNSET
        else:
            n_total_unique_observations = self.n_total_unique_observations

        multiplicity: float | None | Unset
        if isinstance(self.multiplicity, Unset):
            multiplicity = UNSET
        else:
            multiplicity = self.multiplicity

        completeness: float | None | Unset
        if isinstance(self.completeness, Unset):
            completeness = UNSET
        else:
            completeness = self.completeness

        anomalous_completeness: float | None | Unset
        if isinstance(self.anomalous_completeness, Unset):
            anomalous_completeness = UNSET
        else:
            anomalous_completeness = self.anomalous_completeness

        anomalous_multiplicity: float | None | Unset
        if isinstance(self.anomalous_multiplicity, Unset):
            anomalous_multiplicity = UNSET
        else:
            anomalous_multiplicity = self.anomalous_multiplicity

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "autoProcScalingStatisticsId": auto_proc_scaling_statistics_id,
                "scalingStatisticsType": scaling_statistics_type,
            }
        )
        if r_merge is not UNSET:
            field_dict["rMerge"] = r_merge
        if comments is not UNSET:
            field_dict["comments"] = comments
        if fractional_partial_bias is not UNSET:
            field_dict["fractionalPartialBias"] = fractional_partial_bias
        if resolution_limit_high is not UNSET:
            field_dict["resolutionLimitHigh"] = resolution_limit_high
        if resolution_limit_low is not UNSET:
            field_dict["resolutionLimitLow"] = resolution_limit_low
        if r_meas_within_i_plus_i_minus is not UNSET:
            field_dict["rMeasWithinIPlusIMinus"] = r_meas_within_i_plus_i_minus
        if r_meas_all_i_plus_i_minus is not UNSET:
            field_dict["rMeasAllIPlusIMinus"] = r_meas_all_i_plus_i_minus
        if r_pim_within_i_plus_i_minus is not UNSET:
            field_dict["rPimWithinIPlusIMinus"] = r_pim_within_i_plus_i_minus
        if r_pim_all_i_plus_i_minus is not UNSET:
            field_dict["rPimAllIPlusIMinus"] = r_pim_all_i_plus_i_minus
        if cc_half is not UNSET:
            field_dict["ccHalf"] = cc_half
        if cc_anomalous is not UNSET:
            field_dict["ccAnomalous"] = cc_anomalous
        if mean_i_over_sig_i is not UNSET:
            field_dict["meanIOverSigI"] = mean_i_over_sig_i
        if n_total_observations is not UNSET:
            field_dict["nTotalObservations"] = n_total_observations
        if res_i_over_sig_i2 is not UNSET:
            field_dict["resIOverSigI2"] = res_i_over_sig_i2
        if n_total_unique_observations is not UNSET:
            field_dict["nTotalUniqueObservations"] = n_total_unique_observations
        if multiplicity is not UNSET:
            field_dict["multiplicity"] = multiplicity
        if completeness is not UNSET:
            field_dict["completeness"] = completeness
        if anomalous_completeness is not UNSET:
            field_dict["anomalousCompleteness"] = anomalous_completeness
        if anomalous_multiplicity is not UNSET:
            field_dict["anomalousMultiplicity"] = anomalous_multiplicity

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        auto_proc_scaling_statistics_id = d.pop("autoProcScalingStatisticsId")

        scaling_statistics_type = AutoProcScalingStatisticsOutScalingstatisticstype(d.pop("scalingStatisticsType"))

        def _parse_r_merge(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        r_merge = _parse_r_merge(d.pop("rMerge", UNSET))

        def _parse_comments(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        comments = _parse_comments(d.pop("comments", UNSET))

        def _parse_fractional_partial_bias(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        fractional_partial_bias = _parse_fractional_partial_bias(d.pop("fractionalPartialBias", UNSET))

        def _parse_resolution_limit_high(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        resolution_limit_high = _parse_resolution_limit_high(d.pop("resolutionLimitHigh", UNSET))

        def _parse_resolution_limit_low(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        resolution_limit_low = _parse_resolution_limit_low(d.pop("resolutionLimitLow", UNSET))

        def _parse_r_meas_within_i_plus_i_minus(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        r_meas_within_i_plus_i_minus = _parse_r_meas_within_i_plus_i_minus(d.pop("rMeasWithinIPlusIMinus", UNSET))

        def _parse_r_meas_all_i_plus_i_minus(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        r_meas_all_i_plus_i_minus = _parse_r_meas_all_i_plus_i_minus(d.pop("rMeasAllIPlusIMinus", UNSET))

        def _parse_r_pim_within_i_plus_i_minus(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        r_pim_within_i_plus_i_minus = _parse_r_pim_within_i_plus_i_minus(d.pop("rPimWithinIPlusIMinus", UNSET))

        def _parse_r_pim_all_i_plus_i_minus(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        r_pim_all_i_plus_i_minus = _parse_r_pim_all_i_plus_i_minus(d.pop("rPimAllIPlusIMinus", UNSET))

        def _parse_cc_half(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        cc_half = _parse_cc_half(d.pop("ccHalf", UNSET))

        def _parse_cc_anomalous(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        cc_anomalous = _parse_cc_anomalous(d.pop("ccAnomalous", UNSET))

        def _parse_mean_i_over_sig_i(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        mean_i_over_sig_i = _parse_mean_i_over_sig_i(d.pop("meanIOverSigI", UNSET))

        def _parse_n_total_observations(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        n_total_observations = _parse_n_total_observations(d.pop("nTotalObservations", UNSET))

        def _parse_res_i_over_sig_i2(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        res_i_over_sig_i2 = _parse_res_i_over_sig_i2(d.pop("resIOverSigI2", UNSET))

        def _parse_n_total_unique_observations(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        n_total_unique_observations = _parse_n_total_unique_observations(d.pop("nTotalUniqueObservations", UNSET))

        def _parse_multiplicity(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        multiplicity = _parse_multiplicity(d.pop("multiplicity", UNSET))

        def _parse_completeness(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        completeness = _parse_completeness(d.pop("completeness", UNSET))

        def _parse_anomalous_completeness(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        anomalous_completeness = _parse_anomalous_completeness(d.pop("anomalousCompleteness", UNSET))

        def _parse_anomalous_multiplicity(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        anomalous_multiplicity = _parse_anomalous_multiplicity(d.pop("anomalousMultiplicity", UNSET))

        auto_proc_scaling_statistics_out = cls(
            auto_proc_scaling_statistics_id=auto_proc_scaling_statistics_id,
            scaling_statistics_type=scaling_statistics_type,
            r_merge=r_merge,
            comments=comments,
            fractional_partial_bias=fractional_partial_bias,
            resolution_limit_high=resolution_limit_high,
            resolution_limit_low=resolution_limit_low,
            r_meas_within_i_plus_i_minus=r_meas_within_i_plus_i_minus,
            r_meas_all_i_plus_i_minus=r_meas_all_i_plus_i_minus,
            r_pim_within_i_plus_i_minus=r_pim_within_i_plus_i_minus,
            r_pim_all_i_plus_i_minus=r_pim_all_i_plus_i_minus,
            cc_half=cc_half,
            cc_anomalous=cc_anomalous,
            mean_i_over_sig_i=mean_i_over_sig_i,
            n_total_observations=n_total_observations,
            res_i_over_sig_i2=res_i_over_sig_i2,
            n_total_unique_observations=n_total_unique_observations,
            multiplicity=multiplicity,
            completeness=completeness,
            anomalous_completeness=anomalous_completeness,
            anomalous_multiplicity=anomalous_multiplicity,
        )

        auto_proc_scaling_statistics_out.additional_properties = d
        return auto_proc_scaling_statistics_out

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

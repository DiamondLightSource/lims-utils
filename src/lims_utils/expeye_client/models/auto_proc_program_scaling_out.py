from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.auto_proc_program_scaling_out_scaling_statistics_type_type_0 import (
    AutoProcProgramScalingOutScalingStatisticsTypeType0,
)
from ..types import UNSET, Unset

T = TypeVar("T", bound="AutoProcProgramScalingOut")


@_attrs_define
class AutoProcProgramScalingOut:
    """
    Attributes:
        cc_half (float | None | Unset):
        cc_anomalous (float | None | Unset):
        resolution_limit_low (float | None | Unset):
        resolution_limit_high (float | None | Unset):
        r_merge (float | None | Unset):
        r_meas (float | None | Unset):
        mean_i_over_sig_i (float | None | Unset):
        anomalous_completeness (float | None | Unset):
        completeness (float | None | Unset):
        multiplicity (float | None | Unset):
        res_i_over_sig_i2 (float | None | Unset):
        recipe (None | str | Unset):
        scaling_statistics_type (AutoProcProgramScalingOutScalingStatisticsTypeType0 | None | Unset):
    """

    cc_half: float | None | Unset = UNSET
    cc_anomalous: float | None | Unset = UNSET
    resolution_limit_low: float | None | Unset = UNSET
    resolution_limit_high: float | None | Unset = UNSET
    r_merge: float | None | Unset = UNSET
    r_meas: float | None | Unset = UNSET
    mean_i_over_sig_i: float | None | Unset = UNSET
    anomalous_completeness: float | None | Unset = UNSET
    completeness: float | None | Unset = UNSET
    multiplicity: float | None | Unset = UNSET
    res_i_over_sig_i2: float | None | Unset = UNSET
    recipe: None | str | Unset = UNSET
    scaling_statistics_type: AutoProcProgramScalingOutScalingStatisticsTypeType0 | None | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
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

        resolution_limit_low: float | None | Unset
        if isinstance(self.resolution_limit_low, Unset):
            resolution_limit_low = UNSET
        else:
            resolution_limit_low = self.resolution_limit_low

        resolution_limit_high: float | None | Unset
        if isinstance(self.resolution_limit_high, Unset):
            resolution_limit_high = UNSET
        else:
            resolution_limit_high = self.resolution_limit_high

        r_merge: float | None | Unset
        if isinstance(self.r_merge, Unset):
            r_merge = UNSET
        else:
            r_merge = self.r_merge

        r_meas: float | None | Unset
        if isinstance(self.r_meas, Unset):
            r_meas = UNSET
        else:
            r_meas = self.r_meas

        mean_i_over_sig_i: float | None | Unset
        if isinstance(self.mean_i_over_sig_i, Unset):
            mean_i_over_sig_i = UNSET
        else:
            mean_i_over_sig_i = self.mean_i_over_sig_i

        anomalous_completeness: float | None | Unset
        if isinstance(self.anomalous_completeness, Unset):
            anomalous_completeness = UNSET
        else:
            anomalous_completeness = self.anomalous_completeness

        completeness: float | None | Unset
        if isinstance(self.completeness, Unset):
            completeness = UNSET
        else:
            completeness = self.completeness

        multiplicity: float | None | Unset
        if isinstance(self.multiplicity, Unset):
            multiplicity = UNSET
        else:
            multiplicity = self.multiplicity

        res_i_over_sig_i2: float | None | Unset
        if isinstance(self.res_i_over_sig_i2, Unset):
            res_i_over_sig_i2 = UNSET
        else:
            res_i_over_sig_i2 = self.res_i_over_sig_i2

        recipe: None | str | Unset
        if isinstance(self.recipe, Unset):
            recipe = UNSET
        else:
            recipe = self.recipe

        scaling_statistics_type: None | str | Unset
        if isinstance(self.scaling_statistics_type, Unset):
            scaling_statistics_type = UNSET
        elif isinstance(self.scaling_statistics_type, AutoProcProgramScalingOutScalingStatisticsTypeType0):
            scaling_statistics_type = self.scaling_statistics_type.value
        else:
            scaling_statistics_type = self.scaling_statistics_type

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if cc_half is not UNSET:
            field_dict["ccHalf"] = cc_half
        if cc_anomalous is not UNSET:
            field_dict["ccAnomalous"] = cc_anomalous
        if resolution_limit_low is not UNSET:
            field_dict["resolutionLimitLow"] = resolution_limit_low
        if resolution_limit_high is not UNSET:
            field_dict["resolutionLimitHigh"] = resolution_limit_high
        if r_merge is not UNSET:
            field_dict["rMerge"] = r_merge
        if r_meas is not UNSET:
            field_dict["rMeas"] = r_meas
        if mean_i_over_sig_i is not UNSET:
            field_dict["meanIOverSigI"] = mean_i_over_sig_i
        if anomalous_completeness is not UNSET:
            field_dict["anomalousCompleteness"] = anomalous_completeness
        if completeness is not UNSET:
            field_dict["completeness"] = completeness
        if multiplicity is not UNSET:
            field_dict["multiplicity"] = multiplicity
        if res_i_over_sig_i2 is not UNSET:
            field_dict["resIOverSigI2"] = res_i_over_sig_i2
        if recipe is not UNSET:
            field_dict["recipe"] = recipe
        if scaling_statistics_type is not UNSET:
            field_dict["scalingStatisticsType"] = scaling_statistics_type

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)

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

        def _parse_resolution_limit_low(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        resolution_limit_low = _parse_resolution_limit_low(d.pop("resolutionLimitLow", UNSET))

        def _parse_resolution_limit_high(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        resolution_limit_high = _parse_resolution_limit_high(d.pop("resolutionLimitHigh", UNSET))

        def _parse_r_merge(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        r_merge = _parse_r_merge(d.pop("rMerge", UNSET))

        def _parse_r_meas(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        r_meas = _parse_r_meas(d.pop("rMeas", UNSET))

        def _parse_mean_i_over_sig_i(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        mean_i_over_sig_i = _parse_mean_i_over_sig_i(d.pop("meanIOverSigI", UNSET))

        def _parse_anomalous_completeness(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        anomalous_completeness = _parse_anomalous_completeness(d.pop("anomalousCompleteness", UNSET))

        def _parse_completeness(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        completeness = _parse_completeness(d.pop("completeness", UNSET))

        def _parse_multiplicity(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        multiplicity = _parse_multiplicity(d.pop("multiplicity", UNSET))

        def _parse_res_i_over_sig_i2(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        res_i_over_sig_i2 = _parse_res_i_over_sig_i2(d.pop("resIOverSigI2", UNSET))

        def _parse_recipe(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        recipe = _parse_recipe(d.pop("recipe", UNSET))

        def _parse_scaling_statistics_type(
            data: object,
        ) -> AutoProcProgramScalingOutScalingStatisticsTypeType0 | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                scaling_statistics_type_type_0 = AutoProcProgramScalingOutScalingStatisticsTypeType0(data)

                return scaling_statistics_type_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(AutoProcProgramScalingOutScalingStatisticsTypeType0 | None | Unset, data)

        scaling_statistics_type = _parse_scaling_statistics_type(d.pop("scalingStatisticsType", UNSET))

        auto_proc_program_scaling_out = cls(
            cc_half=cc_half,
            cc_anomalous=cc_anomalous,
            resolution_limit_low=resolution_limit_low,
            resolution_limit_high=resolution_limit_high,
            r_merge=r_merge,
            r_meas=r_meas,
            mean_i_over_sig_i=mean_i_over_sig_i,
            anomalous_completeness=anomalous_completeness,
            completeness=completeness,
            multiplicity=multiplicity,
            res_i_over_sig_i2=res_i_over_sig_i2,
            recipe=recipe,
            scaling_statistics_type=scaling_statistics_type,
        )

        auto_proc_program_scaling_out.additional_properties = d
        return auto_proc_program_scaling_out

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

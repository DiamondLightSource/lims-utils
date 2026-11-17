from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.auto_proc_scaling_statistics_out import AutoProcScalingStatisticsOut


T = TypeVar("T", bound="AutoProcWithScalingOut")


@_attrs_define
class AutoProcWithScalingOut:
    """
    Attributes:
        auto_proc_id (int):
        outer_shell_statistics (AutoProcScalingStatisticsOut | None | Unset):
        inner_shell_statistics (AutoProcScalingStatisticsOut | None | Unset):
        overall_statistics (AutoProcScalingStatisticsOut | None | Unset):
        space_group (None | str | Unset):
        cell_a (float | None | Unset):
        cell_b (float | None | Unset):
        cell_c (float | None | Unset):
        cell_alpha (float | None | Unset):
        cell_beta (float | None | Unset):
        cell_gamma (float | None | Unset):
    """

    auto_proc_id: int
    outer_shell_statistics: AutoProcScalingStatisticsOut | None | Unset = UNSET
    inner_shell_statistics: AutoProcScalingStatisticsOut | None | Unset = UNSET
    overall_statistics: AutoProcScalingStatisticsOut | None | Unset = UNSET
    space_group: None | str | Unset = UNSET
    cell_a: float | None | Unset = UNSET
    cell_b: float | None | Unset = UNSET
    cell_c: float | None | Unset = UNSET
    cell_alpha: float | None | Unset = UNSET
    cell_beta: float | None | Unset = UNSET
    cell_gamma: float | None | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.auto_proc_scaling_statistics_out import AutoProcScalingStatisticsOut

        auto_proc_id = self.auto_proc_id

        outer_shell_statistics: dict[str, Any] | None | Unset
        if isinstance(self.outer_shell_statistics, Unset):
            outer_shell_statistics = UNSET
        elif isinstance(self.outer_shell_statistics, AutoProcScalingStatisticsOut):
            outer_shell_statistics = self.outer_shell_statistics.to_dict()
        else:
            outer_shell_statistics = self.outer_shell_statistics

        inner_shell_statistics: dict[str, Any] | None | Unset
        if isinstance(self.inner_shell_statistics, Unset):
            inner_shell_statistics = UNSET
        elif isinstance(self.inner_shell_statistics, AutoProcScalingStatisticsOut):
            inner_shell_statistics = self.inner_shell_statistics.to_dict()
        else:
            inner_shell_statistics = self.inner_shell_statistics

        overall_statistics: dict[str, Any] | None | Unset
        if isinstance(self.overall_statistics, Unset):
            overall_statistics = UNSET
        elif isinstance(self.overall_statistics, AutoProcScalingStatisticsOut):
            overall_statistics = self.overall_statistics.to_dict()
        else:
            overall_statistics = self.overall_statistics

        space_group: None | str | Unset
        if isinstance(self.space_group, Unset):
            space_group = UNSET
        else:
            space_group = self.space_group

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
                "autoProcId": auto_proc_id,
            }
        )
        if outer_shell_statistics is not UNSET:
            field_dict["outerShellStatistics"] = outer_shell_statistics
        if inner_shell_statistics is not UNSET:
            field_dict["innerShellStatistics"] = inner_shell_statistics
        if overall_statistics is not UNSET:
            field_dict["overallStatistics"] = overall_statistics
        if space_group is not UNSET:
            field_dict["spaceGroup"] = space_group
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
        from ..models.auto_proc_scaling_statistics_out import AutoProcScalingStatisticsOut

        d = dict(src_dict)
        auto_proc_id = d.pop("autoProcId")

        def _parse_outer_shell_statistics(data: object) -> AutoProcScalingStatisticsOut | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                outer_shell_statistics_type_0 = AutoProcScalingStatisticsOut.from_dict(data)

                return outer_shell_statistics_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(AutoProcScalingStatisticsOut | None | Unset, data)

        outer_shell_statistics = _parse_outer_shell_statistics(d.pop("outerShellStatistics", UNSET))

        def _parse_inner_shell_statistics(data: object) -> AutoProcScalingStatisticsOut | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                inner_shell_statistics_type_0 = AutoProcScalingStatisticsOut.from_dict(data)

                return inner_shell_statistics_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(AutoProcScalingStatisticsOut | None | Unset, data)

        inner_shell_statistics = _parse_inner_shell_statistics(d.pop("innerShellStatistics", UNSET))

        def _parse_overall_statistics(data: object) -> AutoProcScalingStatisticsOut | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                overall_statistics_type_0 = AutoProcScalingStatisticsOut.from_dict(data)

                return overall_statistics_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(AutoProcScalingStatisticsOut | None | Unset, data)

        overall_statistics = _parse_overall_statistics(d.pop("overallStatistics", UNSET))

        def _parse_space_group(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        space_group = _parse_space_group(d.pop("spaceGroup", UNSET))

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

        auto_proc_with_scaling_out = cls(
            auto_proc_id=auto_proc_id,
            outer_shell_statistics=outer_shell_statistics,
            inner_shell_statistics=inner_shell_statistics,
            overall_statistics=overall_statistics,
            space_group=space_group,
            cell_a=cell_a,
            cell_b=cell_b,
            cell_c=cell_c,
            cell_alpha=cell_alpha,
            cell_beta=cell_beta,
            cell_gamma=cell_gamma,
        )

        auto_proc_with_scaling_out.additional_properties = d
        return auto_proc_with_scaling_out

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

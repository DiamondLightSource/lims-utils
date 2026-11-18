from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.combinator import Combinator
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.processing_job_rule import ProcessingJobRule


T = TypeVar("T", bound="ProcessingJobCombinator")


@_attrs_define
class ProcessingJobCombinator:
    """
    Attributes:
        combinator (Combinator | Unset):
        not_ (bool | Unset):  Default: False.
        rules (list[ProcessingJobCombinator | ProcessingJobRule] | Unset):
    """

    combinator: Combinator | Unset = UNSET
    not_: bool | Unset = False
    rules: list[ProcessingJobCombinator | ProcessingJobRule] | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.processing_job_rule import ProcessingJobRule  # noqa: PLC0415

        combinator: str | Unset = UNSET
        if not isinstance(self.combinator, Unset):
            combinator = self.combinator.value

        not_ = self.not_

        rules: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.rules, Unset):
            rules = []
            for rules_item_data in self.rules:
                rules_item: dict[str, Any]
                if isinstance(rules_item_data, ProcessingJobRule):
                    rules_item = rules_item_data.to_dict()
                else:
                    rules_item = rules_item_data.to_dict()

                rules.append(rules_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if combinator is not UNSET:
            field_dict["combinator"] = combinator
        if not_ is not UNSET:
            field_dict["not"] = not_
        if rules is not UNSET:
            field_dict["rules"] = rules

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.processing_job_rule import ProcessingJobRule  # noqa: PLC0415

        d = dict(src_dict)
        _combinator = d.pop("combinator", UNSET)
        combinator: Combinator | Unset
        if isinstance(_combinator, Unset):
            combinator = UNSET
        else:
            combinator = Combinator(_combinator)

        not_ = d.pop("not", UNSET)

        _rules = d.pop("rules", UNSET)
        rules: list[ProcessingJobCombinator | ProcessingJobRule] | Unset = UNSET
        if _rules is not UNSET:
            rules = []
            for rules_item_data in _rules:

                def _parse_rules_item(data: object) -> ProcessingJobCombinator | ProcessingJobRule:
                    try:
                        if not isinstance(data, dict):
                            raise TypeError()
                        rules_item_type_0 = ProcessingJobRule.from_dict(data)

                        return rules_item_type_0
                    except (TypeError, ValueError, AttributeError, KeyError):
                        pass
                    if not isinstance(data, dict):
                        raise TypeError()
                    rules_item_type_1 = ProcessingJobCombinator.from_dict(data)

                    return rules_item_type_1

                rules_item = _parse_rules_item(rules_item_data)

                rules.append(rules_item)

        processing_job_combinator = cls(
            combinator=combinator,
            not_=not_,
            rules=rules,
        )

        processing_job_combinator.additional_properties = d
        return processing_job_combinator

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

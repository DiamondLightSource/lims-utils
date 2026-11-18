from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.operator import Operator

T = TypeVar("T", bound="ProcessingJobRule")


@_attrs_define
class ProcessingJobRule:
    """
    Attributes:
        field (str):
        value (bool | float | int | list[bool | float | int | str] | str):
        operator (Operator):
    """

    field: str
    value: bool | float | int | list[bool | float | int | str] | str
    operator: Operator
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        field = self.field

        value: bool | float | int | list[bool | float | int | str] | str
        if isinstance(self.value, list):
            value = []
            for value_type_4_item_data in self.value:
                value_type_4_item: bool | float | int | str
                value_type_4_item = value_type_4_item_data
                value.append(value_type_4_item)

        else:
            value = self.value

        operator = self.operator.value

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "field": field,
                "value": value,
                "operator": operator,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        field = d.pop("field")

        def _parse_value(data: object) -> bool | float | int | list[bool | float | int | str] | str:
            try:
                if not isinstance(data, list):
                    raise TypeError()
                value_type_4 = []
                _value_type_4 = data
                for value_type_4_item_data in _value_type_4:

                    def _parse_value_type_4_item(data: object) -> bool | float | int | str:
                        return cast(bool | float | int | str, data)

                    value_type_4_item = _parse_value_type_4_item(value_type_4_item_data)

                    value_type_4.append(value_type_4_item)

                return value_type_4
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(bool | float | int | list[bool | float | int | str] | str, data)

        value = _parse_value(d.pop("value"))

        operator = Operator(d.pop("operator"))

        processing_job_rule = cls(
            field=field,
            value=value,
            operator=operator,
        )

        processing_job_rule.additional_properties = d
        return processing_job_rule

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

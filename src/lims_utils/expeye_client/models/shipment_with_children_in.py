from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.safety_levels import SafetyLevels
from ..models.shipment_safety_levels import ShipmentSafetyLevels
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.dewar_with_children_in import DewarWithChildrenIn
    from ..models.shipment_with_children_in_extra_type_0_type_0 import ShipmentWithChildrenInExtraType0Type0


T = TypeVar("T", bound="ShipmentWithChildrenIn")


@_attrs_define
class ShipmentWithChildrenIn:
    """
    Attributes:
        children (list[DewarWithChildrenIn]):
        creation_date (datetime.datetime | None | Unset):
        shipping_name (None | str | Unset):
        extra (None | ShipmentWithChildrenInExtraType0Type0 | str | Unset):
        comments (None | str | Unset):
        shipping_status (None | str | Unset):
        source (None | str | Unset):
        safety_level (None | SafetyLevels | ShipmentSafetyLevels | Unset):
    """

    children: list[DewarWithChildrenIn]
    creation_date: datetime.datetime | None | Unset = UNSET
    shipping_name: None | str | Unset = UNSET
    extra: None | ShipmentWithChildrenInExtraType0Type0 | str | Unset = UNSET
    comments: None | str | Unset = UNSET
    shipping_status: None | str | Unset = UNSET
    source: None | str | Unset = UNSET
    safety_level: None | SafetyLevels | ShipmentSafetyLevels | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.shipment_with_children_in_extra_type_0_type_0 import ShipmentWithChildrenInExtraType0Type0  # noqa: PLC0415

        children = []
        for children_item_data in self.children:
            children_item = children_item_data.to_dict()
            children.append(children_item)

        creation_date: None | str | Unset
        if isinstance(self.creation_date, Unset):
            creation_date = UNSET
        elif isinstance(self.creation_date, datetime.datetime):
            creation_date = self.creation_date.isoformat()
        else:
            creation_date = self.creation_date

        shipping_name: None | str | Unset
        if isinstance(self.shipping_name, Unset):
            shipping_name = UNSET
        else:
            shipping_name = self.shipping_name

        extra: dict[str, Any] | None | str | Unset
        if isinstance(self.extra, Unset):
            extra = UNSET
        elif isinstance(self.extra, ShipmentWithChildrenInExtraType0Type0):
            extra = self.extra.to_dict()
        else:
            extra = self.extra

        comments: None | str | Unset
        if isinstance(self.comments, Unset):
            comments = UNSET
        else:
            comments = self.comments

        shipping_status: None | str | Unset
        if isinstance(self.shipping_status, Unset):
            shipping_status = UNSET
        else:
            shipping_status = self.shipping_status

        source: None | str | Unset
        if isinstance(self.source, Unset):
            source = UNSET
        else:
            source = self.source

        safety_level: None | str | Unset
        if isinstance(self.safety_level, Unset):
            safety_level = UNSET
        elif isinstance(self.safety_level, SafetyLevels):
            safety_level = self.safety_level.value
        elif isinstance(self.safety_level, ShipmentSafetyLevels):
            safety_level = self.safety_level.value
        else:
            safety_level = self.safety_level

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "children": children,
            }
        )
        if creation_date is not UNSET:
            field_dict["creationDate"] = creation_date
        if shipping_name is not UNSET:
            field_dict["shippingName"] = shipping_name
        if extra is not UNSET:
            field_dict["extra"] = extra
        if comments is not UNSET:
            field_dict["comments"] = comments
        if shipping_status is not UNSET:
            field_dict["shippingStatus"] = shipping_status
        if source is not UNSET:
            field_dict["source"] = source
        if safety_level is not UNSET:
            field_dict["safetyLevel"] = safety_level

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.dewar_with_children_in import DewarWithChildrenIn  # noqa: PLC0415
        from ..models.shipment_with_children_in_extra_type_0_type_0 import ShipmentWithChildrenInExtraType0Type0  # noqa: PLC0415

        d = dict(src_dict)
        children = []
        _children = d.pop("children")
        for children_item_data in _children:
            children_item = DewarWithChildrenIn.from_dict(children_item_data)

            children.append(children_item)

        def _parse_creation_date(data: object) -> datetime.datetime | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                creation_date_type_0 = datetime.datetime.fromisoformat(data)

                return creation_date_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(datetime.datetime | None | Unset, data)

        creation_date = _parse_creation_date(d.pop("creationDate", UNSET))

        def _parse_shipping_name(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        shipping_name = _parse_shipping_name(d.pop("shippingName", UNSET))

        def _parse_extra(data: object) -> None | ShipmentWithChildrenInExtraType0Type0 | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                extra_type_0_type_0 = ShipmentWithChildrenInExtraType0Type0.from_dict(data)

                return extra_type_0_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(None | ShipmentWithChildrenInExtraType0Type0 | str | Unset, data)

        extra = _parse_extra(d.pop("extra", UNSET))

        def _parse_comments(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        comments = _parse_comments(d.pop("comments", UNSET))

        def _parse_shipping_status(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        shipping_status = _parse_shipping_status(d.pop("shippingStatus", UNSET))

        def _parse_source(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        source = _parse_source(d.pop("source", UNSET))

        def _parse_safety_level(data: object) -> None | SafetyLevels | ShipmentSafetyLevels | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                safety_level_type_0 = SafetyLevels(data)

                return safety_level_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            try:
                if not isinstance(data, str):
                    raise TypeError()
                safety_level_type_1 = ShipmentSafetyLevels(data)

                return safety_level_type_1
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(None | SafetyLevels | ShipmentSafetyLevels | Unset, data)

        safety_level = _parse_safety_level(d.pop("safetyLevel", UNSET))

        shipment_with_children_in = cls(
            children=children,
            creation_date=creation_date,
            shipping_name=shipping_name,
            extra=extra,
            comments=comments,
            shipping_status=shipping_status,
            source=source,
            safety_level=safety_level,
        )

        shipment_with_children_in.additional_properties = d
        return shipment_with_children_in

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

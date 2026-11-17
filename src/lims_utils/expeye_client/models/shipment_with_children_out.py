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
    from ..models.dewar_with_children_out import DewarWithChildrenOut
    from ..models.shipment_with_children_out_extra_type_0_type_0 import ShipmentWithChildrenOutExtraType0Type0


T = TypeVar("T", bound="ShipmentWithChildrenOut")


@_attrs_define
class ShipmentWithChildrenOut:
    """
    Attributes:
        shipping_id (int):
        creation_date (datetime.datetime | None | Unset):
        shipping_name (None | str | Unset):
        extra (None | ShipmentWithChildrenOutExtraType0Type0 | str | Unset):
        comments (None | str | Unset):
        shipping_status (None | str | Unset):
        source (None | str | Unset):
        safety_level (None | SafetyLevels | ShipmentSafetyLevels | Unset):
        protein_id (int | None | Unset):
        children (list[DewarWithChildrenOut] | Unset):
    """

    shipping_id: int
    creation_date: datetime.datetime | None | Unset = UNSET
    shipping_name: None | str | Unset = UNSET
    extra: None | ShipmentWithChildrenOutExtraType0Type0 | str | Unset = UNSET
    comments: None | str | Unset = UNSET
    shipping_status: None | str | Unset = UNSET
    source: None | str | Unset = UNSET
    safety_level: None | SafetyLevels | ShipmentSafetyLevels | Unset = UNSET
    protein_id: int | None | Unset = UNSET
    children: list[DewarWithChildrenOut] | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.shipment_with_children_out_extra_type_0_type_0 import (
            ShipmentWithChildrenOutExtraType0Type0,
        )

        shipping_id = self.shipping_id

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
        elif isinstance(self.extra, ShipmentWithChildrenOutExtraType0Type0):
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

        protein_id: int | None | Unset
        if isinstance(self.protein_id, Unset):
            protein_id = UNSET
        else:
            protein_id = self.protein_id

        children: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.children, Unset):
            children = []
            for children_item_data in self.children:
                children_item = children_item_data.to_dict()
                children.append(children_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "shippingId": shipping_id,
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
        if protein_id is not UNSET:
            field_dict["proteinId"] = protein_id
        if children is not UNSET:
            field_dict["children"] = children

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.dewar_with_children_out import DewarWithChildrenOut
        from ..models.shipment_with_children_out_extra_type_0_type_0 import (
            ShipmentWithChildrenOutExtraType0Type0,
        )

        d = dict(src_dict)
        shipping_id = d.pop("shippingId")

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

        def _parse_extra(data: object) -> None | ShipmentWithChildrenOutExtraType0Type0 | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                extra_type_0_type_0 = ShipmentWithChildrenOutExtraType0Type0.from_dict(data)

                return extra_type_0_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(None | ShipmentWithChildrenOutExtraType0Type0 | str | Unset, data)

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

        def _parse_protein_id(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        protein_id = _parse_protein_id(d.pop("proteinId", UNSET))

        _children = d.pop("children", UNSET)
        children: list[DewarWithChildrenOut] | Unset = UNSET
        if _children is not UNSET:
            children = []
            for children_item_data in _children:
                children_item = DewarWithChildrenOut.from_dict(children_item_data)

                children.append(children_item)

        shipment_with_children_out = cls(
            shipping_id=shipping_id,
            creation_date=creation_date,
            shipping_name=shipping_name,
            extra=extra,
            comments=comments,
            shipping_status=shipping_status,
            source=source,
            safety_level=safety_level,
            protein_id=protein_id,
            children=children,
        )

        shipment_with_children_out.additional_properties = d
        return shipment_with_children_out

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

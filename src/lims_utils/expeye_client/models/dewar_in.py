from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.dewar_in_extra_type_0_type_0 import DewarInExtraType0Type0


T = TypeVar("T", bound="DewarIn")


@_attrs_define
class DewarIn:
    """
    Attributes:
        weight (float | None | Unset):
        extra (DewarInExtraType0Type0 | None | str | Unset):
        first_experiment_id (int | None | Unset):
        code (None | str | Unset): Code used to uniquely identify physical dewars/top level containers
        facility_code (None | str | Unset):
        dewar_status (None | str | Unset):
        storage_location (None | str | Unset):
        is_storage_dewar (bool | None | Unset):
        barcode (None | str | Unset): Barcode used for internal tracking, one is used for each journey to Diamond
        comments (None | str | Unset):
        source (None | str | Unset):
        dewar_registry_id (int | None | Unset):
        tracking_number_to_synchrotron (None | str | Unset):
        tracking_number_from_synchrotron (None | str | Unset):
        bl_time_stamp (datetime.datetime | None | Unset):
    """

    weight: float | None | Unset = UNSET
    extra: DewarInExtraType0Type0 | None | str | Unset = UNSET
    first_experiment_id: int | None | Unset = UNSET
    code: None | str | Unset = UNSET
    facility_code: None | str | Unset = UNSET
    dewar_status: None | str | Unset = UNSET
    storage_location: None | str | Unset = UNSET
    is_storage_dewar: bool | None | Unset = UNSET
    barcode: None | str | Unset = UNSET
    comments: None | str | Unset = UNSET
    source: None | str | Unset = UNSET
    dewar_registry_id: int | None | Unset = UNSET
    tracking_number_to_synchrotron: None | str | Unset = UNSET
    tracking_number_from_synchrotron: None | str | Unset = UNSET
    bl_time_stamp: datetime.datetime | None | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.dewar_in_extra_type_0_type_0 import DewarInExtraType0Type0

        weight: float | None | Unset
        if isinstance(self.weight, Unset):
            weight = UNSET
        else:
            weight = self.weight

        extra: dict[str, Any] | None | str | Unset
        if isinstance(self.extra, Unset):
            extra = UNSET
        elif isinstance(self.extra, DewarInExtraType0Type0):
            extra = self.extra.to_dict()
        else:
            extra = self.extra

        first_experiment_id: int | None | Unset
        if isinstance(self.first_experiment_id, Unset):
            first_experiment_id = UNSET
        else:
            first_experiment_id = self.first_experiment_id

        code: None | str | Unset
        if isinstance(self.code, Unset):
            code = UNSET
        else:
            code = self.code

        facility_code: None | str | Unset
        if isinstance(self.facility_code, Unset):
            facility_code = UNSET
        else:
            facility_code = self.facility_code

        dewar_status: None | str | Unset
        if isinstance(self.dewar_status, Unset):
            dewar_status = UNSET
        else:
            dewar_status = self.dewar_status

        storage_location: None | str | Unset
        if isinstance(self.storage_location, Unset):
            storage_location = UNSET
        else:
            storage_location = self.storage_location

        is_storage_dewar: bool | None | Unset
        if isinstance(self.is_storage_dewar, Unset):
            is_storage_dewar = UNSET
        else:
            is_storage_dewar = self.is_storage_dewar

        barcode: None | str | Unset
        if isinstance(self.barcode, Unset):
            barcode = UNSET
        else:
            barcode = self.barcode

        comments: None | str | Unset
        if isinstance(self.comments, Unset):
            comments = UNSET
        else:
            comments = self.comments

        source: None | str | Unset
        if isinstance(self.source, Unset):
            source = UNSET
        else:
            source = self.source

        dewar_registry_id: int | None | Unset
        if isinstance(self.dewar_registry_id, Unset):
            dewar_registry_id = UNSET
        else:
            dewar_registry_id = self.dewar_registry_id

        tracking_number_to_synchrotron: None | str | Unset
        if isinstance(self.tracking_number_to_synchrotron, Unset):
            tracking_number_to_synchrotron = UNSET
        else:
            tracking_number_to_synchrotron = self.tracking_number_to_synchrotron

        tracking_number_from_synchrotron: None | str | Unset
        if isinstance(self.tracking_number_from_synchrotron, Unset):
            tracking_number_from_synchrotron = UNSET
        else:
            tracking_number_from_synchrotron = self.tracking_number_from_synchrotron

        bl_time_stamp: None | str | Unset
        if isinstance(self.bl_time_stamp, Unset):
            bl_time_stamp = UNSET
        elif isinstance(self.bl_time_stamp, datetime.datetime):
            bl_time_stamp = self.bl_time_stamp.isoformat()
        else:
            bl_time_stamp = self.bl_time_stamp

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if weight is not UNSET:
            field_dict["weight"] = weight
        if extra is not UNSET:
            field_dict["extra"] = extra
        if first_experiment_id is not UNSET:
            field_dict["firstExperimentId"] = first_experiment_id
        if code is not UNSET:
            field_dict["code"] = code
        if facility_code is not UNSET:
            field_dict["facilityCode"] = facility_code
        if dewar_status is not UNSET:
            field_dict["dewarStatus"] = dewar_status
        if storage_location is not UNSET:
            field_dict["storageLocation"] = storage_location
        if is_storage_dewar is not UNSET:
            field_dict["isStorageDewar"] = is_storage_dewar
        if barcode is not UNSET:
            field_dict["barcode"] = barcode
        if comments is not UNSET:
            field_dict["comments"] = comments
        if source is not UNSET:
            field_dict["source"] = source
        if dewar_registry_id is not UNSET:
            field_dict["dewarRegistryId"] = dewar_registry_id
        if tracking_number_to_synchrotron is not UNSET:
            field_dict["trackingNumberToSynchrotron"] = tracking_number_to_synchrotron
        if tracking_number_from_synchrotron is not UNSET:
            field_dict["trackingNumberFromSynchrotron"] = tracking_number_from_synchrotron
        if bl_time_stamp is not UNSET:
            field_dict["blTimeStamp"] = bl_time_stamp

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.dewar_in_extra_type_0_type_0 import DewarInExtraType0Type0

        d = dict(src_dict)

        def _parse_weight(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        weight = _parse_weight(d.pop("weight", UNSET))

        def _parse_extra(data: object) -> DewarInExtraType0Type0 | None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                extra_type_0_type_0 = DewarInExtraType0Type0.from_dict(data)

                return extra_type_0_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(DewarInExtraType0Type0 | None | str | Unset, data)

        extra = _parse_extra(d.pop("extra", UNSET))

        def _parse_first_experiment_id(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        first_experiment_id = _parse_first_experiment_id(d.pop("firstExperimentId", UNSET))

        def _parse_code(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        code = _parse_code(d.pop("code", UNSET))

        def _parse_facility_code(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        facility_code = _parse_facility_code(d.pop("facilityCode", UNSET))

        def _parse_dewar_status(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        dewar_status = _parse_dewar_status(d.pop("dewarStatus", UNSET))

        def _parse_storage_location(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        storage_location = _parse_storage_location(d.pop("storageLocation", UNSET))

        def _parse_is_storage_dewar(data: object) -> bool | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(bool | None | Unset, data)

        is_storage_dewar = _parse_is_storage_dewar(d.pop("isStorageDewar", UNSET))

        def _parse_barcode(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        barcode = _parse_barcode(d.pop("barcode", UNSET))

        def _parse_comments(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        comments = _parse_comments(d.pop("comments", UNSET))

        def _parse_source(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        source = _parse_source(d.pop("source", UNSET))

        def _parse_dewar_registry_id(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        dewar_registry_id = _parse_dewar_registry_id(d.pop("dewarRegistryId", UNSET))

        def _parse_tracking_number_to_synchrotron(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        tracking_number_to_synchrotron = _parse_tracking_number_to_synchrotron(
            d.pop("trackingNumberToSynchrotron", UNSET)
        )

        def _parse_tracking_number_from_synchrotron(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        tracking_number_from_synchrotron = _parse_tracking_number_from_synchrotron(
            d.pop("trackingNumberFromSynchrotron", UNSET)
        )

        def _parse_bl_time_stamp(data: object) -> datetime.datetime | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                bl_time_stamp_type_0 = datetime.datetime.fromisoformat(data)

                return bl_time_stamp_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(datetime.datetime | None | Unset, data)

        bl_time_stamp = _parse_bl_time_stamp(d.pop("blTimeStamp", UNSET))

        dewar_in = cls(
            weight=weight,
            extra=extra,
            first_experiment_id=first_experiment_id,
            code=code,
            facility_code=facility_code,
            dewar_status=dewar_status,
            storage_location=storage_location,
            is_storage_dewar=is_storage_dewar,
            barcode=barcode,
            comments=comments,
            source=source,
            dewar_registry_id=dewar_registry_id,
            tracking_number_to_synchrotron=tracking_number_to_synchrotron,
            tracking_number_from_synchrotron=tracking_number_from_synchrotron,
            bl_time_stamp=bl_time_stamp,
        )

        dewar_in.additional_properties = d
        return dewar_in

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

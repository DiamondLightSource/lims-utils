from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="DewarTransportHistoryOut")


@_attrs_define
class DewarTransportHistoryOut:
    """
    Attributes:
        dewar_id (int):
        dewar_status (str):
        dewar_transport_history_id (float):
        storage_location (None | str | Unset):
        arrival_date (datetime.datetime | None | Unset):
    """

    dewar_id: int
    dewar_status: str
    dewar_transport_history_id: float
    storage_location: None | str | Unset = UNSET
    arrival_date: datetime.datetime | None | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        dewar_id = self.dewar_id

        dewar_status = self.dewar_status

        dewar_transport_history_id = self.dewar_transport_history_id

        storage_location: None | str | Unset
        if isinstance(self.storage_location, Unset):
            storage_location = UNSET
        else:
            storage_location = self.storage_location

        arrival_date: None | str | Unset
        if isinstance(self.arrival_date, Unset):
            arrival_date = UNSET
        elif isinstance(self.arrival_date, datetime.datetime):
            arrival_date = self.arrival_date.isoformat()
        else:
            arrival_date = self.arrival_date

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "dewarId": dewar_id,
                "dewarStatus": dewar_status,
                "dewarTransportHistoryId": dewar_transport_history_id,
            }
        )
        if storage_location is not UNSET:
            field_dict["storageLocation"] = storage_location
        if arrival_date is not UNSET:
            field_dict["arrivalDate"] = arrival_date

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        dewar_id = d.pop("dewarId")

        dewar_status = d.pop("dewarStatus")

        dewar_transport_history_id = d.pop("dewarTransportHistoryId")

        def _parse_storage_location(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        storage_location = _parse_storage_location(d.pop("storageLocation", UNSET))

        def _parse_arrival_date(data: object) -> datetime.datetime | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                arrival_date_type_0 = datetime.datetime.fromisoformat(data)

                return arrival_date_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(datetime.datetime | None | Unset, data)

        arrival_date = _parse_arrival_date(d.pop("arrivalDate", UNSET))

        dewar_transport_history_out = cls(
            dewar_id=dewar_id,
            dewar_status=dewar_status,
            dewar_transport_history_id=dewar_transport_history_id,
            storage_location=storage_location,
            arrival_date=arrival_date,
        )

        dewar_transport_history_out.additional_properties = d
        return dewar_transport_history_out

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

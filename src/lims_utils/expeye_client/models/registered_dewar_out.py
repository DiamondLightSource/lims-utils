from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.proposal_out import ProposalOut


T = TypeVar("T", bound="RegisteredDewarOut")


@_attrs_define
class RegisteredDewarOut:
    """
    Attributes:
        facility_code (str):
        dewar_registry_id (int):
        lab_contact_id (int | None | Unset):
        purchase_date (datetime.datetime | None | Unset):
        manufacturer_serial_number (None | str | Unset):
        proposals (list[ProposalOut] | Unset):
    """

    facility_code: str
    dewar_registry_id: int
    lab_contact_id: int | None | Unset = UNSET
    purchase_date: datetime.datetime | None | Unset = UNSET
    manufacturer_serial_number: None | str | Unset = UNSET
    proposals: list[ProposalOut] | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        facility_code = self.facility_code

        dewar_registry_id = self.dewar_registry_id

        lab_contact_id: int | None | Unset
        if isinstance(self.lab_contact_id, Unset):
            lab_contact_id = UNSET
        else:
            lab_contact_id = self.lab_contact_id

        purchase_date: None | str | Unset
        if isinstance(self.purchase_date, Unset):
            purchase_date = UNSET
        elif isinstance(self.purchase_date, datetime.datetime):
            purchase_date = self.purchase_date.isoformat()
        else:
            purchase_date = self.purchase_date

        manufacturer_serial_number: None | str | Unset
        if isinstance(self.manufacturer_serial_number, Unset):
            manufacturer_serial_number = UNSET
        else:
            manufacturer_serial_number = self.manufacturer_serial_number

        proposals: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.proposals, Unset):
            proposals = []
            for proposals_item_data in self.proposals:
                proposals_item = proposals_item_data.to_dict()
                proposals.append(proposals_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "facilityCode": facility_code,
                "dewarRegistryId": dewar_registry_id,
            }
        )
        if lab_contact_id is not UNSET:
            field_dict["labContactId"] = lab_contact_id
        if purchase_date is not UNSET:
            field_dict["purchaseDate"] = purchase_date
        if manufacturer_serial_number is not UNSET:
            field_dict["manufacturerSerialNumber"] = manufacturer_serial_number
        if proposals is not UNSET:
            field_dict["proposals"] = proposals

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.proposal_out import ProposalOut  # noqa: PLC0415

        d = dict(src_dict)
        facility_code = d.pop("facilityCode")

        dewar_registry_id = d.pop("dewarRegistryId")

        def _parse_lab_contact_id(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        lab_contact_id = _parse_lab_contact_id(d.pop("labContactId", UNSET))

        def _parse_purchase_date(data: object) -> datetime.datetime | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                purchase_date_type_0 = datetime.datetime.fromisoformat(data)

                return purchase_date_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(datetime.datetime | None | Unset, data)

        purchase_date = _parse_purchase_date(d.pop("purchaseDate", UNSET))

        def _parse_manufacturer_serial_number(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        manufacturer_serial_number = _parse_manufacturer_serial_number(d.pop("manufacturerSerialNumber", UNSET))

        _proposals = d.pop("proposals", UNSET)
        proposals: list[ProposalOut] | Unset = UNSET
        if _proposals is not UNSET:
            proposals = []
            for proposals_item_data in _proposals:
                proposals_item = ProposalOut.from_dict(proposals_item_data)

                proposals.append(proposals_item)

        registered_dewar_out = cls(
            facility_code=facility_code,
            dewar_registry_id=dewar_registry_id,
            lab_contact_id=lab_contact_id,
            purchase_date=purchase_date,
            manufacturer_serial_number=manufacturer_serial_number,
            proposals=proposals,
        )

        registered_dewar_out.additional_properties = d
        return registered_dewar_out

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

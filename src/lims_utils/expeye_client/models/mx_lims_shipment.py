from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar
from uuid import UUID

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.mx_lims_contact import MxLimsContact
    from ..models.mx_lims_shipment_identifiers import MxLimsShipmentIdentifiers
    from ..models.mx_lims_shipment_urls import MxLimsShipmentUrls


T = TypeVar("T", bound="MxLimsShipment")


@_attrs_define
class MxLimsShipment:
    """
    Attributes:
        mxlims_type (str):
        uuid (UUID):
        proposal_code (str):
        lab_contact_outbound (MxLimsContact):
        lab_contact_return (MxLimsContact):
        urls (MxLimsShipmentUrls | Unset):
        identifiers (MxLimsShipmentIdentifiers | Unset):
    """

    mxlims_type: str
    uuid: UUID
    proposal_code: str
    lab_contact_outbound: MxLimsContact
    lab_contact_return: MxLimsContact
    urls: MxLimsShipmentUrls | Unset = UNSET
    identifiers: MxLimsShipmentIdentifiers | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        mxlims_type = self.mxlims_type

        uuid = str(self.uuid)

        proposal_code = self.proposal_code

        lab_contact_outbound = self.lab_contact_outbound.to_dict()

        lab_contact_return = self.lab_contact_return.to_dict()

        urls: dict[str, Any] | Unset = UNSET
        if not isinstance(self.urls, Unset):
            urls = self.urls.to_dict()

        identifiers: dict[str, Any] | Unset = UNSET
        if not isinstance(self.identifiers, Unset):
            identifiers = self.identifiers.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "mxlimsType": mxlims_type,
                "uuid": uuid,
                "proposalCode": proposal_code,
                "labContactOutbound": lab_contact_outbound,
                "labContactReturn": lab_contact_return,
            }
        )
        if urls is not UNSET:
            field_dict["urls"] = urls
        if identifiers is not UNSET:
            field_dict["identifiers"] = identifiers

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.mx_lims_contact import MxLimsContact
        from ..models.mx_lims_shipment_identifiers import MxLimsShipmentIdentifiers
        from ..models.mx_lims_shipment_urls import MxLimsShipmentUrls

        d = dict(src_dict)
        mxlims_type = d.pop("mxlimsType")

        uuid = UUID(d.pop("uuid"))

        proposal_code = d.pop("proposalCode")

        lab_contact_outbound = MxLimsContact.from_dict(d.pop("labContactOutbound"))

        lab_contact_return = MxLimsContact.from_dict(d.pop("labContactReturn"))

        _urls = d.pop("urls", UNSET)
        urls: MxLimsShipmentUrls | Unset
        if isinstance(_urls, Unset):
            urls = UNSET
        else:
            urls = MxLimsShipmentUrls.from_dict(_urls)

        _identifiers = d.pop("identifiers", UNSET)
        identifiers: MxLimsShipmentIdentifiers | Unset
        if isinstance(_identifiers, Unset):
            identifiers = UNSET
        else:
            identifiers = MxLimsShipmentIdentifiers.from_dict(_identifiers)

        mx_lims_shipment = cls(
            mxlims_type=mxlims_type,
            uuid=uuid,
            proposal_code=proposal_code,
            lab_contact_outbound=lab_contact_outbound,
            lab_contact_return=lab_contact_return,
            urls=urls,
            identifiers=identifiers,
        )

        mx_lims_shipment.additional_properties = d
        return mx_lims_shipment

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

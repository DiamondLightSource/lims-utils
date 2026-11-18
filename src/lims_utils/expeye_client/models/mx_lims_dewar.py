from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar
from uuid import UUID

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.mx_lims_dewar_containerref import MxLimsDewarContainerref
    from ..models.mx_lims_dewar_identifiers import MxLimsDewarIdentifiers
    from ..models.mx_lims_dewar_urls import MxLimsDewarUrls


T = TypeVar("T", bound="MxLimsDewar")


@_attrs_define
class MxLimsDewar:
    """
    Attributes:
        mxlims_type (str):
        uuid (UUID):
        barcode (str):
        container_ref (MxLimsDewarContainerref):
        urls (MxLimsDewarUrls | Unset):
        identifiers (MxLimsDewarIdentifiers | Unset):
    """

    mxlims_type: str
    uuid: UUID
    barcode: str
    container_ref: MxLimsDewarContainerref
    urls: MxLimsDewarUrls | Unset = UNSET
    identifiers: MxLimsDewarIdentifiers | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        mxlims_type = self.mxlims_type

        uuid = str(self.uuid)

        barcode = self.barcode

        container_ref = self.container_ref.to_dict()

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
                "barcode": barcode,
                "containerRef": container_ref,
            }
        )
        if urls is not UNSET:
            field_dict["urls"] = urls
        if identifiers is not UNSET:
            field_dict["identifiers"] = identifiers

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.mx_lims_dewar_containerref import MxLimsDewarContainerref
        from ..models.mx_lims_dewar_identifiers import MxLimsDewarIdentifiers
        from ..models.mx_lims_dewar_urls import MxLimsDewarUrls

        d = dict(src_dict)
        mxlims_type = d.pop("mxlimsType")

        uuid = UUID(d.pop("uuid"))

        barcode = d.pop("barcode")

        container_ref = MxLimsDewarContainerref.from_dict(d.pop("containerRef"))

        _urls = d.pop("urls", UNSET)
        urls: MxLimsDewarUrls | Unset
        if isinstance(_urls, Unset):
            urls = UNSET
        else:
            urls = MxLimsDewarUrls.from_dict(_urls)

        _identifiers = d.pop("identifiers", UNSET)
        identifiers: MxLimsDewarIdentifiers | Unset
        if isinstance(_identifiers, Unset):
            identifiers = UNSET
        else:
            identifiers = MxLimsDewarIdentifiers.from_dict(_identifiers)

        mx_lims_dewar = cls(
            mxlims_type=mxlims_type,
            uuid=uuid,
            barcode=barcode,
            container_ref=container_ref,
            urls=urls,
            identifiers=identifiers,
        )

        mx_lims_dewar.additional_properties = d
        return mx_lims_dewar

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

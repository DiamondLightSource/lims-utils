from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar
from uuid import UUID

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.mx_lims_puck_containerref import MxLimsPuckContainerref
    from ..models.mx_lims_puck_identifiers import MxLimsPuckIdentifiers
    from ..models.mx_lims_puck_urls import MxLimsPuckUrls


T = TypeVar("T", bound="MxLimsPuck")


@_attrs_define
class MxLimsPuck:
    """
    Attributes:
        mxlims_type (str):
        uuid (UUID):
        number_positions (int):
        barcode (str):
        container_ref (MxLimsPuckContainerref):
        urls (MxLimsPuckUrls | Unset):
        identifiers (MxLimsPuckIdentifiers | Unset):
    """

    mxlims_type: str
    uuid: UUID
    number_positions: int
    barcode: str
    container_ref: MxLimsPuckContainerref
    urls: MxLimsPuckUrls | Unset = UNSET
    identifiers: MxLimsPuckIdentifiers | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        mxlims_type = self.mxlims_type

        uuid = str(self.uuid)

        number_positions = self.number_positions

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
                "numberPositions": number_positions,
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
        from ..models.mx_lims_puck_containerref import MxLimsPuckContainerref  # noqa: PLC0415
        from ..models.mx_lims_puck_identifiers import MxLimsPuckIdentifiers  # noqa: PLC0415
        from ..models.mx_lims_puck_urls import MxLimsPuckUrls  # noqa: PLC0415

        d = dict(src_dict)
        mxlims_type = d.pop("mxlimsType")

        uuid = UUID(d.pop("uuid"))

        number_positions = d.pop("numberPositions")

        barcode = d.pop("barcode")

        container_ref = MxLimsPuckContainerref.from_dict(d.pop("containerRef"))

        _urls = d.pop("urls", UNSET)
        urls: MxLimsPuckUrls | Unset
        if isinstance(_urls, Unset):
            urls = UNSET
        else:
            urls = MxLimsPuckUrls.from_dict(_urls)

        _identifiers = d.pop("identifiers", UNSET)
        identifiers: MxLimsPuckIdentifiers | Unset
        if isinstance(_identifiers, Unset):
            identifiers = UNSET
        else:
            identifiers = MxLimsPuckIdentifiers.from_dict(_identifiers)

        mx_lims_puck = cls(
            mxlims_type=mxlims_type,
            uuid=uuid,
            number_positions=number_positions,
            barcode=barcode,
            container_ref=container_ref,
            urls=urls,
            identifiers=identifiers,
        )

        mx_lims_puck.additional_properties = d
        return mx_lims_puck

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

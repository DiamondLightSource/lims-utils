from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast
from uuid import UUID

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.mx_lims_pin_containerref import MxLimsPinContainerref
    from ..models.mx_lims_pin_identifiers import MxLimsPinIdentifiers
    from ..models.mx_lims_pin_sampleref import MxLimsPinSampleref
    from ..models.mx_lims_pin_urls import MxLimsPinUrls


T = TypeVar("T", bound="MxLimsPin")


@_attrs_define
class MxLimsPin:
    """
    Attributes:
        uuid (UUID):
        position_in_puck (int):
        container_ref (MxLimsPinContainerref):
        sample_ref (MxLimsPinSampleref):
        mxlims_type (str | Unset):  Default: 'Pin'.
        urls (MxLimsPinUrls | Unset):
        identifiers (MxLimsPinIdentifiers | Unset):
        barcode (None | str | Unset):
    """

    uuid: UUID
    position_in_puck: int
    container_ref: MxLimsPinContainerref
    sample_ref: MxLimsPinSampleref
    mxlims_type: str | Unset = "Pin"
    urls: MxLimsPinUrls | Unset = UNSET
    identifiers: MxLimsPinIdentifiers | Unset = UNSET
    barcode: None | str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        uuid = str(self.uuid)

        position_in_puck = self.position_in_puck

        container_ref = self.container_ref.to_dict()

        sample_ref = self.sample_ref.to_dict()

        mxlims_type = self.mxlims_type

        urls: dict[str, Any] | Unset = UNSET
        if not isinstance(self.urls, Unset):
            urls = self.urls.to_dict()

        identifiers: dict[str, Any] | Unset = UNSET
        if not isinstance(self.identifiers, Unset):
            identifiers = self.identifiers.to_dict()

        barcode: None | str | Unset
        if isinstance(self.barcode, Unset):
            barcode = UNSET
        else:
            barcode = self.barcode

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "uuid": uuid,
                "positionInPuck": position_in_puck,
                "containerRef": container_ref,
                "sampleRef": sample_ref,
            }
        )
        if mxlims_type is not UNSET:
            field_dict["mxlimsType"] = mxlims_type
        if urls is not UNSET:
            field_dict["urls"] = urls
        if identifiers is not UNSET:
            field_dict["identifiers"] = identifiers
        if barcode is not UNSET:
            field_dict["barcode"] = barcode

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.mx_lims_pin_containerref import MxLimsPinContainerref  # noqa: PLC0415
        from ..models.mx_lims_pin_identifiers import MxLimsPinIdentifiers  # noqa: PLC0415
        from ..models.mx_lims_pin_sampleref import MxLimsPinSampleref  # noqa: PLC0415
        from ..models.mx_lims_pin_urls import MxLimsPinUrls  # noqa: PLC0415

        d = dict(src_dict)
        uuid = UUID(d.pop("uuid"))

        position_in_puck = d.pop("positionInPuck")

        container_ref = MxLimsPinContainerref.from_dict(d.pop("containerRef"))

        sample_ref = MxLimsPinSampleref.from_dict(d.pop("sampleRef"))

        mxlims_type = d.pop("mxlimsType", UNSET)

        _urls = d.pop("urls", UNSET)
        urls: MxLimsPinUrls | Unset
        if isinstance(_urls, Unset):
            urls = UNSET
        else:
            urls = MxLimsPinUrls.from_dict(_urls)

        _identifiers = d.pop("identifiers", UNSET)
        identifiers: MxLimsPinIdentifiers | Unset
        if isinstance(_identifiers, Unset):
            identifiers = UNSET
        else:
            identifiers = MxLimsPinIdentifiers.from_dict(_identifiers)

        def _parse_barcode(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        barcode = _parse_barcode(d.pop("barcode", UNSET))

        mx_lims_pin = cls(
            uuid=uuid,
            position_in_puck=position_in_puck,
            container_ref=container_ref,
            sample_ref=sample_ref,
            mxlims_type=mxlims_type,
            urls=urls,
            identifiers=identifiers,
            barcode=barcode,
        )

        mx_lims_pin.additional_properties = d
        return mx_lims_pin

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

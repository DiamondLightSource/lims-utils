from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar
from uuid import UUID

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.mx_lims_macromolecule_sample_identifiers import MxLimsMacromoleculeSampleIdentifiers
    from ..models.mx_lims_macromolecule_sample_parentsampleref import MxLimsMacromoleculeSampleParentsampleref
    from ..models.mx_lims_macromolecule_sample_urls import MxLimsMacromoleculeSampleUrls


T = TypeVar("T", bound="MxLimsMacromoleculeSample")


@_attrs_define
class MxLimsMacromoleculeSample:
    """
    Attributes:
        mxlims_type (str):
        uuid (UUID):
        name (str):
        parent_sample_ref (MxLimsMacromoleculeSampleParentsampleref):
        urls (MxLimsMacromoleculeSampleUrls | Unset):
        identifiers (MxLimsMacromoleculeSampleIdentifiers | Unset):
    """

    mxlims_type: str
    uuid: UUID
    name: str
    parent_sample_ref: MxLimsMacromoleculeSampleParentsampleref
    urls: MxLimsMacromoleculeSampleUrls | Unset = UNSET
    identifiers: MxLimsMacromoleculeSampleIdentifiers | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        mxlims_type = self.mxlims_type

        uuid = str(self.uuid)

        name = self.name

        parent_sample_ref = self.parent_sample_ref.to_dict()

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
                "name": name,
                "parentSampleRef": parent_sample_ref,
            }
        )
        if urls is not UNSET:
            field_dict["urls"] = urls
        if identifiers is not UNSET:
            field_dict["identifiers"] = identifiers

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.mx_lims_macromolecule_sample_identifiers import (
            MxLimsMacromoleculeSampleIdentifiers,
        )
        from ..models.mx_lims_macromolecule_sample_parentsampleref import (
            MxLimsMacromoleculeSampleParentsampleref,
        )
        from ..models.mx_lims_macromolecule_sample_urls import MxLimsMacromoleculeSampleUrls

        d = dict(src_dict)
        mxlims_type = d.pop("mxlimsType")

        uuid = UUID(d.pop("uuid"))

        name = d.pop("name")

        parent_sample_ref = MxLimsMacromoleculeSampleParentsampleref.from_dict(d.pop("parentSampleRef"))

        _urls = d.pop("urls", UNSET)
        urls: MxLimsMacromoleculeSampleUrls | Unset
        if isinstance(_urls, Unset):
            urls = UNSET
        else:
            urls = MxLimsMacromoleculeSampleUrls.from_dict(_urls)

        _identifiers = d.pop("identifiers", UNSET)
        identifiers: MxLimsMacromoleculeSampleIdentifiers | Unset
        if isinstance(_identifiers, Unset):
            identifiers = UNSET
        else:
            identifiers = MxLimsMacromoleculeSampleIdentifiers.from_dict(_identifiers)

        mx_lims_macromolecule_sample = cls(
            mxlims_type=mxlims_type,
            uuid=uuid,
            name=name,
            parent_sample_ref=parent_sample_ref,
            urls=urls,
            identifiers=identifiers,
        )

        mx_lims_macromolecule_sample.additional_properties = d
        return mx_lims_macromolecule_sample

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

from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.mx_lims_full_shipment_version import MxLimsFullShipmentVersion

if TYPE_CHECKING:
    from ..models.mx_lims_full_shipment_dewar import MxLimsFullShipmentDewar
    from ..models.mx_lims_full_shipment_macromolecule import MxLimsFullShipmentMacromolecule
    from ..models.mx_lims_full_shipment_macromoleculesample import MxLimsFullShipmentMacromoleculesample
    from ..models.mx_lims_full_shipment_pin import MxLimsFullShipmentPin
    from ..models.mx_lims_full_shipment_puck import MxLimsFullShipmentPuck
    from ..models.mx_lims_full_shipment_shipment import MxLimsFullShipmentShipment


T = TypeVar("T", bound="MxLimsFullShipment")


@_attrs_define
class MxLimsFullShipment:
    """
    Attributes:
        version (MxLimsFullShipmentVersion):
        shipment (MxLimsFullShipmentShipment):
        dewar (MxLimsFullShipmentDewar):
        puck (MxLimsFullShipmentPuck):
        macromolecule (MxLimsFullShipmentMacromolecule):
        macromolecule_sample (MxLimsFullShipmentMacromoleculesample):
        pin (MxLimsFullShipmentPin):
    """

    version: MxLimsFullShipmentVersion
    shipment: MxLimsFullShipmentShipment
    dewar: MxLimsFullShipmentDewar
    puck: MxLimsFullShipmentPuck
    macromolecule: MxLimsFullShipmentMacromolecule
    macromolecule_sample: MxLimsFullShipmentMacromoleculesample
    pin: MxLimsFullShipmentPin
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        version = self.version.value

        shipment = self.shipment.to_dict()

        dewar = self.dewar.to_dict()

        puck = self.puck.to_dict()

        macromolecule = self.macromolecule.to_dict()

        macromolecule_sample = self.macromolecule_sample.to_dict()

        pin = self.pin.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "version": version,
                "Shipment": shipment,
                "Dewar": dewar,
                "Puck": puck,
                "Macromolecule": macromolecule,
                "MacromoleculeSample": macromolecule_sample,
                "Pin": pin,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.mx_lims_full_shipment_dewar import MxLimsFullShipmentDewar
        from ..models.mx_lims_full_shipment_macromolecule import MxLimsFullShipmentMacromolecule
        from ..models.mx_lims_full_shipment_macromoleculesample import (
            MxLimsFullShipmentMacromoleculesample,
        )
        from ..models.mx_lims_full_shipment_pin import MxLimsFullShipmentPin
        from ..models.mx_lims_full_shipment_puck import MxLimsFullShipmentPuck
        from ..models.mx_lims_full_shipment_shipment import MxLimsFullShipmentShipment

        d = dict(src_dict)
        version = MxLimsFullShipmentVersion(d.pop("version"))

        shipment = MxLimsFullShipmentShipment.from_dict(d.pop("Shipment"))

        dewar = MxLimsFullShipmentDewar.from_dict(d.pop("Dewar"))

        puck = MxLimsFullShipmentPuck.from_dict(d.pop("Puck"))

        macromolecule = MxLimsFullShipmentMacromolecule.from_dict(d.pop("Macromolecule"))

        macromolecule_sample = MxLimsFullShipmentMacromoleculesample.from_dict(d.pop("MacromoleculeSample"))

        pin = MxLimsFullShipmentPin.from_dict(d.pop("Pin"))

        mx_lims_full_shipment = cls(
            version=version,
            shipment=shipment,
            dewar=dewar,
            puck=puck,
            macromolecule=macromolecule,
            macromolecule_sample=macromolecule_sample,
            pin=pin,
        )

        mx_lims_full_shipment.additional_properties = d
        return mx_lims_full_shipment

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

from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.lab_contact_out import LabContactOut
    from ..models.protein_out import ProteinOut
    from ..models.registered_container_out import RegisteredContainerOut
    from ..models.registered_dewar_out import RegisteredDewarOut


T = TypeVar("T", bound="ShippingDataOut")


@_attrs_define
class ShippingDataOut:
    """
    Attributes:
        lab_contacts (list[LabContactOut]):
        proteins (list[ProteinOut]):
        containers (list[RegisteredContainerOut]):
        dewars (list[RegisteredDewarOut]):
    """

    lab_contacts: list[LabContactOut]
    proteins: list[ProteinOut]
    containers: list[RegisteredContainerOut]
    dewars: list[RegisteredDewarOut]
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        lab_contacts = []
        for lab_contacts_item_data in self.lab_contacts:
            lab_contacts_item = lab_contacts_item_data.to_dict()
            lab_contacts.append(lab_contacts_item)

        proteins = []
        for proteins_item_data in self.proteins:
            proteins_item = proteins_item_data.to_dict()
            proteins.append(proteins_item)

        containers = []
        for containers_item_data in self.containers:
            containers_item = containers_item_data.to_dict()
            containers.append(containers_item)

        dewars = []
        for dewars_item_data in self.dewars:
            dewars_item = dewars_item_data.to_dict()
            dewars.append(dewars_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "labContacts": lab_contacts,
                "proteins": proteins,
                "containers": containers,
                "dewars": dewars,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.lab_contact_out import LabContactOut  # noqa: PLC0415
        from ..models.protein_out import ProteinOut  # noqa: PLC0415
        from ..models.registered_container_out import RegisteredContainerOut  # noqa: PLC0415
        from ..models.registered_dewar_out import RegisteredDewarOut  # noqa: PLC0415

        d = dict(src_dict)
        lab_contacts = []
        _lab_contacts = d.pop("labContacts")
        for lab_contacts_item_data in _lab_contacts:
            lab_contacts_item = LabContactOut.from_dict(lab_contacts_item_data)

            lab_contacts.append(lab_contacts_item)

        proteins = []
        _proteins = d.pop("proteins")
        for proteins_item_data in _proteins:
            proteins_item = ProteinOut.from_dict(proteins_item_data)

            proteins.append(proteins_item)

        containers = []
        _containers = d.pop("containers")
        for containers_item_data in _containers:
            containers_item = RegisteredContainerOut.from_dict(containers_item_data)

            containers.append(containers_item)

        dewars = []
        _dewars = d.pop("dewars")
        for dewars_item_data in _dewars:
            dewars_item = RegisteredDewarOut.from_dict(dewars_item_data)

            dewars.append(dewars_item)

        shipping_data_out = cls(
            lab_contacts=lab_contacts,
            proteins=proteins,
            containers=containers,
            dewars=dewars,
        )

        shipping_data_out.additional_properties = d
        return shipping_data_out

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

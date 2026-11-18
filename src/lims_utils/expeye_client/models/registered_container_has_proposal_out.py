from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="RegisteredContainerHasProposalOut")


@_attrs_define
class RegisteredContainerHasProposalOut:
    """
    Attributes:
        container_registry_has_proposal_id (int):
        container_registry_id (int):
        proposal_id (int):
        person_id (int | None | Unset):
        record_timestamp (datetime.datetime | None | Unset):
    """

    container_registry_has_proposal_id: int
    container_registry_id: int
    proposal_id: int
    person_id: int | None | Unset = UNSET
    record_timestamp: datetime.datetime | None | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        container_registry_has_proposal_id = self.container_registry_has_proposal_id

        container_registry_id = self.container_registry_id

        proposal_id = self.proposal_id

        person_id: int | None | Unset
        if isinstance(self.person_id, Unset):
            person_id = UNSET
        else:
            person_id = self.person_id

        record_timestamp: None | str | Unset
        if isinstance(self.record_timestamp, Unset):
            record_timestamp = UNSET
        elif isinstance(self.record_timestamp, datetime.datetime):
            record_timestamp = self.record_timestamp.isoformat()
        else:
            record_timestamp = self.record_timestamp

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "containerRegistryHasProposalId": container_registry_has_proposal_id,
                "containerRegistryId": container_registry_id,
                "proposalId": proposal_id,
            }
        )
        if person_id is not UNSET:
            field_dict["personId"] = person_id
        if record_timestamp is not UNSET:
            field_dict["recordTimestamp"] = record_timestamp

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        container_registry_has_proposal_id = d.pop("containerRegistryHasProposalId")

        container_registry_id = d.pop("containerRegistryId")

        proposal_id = d.pop("proposalId")

        def _parse_person_id(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        person_id = _parse_person_id(d.pop("personId", UNSET))

        def _parse_record_timestamp(data: object) -> datetime.datetime | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                record_timestamp_type_0 = datetime.datetime.fromisoformat(data)

                return record_timestamp_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(datetime.datetime | None | Unset, data)

        record_timestamp = _parse_record_timestamp(d.pop("recordTimestamp", UNSET))

        registered_container_has_proposal_out = cls(
            container_registry_has_proposal_id=container_registry_has_proposal_id,
            container_registry_id=container_registry_id,
            proposal_id=proposal_id,
            person_id=person_id,
            record_timestamp=record_timestamp,
        )

        registered_container_has_proposal_out.additional_properties = d
        return registered_container_has_proposal_out

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

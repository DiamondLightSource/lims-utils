from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.state_enum import StateEnum
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.shipment_with_children_out import ShipmentWithChildrenOut


T = TypeVar("T", bound="ProposalWithChildrenOut")


@_attrs_define
class ProposalWithChildrenOut:
    """
    Attributes:
        proposal_id (int): Proposal ID
        person_id (int):
        bltime_stamp (datetime.datetime):
        state (StateEnum):
        proposal_code (str):
        proposal_number (str):
        title (None | str | Unset):
        proposal_type (None | str | Unset):
        start_date (datetime.datetime | None | Unset):
        end_date (datetime.datetime | None | Unset):
        sessions (int | None | Unset):
        beamlines (list[str] | None | Unset):
        principal_investigator (None | str | Unset):
        uas_link (None | str | Unset):
        children (list[ShipmentWithChildrenOut] | Unset):
    """

    proposal_id: int
    person_id: int
    bltime_stamp: datetime.datetime
    state: StateEnum
    proposal_code: str
    proposal_number: str
    title: None | str | Unset = UNSET
    proposal_type: None | str | Unset = UNSET
    start_date: datetime.datetime | None | Unset = UNSET
    end_date: datetime.datetime | None | Unset = UNSET
    sessions: int | None | Unset = UNSET
    beamlines: list[str] | None | Unset = UNSET
    principal_investigator: None | str | Unset = UNSET
    uas_link: None | str | Unset = UNSET
    children: list[ShipmentWithChildrenOut] | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        proposal_id = self.proposal_id

        person_id = self.person_id

        bltime_stamp = self.bltime_stamp.isoformat()

        state = self.state.value

        proposal_code = self.proposal_code

        proposal_number = self.proposal_number

        title: None | str | Unset
        if isinstance(self.title, Unset):
            title = UNSET
        else:
            title = self.title

        proposal_type: None | str | Unset
        if isinstance(self.proposal_type, Unset):
            proposal_type = UNSET
        else:
            proposal_type = self.proposal_type

        start_date: None | str | Unset
        if isinstance(self.start_date, Unset):
            start_date = UNSET
        elif isinstance(self.start_date, datetime.datetime):
            start_date = self.start_date.isoformat()
        else:
            start_date = self.start_date

        end_date: None | str | Unset
        if isinstance(self.end_date, Unset):
            end_date = UNSET
        elif isinstance(self.end_date, datetime.datetime):
            end_date = self.end_date.isoformat()
        else:
            end_date = self.end_date

        sessions: int | None | Unset
        if isinstance(self.sessions, Unset):
            sessions = UNSET
        else:
            sessions = self.sessions

        beamlines: list[str] | None | Unset
        if isinstance(self.beamlines, Unset):
            beamlines = UNSET
        elif isinstance(self.beamlines, list):
            beamlines = self.beamlines

        else:
            beamlines = self.beamlines

        principal_investigator: None | str | Unset
        if isinstance(self.principal_investigator, Unset):
            principal_investigator = UNSET
        else:
            principal_investigator = self.principal_investigator

        uas_link: None | str | Unset
        if isinstance(self.uas_link, Unset):
            uas_link = UNSET
        else:
            uas_link = self.uas_link

        children: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.children, Unset):
            children = []
            for children_item_data in self.children:
                children_item = children_item_data.to_dict()
                children.append(children_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "proposalId": proposal_id,
                "personId": person_id,
                "bltimeStamp": bltime_stamp,
                "state": state,
                "proposalCode": proposal_code,
                "proposalNumber": proposal_number,
            }
        )
        if title is not UNSET:
            field_dict["title"] = title
        if proposal_type is not UNSET:
            field_dict["proposalType"] = proposal_type
        if start_date is not UNSET:
            field_dict["startDate"] = start_date
        if end_date is not UNSET:
            field_dict["endDate"] = end_date
        if sessions is not UNSET:
            field_dict["sessions"] = sessions
        if beamlines is not UNSET:
            field_dict["beamlines"] = beamlines
        if principal_investigator is not UNSET:
            field_dict["principalInvestigator"] = principal_investigator
        if uas_link is not UNSET:
            field_dict["uasLink"] = uas_link
        if children is not UNSET:
            field_dict["children"] = children

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.shipment_with_children_out import ShipmentWithChildrenOut

        d = dict(src_dict)
        proposal_id = d.pop("proposalId")

        person_id = d.pop("personId")

        bltime_stamp = datetime.datetime.fromisoformat(d.pop("bltimeStamp"))

        state = StateEnum(d.pop("state"))

        proposal_code = d.pop("proposalCode")

        proposal_number = d.pop("proposalNumber")

        def _parse_title(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        title = _parse_title(d.pop("title", UNSET))

        def _parse_proposal_type(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        proposal_type = _parse_proposal_type(d.pop("proposalType", UNSET))

        def _parse_start_date(data: object) -> datetime.datetime | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                start_date_type_0 = datetime.datetime.fromisoformat(data)

                return start_date_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(datetime.datetime | None | Unset, data)

        start_date = _parse_start_date(d.pop("startDate", UNSET))

        def _parse_end_date(data: object) -> datetime.datetime | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                end_date_type_0 = datetime.datetime.fromisoformat(data)

                return end_date_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(datetime.datetime | None | Unset, data)

        end_date = _parse_end_date(d.pop("endDate", UNSET))

        def _parse_sessions(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        sessions = _parse_sessions(d.pop("sessions", UNSET))

        def _parse_beamlines(data: object) -> list[str] | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                beamlines_type_0 = cast(list[str], data)

                return beamlines_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[str] | None | Unset, data)

        beamlines = _parse_beamlines(d.pop("beamlines", UNSET))

        def _parse_principal_investigator(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        principal_investigator = _parse_principal_investigator(d.pop("principalInvestigator", UNSET))

        def _parse_uas_link(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        uas_link = _parse_uas_link(d.pop("uasLink", UNSET))

        _children = d.pop("children", UNSET)
        children: list[ShipmentWithChildrenOut] | Unset = UNSET
        if _children is not UNSET:
            children = []
            for children_item_data in _children:
                children_item = ShipmentWithChildrenOut.from_dict(children_item_data)

                children.append(children_item)

        proposal_with_children_out = cls(
            proposal_id=proposal_id,
            person_id=person_id,
            bltime_stamp=bltime_stamp,
            state=state,
            proposal_code=proposal_code,
            proposal_number=proposal_number,
            title=title,
            proposal_type=proposal_type,
            start_date=start_date,
            end_date=end_date,
            sessions=sessions,
            beamlines=beamlines,
            principal_investigator=principal_investigator,
            uas_link=uas_link,
            children=children,
        )

        proposal_with_children_out.additional_properties = d
        return proposal_with_children_out

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

from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.person_out import PersonOut


T = TypeVar("T", bound="SessionOut")


@_attrs_define
class SessionOut:
    """
    Attributes:
        proposal_id (int): Proposal ID
        session_id (int): Session ID
        bltime_stamp (datetime.datetime):
        purged_processed_data (bool):
        archived (int): The data for the session is archived and no longer available on disk
        active (bool): Whether the session is currently running
        beam_line_setup_id (int | None | Unset):
        beam_calendar_id (int | None | Unset):
        start_date (datetime.datetime | None | Unset):
        end_date (datetime.datetime | None | Unset):
        beam_line_name (None | str | Unset):
        scheduled (int | None | Unset):
        nb_shifts (int | None | Unset):
        comments (None | str | Unset):
        visit_number (int | None | Unset):
        used_flag (int | None | Unset): Indicates if session has Datacollections or XFE or EnergyScans attached
        last_update (datetime.datetime | None | Unset): Last update timestamp: by default the end of the session, the
            last collect
        parent_proposal (None | str | Unset):
        beam_line_operator (list[str] | None | Unset):
        collection_groups (int | None | Unset):
        users (list[PersonOut] | Unset):
    """

    proposal_id: int
    session_id: int
    bltime_stamp: datetime.datetime
    purged_processed_data: bool
    archived: int
    active: bool
    beam_line_setup_id: int | None | Unset = UNSET
    beam_calendar_id: int | None | Unset = UNSET
    start_date: datetime.datetime | None | Unset = UNSET
    end_date: datetime.datetime | None | Unset = UNSET
    beam_line_name: None | str | Unset = UNSET
    scheduled: int | None | Unset = UNSET
    nb_shifts: int | None | Unset = UNSET
    comments: None | str | Unset = UNSET
    visit_number: int | None | Unset = UNSET
    used_flag: int | None | Unset = UNSET
    last_update: datetime.datetime | None | Unset = UNSET
    parent_proposal: None | str | Unset = UNSET
    beam_line_operator: list[str] | None | Unset = UNSET
    collection_groups: int | None | Unset = UNSET
    users: list[PersonOut] | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        proposal_id = self.proposal_id

        session_id = self.session_id

        bltime_stamp = self.bltime_stamp.isoformat()

        purged_processed_data = self.purged_processed_data

        archived = self.archived

        active = self.active

        beam_line_setup_id: int | None | Unset
        if isinstance(self.beam_line_setup_id, Unset):
            beam_line_setup_id = UNSET
        else:
            beam_line_setup_id = self.beam_line_setup_id

        beam_calendar_id: int | None | Unset
        if isinstance(self.beam_calendar_id, Unset):
            beam_calendar_id = UNSET
        else:
            beam_calendar_id = self.beam_calendar_id

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

        beam_line_name: None | str | Unset
        if isinstance(self.beam_line_name, Unset):
            beam_line_name = UNSET
        else:
            beam_line_name = self.beam_line_name

        scheduled: int | None | Unset
        if isinstance(self.scheduled, Unset):
            scheduled = UNSET
        else:
            scheduled = self.scheduled

        nb_shifts: int | None | Unset
        if isinstance(self.nb_shifts, Unset):
            nb_shifts = UNSET
        else:
            nb_shifts = self.nb_shifts

        comments: None | str | Unset
        if isinstance(self.comments, Unset):
            comments = UNSET
        else:
            comments = self.comments

        visit_number: int | None | Unset
        if isinstance(self.visit_number, Unset):
            visit_number = UNSET
        else:
            visit_number = self.visit_number

        used_flag: int | None | Unset
        if isinstance(self.used_flag, Unset):
            used_flag = UNSET
        else:
            used_flag = self.used_flag

        last_update: None | str | Unset
        if isinstance(self.last_update, Unset):
            last_update = UNSET
        elif isinstance(self.last_update, datetime.datetime):
            last_update = self.last_update.isoformat()
        else:
            last_update = self.last_update

        parent_proposal: None | str | Unset
        if isinstance(self.parent_proposal, Unset):
            parent_proposal = UNSET
        else:
            parent_proposal = self.parent_proposal

        beam_line_operator: list[str] | None | Unset
        if isinstance(self.beam_line_operator, Unset):
            beam_line_operator = UNSET
        elif isinstance(self.beam_line_operator, list):
            beam_line_operator = self.beam_line_operator

        else:
            beam_line_operator = self.beam_line_operator

        collection_groups: int | None | Unset
        if isinstance(self.collection_groups, Unset):
            collection_groups = UNSET
        else:
            collection_groups = self.collection_groups

        users: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.users, Unset):
            users = []
            for users_item_data in self.users:
                users_item = users_item_data.to_dict()
                users.append(users_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "proposalId": proposal_id,
                "sessionId": session_id,
                "bltimeStamp": bltime_stamp,
                "purgedProcessedData": purged_processed_data,
                "archived": archived,
                "active": active,
            }
        )
        if beam_line_setup_id is not UNSET:
            field_dict["beamLineSetupId"] = beam_line_setup_id
        if beam_calendar_id is not UNSET:
            field_dict["beamCalendarId"] = beam_calendar_id
        if start_date is not UNSET:
            field_dict["startDate"] = start_date
        if end_date is not UNSET:
            field_dict["endDate"] = end_date
        if beam_line_name is not UNSET:
            field_dict["beamLineName"] = beam_line_name
        if scheduled is not UNSET:
            field_dict["scheduled"] = scheduled
        if nb_shifts is not UNSET:
            field_dict["nbShifts"] = nb_shifts
        if comments is not UNSET:
            field_dict["comments"] = comments
        if visit_number is not UNSET:
            field_dict["visitNumber"] = visit_number
        if used_flag is not UNSET:
            field_dict["usedFlag"] = used_flag
        if last_update is not UNSET:
            field_dict["lastUpdate"] = last_update
        if parent_proposal is not UNSET:
            field_dict["parentProposal"] = parent_proposal
        if beam_line_operator is not UNSET:
            field_dict["beamLineOperator"] = beam_line_operator
        if collection_groups is not UNSET:
            field_dict["collectionGroups"] = collection_groups
        if users is not UNSET:
            field_dict["users"] = users

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.person_out import PersonOut  # noqa: PLC0415

        d = dict(src_dict)
        proposal_id = d.pop("proposalId")

        session_id = d.pop("sessionId")

        bltime_stamp = datetime.datetime.fromisoformat(d.pop("bltimeStamp"))

        purged_processed_data = d.pop("purgedProcessedData")

        archived = d.pop("archived")

        active = d.pop("active")

        def _parse_beam_line_setup_id(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        beam_line_setup_id = _parse_beam_line_setup_id(d.pop("beamLineSetupId", UNSET))

        def _parse_beam_calendar_id(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        beam_calendar_id = _parse_beam_calendar_id(d.pop("beamCalendarId", UNSET))

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

        def _parse_beam_line_name(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        beam_line_name = _parse_beam_line_name(d.pop("beamLineName", UNSET))

        def _parse_scheduled(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        scheduled = _parse_scheduled(d.pop("scheduled", UNSET))

        def _parse_nb_shifts(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        nb_shifts = _parse_nb_shifts(d.pop("nbShifts", UNSET))

        def _parse_comments(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        comments = _parse_comments(d.pop("comments", UNSET))

        def _parse_visit_number(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        visit_number = _parse_visit_number(d.pop("visitNumber", UNSET))

        def _parse_used_flag(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        used_flag = _parse_used_flag(d.pop("usedFlag", UNSET))

        def _parse_last_update(data: object) -> datetime.datetime | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                last_update_type_0 = datetime.datetime.fromisoformat(data)

                return last_update_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(datetime.datetime | None | Unset, data)

        last_update = _parse_last_update(d.pop("lastUpdate", UNSET))

        def _parse_parent_proposal(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        parent_proposal = _parse_parent_proposal(d.pop("parentProposal", UNSET))

        def _parse_beam_line_operator(data: object) -> list[str] | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                beam_line_operator_type_0 = cast(list[str], data)

                return beam_line_operator_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[str] | None | Unset, data)

        beam_line_operator = _parse_beam_line_operator(d.pop("beamLineOperator", UNSET))

        def _parse_collection_groups(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        collection_groups = _parse_collection_groups(d.pop("collectionGroups", UNSET))

        _users = d.pop("users", UNSET)
        users: list[PersonOut] | Unset = UNSET
        if _users is not UNSET:
            users = []
            for users_item_data in _users:
                users_item = PersonOut.from_dict(users_item_data)

                users.append(users_item)

        session_out = cls(
            proposal_id=proposal_id,
            session_id=session_id,
            bltime_stamp=bltime_stamp,
            purged_processed_data=purged_processed_data,
            archived=archived,
            active=active,
            beam_line_setup_id=beam_line_setup_id,
            beam_calendar_id=beam_calendar_id,
            start_date=start_date,
            end_date=end_date,
            beam_line_name=beam_line_name,
            scheduled=scheduled,
            nb_shifts=nb_shifts,
            comments=comments,
            visit_number=visit_number,
            used_flag=used_flag,
            last_update=last_update,
            parent_proposal=parent_proposal,
            beam_line_operator=beam_line_operator,
            collection_groups=collection_groups,
            users=users,
        )

        session_out.additional_properties = d
        return session_out

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

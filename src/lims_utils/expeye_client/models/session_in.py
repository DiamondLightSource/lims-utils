from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import Any, TypeVar, cast
from uuid import UUID

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="SessionIn")


@_attrs_define
class SessionIn:
    """
    Attributes:
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
        bltime_stamp (datetime.datetime | None | Unset):
        purged_processed_data (bool | None | Unset):
        archived (int | None | Unset): The data for the session is archived and no longer available on disk
        external_id (None | Unset | UUID):
        beam_line_operator (list[str] | None | Unset):
    """

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
    bltime_stamp: datetime.datetime | None | Unset = UNSET
    purged_processed_data: bool | None | Unset = UNSET
    archived: int | None | Unset = UNSET
    external_id: None | Unset | UUID = UNSET
    beam_line_operator: list[str] | None | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
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

        bltime_stamp: None | str | Unset
        if isinstance(self.bltime_stamp, Unset):
            bltime_stamp = UNSET
        elif isinstance(self.bltime_stamp, datetime.datetime):
            bltime_stamp = self.bltime_stamp.isoformat()
        else:
            bltime_stamp = self.bltime_stamp

        purged_processed_data: bool | None | Unset
        if isinstance(self.purged_processed_data, Unset):
            purged_processed_data = UNSET
        else:
            purged_processed_data = self.purged_processed_data

        archived: int | None | Unset
        if isinstance(self.archived, Unset):
            archived = UNSET
        else:
            archived = self.archived

        external_id: None | str | Unset
        if isinstance(self.external_id, Unset):
            external_id = UNSET
        elif isinstance(self.external_id, UUID):
            external_id = str(self.external_id)
        else:
            external_id = self.external_id

        beam_line_operator: list[str] | None | Unset
        if isinstance(self.beam_line_operator, Unset):
            beam_line_operator = UNSET
        elif isinstance(self.beam_line_operator, list):
            beam_line_operator = self.beam_line_operator

        else:
            beam_line_operator = self.beam_line_operator

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
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
        if bltime_stamp is not UNSET:
            field_dict["bltimeStamp"] = bltime_stamp
        if purged_processed_data is not UNSET:
            field_dict["purgedProcessedData"] = purged_processed_data
        if archived is not UNSET:
            field_dict["archived"] = archived
        if external_id is not UNSET:
            field_dict["externalId"] = external_id
        if beam_line_operator is not UNSET:
            field_dict["beamLineOperator"] = beam_line_operator

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)

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

        def _parse_bltime_stamp(data: object) -> datetime.datetime | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                bltime_stamp_type_0 = datetime.datetime.fromisoformat(data)

                return bltime_stamp_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(datetime.datetime | None | Unset, data)

        bltime_stamp = _parse_bltime_stamp(d.pop("bltimeStamp", UNSET))

        def _parse_purged_processed_data(data: object) -> bool | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(bool | None | Unset, data)

        purged_processed_data = _parse_purged_processed_data(d.pop("purgedProcessedData", UNSET))

        def _parse_archived(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        archived = _parse_archived(d.pop("archived", UNSET))

        def _parse_external_id(data: object) -> None | Unset | UUID:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                external_id_type_0 = UUID(data)

                return external_id_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(None | Unset | UUID, data)

        external_id = _parse_external_id(d.pop("externalId", UNSET))

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

        session_in = cls(
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
            bltime_stamp=bltime_stamp,
            purged_processed_data=purged_processed_data,
            archived=archived,
            external_id=external_id,
            beam_line_operator=beam_line_operator,
        )

        session_in.additional_properties = d
        return session_in

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

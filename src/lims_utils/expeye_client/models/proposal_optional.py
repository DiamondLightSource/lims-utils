from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.state_enum import StateEnum
from ..types import UNSET, Unset

T = TypeVar("T", bound="ProposalOptional")


@_attrs_define
class ProposalOptional:
    """
    Attributes:
        title (None | str | Unset):
        proposal_type (None | str | Unset):
        start_date (datetime.datetime | None | Unset):
        end_date (datetime.datetime | None | Unset):
        person_id (int | None | Unset):
        bltime_stamp (datetime.datetime | None | Unset):
        state (None | StateEnum | Unset):
    """

    title: None | str | Unset = UNSET
    proposal_type: None | str | Unset = UNSET
    start_date: datetime.datetime | None | Unset = UNSET
    end_date: datetime.datetime | None | Unset = UNSET
    person_id: int | None | Unset = UNSET
    bltime_stamp: datetime.datetime | None | Unset = UNSET
    state: None | StateEnum | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
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

        person_id: int | None | Unset
        if isinstance(self.person_id, Unset):
            person_id = UNSET
        else:
            person_id = self.person_id

        bltime_stamp: None | str | Unset
        if isinstance(self.bltime_stamp, Unset):
            bltime_stamp = UNSET
        elif isinstance(self.bltime_stamp, datetime.datetime):
            bltime_stamp = self.bltime_stamp.isoformat()
        else:
            bltime_stamp = self.bltime_stamp

        state: None | str | Unset
        if isinstance(self.state, Unset):
            state = UNSET
        elif isinstance(self.state, StateEnum):
            state = self.state.value
        else:
            state = self.state

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if title is not UNSET:
            field_dict["title"] = title
        if proposal_type is not UNSET:
            field_dict["proposalType"] = proposal_type
        if start_date is not UNSET:
            field_dict["startDate"] = start_date
        if end_date is not UNSET:
            field_dict["endDate"] = end_date
        if person_id is not UNSET:
            field_dict["personId"] = person_id
        if bltime_stamp is not UNSET:
            field_dict["bltimeStamp"] = bltime_stamp
        if state is not UNSET:
            field_dict["state"] = state

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)

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

        def _parse_person_id(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        person_id = _parse_person_id(d.pop("personId", UNSET))

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

        def _parse_state(data: object) -> None | StateEnum | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                state_type_0 = StateEnum(data)

                return state_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(None | StateEnum | Unset, data)

        state = _parse_state(d.pop("state", UNSET))

        proposal_optional = cls(
            title=title,
            proposal_type=proposal_type,
            start_date=start_date,
            end_date=end_date,
            person_id=person_id,
            bltime_stamp=bltime_stamp,
            state=state,
        )

        proposal_optional.additional_properties = d
        return proposal_optional

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

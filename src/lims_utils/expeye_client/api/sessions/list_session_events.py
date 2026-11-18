import datetime
from http import HTTPStatus
from typing import Any
from urllib.parse import quote

import httpx2

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.http_validation_error import HTTPValidationError
from ...models.paged_union_session_event_out_session_event_with_children_out import (
    PagedUnionSessionEventOutSessionEventWithChildrenOut,
)
from ...types import UNSET, Response, Unset


def _get_kwargs(
    proposal_reference: str,
    visit_number: int,
    *,
    exclude: list[str] | Unset = UNSET,
    start_time: datetime.datetime | None | Unset = UNSET,
    end_time: datetime.datetime | None | Unset = UNSET,
    search: None | str | Unset = UNSET,
    page: int | Unset = 0,
    limit: int | Unset = 25,
) -> dict[str, Any]:

    params: dict[str, Any] = {}

    json_exclude: list[str] | Unset = UNSET
    if not isinstance(exclude, Unset):
        json_exclude = exclude

    params["exclude"] = json_exclude

    json_start_time: None | str | Unset
    if isinstance(start_time, Unset):
        json_start_time = UNSET
    elif isinstance(start_time, datetime.datetime):
        json_start_time = start_time.isoformat()
    else:
        json_start_time = start_time
    params["startTime"] = json_start_time

    json_end_time: None | str | Unset
    if isinstance(end_time, Unset):
        json_end_time = UNSET
    elif isinstance(end_time, datetime.datetime):
        json_end_time = end_time.isoformat()
    else:
        json_end_time = end_time
    params["endTime"] = json_end_time

    json_search: None | str | Unset
    if isinstance(search, Unset):
        json_search = UNSET
    else:
        json_search = search
    params["search"] = json_search

    params["page"] = page

    params["limit"] = limit

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/proposals/{proposal_reference}/sessions/{visit_number}/events".format(
            proposal_reference=quote(str(proposal_reference), safe=""),
            visit_number=quote(str(visit_number), safe=""),
        ),
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx2.Response
) -> HTTPValidationError | PagedUnionSessionEventOutSessionEventWithChildrenOut | None:
    if response.status_code == 200:
        response_200 = PagedUnionSessionEventOutSessionEventWithChildrenOut.from_dict(response.json())

        return response_200

    if response.status_code == 422:
        response_422 = HTTPValidationError.from_dict(response.json())

        return response_422

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx2.Response
) -> Response[HTTPValidationError | PagedUnionSessionEventOutSessionEventWithChildrenOut]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    proposal_reference: str,
    visit_number: int,
    *,
    client: AuthenticatedClient,
    exclude: list[str] | Unset = UNSET,
    start_time: datetime.datetime | None | Unset = UNSET,
    end_time: datetime.datetime | None | Unset = UNSET,
    search: None | str | Unset = UNSET,
    page: int | Unset = 0,
    limit: int | Unset = 25,
) -> Response[HTTPValidationError | PagedUnionSessionEventOutSessionEventWithChildrenOut]:
    """Get Session Events

     Get session events (robot actions, fluorescence spectrums, data collection groups, energy scans)

    Args:
        proposal_reference (str):
        visit_number (int):
        exclude (list[str] | Unset):
        start_time (datetime.datetime | None | Unset):
        end_time (datetime.datetime | None | Unset):
        search (None | str | Unset):
        page (int | Unset): Page number/Results to skip. Negative numbers count backwards from the
            last page Default: 0.
        limit (int | Unset): Number of results to show Default: 25.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and
        Client.raise_on_unexpected_status is True.
        httpx2.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[HTTPValidationError | PagedUnionSessionEventOutSessionEventWithChildrenOut]
    """

    kwargs = _get_kwargs(
        proposal_reference=proposal_reference,
        visit_number=visit_number,
        exclude=exclude,
        start_time=start_time,
        end_time=end_time,
        search=search,
        page=page,
        limit=limit,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    proposal_reference: str,
    visit_number: int,
    *,
    client: AuthenticatedClient,
    exclude: list[str] | Unset = UNSET,
    start_time: datetime.datetime | None | Unset = UNSET,
    end_time: datetime.datetime | None | Unset = UNSET,
    search: None | str | Unset = UNSET,
    page: int | Unset = 0,
    limit: int | Unset = 25,
) -> HTTPValidationError | PagedUnionSessionEventOutSessionEventWithChildrenOut | None:
    """Get Session Events

     Get session events (robot actions, fluorescence spectrums, data collection groups, energy scans)

    Args:
        proposal_reference (str):
        visit_number (int):
        exclude (list[str] | Unset):
        start_time (datetime.datetime | None | Unset):
        end_time (datetime.datetime | None | Unset):
        search (None | str | Unset):
        page (int | Unset): Page number/Results to skip. Negative numbers count backwards from the
            last page Default: 0.
        limit (int | Unset): Number of results to show Default: 25.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and
        Client.raise_on_unexpected_status is True.
        httpx2.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        HTTPValidationError | PagedUnionSessionEventOutSessionEventWithChildrenOut
    """

    return sync_detailed(
        proposal_reference=proposal_reference,
        visit_number=visit_number,
        client=client,
        exclude=exclude,
        start_time=start_time,
        end_time=end_time,
        search=search,
        page=page,
        limit=limit,
    ).parsed


async def asyncio_detailed(
    proposal_reference: str,
    visit_number: int,
    *,
    client: AuthenticatedClient,
    exclude: list[str] | Unset = UNSET,
    start_time: datetime.datetime | None | Unset = UNSET,
    end_time: datetime.datetime | None | Unset = UNSET,
    search: None | str | Unset = UNSET,
    page: int | Unset = 0,
    limit: int | Unset = 25,
) -> Response[HTTPValidationError | PagedUnionSessionEventOutSessionEventWithChildrenOut]:
    """Get Session Events

     Get session events (robot actions, fluorescence spectrums, data collection groups, energy scans)

    Args:
        proposal_reference (str):
        visit_number (int):
        exclude (list[str] | Unset):
        start_time (datetime.datetime | None | Unset):
        end_time (datetime.datetime | None | Unset):
        search (None | str | Unset):
        page (int | Unset): Page number/Results to skip. Negative numbers count backwards from the
            last page Default: 0.
        limit (int | Unset): Number of results to show Default: 25.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and
        Client.raise_on_unexpected_status is True.
        httpx2.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[HTTPValidationError | PagedUnionSessionEventOutSessionEventWithChildrenOut]
    """

    kwargs = _get_kwargs(
        proposal_reference=proposal_reference,
        visit_number=visit_number,
        exclude=exclude,
        start_time=start_time,
        end_time=end_time,
        search=search,
        page=page,
        limit=limit,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    proposal_reference: str,
    visit_number: int,
    *,
    client: AuthenticatedClient,
    exclude: list[str] | Unset = UNSET,
    start_time: datetime.datetime | None | Unset = UNSET,
    end_time: datetime.datetime | None | Unset = UNSET,
    search: None | str | Unset = UNSET,
    page: int | Unset = 0,
    limit: int | Unset = 25,
) -> HTTPValidationError | PagedUnionSessionEventOutSessionEventWithChildrenOut | None:
    """Get Session Events

     Get session events (robot actions, fluorescence spectrums, data collection groups, energy scans)

    Args:
        proposal_reference (str):
        visit_number (int):
        exclude (list[str] | Unset):
        start_time (datetime.datetime | None | Unset):
        end_time (datetime.datetime | None | Unset):
        search (None | str | Unset):
        page (int | Unset): Page number/Results to skip. Negative numbers count backwards from the
            last page Default: 0.
        limit (int | Unset): Number of results to show Default: 25.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and
        Client.raise_on_unexpected_status is True.
        httpx2.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        HTTPValidationError | PagedUnionSessionEventOutSessionEventWithChildrenOut
    """

    return (
        await asyncio_detailed(
            proposal_reference=proposal_reference,
            visit_number=visit_number,
            client=client,
            exclude=exclude,
            start_time=start_time,
            end_time=end_time,
            search=search,
            page=page,
            limit=limit,
        )
    ).parsed

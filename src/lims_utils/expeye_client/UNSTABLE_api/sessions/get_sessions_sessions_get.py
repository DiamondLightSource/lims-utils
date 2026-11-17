import datetime
from http import HTTPStatus
from typing import Any

import httpx2

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.http_validation_error import HTTPValidationError
from ...models.paged_session_out import PagedSessionOut
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    search: None | str | Unset = UNSET,
    beam_line_name: list[str] | None | Unset = UNSET,
    proposal_code: None | str | Unset = UNSET,
    min_end_date: datetime.datetime | None | Unset = UNSET,
    max_end_date: datetime.datetime | None | Unset = UNSET,
    min_start_date: datetime.datetime | None | Unset = UNSET,
    max_start_date: datetime.datetime | None | Unset = UNSET,
    active: bool | Unset = False,
    count_collections: bool | Unset = False,
    hide_null: bool | Unset = True,
    page: int | Unset = 0,
    limit: int | Unset = 25,
) -> dict[str, Any]:

    params: dict[str, Any] = {}

    json_search: None | str | Unset
    if isinstance(search, Unset):
        json_search = UNSET
    else:
        json_search = search
    params["search"] = json_search

    json_beam_line_name: list[str] | None | Unset
    if isinstance(beam_line_name, Unset):
        json_beam_line_name = UNSET
    elif isinstance(beam_line_name, list):
        json_beam_line_name = beam_line_name

    else:
        json_beam_line_name = beam_line_name
    params["beamLineName"] = json_beam_line_name

    json_proposal_code: None | str | Unset
    if isinstance(proposal_code, Unset):
        json_proposal_code = UNSET
    else:
        json_proposal_code = proposal_code
    params["proposalCode"] = json_proposal_code

    json_min_end_date: None | str | Unset
    if isinstance(min_end_date, Unset):
        json_min_end_date = UNSET
    elif isinstance(min_end_date, datetime.datetime):
        json_min_end_date = min_end_date.isoformat()
    else:
        json_min_end_date = min_end_date
    params["minEndDate"] = json_min_end_date

    json_max_end_date: None | str | Unset
    if isinstance(max_end_date, Unset):
        json_max_end_date = UNSET
    elif isinstance(max_end_date, datetime.datetime):
        json_max_end_date = max_end_date.isoformat()
    else:
        json_max_end_date = max_end_date
    params["maxEndDate"] = json_max_end_date

    json_min_start_date: None | str | Unset
    if isinstance(min_start_date, Unset):
        json_min_start_date = UNSET
    elif isinstance(min_start_date, datetime.datetime):
        json_min_start_date = min_start_date.isoformat()
    else:
        json_min_start_date = min_start_date
    params["minStartDate"] = json_min_start_date

    json_max_start_date: None | str | Unset
    if isinstance(max_start_date, Unset):
        json_max_start_date = UNSET
    elif isinstance(max_start_date, datetime.datetime):
        json_max_start_date = max_start_date.isoformat()
    else:
        json_max_start_date = max_start_date
    params["maxStartDate"] = json_max_start_date

    params["active"] = active

    params["countCollections"] = count_collections

    params["hideNull"] = hide_null

    params["page"] = page

    params["limit"] = limit

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/sessions",
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx2.Response
) -> HTTPValidationError | PagedSessionOut | None:
    if response.status_code == 200:
        response_200 = PagedSessionOut.from_dict(response.json())

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
) -> Response[HTTPValidationError | PagedSessionOut]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient,
    search: None | str | Unset = UNSET,
    beam_line_name: list[str] | None | Unset = UNSET,
    proposal_code: None | str | Unset = UNSET,
    min_end_date: datetime.datetime | None | Unset = UNSET,
    max_end_date: datetime.datetime | None | Unset = UNSET,
    min_start_date: datetime.datetime | None | Unset = UNSET,
    max_start_date: datetime.datetime | None | Unset = UNSET,
    active: bool | Unset = False,
    count_collections: bool | Unset = False,
    hide_null: bool | Unset = True,
    page: int | Unset = 0,
    limit: int | Unset = 25,
) -> Response[HTTPValidationError | PagedSessionOut]:
    """Get Sessions

     List visits

    Args:
        search (None | str | Unset):
        beam_line_name (list[str] | None | Unset):
        proposal_code (None | str | Unset):
        min_end_date (datetime.datetime | None | Unset):
        max_end_date (datetime.datetime | None | Unset):
        min_start_date (datetime.datetime | None | Unset):
        max_start_date (datetime.datetime | None | Unset):
        active (bool | Unset):  Default: False.
        count_collections (bool | Unset):  Default: False.
        hide_null (bool | Unset):  Default: True.
        page (int | Unset): Page number/Results to skip. Negative numbers count backwards from the
            last page Default: 0.
        limit (int | Unset): Number of results to show Default: 25.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx2.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[HTTPValidationError | PagedSessionOut]
    """

    kwargs = _get_kwargs(
        search=search,
        beam_line_name=beam_line_name,
        proposal_code=proposal_code,
        min_end_date=min_end_date,
        max_end_date=max_end_date,
        min_start_date=min_start_date,
        max_start_date=max_start_date,
        active=active,
        count_collections=count_collections,
        hide_null=hide_null,
        page=page,
        limit=limit,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: AuthenticatedClient,
    search: None | str | Unset = UNSET,
    beam_line_name: list[str] | None | Unset = UNSET,
    proposal_code: None | str | Unset = UNSET,
    min_end_date: datetime.datetime | None | Unset = UNSET,
    max_end_date: datetime.datetime | None | Unset = UNSET,
    min_start_date: datetime.datetime | None | Unset = UNSET,
    max_start_date: datetime.datetime | None | Unset = UNSET,
    active: bool | Unset = False,
    count_collections: bool | Unset = False,
    hide_null: bool | Unset = True,
    page: int | Unset = 0,
    limit: int | Unset = 25,
) -> HTTPValidationError | PagedSessionOut | None:
    """Get Sessions

     List visits

    Args:
        search (None | str | Unset):
        beam_line_name (list[str] | None | Unset):
        proposal_code (None | str | Unset):
        min_end_date (datetime.datetime | None | Unset):
        max_end_date (datetime.datetime | None | Unset):
        min_start_date (datetime.datetime | None | Unset):
        max_start_date (datetime.datetime | None | Unset):
        active (bool | Unset):  Default: False.
        count_collections (bool | Unset):  Default: False.
        hide_null (bool | Unset):  Default: True.
        page (int | Unset): Page number/Results to skip. Negative numbers count backwards from the
            last page Default: 0.
        limit (int | Unset): Number of results to show Default: 25.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx2.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        HTTPValidationError | PagedSessionOut
    """

    return sync_detailed(
        client=client,
        search=search,
        beam_line_name=beam_line_name,
        proposal_code=proposal_code,
        min_end_date=min_end_date,
        max_end_date=max_end_date,
        min_start_date=min_start_date,
        max_start_date=max_start_date,
        active=active,
        count_collections=count_collections,
        hide_null=hide_null,
        page=page,
        limit=limit,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    search: None | str | Unset = UNSET,
    beam_line_name: list[str] | None | Unset = UNSET,
    proposal_code: None | str | Unset = UNSET,
    min_end_date: datetime.datetime | None | Unset = UNSET,
    max_end_date: datetime.datetime | None | Unset = UNSET,
    min_start_date: datetime.datetime | None | Unset = UNSET,
    max_start_date: datetime.datetime | None | Unset = UNSET,
    active: bool | Unset = False,
    count_collections: bool | Unset = False,
    hide_null: bool | Unset = True,
    page: int | Unset = 0,
    limit: int | Unset = 25,
) -> Response[HTTPValidationError | PagedSessionOut]:
    """Get Sessions

     List visits

    Args:
        search (None | str | Unset):
        beam_line_name (list[str] | None | Unset):
        proposal_code (None | str | Unset):
        min_end_date (datetime.datetime | None | Unset):
        max_end_date (datetime.datetime | None | Unset):
        min_start_date (datetime.datetime | None | Unset):
        max_start_date (datetime.datetime | None | Unset):
        active (bool | Unset):  Default: False.
        count_collections (bool | Unset):  Default: False.
        hide_null (bool | Unset):  Default: True.
        page (int | Unset): Page number/Results to skip. Negative numbers count backwards from the
            last page Default: 0.
        limit (int | Unset): Number of results to show Default: 25.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx2.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[HTTPValidationError | PagedSessionOut]
    """

    kwargs = _get_kwargs(
        search=search,
        beam_line_name=beam_line_name,
        proposal_code=proposal_code,
        min_end_date=min_end_date,
        max_end_date=max_end_date,
        min_start_date=min_start_date,
        max_start_date=max_start_date,
        active=active,
        count_collections=count_collections,
        hide_null=hide_null,
        page=page,
        limit=limit,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient,
    search: None | str | Unset = UNSET,
    beam_line_name: list[str] | None | Unset = UNSET,
    proposal_code: None | str | Unset = UNSET,
    min_end_date: datetime.datetime | None | Unset = UNSET,
    max_end_date: datetime.datetime | None | Unset = UNSET,
    min_start_date: datetime.datetime | None | Unset = UNSET,
    max_start_date: datetime.datetime | None | Unset = UNSET,
    active: bool | Unset = False,
    count_collections: bool | Unset = False,
    hide_null: bool | Unset = True,
    page: int | Unset = 0,
    limit: int | Unset = 25,
) -> HTTPValidationError | PagedSessionOut | None:
    """Get Sessions

     List visits

    Args:
        search (None | str | Unset):
        beam_line_name (list[str] | None | Unset):
        proposal_code (None | str | Unset):
        min_end_date (datetime.datetime | None | Unset):
        max_end_date (datetime.datetime | None | Unset):
        min_start_date (datetime.datetime | None | Unset):
        max_start_date (datetime.datetime | None | Unset):
        active (bool | Unset):  Default: False.
        count_collections (bool | Unset):  Default: False.
        hide_null (bool | Unset):  Default: True.
        page (int | Unset): Page number/Results to skip. Negative numbers count backwards from the
            last page Default: 0.
        limit (int | Unset): Number of results to show Default: 25.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx2.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        HTTPValidationError | PagedSessionOut
    """

    return (
        await asyncio_detailed(
            client=client,
            search=search,
            beam_line_name=beam_line_name,
            proposal_code=proposal_code,
            min_end_date=min_end_date,
            max_end_date=max_end_date,
            min_start_date=min_start_date,
            max_start_date=max_start_date,
            active=active,
            count_collections=count_collections,
            hide_null=hide_null,
            page=page,
            limit=limit,
        )
    ).parsed

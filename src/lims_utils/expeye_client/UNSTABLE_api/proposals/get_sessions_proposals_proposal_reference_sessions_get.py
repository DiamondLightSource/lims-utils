from http import HTTPStatus
from typing import Any
from urllib.parse import quote

import httpx2

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.http_validation_error import HTTPValidationError
from ...models.paged_session_out import PagedSessionOut
from ...types import UNSET, Response, Unset


def _get_kwargs(
    proposal_reference: str,
    *,
    search: str | Unset = "",
    beam_line_name: list[str] | None | Unset = UNSET,
    active: bool | Unset = False,
    count_collections: bool | Unset = True,
    hide_null: bool | Unset = True,
    page: int | Unset = 0,
    limit: int | Unset = 25,
) -> dict[str, Any]:

    params: dict[str, Any] = {}

    params["search"] = search

    json_beam_line_name: list[str] | None | Unset
    if isinstance(beam_line_name, Unset):
        json_beam_line_name = UNSET
    elif isinstance(beam_line_name, list):
        json_beam_line_name = beam_line_name

    else:
        json_beam_line_name = beam_line_name
    params["beamLineName"] = json_beam_line_name

    params["active"] = active

    params["countCollections"] = count_collections

    params["hideNull"] = hide_null

    params["page"] = page

    params["limit"] = limit

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/proposals/{proposal_reference}/sessions".format(
            proposal_reference=quote(str(proposal_reference), safe=""),
        ),
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
    proposal_reference: str,
    *,
    client: AuthenticatedClient,
    search: str | Unset = "",
    beam_line_name: list[str] | None | Unset = UNSET,
    active: bool | Unset = False,
    count_collections: bool | Unset = True,
    hide_null: bool | Unset = True,
    page: int | Unset = 0,
    limit: int | Unset = 25,
) -> Response[HTTPValidationError | PagedSessionOut]:
    """Get Sessions

     Get sessions belonging to proposal

    Args:
        proposal_reference (str):
        search (str | Unset):  Default: ''.
        beam_line_name (list[str] | None | Unset):
        active (bool | Unset):  Default: False.
        count_collections (bool | Unset):  Default: True.
        hide_null (bool | Unset):  Default: True.
        page (int | Unset): Page number/Results to skip. Negative numbers count backwards from the
            last page Default: 0.
        limit (int | Unset): Number of results to show Default: 25.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and
            Client.raise_on_unexpected_status is True.
        httpx2.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[HTTPValidationError | PagedSessionOut]
    """

    kwargs = _get_kwargs(
        proposal_reference=proposal_reference,
        search=search,
        beam_line_name=beam_line_name,
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
    proposal_reference: str,
    *,
    client: AuthenticatedClient,
    search: str | Unset = "",
    beam_line_name: list[str] | None | Unset = UNSET,
    active: bool | Unset = False,
    count_collections: bool | Unset = True,
    hide_null: bool | Unset = True,
    page: int | Unset = 0,
    limit: int | Unset = 25,
) -> HTTPValidationError | PagedSessionOut | None:
    """Get Sessions

     Get sessions belonging to proposal

    Args:
        proposal_reference (str):
        search (str | Unset):  Default: ''.
        beam_line_name (list[str] | None | Unset):
        active (bool | Unset):  Default: False.
        count_collections (bool | Unset):  Default: True.
        hide_null (bool | Unset):  Default: True.
        page (int | Unset): Page number/Results to skip. Negative numbers count backwards from the
            last page Default: 0.
        limit (int | Unset): Number of results to show Default: 25.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and
            Client.raise_on_unexpected_status is True.
        httpx2.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        HTTPValidationError | PagedSessionOut
    """

    return sync_detailed(
        proposal_reference=proposal_reference,
        client=client,
        search=search,
        beam_line_name=beam_line_name,
        active=active,
        count_collections=count_collections,
        hide_null=hide_null,
        page=page,
        limit=limit,
    ).parsed


async def asyncio_detailed(
    proposal_reference: str,
    *,
    client: AuthenticatedClient,
    search: str | Unset = "",
    beam_line_name: list[str] | None | Unset = UNSET,
    active: bool | Unset = False,
    count_collections: bool | Unset = True,
    hide_null: bool | Unset = True,
    page: int | Unset = 0,
    limit: int | Unset = 25,
) -> Response[HTTPValidationError | PagedSessionOut]:
    """Get Sessions

     Get sessions belonging to proposal

    Args:
        proposal_reference (str):
        search (str | Unset):  Default: ''.
        beam_line_name (list[str] | None | Unset):
        active (bool | Unset):  Default: False.
        count_collections (bool | Unset):  Default: True.
        hide_null (bool | Unset):  Default: True.
        page (int | Unset): Page number/Results to skip. Negative numbers count backwards from the
            last page Default: 0.
        limit (int | Unset): Number of results to show Default: 25.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and
            Client.raise_on_unexpected_status is True.
        httpx2.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[HTTPValidationError | PagedSessionOut]
    """

    kwargs = _get_kwargs(
        proposal_reference=proposal_reference,
        search=search,
        beam_line_name=beam_line_name,
        active=active,
        count_collections=count_collections,
        hide_null=hide_null,
        page=page,
        limit=limit,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    proposal_reference: str,
    *,
    client: AuthenticatedClient,
    search: str | Unset = "",
    beam_line_name: list[str] | None | Unset = UNSET,
    active: bool | Unset = False,
    count_collections: bool | Unset = True,
    hide_null: bool | Unset = True,
    page: int | Unset = 0,
    limit: int | Unset = 25,
) -> HTTPValidationError | PagedSessionOut | None:
    """Get Sessions

     Get sessions belonging to proposal

    Args:
        proposal_reference (str):
        search (str | Unset):  Default: ''.
        beam_line_name (list[str] | None | Unset):
        active (bool | Unset):  Default: False.
        count_collections (bool | Unset):  Default: True.
        hide_null (bool | Unset):  Default: True.
        page (int | Unset): Page number/Results to skip. Negative numbers count backwards from the
            last page Default: 0.
        limit (int | Unset): Number of results to show Default: 25.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and
            Client.raise_on_unexpected_status is True.
        httpx2.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        HTTPValidationError | PagedSessionOut
    """

    return (
        await asyncio_detailed(
            proposal_reference=proposal_reference,
            client=client,
            search=search,
            beam_line_name=beam_line_name,
            active=active,
            count_collections=count_collections,
            hide_null=hide_null,
            page=page,
            limit=limit,
        )
    ).parsed

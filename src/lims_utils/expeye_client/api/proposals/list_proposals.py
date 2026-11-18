from http import HTTPStatus
from typing import Any

import httpx2

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.http_validation_error import HTTPValidationError
from ...models.paged_proposal_out import PagedProposalOut
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    search: str | Unset = "",
    proposal_reference: str | Unset = "",
    title: str | Unset = "",
    beam_line_name: str | Unset = "",
    principal_investigator: str | Unset = "",
    page: int | Unset = 0,
    limit: int | Unset = 25,
) -> dict[str, Any]:

    params: dict[str, Any] = {}

    params["search"] = search

    params["proposalReference"] = proposal_reference

    params["title"] = title

    params["beamLineName"] = beam_line_name

    params["principalInvestigator"] = principal_investigator

    params["page"] = page

    params["limit"] = limit

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/proposals",
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx2.Response
) -> HTTPValidationError | PagedProposalOut | None:
    if response.status_code == 200:
        response_200 = PagedProposalOut.from_dict(response.json())

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
) -> Response[HTTPValidationError | PagedProposalOut]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient,
    search: str | Unset = "",
    proposal_reference: str | Unset = "",
    title: str | Unset = "",
    beam_line_name: str | Unset = "",
    principal_investigator: str | Unset = "",
    page: int | Unset = 0,
    limit: int | Unset = 25,
) -> Response[HTTPValidationError | PagedProposalOut]:
    """Get Proposals

     List proposals

    Args:
        search (str | Unset):  Default: ''.
        proposal_reference (str | Unset):  Default: ''.
        title (str | Unset):  Default: ''.
        beam_line_name (str | Unset):  Default: ''.
        principal_investigator (str | Unset):  Default: ''.
        page (int | Unset): Page number/Results to skip. Negative numbers count backwards from the
            last page Default: 0.
        limit (int | Unset): Number of results to show Default: 25.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and
        Client.raise_on_unexpected_status is True.
        httpx2.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[HTTPValidationError | PagedProposalOut]
    """

    kwargs = _get_kwargs(
        search=search,
        proposal_reference=proposal_reference,
        title=title,
        beam_line_name=beam_line_name,
        principal_investigator=principal_investigator,
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
    search: str | Unset = "",
    proposal_reference: str | Unset = "",
    title: str | Unset = "",
    beam_line_name: str | Unset = "",
    principal_investigator: str | Unset = "",
    page: int | Unset = 0,
    limit: int | Unset = 25,
) -> HTTPValidationError | PagedProposalOut | None:
    """Get Proposals

     List proposals

    Args:
        search (str | Unset):  Default: ''.
        proposal_reference (str | Unset):  Default: ''.
        title (str | Unset):  Default: ''.
        beam_line_name (str | Unset):  Default: ''.
        principal_investigator (str | Unset):  Default: ''.
        page (int | Unset): Page number/Results to skip. Negative numbers count backwards from the
            last page Default: 0.
        limit (int | Unset): Number of results to show Default: 25.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and
        Client.raise_on_unexpected_status is True.
        httpx2.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        HTTPValidationError | PagedProposalOut
    """

    return sync_detailed(
        client=client,
        search=search,
        proposal_reference=proposal_reference,
        title=title,
        beam_line_name=beam_line_name,
        principal_investigator=principal_investigator,
        page=page,
        limit=limit,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    search: str | Unset = "",
    proposal_reference: str | Unset = "",
    title: str | Unset = "",
    beam_line_name: str | Unset = "",
    principal_investigator: str | Unset = "",
    page: int | Unset = 0,
    limit: int | Unset = 25,
) -> Response[HTTPValidationError | PagedProposalOut]:
    """Get Proposals

     List proposals

    Args:
        search (str | Unset):  Default: ''.
        proposal_reference (str | Unset):  Default: ''.
        title (str | Unset):  Default: ''.
        beam_line_name (str | Unset):  Default: ''.
        principal_investigator (str | Unset):  Default: ''.
        page (int | Unset): Page number/Results to skip. Negative numbers count backwards from the
            last page Default: 0.
        limit (int | Unset): Number of results to show Default: 25.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and
        Client.raise_on_unexpected_status is True.
        httpx2.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[HTTPValidationError | PagedProposalOut]
    """

    kwargs = _get_kwargs(
        search=search,
        proposal_reference=proposal_reference,
        title=title,
        beam_line_name=beam_line_name,
        principal_investigator=principal_investigator,
        page=page,
        limit=limit,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient,
    search: str | Unset = "",
    proposal_reference: str | Unset = "",
    title: str | Unset = "",
    beam_line_name: str | Unset = "",
    principal_investigator: str | Unset = "",
    page: int | Unset = 0,
    limit: int | Unset = 25,
) -> HTTPValidationError | PagedProposalOut | None:
    """Get Proposals

     List proposals

    Args:
        search (str | Unset):  Default: ''.
        proposal_reference (str | Unset):  Default: ''.
        title (str | Unset):  Default: ''.
        beam_line_name (str | Unset):  Default: ''.
        principal_investigator (str | Unset):  Default: ''.
        page (int | Unset): Page number/Results to skip. Negative numbers count backwards from the
            last page Default: 0.
        limit (int | Unset): Number of results to show Default: 25.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and
        Client.raise_on_unexpected_status is True.
        httpx2.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        HTTPValidationError | PagedProposalOut
    """

    return (
        await asyncio_detailed(
            client=client,
            search=search,
            proposal_reference=proposal_reference,
            title=title,
            beam_line_name=beam_line_name,
            principal_investigator=principal_investigator,
            page=page,
            limit=limit,
        )
    ).parsed

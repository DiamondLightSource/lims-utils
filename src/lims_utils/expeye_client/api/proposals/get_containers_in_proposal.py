from http import HTTPStatus
from typing import Any
from urllib.parse import quote

import httpx2

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.http_validation_error import HTTPValidationError
from ...models.paged_container_out import PagedContainerOut
from ...types import UNSET, Response, Unset


def _get_kwargs(
    proposal_reference: str,
    *,
    dewar_status: None | str | Unset = UNSET,
    container_status: None | str | Unset = UNSET,
    beamline_location: None | str | Unset = UNSET,
    page: int | Unset = 0,
    limit: int | Unset = 25,
) -> dict[str, Any]:

    params: dict[str, Any] = {}

    json_dewar_status: None | str | Unset
    if isinstance(dewar_status, Unset):
        json_dewar_status = UNSET
    else:
        json_dewar_status = dewar_status
    params["dewarStatus"] = json_dewar_status

    json_container_status: None | str | Unset
    if isinstance(container_status, Unset):
        json_container_status = UNSET
    else:
        json_container_status = container_status
    params["containerStatus"] = json_container_status

    json_beamline_location: None | str | Unset
    if isinstance(beamline_location, Unset):
        json_beamline_location = UNSET
    else:
        json_beamline_location = beamline_location
    params["beamlineLocation"] = json_beamline_location

    params["page"] = page

    params["limit"] = limit

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/proposals/{proposal_reference}/containers".format(
            proposal_reference=quote(str(proposal_reference), safe=""),
        ),
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx2.Response
) -> HTTPValidationError | PagedContainerOut | None:
    if response.status_code == 200:
        response_200 = PagedContainerOut.from_dict(response.json())

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
) -> Response[HTTPValidationError | PagedContainerOut]:
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
    dewar_status: None | str | Unset = UNSET,
    container_status: None | str | Unset = UNSET,
    beamline_location: None | str | Unset = UNSET,
    page: int | Unset = 0,
    limit: int | Unset = 25,
) -> Response[HTTPValidationError | PagedContainerOut]:
    """Get Containers In Proposal

     Get proposal containers

    Args:
        proposal_reference (str):
        dewar_status (None | str | Unset):
        container_status (None | str | Unset):
        beamline_location (None | str | Unset):
        page (int | Unset): Page number/Results to skip. Negative numbers count backwards from the
            last page Default: 0.
        limit (int | Unset): Number of results to show Default: 25.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and
        Client.raise_on_unexpected_status is True.
        httpx2.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[HTTPValidationError | PagedContainerOut]
    """

    kwargs = _get_kwargs(
        proposal_reference=proposal_reference,
        dewar_status=dewar_status,
        container_status=container_status,
        beamline_location=beamline_location,
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
    dewar_status: None | str | Unset = UNSET,
    container_status: None | str | Unset = UNSET,
    beamline_location: None | str | Unset = UNSET,
    page: int | Unset = 0,
    limit: int | Unset = 25,
) -> HTTPValidationError | PagedContainerOut | None:
    """Get Containers In Proposal

     Get proposal containers

    Args:
        proposal_reference (str):
        dewar_status (None | str | Unset):
        container_status (None | str | Unset):
        beamline_location (None | str | Unset):
        page (int | Unset): Page number/Results to skip. Negative numbers count backwards from the
            last page Default: 0.
        limit (int | Unset): Number of results to show Default: 25.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and
        Client.raise_on_unexpected_status is True.
        httpx2.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        HTTPValidationError | PagedContainerOut
    """

    return sync_detailed(
        proposal_reference=proposal_reference,
        client=client,
        dewar_status=dewar_status,
        container_status=container_status,
        beamline_location=beamline_location,
        page=page,
        limit=limit,
    ).parsed


async def asyncio_detailed(
    proposal_reference: str,
    *,
    client: AuthenticatedClient,
    dewar_status: None | str | Unset = UNSET,
    container_status: None | str | Unset = UNSET,
    beamline_location: None | str | Unset = UNSET,
    page: int | Unset = 0,
    limit: int | Unset = 25,
) -> Response[HTTPValidationError | PagedContainerOut]:
    """Get Containers In Proposal

     Get proposal containers

    Args:
        proposal_reference (str):
        dewar_status (None | str | Unset):
        container_status (None | str | Unset):
        beamline_location (None | str | Unset):
        page (int | Unset): Page number/Results to skip. Negative numbers count backwards from the
            last page Default: 0.
        limit (int | Unset): Number of results to show Default: 25.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and
        Client.raise_on_unexpected_status is True.
        httpx2.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[HTTPValidationError | PagedContainerOut]
    """

    kwargs = _get_kwargs(
        proposal_reference=proposal_reference,
        dewar_status=dewar_status,
        container_status=container_status,
        beamline_location=beamline_location,
        page=page,
        limit=limit,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    proposal_reference: str,
    *,
    client: AuthenticatedClient,
    dewar_status: None | str | Unset = UNSET,
    container_status: None | str | Unset = UNSET,
    beamline_location: None | str | Unset = UNSET,
    page: int | Unset = 0,
    limit: int | Unset = 25,
) -> HTTPValidationError | PagedContainerOut | None:
    """Get Containers In Proposal

     Get proposal containers

    Args:
        proposal_reference (str):
        dewar_status (None | str | Unset):
        container_status (None | str | Unset):
        beamline_location (None | str | Unset):
        page (int | Unset): Page number/Results to skip. Negative numbers count backwards from the
            last page Default: 0.
        limit (int | Unset): Number of results to show Default: 25.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and
        Client.raise_on_unexpected_status is True.
        httpx2.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        HTTPValidationError | PagedContainerOut
    """

    return (
        await asyncio_detailed(
            proposal_reference=proposal_reference,
            client=client,
            dewar_status=dewar_status,
            container_status=container_status,
            beamline_location=beamline_location,
            page=page,
            limit=limit,
        )
    ).parsed

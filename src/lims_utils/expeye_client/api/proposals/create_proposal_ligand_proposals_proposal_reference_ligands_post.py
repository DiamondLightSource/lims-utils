from http import HTTPStatus
from typing import Any
from urllib.parse import quote

import httpx2

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.http_validation_error import HTTPValidationError
from ...models.ligand_in import LigandIn
from ...models.ligand_out import LigandOut
from ...types import Response


def _get_kwargs(
    proposal_reference: str,
    *,
    body: LigandIn,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/proposals/{proposal_reference}/ligands".format(
            proposal_reference=quote(str(proposal_reference), safe=""),
        ),
    }

    _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx2.Response
) -> HTTPValidationError | LigandOut | None:
    if response.status_code == 201:
        response_201 = LigandOut.from_dict(response.json())

        return response_201

    if response.status_code == 422:
        response_422 = HTTPValidationError.from_dict(response.json())

        return response_422

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx2.Response
) -> Response[HTTPValidationError | LigandOut]:
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
    body: LigandIn,
) -> Response[HTTPValidationError | LigandOut]:
    """Create Proposal Ligand

     Create new ligand for proposal

    Args:
        proposal_reference (str):
        body (LigandIn):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx2.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[HTTPValidationError | LigandOut]
    """

    kwargs = _get_kwargs(
        proposal_reference=proposal_reference,
        body=body,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    proposal_reference: str,
    *,
    client: AuthenticatedClient,
    body: LigandIn,
) -> HTTPValidationError | LigandOut | None:
    """Create Proposal Ligand

     Create new ligand for proposal

    Args:
        proposal_reference (str):
        body (LigandIn):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx2.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        HTTPValidationError | LigandOut
    """

    return sync_detailed(
        proposal_reference=proposal_reference,
        client=client,
        body=body,
    ).parsed


async def asyncio_detailed(
    proposal_reference: str,
    *,
    client: AuthenticatedClient,
    body: LigandIn,
) -> Response[HTTPValidationError | LigandOut]:
    """Create Proposal Ligand

     Create new ligand for proposal

    Args:
        proposal_reference (str):
        body (LigandIn):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx2.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[HTTPValidationError | LigandOut]
    """

    kwargs = _get_kwargs(
        proposal_reference=proposal_reference,
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    proposal_reference: str,
    *,
    client: AuthenticatedClient,
    body: LigandIn,
) -> HTTPValidationError | LigandOut | None:
    """Create Proposal Ligand

     Create new ligand for proposal

    Args:
        proposal_reference (str):
        body (LigandIn):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx2.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        HTTPValidationError | LigandOut
    """

    return (
        await asyncio_detailed(
            proposal_reference=proposal_reference,
            client=client,
            body=body,
        )
    ).parsed

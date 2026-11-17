from http import HTTPStatus
from typing import Any
from urllib.parse import quote

import httpx2

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.http_validation_error import HTTPValidationError
from ...models.proposal_optional import ProposalOptional
from ...models.proposal_out import ProposalOut
from ...types import Response


def _get_kwargs(
    proposal_reference: str,
    *,
    body: ProposalOptional,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "patch",
        "url": "/proposals/{proposal_reference}".format(
            proposal_reference=quote(str(proposal_reference), safe=""),
        ),
    }

    _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx2.Response
) -> HTTPValidationError | ProposalOut | None:
    if response.status_code == 200:
        response_200 = ProposalOut.from_dict(response.json())

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
) -> Response[HTTPValidationError | ProposalOut]:
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
    body: ProposalOptional,
) -> Response[HTTPValidationError | ProposalOut]:
    """Update Proposal

     Update existing proposal

    Args:
        proposal_reference (str):
        body (ProposalOptional):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and
            Client.raise_on_unexpected_status is True.
        httpx2.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[HTTPValidationError | ProposalOut]
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
    body: ProposalOptional,
) -> HTTPValidationError | ProposalOut | None:
    """Update Proposal

     Update existing proposal

    Args:
        proposal_reference (str):
        body (ProposalOptional):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and
            Client.raise_on_unexpected_status is True.
        httpx2.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        HTTPValidationError | ProposalOut
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
    body: ProposalOptional,
) -> Response[HTTPValidationError | ProposalOut]:
    """Update Proposal

     Update existing proposal

    Args:
        proposal_reference (str):
        body (ProposalOptional):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and
            Client.raise_on_unexpected_status is True.
        httpx2.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[HTTPValidationError | ProposalOut]
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
    body: ProposalOptional,
) -> HTTPValidationError | ProposalOut | None:
    """Update Proposal

     Update existing proposal

    Args:
        proposal_reference (str):
        body (ProposalOptional):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and
            Client.raise_on_unexpected_status is True.
        httpx2.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        HTTPValidationError | ProposalOut
    """

    return (
        await asyncio_detailed(
            proposal_reference=proposal_reference,
            client=client,
            body=body,
        )
    ).parsed

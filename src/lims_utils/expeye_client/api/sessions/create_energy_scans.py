from http import HTTPStatus
from typing import Any
from urllib.parse import quote

import httpx2

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.energy_scan_in import EnergyScanIn
from ...models.energy_scan_out import EnergyScanOut
from ...models.http_validation_error import HTTPValidationError
from ...types import Response


def _get_kwargs(
    proposal_reference: str,
    visit_number: int,
    *,
    body: EnergyScanIn,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/proposals/{proposal_reference}/sessions/{visit_number}/energy-scans".format(
            proposal_reference=quote(str(proposal_reference), safe=""),
            visit_number=quote(str(visit_number), safe=""),
        ),
    }

    _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx2.Response
) -> EnergyScanOut | HTTPValidationError | None:
    if response.status_code == 201:
        response_201 = EnergyScanOut.from_dict(response.json())

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
) -> Response[EnergyScanOut | HTTPValidationError]:
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
    body: EnergyScanIn,
) -> Response[EnergyScanOut | HTTPValidationError]:
    """Create Energy Scans

     Create new energy scan

    Args:
        proposal_reference (str):
        visit_number (int):
        body (EnergyScanIn):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and
        Client.raise_on_unexpected_status is True.
        httpx2.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[EnergyScanOut | HTTPValidationError]
    """

    kwargs = _get_kwargs(
        proposal_reference=proposal_reference,
        visit_number=visit_number,
        body=body,
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
    body: EnergyScanIn,
) -> EnergyScanOut | HTTPValidationError | None:
    """Create Energy Scans

     Create new energy scan

    Args:
        proposal_reference (str):
        visit_number (int):
        body (EnergyScanIn):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and
        Client.raise_on_unexpected_status is True.
        httpx2.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        EnergyScanOut | HTTPValidationError
    """

    return sync_detailed(
        proposal_reference=proposal_reference,
        visit_number=visit_number,
        client=client,
        body=body,
    ).parsed


async def asyncio_detailed(
    proposal_reference: str,
    visit_number: int,
    *,
    client: AuthenticatedClient,
    body: EnergyScanIn,
) -> Response[EnergyScanOut | HTTPValidationError]:
    """Create Energy Scans

     Create new energy scan

    Args:
        proposal_reference (str):
        visit_number (int):
        body (EnergyScanIn):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and
        Client.raise_on_unexpected_status is True.
        httpx2.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[EnergyScanOut | HTTPValidationError]
    """

    kwargs = _get_kwargs(
        proposal_reference=proposal_reference,
        visit_number=visit_number,
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    proposal_reference: str,
    visit_number: int,
    *,
    client: AuthenticatedClient,
    body: EnergyScanIn,
) -> EnergyScanOut | HTTPValidationError | None:
    """Create Energy Scans

     Create new energy scan

    Args:
        proposal_reference (str):
        visit_number (int):
        body (EnergyScanIn):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and
        Client.raise_on_unexpected_status is True.
        httpx2.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        EnergyScanOut | HTTPValidationError
    """

    return (
        await asyncio_detailed(
            proposal_reference=proposal_reference,
            visit_number=visit_number,
            client=client,
            body=body,
        )
    ).parsed

from http import HTTPStatus
from typing import Any
from urllib.parse import quote

import httpx2

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.http_validation_error import HTTPValidationError
from ...models.registered_dewar_out import RegisteredDewarOut
from ...types import Response


def _get_kwargs(
    proposal_reference: str,
    facility_code: str,
) -> dict[str, Any]:

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/proposals/{proposal_reference}/dewar-registry/{facility_code}".format(
            proposal_reference=quote(str(proposal_reference), safe=""),
            facility_code=quote(str(facility_code), safe=""),
        ),
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx2.Response
) -> HTTPValidationError | RegisteredDewarOut | None:
    if response.status_code == 200:
        response_200 = RegisteredDewarOut.from_dict(response.json())

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
) -> Response[HTTPValidationError | RegisteredDewarOut]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    proposal_reference: str,
    facility_code: str,
    *,
    client: AuthenticatedClient,
) -> Response[HTTPValidationError | RegisteredDewarOut]:
    """Get Dewar Registry Entry

     Get dewar registry entry information

    Args:
        proposal_reference (str):
        facility_code (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and
            Client.raise_on_unexpected_status is True.
        httpx2.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[HTTPValidationError | RegisteredDewarOut]
    """

    kwargs = _get_kwargs(
        proposal_reference=proposal_reference,
        facility_code=facility_code,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    proposal_reference: str,
    facility_code: str,
    *,
    client: AuthenticatedClient,
) -> HTTPValidationError | RegisteredDewarOut | None:
    """Get Dewar Registry Entry

     Get dewar registry entry information

    Args:
        proposal_reference (str):
        facility_code (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and
            Client.raise_on_unexpected_status is True.
        httpx2.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        HTTPValidationError | RegisteredDewarOut
    """

    return sync_detailed(
        proposal_reference=proposal_reference,
        facility_code=facility_code,
        client=client,
    ).parsed


async def asyncio_detailed(
    proposal_reference: str,
    facility_code: str,
    *,
    client: AuthenticatedClient,
) -> Response[HTTPValidationError | RegisteredDewarOut]:
    """Get Dewar Registry Entry

     Get dewar registry entry information

    Args:
        proposal_reference (str):
        facility_code (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and
            Client.raise_on_unexpected_status is True.
        httpx2.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[HTTPValidationError | RegisteredDewarOut]
    """

    kwargs = _get_kwargs(
        proposal_reference=proposal_reference,
        facility_code=facility_code,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    proposal_reference: str,
    facility_code: str,
    *,
    client: AuthenticatedClient,
) -> HTTPValidationError | RegisteredDewarOut | None:
    """Get Dewar Registry Entry

     Get dewar registry entry information

    Args:
        proposal_reference (str):
        facility_code (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and
            Client.raise_on_unexpected_status is True.
        httpx2.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        HTTPValidationError | RegisteredDewarOut
    """

    return (
        await asyncio_detailed(
            proposal_reference=proposal_reference,
            facility_code=facility_code,
            client=client,
        )
    ).parsed

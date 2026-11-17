from http import HTTPStatus
from typing import Any
from urllib.parse import quote

import httpx2

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.energy_scan_out import EnergyScanOut
from ...models.http_validation_error import HTTPValidationError
from ...types import Response


def _get_kwargs(
    energy_scan_id: int,
) -> dict[str, Any]:

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/energy-scans/{energy_scan_id}".format(
            energy_scan_id=quote(str(energy_scan_id), safe=""),
        ),
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx2.Response
) -> EnergyScanOut | HTTPValidationError | None:
    if response.status_code == 200:
        response_200 = EnergyScanOut.from_dict(response.json())

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
) -> Response[EnergyScanOut | HTTPValidationError]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    energy_scan_id: int,
    *,
    client: AuthenticatedClient,
) -> Response[EnergyScanOut | HTTPValidationError]:
    """Get Energy Scan

     Get energy scan

    Args:
        energy_scan_id (int):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx2.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[EnergyScanOut | HTTPValidationError]
    """

    kwargs = _get_kwargs(
        energy_scan_id=energy_scan_id,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    energy_scan_id: int,
    *,
    client: AuthenticatedClient,
) -> EnergyScanOut | HTTPValidationError | None:
    """Get Energy Scan

     Get energy scan

    Args:
        energy_scan_id (int):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx2.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        EnergyScanOut | HTTPValidationError
    """

    return sync_detailed(
        energy_scan_id=energy_scan_id,
        client=client,
    ).parsed


async def asyncio_detailed(
    energy_scan_id: int,
    *,
    client: AuthenticatedClient,
) -> Response[EnergyScanOut | HTTPValidationError]:
    """Get Energy Scan

     Get energy scan

    Args:
        energy_scan_id (int):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx2.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[EnergyScanOut | HTTPValidationError]
    """

    kwargs = _get_kwargs(
        energy_scan_id=energy_scan_id,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    energy_scan_id: int,
    *,
    client: AuthenticatedClient,
) -> EnergyScanOut | HTTPValidationError | None:
    """Get Energy Scan

     Get energy scan

    Args:
        energy_scan_id (int):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx2.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        EnergyScanOut | HTTPValidationError
    """

    return (
        await asyncio_detailed(
            energy_scan_id=energy_scan_id,
            client=client,
        )
    ).parsed

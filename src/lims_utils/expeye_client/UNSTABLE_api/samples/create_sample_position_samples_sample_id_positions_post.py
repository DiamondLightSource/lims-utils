from http import HTTPStatus
from typing import Any
from urllib.parse import quote

import httpx2

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.http_validation_error import HTTPValidationError
from ...models.sample_position_in import SamplePositionIn
from ...models.sample_position_out import SamplePositionOut
from ...types import Response


def _get_kwargs(
    sample_id: int,
    *,
    body: SamplePositionIn,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/samples/{sample_id}/positions".format(
            sample_id=quote(str(sample_id), safe=""),
        ),
    }

    _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx2.Response
) -> HTTPValidationError | SamplePositionOut | None:
    if response.status_code == 201:
        response_201 = SamplePositionOut.from_dict(response.json())

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
) -> Response[HTTPValidationError | SamplePositionOut]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    sample_id: int,
    *,
    client: AuthenticatedClient,
    body: SamplePositionIn,
) -> Response[HTTPValidationError | SamplePositionOut]:
    """Create Sample Position

     Create new sample position

    Args:
        sample_id (int):
        body (SamplePositionIn):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx2.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[HTTPValidationError | SamplePositionOut]
    """

    kwargs = _get_kwargs(
        sample_id=sample_id,
        body=body,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    sample_id: int,
    *,
    client: AuthenticatedClient,
    body: SamplePositionIn,
) -> HTTPValidationError | SamplePositionOut | None:
    """Create Sample Position

     Create new sample position

    Args:
        sample_id (int):
        body (SamplePositionIn):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx2.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        HTTPValidationError | SamplePositionOut
    """

    return sync_detailed(
        sample_id=sample_id,
        client=client,
        body=body,
    ).parsed


async def asyncio_detailed(
    sample_id: int,
    *,
    client: AuthenticatedClient,
    body: SamplePositionIn,
) -> Response[HTTPValidationError | SamplePositionOut]:
    """Create Sample Position

     Create new sample position

    Args:
        sample_id (int):
        body (SamplePositionIn):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx2.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[HTTPValidationError | SamplePositionOut]
    """

    kwargs = _get_kwargs(
        sample_id=sample_id,
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    sample_id: int,
    *,
    client: AuthenticatedClient,
    body: SamplePositionIn,
) -> HTTPValidationError | SamplePositionOut | None:
    """Create Sample Position

     Create new sample position

    Args:
        sample_id (int):
        body (SamplePositionIn):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx2.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        HTTPValidationError | SamplePositionOut
    """

    return (
        await asyncio_detailed(
            sample_id=sample_id,
            client=client,
            body=body,
        )
    ).parsed

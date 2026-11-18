from http import HTTPStatus
from typing import Any
from urllib.parse import quote

import httpx2

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.dewar_transport_history_in import DewarTransportHistoryIn
from ...models.dewar_transport_history_out import DewarTransportHistoryOut
from ...models.http_validation_error import HTTPValidationError
from ...types import Response


def _get_kwargs(
    dewar_id: int,
    *,
    body: DewarTransportHistoryIn,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/dewars/{dewar_id}/history".format(
            dewar_id=quote(str(dewar_id), safe=""),
        ),
    }

    _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx2.Response
) -> DewarTransportHistoryOut | HTTPValidationError | None:
    if response.status_code == 201:
        response_201 = DewarTransportHistoryOut.from_dict(response.json())

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
) -> Response[DewarTransportHistoryOut | HTTPValidationError]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    dewar_id: int,
    *,
    client: AuthenticatedClient,
    body: DewarTransportHistoryIn,
) -> Response[DewarTransportHistoryOut | HTTPValidationError]:
    """Create Dewar History Entry

     Create dewar history entry

    Args:
        dewar_id (int):
        body (DewarTransportHistoryIn):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and
        Client.raise_on_unexpected_status is True.
        httpx2.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[DewarTransportHistoryOut | HTTPValidationError]
    """

    kwargs = _get_kwargs(
        dewar_id=dewar_id,
        body=body,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    dewar_id: int,
    *,
    client: AuthenticatedClient,
    body: DewarTransportHistoryIn,
) -> DewarTransportHistoryOut | HTTPValidationError | None:
    """Create Dewar History Entry

     Create dewar history entry

    Args:
        dewar_id (int):
        body (DewarTransportHistoryIn):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and
        Client.raise_on_unexpected_status is True.
        httpx2.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        DewarTransportHistoryOut | HTTPValidationError
    """

    return sync_detailed(
        dewar_id=dewar_id,
        client=client,
        body=body,
    ).parsed


async def asyncio_detailed(
    dewar_id: int,
    *,
    client: AuthenticatedClient,
    body: DewarTransportHistoryIn,
) -> Response[DewarTransportHistoryOut | HTTPValidationError]:
    """Create Dewar History Entry

     Create dewar history entry

    Args:
        dewar_id (int):
        body (DewarTransportHistoryIn):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and
        Client.raise_on_unexpected_status is True.
        httpx2.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[DewarTransportHistoryOut | HTTPValidationError]
    """

    kwargs = _get_kwargs(
        dewar_id=dewar_id,
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    dewar_id: int,
    *,
    client: AuthenticatedClient,
    body: DewarTransportHistoryIn,
) -> DewarTransportHistoryOut | HTTPValidationError | None:
    """Create Dewar History Entry

     Create dewar history entry

    Args:
        dewar_id (int):
        body (DewarTransportHistoryIn):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and
        Client.raise_on_unexpected_status is True.
        httpx2.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        DewarTransportHistoryOut | HTTPValidationError
    """

    return (
        await asyncio_detailed(
            dewar_id=dewar_id,
            client=client,
            body=body,
        )
    ).parsed

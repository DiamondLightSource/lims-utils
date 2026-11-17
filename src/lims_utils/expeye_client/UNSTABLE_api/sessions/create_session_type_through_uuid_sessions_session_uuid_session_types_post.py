from http import HTTPStatus
from typing import Any
from urllib.parse import quote
from uuid import UUID

import httpx2

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.http_validation_error import HTTPValidationError
from ...models.session_type_in import SessionTypeIn
from ...models.session_type_out import SessionTypeOut
from ...types import Response


def _get_kwargs(
    session_uuid: UUID,
    *,
    body: SessionTypeIn,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/sessions/{session_uuid}/session-types".format(
            session_uuid=quote(str(session_uuid), safe=""),
        ),
    }

    _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx2.Response
) -> HTTPValidationError | SessionTypeOut | None:
    if response.status_code == 201:
        response_201 = SessionTypeOut.from_dict(response.json())

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
) -> Response[HTTPValidationError | SessionTypeOut]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    session_uuid: UUID,
    *,
    client: AuthenticatedClient,
    body: SessionTypeIn,
) -> Response[HTTPValidationError | SessionTypeOut]:
    """Create Session Type Through Uuid

     Add new session type to session (using UUID)

    Args:
        session_uuid (UUID):
        body (SessionTypeIn):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx2.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[HTTPValidationError | SessionTypeOut]
    """

    kwargs = _get_kwargs(
        session_uuid=session_uuid,
        body=body,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    session_uuid: UUID,
    *,
    client: AuthenticatedClient,
    body: SessionTypeIn,
) -> HTTPValidationError | SessionTypeOut | None:
    """Create Session Type Through Uuid

     Add new session type to session (using UUID)

    Args:
        session_uuid (UUID):
        body (SessionTypeIn):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx2.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        HTTPValidationError | SessionTypeOut
    """

    return sync_detailed(
        session_uuid=session_uuid,
        client=client,
        body=body,
    ).parsed


async def asyncio_detailed(
    session_uuid: UUID,
    *,
    client: AuthenticatedClient,
    body: SessionTypeIn,
) -> Response[HTTPValidationError | SessionTypeOut]:
    """Create Session Type Through Uuid

     Add new session type to session (using UUID)

    Args:
        session_uuid (UUID):
        body (SessionTypeIn):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx2.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[HTTPValidationError | SessionTypeOut]
    """

    kwargs = _get_kwargs(
        session_uuid=session_uuid,
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    session_uuid: UUID,
    *,
    client: AuthenticatedClient,
    body: SessionTypeIn,
) -> HTTPValidationError | SessionTypeOut | None:
    """Create Session Type Through Uuid

     Add new session type to session (using UUID)

    Args:
        session_uuid (UUID):
        body (SessionTypeIn):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx2.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        HTTPValidationError | SessionTypeOut
    """

    return (
        await asyncio_detailed(
            session_uuid=session_uuid,
            client=client,
            body=body,
        )
    ).parsed

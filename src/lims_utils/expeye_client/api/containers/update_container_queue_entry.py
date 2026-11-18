from http import HTTPStatus
from typing import Any
from urllib.parse import quote

import httpx2

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.container_queue_in import ContainerQueueIn
from ...models.container_queue_out import ContainerQueueOut
from ...models.http_validation_error import HTTPValidationError
from ...types import Response


def _get_kwargs(
    container_id: int,
    container_queue_id: int,
    *,
    body: ContainerQueueIn,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "patch",
        "url": "/containers/{container_id}/container-queue/{container_queue_id}".format(
            container_id=quote(str(container_id), safe=""),
            container_queue_id=quote(str(container_queue_id), safe=""),
        ),
    }

    _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx2.Response
) -> ContainerQueueOut | HTTPValidationError | None:
    if response.status_code == 200:
        response_200 = ContainerQueueOut.from_dict(response.json())

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
) -> Response[ContainerQueueOut | HTTPValidationError]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    container_id: int,
    container_queue_id: int,
    *,
    client: AuthenticatedClient,
    body: ContainerQueueIn,
) -> Response[ContainerQueueOut | HTTPValidationError]:
    """Update Container Queue Entry

     Update container queue entry

    Args:
        container_id (int):
        container_queue_id (int):
        body (ContainerQueueIn):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and
        Client.raise_on_unexpected_status is True.
        httpx2.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ContainerQueueOut | HTTPValidationError]
    """

    kwargs = _get_kwargs(
        container_id=container_id,
        container_queue_id=container_queue_id,
        body=body,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    container_id: int,
    container_queue_id: int,
    *,
    client: AuthenticatedClient,
    body: ContainerQueueIn,
) -> ContainerQueueOut | HTTPValidationError | None:
    """Update Container Queue Entry

     Update container queue entry

    Args:
        container_id (int):
        container_queue_id (int):
        body (ContainerQueueIn):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and
        Client.raise_on_unexpected_status is True.
        httpx2.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ContainerQueueOut | HTTPValidationError
    """

    return sync_detailed(
        container_id=container_id,
        container_queue_id=container_queue_id,
        client=client,
        body=body,
    ).parsed


async def asyncio_detailed(
    container_id: int,
    container_queue_id: int,
    *,
    client: AuthenticatedClient,
    body: ContainerQueueIn,
) -> Response[ContainerQueueOut | HTTPValidationError]:
    """Update Container Queue Entry

     Update container queue entry

    Args:
        container_id (int):
        container_queue_id (int):
        body (ContainerQueueIn):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and
        Client.raise_on_unexpected_status is True.
        httpx2.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ContainerQueueOut | HTTPValidationError]
    """

    kwargs = _get_kwargs(
        container_id=container_id,
        container_queue_id=container_queue_id,
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    container_id: int,
    container_queue_id: int,
    *,
    client: AuthenticatedClient,
    body: ContainerQueueIn,
) -> ContainerQueueOut | HTTPValidationError | None:
    """Update Container Queue Entry

     Update container queue entry

    Args:
        container_id (int):
        container_queue_id (int):
        body (ContainerQueueIn):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and
        Client.raise_on_unexpected_status is True.
        httpx2.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ContainerQueueOut | HTTPValidationError
    """

    return (
        await asyncio_detailed(
            container_id=container_id,
            container_queue_id=container_queue_id,
            client=client,
            body=body,
        )
    ).parsed

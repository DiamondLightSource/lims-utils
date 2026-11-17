from http import HTTPStatus
from typing import Any
from urllib.parse import quote

import httpx2

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.container_load import ContainerLoad
from ...models.container_out import ContainerOut
from ...models.http_validation_error import HTTPValidationError
from ...types import Response


def _get_kwargs(
    container_id: int,
    *,
    body: ContainerLoad,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/containers/{container_id}/assign".format(
            container_id=quote(str(container_id), safe=""),
        ),
    }

    _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx2.Response
) -> ContainerOut | HTTPValidationError | None:
    if response.status_code == 200:
        response_200 = ContainerOut.from_dict(response.json())

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
) -> Response[ContainerOut | HTTPValidationError]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    container_id: int,
    *,
    client: AuthenticatedClient,
    body: ContainerLoad,
) -> Response[ContainerOut | HTTPValidationError]:
    """Load Or Unload Puck

     Toggle load/unload state of puck and append to history

    Args:
        container_id (int):
        body (ContainerLoad):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and
            Client.raise_on_unexpected_status is True.
        httpx2.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ContainerOut | HTTPValidationError]
    """

    kwargs = _get_kwargs(
        container_id=container_id,
        body=body,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    container_id: int,
    *,
    client: AuthenticatedClient,
    body: ContainerLoad,
) -> ContainerOut | HTTPValidationError | None:
    """Load Or Unload Puck

     Toggle load/unload state of puck and append to history

    Args:
        container_id (int):
        body (ContainerLoad):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and
            Client.raise_on_unexpected_status is True.
        httpx2.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ContainerOut | HTTPValidationError
    """

    return sync_detailed(
        container_id=container_id,
        client=client,
        body=body,
    ).parsed


async def asyncio_detailed(
    container_id: int,
    *,
    client: AuthenticatedClient,
    body: ContainerLoad,
) -> Response[ContainerOut | HTTPValidationError]:
    """Load Or Unload Puck

     Toggle load/unload state of puck and append to history

    Args:
        container_id (int):
        body (ContainerLoad):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and
            Client.raise_on_unexpected_status is True.
        httpx2.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ContainerOut | HTTPValidationError]
    """

    kwargs = _get_kwargs(
        container_id=container_id,
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    container_id: int,
    *,
    client: AuthenticatedClient,
    body: ContainerLoad,
) -> ContainerOut | HTTPValidationError | None:
    """Load Or Unload Puck

     Toggle load/unload state of puck and append to history

    Args:
        container_id (int):
        body (ContainerLoad):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and
            Client.raise_on_unexpected_status is True.
        httpx2.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ContainerOut | HTTPValidationError
    """

    return (
        await asyncio_detailed(
            container_id=container_id,
            client=client,
            body=body,
        )
    ).parsed

from http import HTTPStatus
from typing import Any
from urllib.parse import quote

import httpx2

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.container_history_in import ContainerHistoryIn
from ...models.container_history_out import ContainerHistoryOut
from ...models.http_validation_error import HTTPValidationError
from ...types import UNSET, Response, Unset


def _get_kwargs(
    container_id: int,
    *,
    body: ContainerHistoryIn,
    update_container: bool | Unset = False,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    params: dict[str, Any] = {}

    params["updateContainer"] = update_container

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/containers/{container_id}/history".format(
            container_id=quote(str(container_id), safe=""),
        ),
        "params": params,
    }

    _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx2.Response
) -> ContainerHistoryOut | HTTPValidationError | None:
    if response.status_code == 201:
        response_201 = ContainerHistoryOut.from_dict(response.json())

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
) -> Response[ContainerHistoryOut | HTTPValidationError]:
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
    body: ContainerHistoryIn,
    update_container: bool | Unset = False,
) -> Response[ContainerHistoryOut | HTTPValidationError]:
    """Create Container History

     Create new container history entry

    Args:
        container_id (int):
        update_container (bool | Unset):  Default: False.
        body (ContainerHistoryIn):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and
        Client.raise_on_unexpected_status is True.
        httpx2.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ContainerHistoryOut | HTTPValidationError]
    """

    kwargs = _get_kwargs(
        container_id=container_id,
        body=body,
        update_container=update_container,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    container_id: int,
    *,
    client: AuthenticatedClient,
    body: ContainerHistoryIn,
    update_container: bool | Unset = False,
) -> ContainerHistoryOut | HTTPValidationError | None:
    """Create Container History

     Create new container history entry

    Args:
        container_id (int):
        update_container (bool | Unset):  Default: False.
        body (ContainerHistoryIn):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and
        Client.raise_on_unexpected_status is True.
        httpx2.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ContainerHistoryOut | HTTPValidationError
    """

    return sync_detailed(
        container_id=container_id,
        client=client,
        body=body,
        update_container=update_container,
    ).parsed


async def asyncio_detailed(
    container_id: int,
    *,
    client: AuthenticatedClient,
    body: ContainerHistoryIn,
    update_container: bool | Unset = False,
) -> Response[ContainerHistoryOut | HTTPValidationError]:
    """Create Container History

     Create new container history entry

    Args:
        container_id (int):
        update_container (bool | Unset):  Default: False.
        body (ContainerHistoryIn):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and
        Client.raise_on_unexpected_status is True.
        httpx2.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ContainerHistoryOut | HTTPValidationError]
    """

    kwargs = _get_kwargs(
        container_id=container_id,
        body=body,
        update_container=update_container,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    container_id: int,
    *,
    client: AuthenticatedClient,
    body: ContainerHistoryIn,
    update_container: bool | Unset = False,
) -> ContainerHistoryOut | HTTPValidationError | None:
    """Create Container History

     Create new container history entry

    Args:
        container_id (int):
        update_container (bool | Unset):  Default: False.
        body (ContainerHistoryIn):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and
        Client.raise_on_unexpected_status is True.
        httpx2.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ContainerHistoryOut | HTTPValidationError
    """

    return (
        await asyncio_detailed(
            container_id=container_id,
            client=client,
            body=body,
            update_container=update_container,
        )
    ).parsed

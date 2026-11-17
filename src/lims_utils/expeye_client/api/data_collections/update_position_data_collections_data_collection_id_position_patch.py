from http import HTTPStatus
from typing import Any
from urllib.parse import quote

import httpx2

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.http_validation_error import HTTPValidationError
from ...models.position_optional import PositionOptional
from ...models.position_out import PositionOut
from ...types import Response


def _get_kwargs(
    data_collection_id: int,
    *,
    body: PositionOptional,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "patch",
        "url": "/data-collections/{data_collection_id}/position".format(
            data_collection_id=quote(str(data_collection_id), safe=""),
        ),
    }

    _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx2.Response
) -> HTTPValidationError | PositionOut | None:
    if response.status_code == 200:
        response_200 = PositionOut.from_dict(response.json())

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
) -> Response[HTTPValidationError | PositionOut]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    data_collection_id: int,
    *,
    client: AuthenticatedClient,
    body: PositionOptional,
) -> Response[HTTPValidationError | PositionOut]:
    """Update Position

     Update data collection position

    Args:
        data_collection_id (int):
        body (PositionOptional):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx2.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[HTTPValidationError | PositionOut]
    """

    kwargs = _get_kwargs(
        data_collection_id=data_collection_id,
        body=body,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    data_collection_id: int,
    *,
    client: AuthenticatedClient,
    body: PositionOptional,
) -> HTTPValidationError | PositionOut | None:
    """Update Position

     Update data collection position

    Args:
        data_collection_id (int):
        body (PositionOptional):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx2.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        HTTPValidationError | PositionOut
    """

    return sync_detailed(
        data_collection_id=data_collection_id,
        client=client,
        body=body,
    ).parsed


async def asyncio_detailed(
    data_collection_id: int,
    *,
    client: AuthenticatedClient,
    body: PositionOptional,
) -> Response[HTTPValidationError | PositionOut]:
    """Update Position

     Update data collection position

    Args:
        data_collection_id (int):
        body (PositionOptional):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx2.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[HTTPValidationError | PositionOut]
    """

    kwargs = _get_kwargs(
        data_collection_id=data_collection_id,
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    data_collection_id: int,
    *,
    client: AuthenticatedClient,
    body: PositionOptional,
) -> HTTPValidationError | PositionOut | None:
    """Update Position

     Update data collection position

    Args:
        data_collection_id (int):
        body (PositionOptional):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx2.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        HTTPValidationError | PositionOut
    """

    return (
        await asyncio_detailed(
            data_collection_id=data_collection_id,
            client=client,
            body=body,
        )
    ).parsed

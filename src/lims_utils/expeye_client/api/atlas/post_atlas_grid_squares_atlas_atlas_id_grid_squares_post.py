from http import HTTPStatus
from typing import Any
from urllib.parse import quote

import httpx2

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.grid_square_in import GridSquareIn
from ...models.grid_square_out import GridSquareOut
from ...models.http_validation_error import HTTPValidationError
from ...types import Response


def _get_kwargs(
    atlas_id: int,
    *,
    body: list[GridSquareIn],
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/atlas/{atlas_id}/grid-squares".format(
            atlas_id=quote(str(atlas_id), safe=""),
        ),
    }

    _kwargs["json"] = []
    for body_item_data in body:
        body_item = body_item_data.to_dict()
        _kwargs["json"].append(body_item)

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx2.Response
) -> HTTPValidationError | list[GridSquareOut] | None:
    if response.status_code == 201:
        response_201 = []
        _response_201 = response.json()
        for response_201_item_data in _response_201:
            response_201_item = GridSquareOut.from_dict(response_201_item_data)

            response_201.append(response_201_item)

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
) -> Response[HTTPValidationError | list[GridSquareOut]]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    atlas_id: int,
    *,
    client: AuthenticatedClient,
    body: list[GridSquareIn],
) -> Response[HTTPValidationError | list[GridSquareOut]]:
    """Post Atlas Grid Squares

     Create grid squares for an atlas

    Args:
        atlas_id (int):
        body (list[GridSquareIn]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx2.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[HTTPValidationError | list[GridSquareOut]]
    """

    kwargs = _get_kwargs(
        atlas_id=atlas_id,
        body=body,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    atlas_id: int,
    *,
    client: AuthenticatedClient,
    body: list[GridSquareIn],
) -> HTTPValidationError | list[GridSquareOut] | None:
    """Post Atlas Grid Squares

     Create grid squares for an atlas

    Args:
        atlas_id (int):
        body (list[GridSquareIn]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx2.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        HTTPValidationError | list[GridSquareOut]
    """

    return sync_detailed(
        atlas_id=atlas_id,
        client=client,
        body=body,
    ).parsed


async def asyncio_detailed(
    atlas_id: int,
    *,
    client: AuthenticatedClient,
    body: list[GridSquareIn],
) -> Response[HTTPValidationError | list[GridSquareOut]]:
    """Post Atlas Grid Squares

     Create grid squares for an atlas

    Args:
        atlas_id (int):
        body (list[GridSquareIn]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx2.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[HTTPValidationError | list[GridSquareOut]]
    """

    kwargs = _get_kwargs(
        atlas_id=atlas_id,
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    atlas_id: int,
    *,
    client: AuthenticatedClient,
    body: list[GridSquareIn],
) -> HTTPValidationError | list[GridSquareOut] | None:
    """Post Atlas Grid Squares

     Create grid squares for an atlas

    Args:
        atlas_id (int):
        body (list[GridSquareIn]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx2.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        HTTPValidationError | list[GridSquareOut]
    """

    return (
        await asyncio_detailed(
            atlas_id=atlas_id,
            client=client,
            body=body,
        )
    ).parsed

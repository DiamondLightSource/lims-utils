from http import HTTPStatus
from typing import Any
from urllib.parse import quote

import httpx2

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.foil_hole_in import FoilHoleIn
from ...models.foil_hole_out import FoilHoleOut
from ...models.http_validation_error import HTTPValidationError
from ...types import Response


def _get_kwargs(
    grid_square_id: int,
    *,
    body: list[FoilHoleIn],
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/grid-squares/{grid_square_id}/foil-holes".format(
            grid_square_id=quote(str(grid_square_id), safe=""),
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
) -> HTTPValidationError | list[FoilHoleOut] | None:
    if response.status_code == 201:
        response_201 = []
        _response_201 = response.json()
        for response_201_item_data in _response_201:
            response_201_item = FoilHoleOut.from_dict(response_201_item_data)

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
) -> Response[HTTPValidationError | list[FoilHoleOut]]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    grid_square_id: int,
    *,
    client: AuthenticatedClient,
    body: list[FoilHoleIn],
) -> Response[HTTPValidationError | list[FoilHoleOut]]:
    """Post Grid Square Foil Holes

     Create foil holes for a grid square

    Args:
        grid_square_id (int):
        body (list[FoilHoleIn]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx2.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[HTTPValidationError | list[FoilHoleOut]]
    """

    kwargs = _get_kwargs(
        grid_square_id=grid_square_id,
        body=body,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    grid_square_id: int,
    *,
    client: AuthenticatedClient,
    body: list[FoilHoleIn],
) -> HTTPValidationError | list[FoilHoleOut] | None:
    """Post Grid Square Foil Holes

     Create foil holes for a grid square

    Args:
        grid_square_id (int):
        body (list[FoilHoleIn]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx2.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        HTTPValidationError | list[FoilHoleOut]
    """

    return sync_detailed(
        grid_square_id=grid_square_id,
        client=client,
        body=body,
    ).parsed


async def asyncio_detailed(
    grid_square_id: int,
    *,
    client: AuthenticatedClient,
    body: list[FoilHoleIn],
) -> Response[HTTPValidationError | list[FoilHoleOut]]:
    """Post Grid Square Foil Holes

     Create foil holes for a grid square

    Args:
        grid_square_id (int):
        body (list[FoilHoleIn]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx2.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[HTTPValidationError | list[FoilHoleOut]]
    """

    kwargs = _get_kwargs(
        grid_square_id=grid_square_id,
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    grid_square_id: int,
    *,
    client: AuthenticatedClient,
    body: list[FoilHoleIn],
) -> HTTPValidationError | list[FoilHoleOut] | None:
    """Post Grid Square Foil Holes

     Create foil holes for a grid square

    Args:
        grid_square_id (int):
        body (list[FoilHoleIn]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx2.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        HTTPValidationError | list[FoilHoleOut]
    """

    return (
        await asyncio_detailed(
            grid_square_id=grid_square_id,
            client=client,
            body=body,
        )
    ).parsed

from http import HTTPStatus
from typing import Any
from urllib.parse import quote

import httpx2

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.foil_hole_optional_with_id import FoilHoleOptionalWithId
from ...models.http_validation_error import HTTPValidationError
from ...models.paged_foil_hole_out import PagedFoilHoleOut
from ...types import Response


def _get_kwargs(
    grid_square_id: int,
    *,
    body: list[FoilHoleOptionalWithId],
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "patch",
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
) -> HTTPValidationError | PagedFoilHoleOut | None:
    if response.status_code == 200:
        response_200 = PagedFoilHoleOut.from_dict(response.json())

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
) -> Response[HTTPValidationError | PagedFoilHoleOut]:
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
    body: list[FoilHoleOptionalWithId],
) -> Response[HTTPValidationError | PagedFoilHoleOut]:
    """Update Foil Holes In Grid Square

     Update multiple foil holes in grid square

    Args:
        grid_square_id (int):
        body (list[FoilHoleOptionalWithId]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and
            Client.raise_on_unexpected_status is True.
        httpx2.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[HTTPValidationError | PagedFoilHoleOut]
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
    body: list[FoilHoleOptionalWithId],
) -> HTTPValidationError | PagedFoilHoleOut | None:
    """Update Foil Holes In Grid Square

     Update multiple foil holes in grid square

    Args:
        grid_square_id (int):
        body (list[FoilHoleOptionalWithId]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and
            Client.raise_on_unexpected_status is True.
        httpx2.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        HTTPValidationError | PagedFoilHoleOut
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
    body: list[FoilHoleOptionalWithId],
) -> Response[HTTPValidationError | PagedFoilHoleOut]:
    """Update Foil Holes In Grid Square

     Update multiple foil holes in grid square

    Args:
        grid_square_id (int):
        body (list[FoilHoleOptionalWithId]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and
            Client.raise_on_unexpected_status is True.
        httpx2.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[HTTPValidationError | PagedFoilHoleOut]
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
    body: list[FoilHoleOptionalWithId],
) -> HTTPValidationError | PagedFoilHoleOut | None:
    """Update Foil Holes In Grid Square

     Update multiple foil holes in grid square

    Args:
        grid_square_id (int):
        body (list[FoilHoleOptionalWithId]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and
            Client.raise_on_unexpected_status is True.
        httpx2.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        HTTPValidationError | PagedFoilHoleOut
    """

    return (
        await asyncio_detailed(
            grid_square_id=grid_square_id,
            client=client,
            body=body,
        )
    ).parsed

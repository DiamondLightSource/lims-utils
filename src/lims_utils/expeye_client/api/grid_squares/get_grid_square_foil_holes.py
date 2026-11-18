from http import HTTPStatus
from typing import Any
from urllib.parse import quote

import httpx2

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.http_validation_error import HTTPValidationError
from ...models.paged_foil_hole_out import PagedFoilHoleOut
from ...types import UNSET, Response, Unset


def _get_kwargs(
    grid_square_id: int,
    *,
    page: int | Unset = 0,
    limit: int | Unset = 25,
) -> dict[str, Any]:

    params: dict[str, Any] = {}

    params["page"] = page

    params["limit"] = limit

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/grid-squares/{grid_square_id}/foil-holes".format(
            grid_square_id=quote(str(grid_square_id), safe=""),
        ),
        "params": params,
    }

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
    page: int | Unset = 0,
    limit: int | Unset = 25,
) -> Response[HTTPValidationError | PagedFoilHoleOut]:
    """Get Grid Square Foil Holes

     Get foil holes for a grid square

    Args:
        grid_square_id (int):
        page (int | Unset): Page number/Results to skip. Negative numbers count backwards from the
            last page Default: 0.
        limit (int | Unset): Number of results to show Default: 25.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and
        Client.raise_on_unexpected_status is True.
        httpx2.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[HTTPValidationError | PagedFoilHoleOut]
    """

    kwargs = _get_kwargs(
        grid_square_id=grid_square_id,
        page=page,
        limit=limit,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    grid_square_id: int,
    *,
    client: AuthenticatedClient,
    page: int | Unset = 0,
    limit: int | Unset = 25,
) -> HTTPValidationError | PagedFoilHoleOut | None:
    """Get Grid Square Foil Holes

     Get foil holes for a grid square

    Args:
        grid_square_id (int):
        page (int | Unset): Page number/Results to skip. Negative numbers count backwards from the
            last page Default: 0.
        limit (int | Unset): Number of results to show Default: 25.

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
        page=page,
        limit=limit,
    ).parsed


async def asyncio_detailed(
    grid_square_id: int,
    *,
    client: AuthenticatedClient,
    page: int | Unset = 0,
    limit: int | Unset = 25,
) -> Response[HTTPValidationError | PagedFoilHoleOut]:
    """Get Grid Square Foil Holes

     Get foil holes for a grid square

    Args:
        grid_square_id (int):
        page (int | Unset): Page number/Results to skip. Negative numbers count backwards from the
            last page Default: 0.
        limit (int | Unset): Number of results to show Default: 25.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and
        Client.raise_on_unexpected_status is True.
        httpx2.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[HTTPValidationError | PagedFoilHoleOut]
    """

    kwargs = _get_kwargs(
        grid_square_id=grid_square_id,
        page=page,
        limit=limit,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    grid_square_id: int,
    *,
    client: AuthenticatedClient,
    page: int | Unset = 0,
    limit: int | Unset = 25,
) -> HTTPValidationError | PagedFoilHoleOut | None:
    """Get Grid Square Foil Holes

     Get foil holes for a grid square

    Args:
        grid_square_id (int):
        page (int | Unset): Page number/Results to skip. Negative numbers count backwards from the
            last page Default: 0.
        limit (int | Unset): Number of results to show Default: 25.

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
            page=page,
            limit=limit,
        )
    ).parsed

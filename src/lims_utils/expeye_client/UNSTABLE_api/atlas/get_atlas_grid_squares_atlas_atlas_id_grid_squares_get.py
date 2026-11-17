from http import HTTPStatus
from typing import Any
from urllib.parse import quote

import httpx2

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.http_validation_error import HTTPValidationError
from ...models.paged_grid_square_out import PagedGridSquareOut
from ...types import UNSET, Response, Unset


def _get_kwargs(
    atlas_id: int,
    *,
    hide_squares: bool | Unset = False,
    hide_empty_search_maps: bool | Unset = False,
    page: int | Unset = 0,
    limit: int | Unset = 25,
) -> dict[str, Any]:

    params: dict[str, Any] = {}

    params["hideSquares"] = hide_squares

    params["hideEmptySearchMaps"] = hide_empty_search_maps

    params["page"] = page

    params["limit"] = limit

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/atlas/{atlas_id}/grid-squares".format(
            atlas_id=quote(str(atlas_id), safe=""),
        ),
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx2.Response
) -> HTTPValidationError | PagedGridSquareOut | None:
    if response.status_code == 200:
        response_200 = PagedGridSquareOut.from_dict(response.json())

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
) -> Response[HTTPValidationError | PagedGridSquareOut]:
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
    hide_squares: bool | Unset = False,
    hide_empty_search_maps: bool | Unset = False,
    page: int | Unset = 0,
    limit: int | Unset = 25,
) -> Response[HTTPValidationError | PagedGridSquareOut]:
    """Get Atlas Grid Squares

     Get grid squares for an atlas

    Args:
        atlas_id (int):
        hide_squares (bool | Unset):  Default: False.
        hide_empty_search_maps (bool | Unset):  Default: False.
        page (int | Unset): Page number/Results to skip. Negative numbers count backwards from the
            last page Default: 0.
        limit (int | Unset): Number of results to show Default: 25.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and
            Client.raise_on_unexpected_status is True.
        httpx2.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[HTTPValidationError | PagedGridSquareOut]
    """

    kwargs = _get_kwargs(
        atlas_id=atlas_id,
        hide_squares=hide_squares,
        hide_empty_search_maps=hide_empty_search_maps,
        page=page,
        limit=limit,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    atlas_id: int,
    *,
    client: AuthenticatedClient,
    hide_squares: bool | Unset = False,
    hide_empty_search_maps: bool | Unset = False,
    page: int | Unset = 0,
    limit: int | Unset = 25,
) -> HTTPValidationError | PagedGridSquareOut | None:
    """Get Atlas Grid Squares

     Get grid squares for an atlas

    Args:
        atlas_id (int):
        hide_squares (bool | Unset):  Default: False.
        hide_empty_search_maps (bool | Unset):  Default: False.
        page (int | Unset): Page number/Results to skip. Negative numbers count backwards from the
            last page Default: 0.
        limit (int | Unset): Number of results to show Default: 25.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and
            Client.raise_on_unexpected_status is True.
        httpx2.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        HTTPValidationError | PagedGridSquareOut
    """

    return sync_detailed(
        atlas_id=atlas_id,
        client=client,
        hide_squares=hide_squares,
        hide_empty_search_maps=hide_empty_search_maps,
        page=page,
        limit=limit,
    ).parsed


async def asyncio_detailed(
    atlas_id: int,
    *,
    client: AuthenticatedClient,
    hide_squares: bool | Unset = False,
    hide_empty_search_maps: bool | Unset = False,
    page: int | Unset = 0,
    limit: int | Unset = 25,
) -> Response[HTTPValidationError | PagedGridSquareOut]:
    """Get Atlas Grid Squares

     Get grid squares for an atlas

    Args:
        atlas_id (int):
        hide_squares (bool | Unset):  Default: False.
        hide_empty_search_maps (bool | Unset):  Default: False.
        page (int | Unset): Page number/Results to skip. Negative numbers count backwards from the
            last page Default: 0.
        limit (int | Unset): Number of results to show Default: 25.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and
            Client.raise_on_unexpected_status is True.
        httpx2.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[HTTPValidationError | PagedGridSquareOut]
    """

    kwargs = _get_kwargs(
        atlas_id=atlas_id,
        hide_squares=hide_squares,
        hide_empty_search_maps=hide_empty_search_maps,
        page=page,
        limit=limit,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    atlas_id: int,
    *,
    client: AuthenticatedClient,
    hide_squares: bool | Unset = False,
    hide_empty_search_maps: bool | Unset = False,
    page: int | Unset = 0,
    limit: int | Unset = 25,
) -> HTTPValidationError | PagedGridSquareOut | None:
    """Get Atlas Grid Squares

     Get grid squares for an atlas

    Args:
        atlas_id (int):
        hide_squares (bool | Unset):  Default: False.
        hide_empty_search_maps (bool | Unset):  Default: False.
        page (int | Unset): Page number/Results to skip. Negative numbers count backwards from the
            last page Default: 0.
        limit (int | Unset): Number of results to show Default: 25.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and
            Client.raise_on_unexpected_status is True.
        httpx2.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        HTTPValidationError | PagedGridSquareOut
    """

    return (
        await asyncio_detailed(
            atlas_id=atlas_id,
            client=client,
            hide_squares=hide_squares,
            hide_empty_search_maps=hide_empty_search_maps,
            page=page,
            limit=limit,
        )
    ).parsed

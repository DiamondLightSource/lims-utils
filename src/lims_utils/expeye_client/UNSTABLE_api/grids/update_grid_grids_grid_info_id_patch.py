from http import HTTPStatus
from typing import Any
from urllib.parse import quote

import httpx2

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.grid_info_optional import GridInfoOptional
from ...models.grid_info_out import GridInfoOut
from ...models.http_validation_error import HTTPValidationError
from ...types import Response


def _get_kwargs(
    grid_info_id: int,
    *,
    body: GridInfoOptional,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "patch",
        "url": "/grids/{grid_info_id}".format(
            grid_info_id=quote(str(grid_info_id), safe=""),
        ),
    }

    _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx2.Response
) -> GridInfoOut | HTTPValidationError | None:
    if response.status_code == 200:
        response_200 = GridInfoOut.from_dict(response.json())

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
) -> Response[GridInfoOut | HTTPValidationError]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    grid_info_id: int,
    *,
    client: AuthenticatedClient,
    body: GridInfoOptional,
) -> Response[GridInfoOut | HTTPValidationError]:
    """Update Grid

     Update grid

    Args:
        grid_info_id (int):
        body (GridInfoOptional):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and
            Client.raise_on_unexpected_status is True.
        httpx2.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[GridInfoOut | HTTPValidationError]
    """

    kwargs = _get_kwargs(
        grid_info_id=grid_info_id,
        body=body,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    grid_info_id: int,
    *,
    client: AuthenticatedClient,
    body: GridInfoOptional,
) -> GridInfoOut | HTTPValidationError | None:
    """Update Grid

     Update grid

    Args:
        grid_info_id (int):
        body (GridInfoOptional):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and
            Client.raise_on_unexpected_status is True.
        httpx2.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        GridInfoOut | HTTPValidationError
    """

    return sync_detailed(
        grid_info_id=grid_info_id,
        client=client,
        body=body,
    ).parsed


async def asyncio_detailed(
    grid_info_id: int,
    *,
    client: AuthenticatedClient,
    body: GridInfoOptional,
) -> Response[GridInfoOut | HTTPValidationError]:
    """Update Grid

     Update grid

    Args:
        grid_info_id (int):
        body (GridInfoOptional):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and
            Client.raise_on_unexpected_status is True.
        httpx2.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[GridInfoOut | HTTPValidationError]
    """

    kwargs = _get_kwargs(
        grid_info_id=grid_info_id,
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    grid_info_id: int,
    *,
    client: AuthenticatedClient,
    body: GridInfoOptional,
) -> GridInfoOut | HTTPValidationError | None:
    """Update Grid

     Update grid

    Args:
        grid_info_id (int):
        body (GridInfoOptional):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and
            Client.raise_on_unexpected_status is True.
        httpx2.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        GridInfoOut | HTTPValidationError
    """

    return (
        await asyncio_detailed(
            grid_info_id=grid_info_id,
            client=client,
            body=body,
        )
    ).parsed

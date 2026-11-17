from http import HTTPStatus
from typing import Any
from urllib.parse import quote

import httpx2

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.http_validation_error import HTTPValidationError
from ...models.tomogram_out import TomogramOut
from ...types import Response


def _get_kwargs(
    tomogram_id: int,
) -> dict[str, Any]:

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/tomograms/{tomogram_id}".format(
            tomogram_id=quote(str(tomogram_id), safe=""),
        ),
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx2.Response
) -> HTTPValidationError | TomogramOut | None:
    if response.status_code == 200:
        response_200 = TomogramOut.from_dict(response.json())

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
) -> Response[HTTPValidationError | TomogramOut]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    tomogram_id: int,
    *,
    client: AuthenticatedClient,
) -> Response[HTTPValidationError | TomogramOut]:
    """Get Tomogram

     Get a single tomogram

    Args:
        tomogram_id (int):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx2.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[HTTPValidationError | TomogramOut]
    """

    kwargs = _get_kwargs(
        tomogram_id=tomogram_id,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    tomogram_id: int,
    *,
    client: AuthenticatedClient,
) -> HTTPValidationError | TomogramOut | None:
    """Get Tomogram

     Get a single tomogram

    Args:
        tomogram_id (int):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx2.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        HTTPValidationError | TomogramOut
    """

    return sync_detailed(
        tomogram_id=tomogram_id,
        client=client,
    ).parsed


async def asyncio_detailed(
    tomogram_id: int,
    *,
    client: AuthenticatedClient,
) -> Response[HTTPValidationError | TomogramOut]:
    """Get Tomogram

     Get a single tomogram

    Args:
        tomogram_id (int):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx2.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[HTTPValidationError | TomogramOut]
    """

    kwargs = _get_kwargs(
        tomogram_id=tomogram_id,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    tomogram_id: int,
    *,
    client: AuthenticatedClient,
) -> HTTPValidationError | TomogramOut | None:
    """Get Tomogram

     Get a single tomogram

    Args:
        tomogram_id (int):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx2.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        HTTPValidationError | TomogramOut
    """

    return (
        await asyncio_detailed(
            tomogram_id=tomogram_id,
            client=client,
        )
    ).parsed

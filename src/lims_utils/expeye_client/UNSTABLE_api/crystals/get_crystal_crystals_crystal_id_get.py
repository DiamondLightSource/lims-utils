from http import HTTPStatus
from typing import Any
from urllib.parse import quote

import httpx2

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.crystal_out import CrystalOut
from ...models.http_validation_error import HTTPValidationError
from ...types import Response


def _get_kwargs(
    crystal_id: int,
) -> dict[str, Any]:

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/crystals/{crystal_id}".format(
            crystal_id=quote(str(crystal_id), safe=""),
        ),
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx2.Response
) -> CrystalOut | HTTPValidationError | None:
    if response.status_code == 200:
        response_200 = CrystalOut.from_dict(response.json())

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
) -> Response[CrystalOut | HTTPValidationError]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    crystal_id: int,
    *,
    client: AuthenticatedClient,
) -> Response[CrystalOut | HTTPValidationError]:
    """Get Crystal

     Get crystal

    Args:
        crystal_id (int):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx2.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[CrystalOut | HTTPValidationError]
    """

    kwargs = _get_kwargs(
        crystal_id=crystal_id,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    crystal_id: int,
    *,
    client: AuthenticatedClient,
) -> CrystalOut | HTTPValidationError | None:
    """Get Crystal

     Get crystal

    Args:
        crystal_id (int):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx2.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        CrystalOut | HTTPValidationError
    """

    return sync_detailed(
        crystal_id=crystal_id,
        client=client,
    ).parsed


async def asyncio_detailed(
    crystal_id: int,
    *,
    client: AuthenticatedClient,
) -> Response[CrystalOut | HTTPValidationError]:
    """Get Crystal

     Get crystal

    Args:
        crystal_id (int):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx2.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[CrystalOut | HTTPValidationError]
    """

    kwargs = _get_kwargs(
        crystal_id=crystal_id,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    crystal_id: int,
    *,
    client: AuthenticatedClient,
) -> CrystalOut | HTTPValidationError | None:
    """Get Crystal

     Get crystal

    Args:
        crystal_id (int):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx2.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        CrystalOut | HTTPValidationError
    """

    return (
        await asyncio_detailed(
            crystal_id=crystal_id,
            client=client,
        )
    ).parsed

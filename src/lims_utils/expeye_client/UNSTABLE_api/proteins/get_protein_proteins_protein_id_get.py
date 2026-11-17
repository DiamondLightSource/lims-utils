from http import HTTPStatus
from typing import Any
from urllib.parse import quote

import httpx2

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.http_validation_error import HTTPValidationError
from ...models.protein_out import ProteinOut
from ...types import Response


def _get_kwargs(
    protein_id: int,
) -> dict[str, Any]:

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/proteins/{protein_id}".format(
            protein_id=quote(str(protein_id), safe=""),
        ),
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx2.Response
) -> HTTPValidationError | ProteinOut | None:
    if response.status_code == 200:
        response_200 = ProteinOut.from_dict(response.json())

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
) -> Response[HTTPValidationError | ProteinOut]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    protein_id: int,
    *,
    client: AuthenticatedClient,
) -> Response[HTTPValidationError | ProteinOut]:
    """Get Protein

     Get protein

    Args:
        protein_id (int):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and
            Client.raise_on_unexpected_status is True.
        httpx2.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[HTTPValidationError | ProteinOut]
    """

    kwargs = _get_kwargs(
        protein_id=protein_id,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    protein_id: int,
    *,
    client: AuthenticatedClient,
) -> HTTPValidationError | ProteinOut | None:
    """Get Protein

     Get protein

    Args:
        protein_id (int):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and
            Client.raise_on_unexpected_status is True.
        httpx2.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        HTTPValidationError | ProteinOut
    """

    return sync_detailed(
        protein_id=protein_id,
        client=client,
    ).parsed


async def asyncio_detailed(
    protein_id: int,
    *,
    client: AuthenticatedClient,
) -> Response[HTTPValidationError | ProteinOut]:
    """Get Protein

     Get protein

    Args:
        protein_id (int):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and
            Client.raise_on_unexpected_status is True.
        httpx2.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[HTTPValidationError | ProteinOut]
    """

    kwargs = _get_kwargs(
        protein_id=protein_id,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    protein_id: int,
    *,
    client: AuthenticatedClient,
) -> HTTPValidationError | ProteinOut | None:
    """Get Protein

     Get protein

    Args:
        protein_id (int):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and
            Client.raise_on_unexpected_status is True.
        httpx2.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        HTTPValidationError | ProteinOut
    """

    return (
        await asyncio_detailed(
            protein_id=protein_id,
            client=client,
        )
    ).parsed

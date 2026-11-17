from http import HTTPStatus
from typing import Any
from urllib.parse import quote

import httpx2

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.http_validation_error import HTTPValidationError
from ...models.ligand_out import LigandOut
from ...types import Response


def _get_kwargs(
    ligand_id: int,
) -> dict[str, Any]:

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/ligands/{ligand_id}".format(
            ligand_id=quote(str(ligand_id), safe=""),
        ),
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx2.Response
) -> HTTPValidationError | LigandOut | None:
    if response.status_code == 200:
        response_200 = LigandOut.from_dict(response.json())

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
) -> Response[HTTPValidationError | LigandOut]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    ligand_id: int,
    *,
    client: AuthenticatedClient,
) -> Response[HTTPValidationError | LigandOut]:
    """Get Ligand

     Get ligand by ligandId

    Args:
        ligand_id (int):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and
            Client.raise_on_unexpected_status is True.
        httpx2.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[HTTPValidationError | LigandOut]
    """

    kwargs = _get_kwargs(
        ligand_id=ligand_id,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    ligand_id: int,
    *,
    client: AuthenticatedClient,
) -> HTTPValidationError | LigandOut | None:
    """Get Ligand

     Get ligand by ligandId

    Args:
        ligand_id (int):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and
            Client.raise_on_unexpected_status is True.
        httpx2.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        HTTPValidationError | LigandOut
    """

    return sync_detailed(
        ligand_id=ligand_id,
        client=client,
    ).parsed


async def asyncio_detailed(
    ligand_id: int,
    *,
    client: AuthenticatedClient,
) -> Response[HTTPValidationError | LigandOut]:
    """Get Ligand

     Get ligand by ligandId

    Args:
        ligand_id (int):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and
            Client.raise_on_unexpected_status is True.
        httpx2.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[HTTPValidationError | LigandOut]
    """

    kwargs = _get_kwargs(
        ligand_id=ligand_id,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    ligand_id: int,
    *,
    client: AuthenticatedClient,
) -> HTTPValidationError | LigandOut | None:
    """Get Ligand

     Get ligand by ligandId

    Args:
        ligand_id (int):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and
            Client.raise_on_unexpected_status is True.
        httpx2.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        HTTPValidationError | LigandOut
    """

    return (
        await asyncio_detailed(
            ligand_id=ligand_id,
            client=client,
        )
    ).parsed

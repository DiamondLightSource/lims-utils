from http import HTTPStatus
from typing import Any
from urllib.parse import quote

import httpx2

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.http_validation_error import HTTPValidationError
from ...models.sample_ligand_out import SampleLigandOut
from ...types import Response


def _get_kwargs(
    sample_id: int,
    ligand_id: int,
) -> dict[str, Any]:

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/samples/{sample_id}/ligands/{ligand_id}".format(
            sample_id=quote(str(sample_id), safe=""),
            ligand_id=quote(str(ligand_id), safe=""),
        ),
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx2.Response
) -> HTTPValidationError | SampleLigandOut | None:
    if response.status_code == 201:
        response_201 = SampleLigandOut.from_dict(response.json())

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
) -> Response[HTTPValidationError | SampleLigandOut]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    sample_id: int,
    ligand_id: int,
    *,
    client: AuthenticatedClient,
) -> Response[HTTPValidationError | SampleLigandOut]:
    """Create Sample Ligand

     Add ligand to sample

    Args:
        sample_id (int):
        ligand_id (int):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and
            Client.raise_on_unexpected_status is True.
        httpx2.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[HTTPValidationError | SampleLigandOut]
    """

    kwargs = _get_kwargs(
        sample_id=sample_id,
        ligand_id=ligand_id,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    sample_id: int,
    ligand_id: int,
    *,
    client: AuthenticatedClient,
) -> HTTPValidationError | SampleLigandOut | None:
    """Create Sample Ligand

     Add ligand to sample

    Args:
        sample_id (int):
        ligand_id (int):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and
            Client.raise_on_unexpected_status is True.
        httpx2.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        HTTPValidationError | SampleLigandOut
    """

    return sync_detailed(
        sample_id=sample_id,
        ligand_id=ligand_id,
        client=client,
    ).parsed


async def asyncio_detailed(
    sample_id: int,
    ligand_id: int,
    *,
    client: AuthenticatedClient,
) -> Response[HTTPValidationError | SampleLigandOut]:
    """Create Sample Ligand

     Add ligand to sample

    Args:
        sample_id (int):
        ligand_id (int):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and
            Client.raise_on_unexpected_status is True.
        httpx2.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[HTTPValidationError | SampleLigandOut]
    """

    kwargs = _get_kwargs(
        sample_id=sample_id,
        ligand_id=ligand_id,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    sample_id: int,
    ligand_id: int,
    *,
    client: AuthenticatedClient,
) -> HTTPValidationError | SampleLigandOut | None:
    """Create Sample Ligand

     Add ligand to sample

    Args:
        sample_id (int):
        ligand_id (int):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and
            Client.raise_on_unexpected_status is True.
        httpx2.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        HTTPValidationError | SampleLigandOut
    """

    return (
        await asyncio_detailed(
            sample_id=sample_id,
            ligand_id=ligand_id,
            client=client,
        )
    ).parsed

from http import HTTPStatus
from typing import Any
from urllib.parse import quote

import httpx2

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.http_validation_error import HTTPValidationError
from ...models.pdb_ligand_out import PDBLigandOut
from ...types import Response


def _get_kwargs(
    ligand_id: int,
    pdb_id: int,
) -> dict[str, Any]:

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/ligands/{ligand_id}/pdb-entries/{pdb_id}".format(
            ligand_id=quote(str(ligand_id), safe=""),
            pdb_id=quote(str(pdb_id), safe=""),
        ),
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx2.Response
) -> HTTPValidationError | PDBLigandOut | None:
    if response.status_code == 201:
        response_201 = PDBLigandOut.from_dict(response.json())

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
) -> Response[HTTPValidationError | PDBLigandOut]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    ligand_id: int,
    pdb_id: int,
    *,
    client: AuthenticatedClient,
) -> Response[HTTPValidationError | PDBLigandOut]:
    """Create Pdb Ligand

     Link a PDB entry to a ligand

    Args:
        ligand_id (int):
        pdb_id (int):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx2.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[HTTPValidationError | PDBLigandOut]
    """

    kwargs = _get_kwargs(
        ligand_id=ligand_id,
        pdb_id=pdb_id,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    ligand_id: int,
    pdb_id: int,
    *,
    client: AuthenticatedClient,
) -> HTTPValidationError | PDBLigandOut | None:
    """Create Pdb Ligand

     Link a PDB entry to a ligand

    Args:
        ligand_id (int):
        pdb_id (int):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx2.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        HTTPValidationError | PDBLigandOut
    """

    return sync_detailed(
        ligand_id=ligand_id,
        pdb_id=pdb_id,
        client=client,
    ).parsed


async def asyncio_detailed(
    ligand_id: int,
    pdb_id: int,
    *,
    client: AuthenticatedClient,
) -> Response[HTTPValidationError | PDBLigandOut]:
    """Create Pdb Ligand

     Link a PDB entry to a ligand

    Args:
        ligand_id (int):
        pdb_id (int):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx2.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[HTTPValidationError | PDBLigandOut]
    """

    kwargs = _get_kwargs(
        ligand_id=ligand_id,
        pdb_id=pdb_id,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    ligand_id: int,
    pdb_id: int,
    *,
    client: AuthenticatedClient,
) -> HTTPValidationError | PDBLigandOut | None:
    """Create Pdb Ligand

     Link a PDB entry to a ligand

    Args:
        ligand_id (int):
        pdb_id (int):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx2.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        HTTPValidationError | PDBLigandOut
    """

    return (
        await asyncio_detailed(
            ligand_id=ligand_id,
            pdb_id=pdb_id,
            client=client,
        )
    ).parsed

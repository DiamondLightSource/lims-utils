from http import HTTPStatus
from typing import Any
from urllib.parse import quote

import httpx2

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.http_validation_error import HTTPValidationError
from ...models.paged_pdb_out import PagedPDBOut
from ...types import UNSET, Response, Unset


def _get_kwargs(
    ligand_id: int,
    *,
    name: None | str | Unset = UNSET,
    code: None | str | Unset = UNSET,
    page: int | Unset = 0,
    limit: int | Unset = 25,
) -> dict[str, Any]:

    params: dict[str, Any] = {}

    json_name: None | str | Unset
    if isinstance(name, Unset):
        json_name = UNSET
    else:
        json_name = name
    params["name"] = json_name

    json_code: None | str | Unset
    if isinstance(code, Unset):
        json_code = UNSET
    else:
        json_code = code
    params["code"] = json_code

    params["page"] = page

    params["limit"] = limit

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/ligands/{ligand_id}/pdb-entries".format(
            ligand_id=quote(str(ligand_id), safe=""),
        ),
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx2.Response
) -> HTTPValidationError | PagedPDBOut | None:
    if response.status_code == 200:
        response_200 = PagedPDBOut.from_dict(response.json())

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
) -> Response[HTTPValidationError | PagedPDBOut]:
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
    name: None | str | Unset = UNSET,
    code: None | str | Unset = UNSET,
    page: int | Unset = 0,
    limit: int | Unset = 25,
) -> Response[HTTPValidationError | PagedPDBOut]:
    """Get Ligand Pdbs

     Get ligand PDB entries

    Args:
        ligand_id (int):
        name (None | str | Unset):
        code (None | str | Unset):
        page (int | Unset): Page number/Results to skip. Negative numbers count backwards from the
            last page Default: 0.
        limit (int | Unset): Number of results to show Default: 25.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and
        Client.raise_on_unexpected_status is True.
        httpx2.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[HTTPValidationError | PagedPDBOut]
    """

    kwargs = _get_kwargs(
        ligand_id=ligand_id,
        name=name,
        code=code,
        page=page,
        limit=limit,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    ligand_id: int,
    *,
    client: AuthenticatedClient,
    name: None | str | Unset = UNSET,
    code: None | str | Unset = UNSET,
    page: int | Unset = 0,
    limit: int | Unset = 25,
) -> HTTPValidationError | PagedPDBOut | None:
    """Get Ligand Pdbs

     Get ligand PDB entries

    Args:
        ligand_id (int):
        name (None | str | Unset):
        code (None | str | Unset):
        page (int | Unset): Page number/Results to skip. Negative numbers count backwards from the
            last page Default: 0.
        limit (int | Unset): Number of results to show Default: 25.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and
        Client.raise_on_unexpected_status is True.
        httpx2.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        HTTPValidationError | PagedPDBOut
    """

    return sync_detailed(
        ligand_id=ligand_id,
        client=client,
        name=name,
        code=code,
        page=page,
        limit=limit,
    ).parsed


async def asyncio_detailed(
    ligand_id: int,
    *,
    client: AuthenticatedClient,
    name: None | str | Unset = UNSET,
    code: None | str | Unset = UNSET,
    page: int | Unset = 0,
    limit: int | Unset = 25,
) -> Response[HTTPValidationError | PagedPDBOut]:
    """Get Ligand Pdbs

     Get ligand PDB entries

    Args:
        ligand_id (int):
        name (None | str | Unset):
        code (None | str | Unset):
        page (int | Unset): Page number/Results to skip. Negative numbers count backwards from the
            last page Default: 0.
        limit (int | Unset): Number of results to show Default: 25.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and
        Client.raise_on_unexpected_status is True.
        httpx2.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[HTTPValidationError | PagedPDBOut]
    """

    kwargs = _get_kwargs(
        ligand_id=ligand_id,
        name=name,
        code=code,
        page=page,
        limit=limit,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    ligand_id: int,
    *,
    client: AuthenticatedClient,
    name: None | str | Unset = UNSET,
    code: None | str | Unset = UNSET,
    page: int | Unset = 0,
    limit: int | Unset = 25,
) -> HTTPValidationError | PagedPDBOut | None:
    """Get Ligand Pdbs

     Get ligand PDB entries

    Args:
        ligand_id (int):
        name (None | str | Unset):
        code (None | str | Unset):
        page (int | Unset): Page number/Results to skip. Negative numbers count backwards from the
            last page Default: 0.
        limit (int | Unset): Number of results to show Default: 25.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and
        Client.raise_on_unexpected_status is True.
        httpx2.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        HTTPValidationError | PagedPDBOut
    """

    return (
        await asyncio_detailed(
            ligand_id=ligand_id,
            client=client,
            name=name,
            code=code,
            page=page,
            limit=limit,
        )
    ).parsed

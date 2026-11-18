from http import HTTPStatus
from typing import Any
from urllib.parse import quote

import httpx2

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.http_validation_error import HTTPValidationError
from ...models.paged_mxmr_run_blob_out import PagedMXMRRunBlobOut
from ...types import UNSET, Response, Unset


def _get_kwargs(
    proposal_reference: str,
    visit_number: int,
    *,
    file_path: None | str | Unset = UNSET,
    page: int | Unset = 0,
    limit: int | Unset = 25,
) -> dict[str, Any]:

    params: dict[str, Any] = {}

    json_file_path: None | str | Unset
    if isinstance(file_path, Unset):
        json_file_path = UNSET
    else:
        json_file_path = file_path
    params["filePath"] = json_file_path

    params["page"] = page

    params["limit"] = limit

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/proposals/{proposal_reference}/sessions/{visit_number}/blobs".format(
            proposal_reference=quote(str(proposal_reference), safe=""),
            visit_number=quote(str(visit_number), safe=""),
        ),
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx2.Response
) -> HTTPValidationError | PagedMXMRRunBlobOut | None:
    if response.status_code == 200:
        response_200 = PagedMXMRRunBlobOut.from_dict(response.json())

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
) -> Response[HTTPValidationError | PagedMXMRRunBlobOut]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    proposal_reference: str,
    visit_number: int,
    *,
    client: AuthenticatedClient,
    file_path: None | str | Unset = UNSET,
    page: int | Unset = 0,
    limit: int | Unset = 25,
) -> Response[HTTPValidationError | PagedMXMRRunBlobOut]:
    """Get Mxmrrun Blobs

     Get processing program MXMRRun Blobs

    Args:
        proposal_reference (str):
        visit_number (int):
        file_path (None | str | Unset):
        page (int | Unset): Page number/Results to skip. Negative numbers count backwards from the
            last page Default: 0.
        limit (int | Unset): Number of results to show Default: 25.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and
        Client.raise_on_unexpected_status is True.
        httpx2.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[HTTPValidationError | PagedMXMRRunBlobOut]
    """

    kwargs = _get_kwargs(
        proposal_reference=proposal_reference,
        visit_number=visit_number,
        file_path=file_path,
        page=page,
        limit=limit,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    proposal_reference: str,
    visit_number: int,
    *,
    client: AuthenticatedClient,
    file_path: None | str | Unset = UNSET,
    page: int | Unset = 0,
    limit: int | Unset = 25,
) -> HTTPValidationError | PagedMXMRRunBlobOut | None:
    """Get Mxmrrun Blobs

     Get processing program MXMRRun Blobs

    Args:
        proposal_reference (str):
        visit_number (int):
        file_path (None | str | Unset):
        page (int | Unset): Page number/Results to skip. Negative numbers count backwards from the
            last page Default: 0.
        limit (int | Unset): Number of results to show Default: 25.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and
        Client.raise_on_unexpected_status is True.
        httpx2.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        HTTPValidationError | PagedMXMRRunBlobOut
    """

    return sync_detailed(
        proposal_reference=proposal_reference,
        visit_number=visit_number,
        client=client,
        file_path=file_path,
        page=page,
        limit=limit,
    ).parsed


async def asyncio_detailed(
    proposal_reference: str,
    visit_number: int,
    *,
    client: AuthenticatedClient,
    file_path: None | str | Unset = UNSET,
    page: int | Unset = 0,
    limit: int | Unset = 25,
) -> Response[HTTPValidationError | PagedMXMRRunBlobOut]:
    """Get Mxmrrun Blobs

     Get processing program MXMRRun Blobs

    Args:
        proposal_reference (str):
        visit_number (int):
        file_path (None | str | Unset):
        page (int | Unset): Page number/Results to skip. Negative numbers count backwards from the
            last page Default: 0.
        limit (int | Unset): Number of results to show Default: 25.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and
        Client.raise_on_unexpected_status is True.
        httpx2.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[HTTPValidationError | PagedMXMRRunBlobOut]
    """

    kwargs = _get_kwargs(
        proposal_reference=proposal_reference,
        visit_number=visit_number,
        file_path=file_path,
        page=page,
        limit=limit,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    proposal_reference: str,
    visit_number: int,
    *,
    client: AuthenticatedClient,
    file_path: None | str | Unset = UNSET,
    page: int | Unset = 0,
    limit: int | Unset = 25,
) -> HTTPValidationError | PagedMXMRRunBlobOut | None:
    """Get Mxmrrun Blobs

     Get processing program MXMRRun Blobs

    Args:
        proposal_reference (str):
        visit_number (int):
        file_path (None | str | Unset):
        page (int | Unset): Page number/Results to skip. Negative numbers count backwards from the
            last page Default: 0.
        limit (int | Unset): Number of results to show Default: 25.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and
        Client.raise_on_unexpected_status is True.
        httpx2.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        HTTPValidationError | PagedMXMRRunBlobOut
    """

    return (
        await asyncio_detailed(
            proposal_reference=proposal_reference,
            visit_number=visit_number,
            client=client,
            file_path=file_path,
            page=page,
            limit=limit,
        )
    ).parsed

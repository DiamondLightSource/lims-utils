from http import HTTPStatus
from typing import Any
from urllib.parse import quote

import httpx2

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.http_validation_error import HTTPValidationError
from ...models.paged_auto_proc_program_attachment_out import PagedAutoProcProgramAttachmentOut
from ...types import UNSET, Response, Unset


def _get_kwargs(
    auto_proc_program_id: int,
    *,
    file_path: None | str | Unset = UNSET,
    file_name: None | str | Unset = UNSET,
    file_type: None | str | Unset = UNSET,
    importance_rank: int | None | Unset = UNSET,
    search: None | str | Unset = UNSET,
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

    json_file_name: None | str | Unset
    if isinstance(file_name, Unset):
        json_file_name = UNSET
    else:
        json_file_name = file_name
    params["fileName"] = json_file_name

    json_file_type: None | str | Unset
    if isinstance(file_type, Unset):
        json_file_type = UNSET
    else:
        json_file_type = file_type
    params["fileType"] = json_file_type

    json_importance_rank: int | None | Unset
    if isinstance(importance_rank, Unset):
        json_importance_rank = UNSET
    else:
        json_importance_rank = importance_rank
    params["importanceRank"] = json_importance_rank

    json_search: None | str | Unset
    if isinstance(search, Unset):
        json_search = UNSET
    else:
        json_search = search
    params["search"] = json_search

    params["page"] = page

    params["limit"] = limit

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/processing-programs/{auto_proc_program_id}/attachments".format(
            auto_proc_program_id=quote(str(auto_proc_program_id), safe=""),
        ),
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx2.Response
) -> HTTPValidationError | PagedAutoProcProgramAttachmentOut | None:
    if response.status_code == 200:
        response_200 = PagedAutoProcProgramAttachmentOut.from_dict(response.json())

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
) -> Response[HTTPValidationError | PagedAutoProcProgramAttachmentOut]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    auto_proc_program_id: int,
    *,
    client: AuthenticatedClient,
    file_path: None | str | Unset = UNSET,
    file_name: None | str | Unset = UNSET,
    file_type: None | str | Unset = UNSET,
    importance_rank: int | None | Unset = UNSET,
    search: None | str | Unset = UNSET,
    page: int | Unset = 0,
    limit: int | Unset = 25,
) -> Response[HTTPValidationError | PagedAutoProcProgramAttachmentOut]:
    """Get Auto Proc Program Attachments

     Get processing program attachments

    Args:
        auto_proc_program_id (int):
        file_path (None | str | Unset):
        file_name (None | str | Unset):
        file_type (None | str | Unset):
        importance_rank (int | None | Unset):
        search (None | str | Unset):
        page (int | Unset): Page number/Results to skip. Negative numbers count backwards from the
            last page Default: 0.
        limit (int | Unset): Number of results to show Default: 25.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and
        Client.raise_on_unexpected_status is True.
        httpx2.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[HTTPValidationError | PagedAutoProcProgramAttachmentOut]
    """

    kwargs = _get_kwargs(
        auto_proc_program_id=auto_proc_program_id,
        file_path=file_path,
        file_name=file_name,
        file_type=file_type,
        importance_rank=importance_rank,
        search=search,
        page=page,
        limit=limit,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    auto_proc_program_id: int,
    *,
    client: AuthenticatedClient,
    file_path: None | str | Unset = UNSET,
    file_name: None | str | Unset = UNSET,
    file_type: None | str | Unset = UNSET,
    importance_rank: int | None | Unset = UNSET,
    search: None | str | Unset = UNSET,
    page: int | Unset = 0,
    limit: int | Unset = 25,
) -> HTTPValidationError | PagedAutoProcProgramAttachmentOut | None:
    """Get Auto Proc Program Attachments

     Get processing program attachments

    Args:
        auto_proc_program_id (int):
        file_path (None | str | Unset):
        file_name (None | str | Unset):
        file_type (None | str | Unset):
        importance_rank (int | None | Unset):
        search (None | str | Unset):
        page (int | Unset): Page number/Results to skip. Negative numbers count backwards from the
            last page Default: 0.
        limit (int | Unset): Number of results to show Default: 25.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and
        Client.raise_on_unexpected_status is True.
        httpx2.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        HTTPValidationError | PagedAutoProcProgramAttachmentOut
    """

    return sync_detailed(
        auto_proc_program_id=auto_proc_program_id,
        client=client,
        file_path=file_path,
        file_name=file_name,
        file_type=file_type,
        importance_rank=importance_rank,
        search=search,
        page=page,
        limit=limit,
    ).parsed


async def asyncio_detailed(
    auto_proc_program_id: int,
    *,
    client: AuthenticatedClient,
    file_path: None | str | Unset = UNSET,
    file_name: None | str | Unset = UNSET,
    file_type: None | str | Unset = UNSET,
    importance_rank: int | None | Unset = UNSET,
    search: None | str | Unset = UNSET,
    page: int | Unset = 0,
    limit: int | Unset = 25,
) -> Response[HTTPValidationError | PagedAutoProcProgramAttachmentOut]:
    """Get Auto Proc Program Attachments

     Get processing program attachments

    Args:
        auto_proc_program_id (int):
        file_path (None | str | Unset):
        file_name (None | str | Unset):
        file_type (None | str | Unset):
        importance_rank (int | None | Unset):
        search (None | str | Unset):
        page (int | Unset): Page number/Results to skip. Negative numbers count backwards from the
            last page Default: 0.
        limit (int | Unset): Number of results to show Default: 25.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and
        Client.raise_on_unexpected_status is True.
        httpx2.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[HTTPValidationError | PagedAutoProcProgramAttachmentOut]
    """

    kwargs = _get_kwargs(
        auto_proc_program_id=auto_proc_program_id,
        file_path=file_path,
        file_name=file_name,
        file_type=file_type,
        importance_rank=importance_rank,
        search=search,
        page=page,
        limit=limit,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    auto_proc_program_id: int,
    *,
    client: AuthenticatedClient,
    file_path: None | str | Unset = UNSET,
    file_name: None | str | Unset = UNSET,
    file_type: None | str | Unset = UNSET,
    importance_rank: int | None | Unset = UNSET,
    search: None | str | Unset = UNSET,
    page: int | Unset = 0,
    limit: int | Unset = 25,
) -> HTTPValidationError | PagedAutoProcProgramAttachmentOut | None:
    """Get Auto Proc Program Attachments

     Get processing program attachments

    Args:
        auto_proc_program_id (int):
        file_path (None | str | Unset):
        file_name (None | str | Unset):
        file_type (None | str | Unset):
        importance_rank (int | None | Unset):
        search (None | str | Unset):
        page (int | Unset): Page number/Results to skip. Negative numbers count backwards from the
            last page Default: 0.
        limit (int | Unset): Number of results to show Default: 25.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and
        Client.raise_on_unexpected_status is True.
        httpx2.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        HTTPValidationError | PagedAutoProcProgramAttachmentOut
    """

    return (
        await asyncio_detailed(
            auto_proc_program_id=auto_proc_program_id,
            client=client,
            file_path=file_path,
            file_name=file_name,
            file_type=file_type,
            importance_rank=importance_rank,
            search=search,
            page=page,
            limit=limit,
        )
    ).parsed

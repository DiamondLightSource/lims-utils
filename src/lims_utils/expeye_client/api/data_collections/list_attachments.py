from http import HTTPStatus
from typing import Any
from urllib.parse import quote

import httpx2

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.file_attachment_type import FileAttachmentType
from ...models.http_validation_error import HTTPValidationError
from ...models.paged_data_collection_file_attachment_out import PagedDataCollectionFileAttachmentOut
from ...types import UNSET, Response, Unset


def _get_kwargs(
    data_collection_id: int,
    *,
    filetype: FileAttachmentType | None | Unset = UNSET,
    search: None | str | Unset = UNSET,
    page: int | Unset = 0,
    limit: int | Unset = 25,
) -> dict[str, Any]:

    params: dict[str, Any] = {}

    json_filetype: None | str | Unset
    if isinstance(filetype, Unset):
        json_filetype = UNSET
    elif isinstance(filetype, FileAttachmentType):
        json_filetype = filetype.value
    else:
        json_filetype = filetype
    params["filetype"] = json_filetype

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
        "url": "/data-collections/{data_collection_id}/attachments".format(
            data_collection_id=quote(str(data_collection_id), safe=""),
        ),
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx2.Response
) -> HTTPValidationError | PagedDataCollectionFileAttachmentOut | None:
    if response.status_code == 200:
        response_200 = PagedDataCollectionFileAttachmentOut.from_dict(response.json())

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
) -> Response[HTTPValidationError | PagedDataCollectionFileAttachmentOut]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    data_collection_id: int,
    *,
    client: AuthenticatedClient,
    filetype: FileAttachmentType | None | Unset = UNSET,
    search: None | str | Unset = UNSET,
    page: int | Unset = 0,
    limit: int | Unset = 25,
) -> Response[HTTPValidationError | PagedDataCollectionFileAttachmentOut]:
    """Get Attachments

     Get attachments that belong to the data collection

    Args:
        data_collection_id (int):
        filetype (FileAttachmentType | None | Unset):
        search (None | str | Unset):
        page (int | Unset): Page number/Results to skip. Negative numbers count backwards from the
            last page Default: 0.
        limit (int | Unset): Number of results to show Default: 25.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and
        Client.raise_on_unexpected_status is True.
        httpx2.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[HTTPValidationError | PagedDataCollectionFileAttachmentOut]
    """

    kwargs = _get_kwargs(
        data_collection_id=data_collection_id,
        filetype=filetype,
        search=search,
        page=page,
        limit=limit,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    data_collection_id: int,
    *,
    client: AuthenticatedClient,
    filetype: FileAttachmentType | None | Unset = UNSET,
    search: None | str | Unset = UNSET,
    page: int | Unset = 0,
    limit: int | Unset = 25,
) -> HTTPValidationError | PagedDataCollectionFileAttachmentOut | None:
    """Get Attachments

     Get attachments that belong to the data collection

    Args:
        data_collection_id (int):
        filetype (FileAttachmentType | None | Unset):
        search (None | str | Unset):
        page (int | Unset): Page number/Results to skip. Negative numbers count backwards from the
            last page Default: 0.
        limit (int | Unset): Number of results to show Default: 25.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and
        Client.raise_on_unexpected_status is True.
        httpx2.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        HTTPValidationError | PagedDataCollectionFileAttachmentOut
    """

    return sync_detailed(
        data_collection_id=data_collection_id,
        client=client,
        filetype=filetype,
        search=search,
        page=page,
        limit=limit,
    ).parsed


async def asyncio_detailed(
    data_collection_id: int,
    *,
    client: AuthenticatedClient,
    filetype: FileAttachmentType | None | Unset = UNSET,
    search: None | str | Unset = UNSET,
    page: int | Unset = 0,
    limit: int | Unset = 25,
) -> Response[HTTPValidationError | PagedDataCollectionFileAttachmentOut]:
    """Get Attachments

     Get attachments that belong to the data collection

    Args:
        data_collection_id (int):
        filetype (FileAttachmentType | None | Unset):
        search (None | str | Unset):
        page (int | Unset): Page number/Results to skip. Negative numbers count backwards from the
            last page Default: 0.
        limit (int | Unset): Number of results to show Default: 25.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and
        Client.raise_on_unexpected_status is True.
        httpx2.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[HTTPValidationError | PagedDataCollectionFileAttachmentOut]
    """

    kwargs = _get_kwargs(
        data_collection_id=data_collection_id,
        filetype=filetype,
        search=search,
        page=page,
        limit=limit,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    data_collection_id: int,
    *,
    client: AuthenticatedClient,
    filetype: FileAttachmentType | None | Unset = UNSET,
    search: None | str | Unset = UNSET,
    page: int | Unset = 0,
    limit: int | Unset = 25,
) -> HTTPValidationError | PagedDataCollectionFileAttachmentOut | None:
    """Get Attachments

     Get attachments that belong to the data collection

    Args:
        data_collection_id (int):
        filetype (FileAttachmentType | None | Unset):
        search (None | str | Unset):
        page (int | Unset): Page number/Results to skip. Negative numbers count backwards from the
            last page Default: 0.
        limit (int | Unset): Number of results to show Default: 25.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and
        Client.raise_on_unexpected_status is True.
        httpx2.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        HTTPValidationError | PagedDataCollectionFileAttachmentOut
    """

    return (
        await asyncio_detailed(
            data_collection_id=data_collection_id,
            client=client,
            filetype=filetype,
            search=search,
            page=page,
            limit=limit,
        )
    ).parsed

import datetime
from http import HTTPStatus
from typing import Any
from urllib.parse import quote

import httpx2

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.http_validation_error import HTTPValidationError
from ...models.paged_container_history_out import PagedContainerHistoryOut
from ...types import UNSET, Response, Unset


def _get_kwargs(
    container_id: int,
    *,
    min_date: datetime.datetime | None | Unset = UNSET,
    max_date: datetime.datetime | None | Unset = UNSET,
    page: int | Unset = 0,
    limit: int | Unset = 25,
) -> dict[str, Any]:

    params: dict[str, Any] = {}

    json_min_date: None | str | Unset
    if isinstance(min_date, Unset):
        json_min_date = UNSET
    elif isinstance(min_date, datetime.datetime):
        json_min_date = min_date.isoformat()
    else:
        json_min_date = min_date
    params["minDate"] = json_min_date

    json_max_date: None | str | Unset
    if isinstance(max_date, Unset):
        json_max_date = UNSET
    elif isinstance(max_date, datetime.datetime):
        json_max_date = max_date.isoformat()
    else:
        json_max_date = max_date
    params["maxDate"] = json_max_date

    params["page"] = page

    params["limit"] = limit

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/containers/{container_id}/history".format(
            container_id=quote(str(container_id), safe=""),
        ),
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx2.Response
) -> HTTPValidationError | PagedContainerHistoryOut | None:
    if response.status_code == 200:
        response_200 = PagedContainerHistoryOut.from_dict(response.json())

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
) -> Response[HTTPValidationError | PagedContainerHistoryOut]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    container_id: int,
    *,
    client: AuthenticatedClient,
    min_date: datetime.datetime | None | Unset = UNSET,
    max_date: datetime.datetime | None | Unset = UNSET,
    page: int | Unset = 0,
    limit: int | Unset = 25,
) -> Response[HTTPValidationError | PagedContainerHistoryOut]:
    """Get Container History

     Get container history

    Args:
        container_id (int):
        min_date (datetime.datetime | None | Unset):
        max_date (datetime.datetime | None | Unset):
        page (int | Unset): Page number/Results to skip. Negative numbers count backwards from the
            last page Default: 0.
        limit (int | Unset): Number of results to show Default: 25.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and
        Client.raise_on_unexpected_status is True.
        httpx2.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[HTTPValidationError | PagedContainerHistoryOut]
    """

    kwargs = _get_kwargs(
        container_id=container_id,
        min_date=min_date,
        max_date=max_date,
        page=page,
        limit=limit,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    container_id: int,
    *,
    client: AuthenticatedClient,
    min_date: datetime.datetime | None | Unset = UNSET,
    max_date: datetime.datetime | None | Unset = UNSET,
    page: int | Unset = 0,
    limit: int | Unset = 25,
) -> HTTPValidationError | PagedContainerHistoryOut | None:
    """Get Container History

     Get container history

    Args:
        container_id (int):
        min_date (datetime.datetime | None | Unset):
        max_date (datetime.datetime | None | Unset):
        page (int | Unset): Page number/Results to skip. Negative numbers count backwards from the
            last page Default: 0.
        limit (int | Unset): Number of results to show Default: 25.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and
        Client.raise_on_unexpected_status is True.
        httpx2.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        HTTPValidationError | PagedContainerHistoryOut
    """

    return sync_detailed(
        container_id=container_id,
        client=client,
        min_date=min_date,
        max_date=max_date,
        page=page,
        limit=limit,
    ).parsed


async def asyncio_detailed(
    container_id: int,
    *,
    client: AuthenticatedClient,
    min_date: datetime.datetime | None | Unset = UNSET,
    max_date: datetime.datetime | None | Unset = UNSET,
    page: int | Unset = 0,
    limit: int | Unset = 25,
) -> Response[HTTPValidationError | PagedContainerHistoryOut]:
    """Get Container History

     Get container history

    Args:
        container_id (int):
        min_date (datetime.datetime | None | Unset):
        max_date (datetime.datetime | None | Unset):
        page (int | Unset): Page number/Results to skip. Negative numbers count backwards from the
            last page Default: 0.
        limit (int | Unset): Number of results to show Default: 25.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and
        Client.raise_on_unexpected_status is True.
        httpx2.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[HTTPValidationError | PagedContainerHistoryOut]
    """

    kwargs = _get_kwargs(
        container_id=container_id,
        min_date=min_date,
        max_date=max_date,
        page=page,
        limit=limit,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    container_id: int,
    *,
    client: AuthenticatedClient,
    min_date: datetime.datetime | None | Unset = UNSET,
    max_date: datetime.datetime | None | Unset = UNSET,
    page: int | Unset = 0,
    limit: int | Unset = 25,
) -> HTTPValidationError | PagedContainerHistoryOut | None:
    """Get Container History

     Get container history

    Args:
        container_id (int):
        min_date (datetime.datetime | None | Unset):
        max_date (datetime.datetime | None | Unset):
        page (int | Unset): Page number/Results to skip. Negative numbers count backwards from the
            last page Default: 0.
        limit (int | Unset): Number of results to show Default: 25.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and
        Client.raise_on_unexpected_status is True.
        httpx2.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        HTTPValidationError | PagedContainerHistoryOut
    """

    return (
        await asyncio_detailed(
            container_id=container_id,
            client=client,
            min_date=min_date,
            max_date=max_date,
            page=page,
            limit=limit,
        )
    ).parsed

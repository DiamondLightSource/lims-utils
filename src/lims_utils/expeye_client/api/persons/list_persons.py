from http import HTTPStatus
from typing import Any

import httpx2

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.http_validation_error import HTTPValidationError
from ...models.paged_person_out import PagedPersonOut
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    search: str | Unset = "",
    include_missing_email: bool | Unset = False,
    page: int | Unset = 0,
    limit: int | Unset = 25,
) -> dict[str, Any]:

    params: dict[str, Any] = {}

    params["search"] = search

    params["includeMissingEmail"] = include_missing_email

    params["page"] = page

    params["limit"] = limit

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/persons",
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx2.Response
) -> HTTPValidationError | PagedPersonOut | None:
    if response.status_code == 200:
        response_200 = PagedPersonOut.from_dict(response.json())

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
) -> Response[HTTPValidationError | PagedPersonOut]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient,
    search: str | Unset = "",
    include_missing_email: bool | Unset = False,
    page: int | Unset = 0,
    limit: int | Unset = 25,
) -> Response[HTTPValidationError | PagedPersonOut]:
    """Get Persons

     Get persons

    Args:
        search (str | Unset):  Default: ''.
        include_missing_email (bool | Unset):  Default: False.
        page (int | Unset): Page number/Results to skip. Negative numbers count backwards from the
            last page Default: 0.
        limit (int | Unset): Number of results to show Default: 25.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and
        Client.raise_on_unexpected_status is True.
        httpx2.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[HTTPValidationError | PagedPersonOut]
    """

    kwargs = _get_kwargs(
        search=search,
        include_missing_email=include_missing_email,
        page=page,
        limit=limit,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: AuthenticatedClient,
    search: str | Unset = "",
    include_missing_email: bool | Unset = False,
    page: int | Unset = 0,
    limit: int | Unset = 25,
) -> HTTPValidationError | PagedPersonOut | None:
    """Get Persons

     Get persons

    Args:
        search (str | Unset):  Default: ''.
        include_missing_email (bool | Unset):  Default: False.
        page (int | Unset): Page number/Results to skip. Negative numbers count backwards from the
            last page Default: 0.
        limit (int | Unset): Number of results to show Default: 25.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and
        Client.raise_on_unexpected_status is True.
        httpx2.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        HTTPValidationError | PagedPersonOut
    """

    return sync_detailed(
        client=client,
        search=search,
        include_missing_email=include_missing_email,
        page=page,
        limit=limit,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    search: str | Unset = "",
    include_missing_email: bool | Unset = False,
    page: int | Unset = 0,
    limit: int | Unset = 25,
) -> Response[HTTPValidationError | PagedPersonOut]:
    """Get Persons

     Get persons

    Args:
        search (str | Unset):  Default: ''.
        include_missing_email (bool | Unset):  Default: False.
        page (int | Unset): Page number/Results to skip. Negative numbers count backwards from the
            last page Default: 0.
        limit (int | Unset): Number of results to show Default: 25.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and
        Client.raise_on_unexpected_status is True.
        httpx2.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[HTTPValidationError | PagedPersonOut]
    """

    kwargs = _get_kwargs(
        search=search,
        include_missing_email=include_missing_email,
        page=page,
        limit=limit,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient,
    search: str | Unset = "",
    include_missing_email: bool | Unset = False,
    page: int | Unset = 0,
    limit: int | Unset = 25,
) -> HTTPValidationError | PagedPersonOut | None:
    """Get Persons

     Get persons

    Args:
        search (str | Unset):  Default: ''.
        include_missing_email (bool | Unset):  Default: False.
        page (int | Unset): Page number/Results to skip. Negative numbers count backwards from the
            last page Default: 0.
        limit (int | Unset): Number of results to show Default: 25.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and
        Client.raise_on_unexpected_status is True.
        httpx2.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        HTTPValidationError | PagedPersonOut
    """

    return (
        await asyncio_detailed(
            client=client,
            search=search,
            include_missing_email=include_missing_email,
            page=page,
            limit=limit,
        )
    ).parsed

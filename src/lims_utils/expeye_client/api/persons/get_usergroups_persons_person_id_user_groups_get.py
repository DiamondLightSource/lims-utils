from http import HTTPStatus
from typing import Any
from urllib.parse import quote
from uuid import UUID

import httpx2

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.http_validation_error import HTTPValidationError
from ...models.paged_user_group_out import PagedUserGroupOut
from ...types import UNSET, Response, Unset


def _get_kwargs(
    person_id: int | UUID,
    *,
    page: int | Unset = 0,
    limit: int | Unset = 25,
) -> dict[str, Any]:

    params: dict[str, Any] = {}

    params["page"] = page

    params["limit"] = limit

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/persons/{person_id}/user-groups".format(
            person_id=quote(str(person_id), safe=""),
        ),
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx2.Response
) -> HTTPValidationError | PagedUserGroupOut | None:
    if response.status_code == 200:
        response_200 = PagedUserGroupOut.from_dict(response.json())

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
) -> Response[HTTPValidationError | PagedUserGroupOut]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    person_id: int | UUID,
    *,
    client: AuthenticatedClient,
    page: int | Unset = 0,
    limit: int | Unset = 25,
) -> Response[HTTPValidationError | PagedUserGroupOut]:
    """Get Usergroups

     Get usergroups person is in

    Args:
        person_id (int | UUID):
        page (int | Unset): Page number/Results to skip. Negative numbers count backwards from the
            last page Default: 0.
        limit (int | Unset): Number of results to show Default: 25.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx2.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[HTTPValidationError | PagedUserGroupOut]
    """

    kwargs = _get_kwargs(
        person_id=person_id,
        page=page,
        limit=limit,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    person_id: int | UUID,
    *,
    client: AuthenticatedClient,
    page: int | Unset = 0,
    limit: int | Unset = 25,
) -> HTTPValidationError | PagedUserGroupOut | None:
    """Get Usergroups

     Get usergroups person is in

    Args:
        person_id (int | UUID):
        page (int | Unset): Page number/Results to skip. Negative numbers count backwards from the
            last page Default: 0.
        limit (int | Unset): Number of results to show Default: 25.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx2.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        HTTPValidationError | PagedUserGroupOut
    """

    return sync_detailed(
        person_id=person_id,
        client=client,
        page=page,
        limit=limit,
    ).parsed


async def asyncio_detailed(
    person_id: int | UUID,
    *,
    client: AuthenticatedClient,
    page: int | Unset = 0,
    limit: int | Unset = 25,
) -> Response[HTTPValidationError | PagedUserGroupOut]:
    """Get Usergroups

     Get usergroups person is in

    Args:
        person_id (int | UUID):
        page (int | Unset): Page number/Results to skip. Negative numbers count backwards from the
            last page Default: 0.
        limit (int | Unset): Number of results to show Default: 25.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx2.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[HTTPValidationError | PagedUserGroupOut]
    """

    kwargs = _get_kwargs(
        person_id=person_id,
        page=page,
        limit=limit,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    person_id: int | UUID,
    *,
    client: AuthenticatedClient,
    page: int | Unset = 0,
    limit: int | Unset = 25,
) -> HTTPValidationError | PagedUserGroupOut | None:
    """Get Usergroups

     Get usergroups person is in

    Args:
        person_id (int | UUID):
        page (int | Unset): Page number/Results to skip. Negative numbers count backwards from the
            last page Default: 0.
        limit (int | Unset): Number of results to show Default: 25.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx2.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        HTTPValidationError | PagedUserGroupOut
    """

    return (
        await asyncio_detailed(
            person_id=person_id,
            client=client,
            page=page,
            limit=limit,
        )
    ).parsed

from http import HTTPStatus
from typing import Any
from urllib.parse import quote

import httpx2

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.http_validation_error import HTTPValidationError
from ...models.user_group_out import UserGroupOut
from ...types import Response


def _get_kwargs(
    usergroup_id: str,
) -> dict[str, Any]:

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/user-groups/{usergroup_id}".format(
            usergroup_id=quote(str(usergroup_id), safe=""),
        ),
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx2.Response
) -> HTTPValidationError | UserGroupOut | None:
    if response.status_code == 200:
        response_200 = UserGroupOut.from_dict(response.json())

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
) -> Response[HTTPValidationError | UserGroupOut]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    usergroup_id: str,
    *,
    client: AuthenticatedClient,
) -> Response[HTTPValidationError | UserGroupOut]:
    """Get Usergroup

     Get user group

    Args:
        usergroup_id (str): User group ID or usergroup name

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and
        Client.raise_on_unexpected_status is True.
        httpx2.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[HTTPValidationError | UserGroupOut]
    """

    kwargs = _get_kwargs(
        usergroup_id=usergroup_id,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    usergroup_id: str,
    *,
    client: AuthenticatedClient,
) -> HTTPValidationError | UserGroupOut | None:
    """Get Usergroup

     Get user group

    Args:
        usergroup_id (str): User group ID or usergroup name

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and
        Client.raise_on_unexpected_status is True.
        httpx2.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        HTTPValidationError | UserGroupOut
    """

    return sync_detailed(
        usergroup_id=usergroup_id,
        client=client,
    ).parsed


async def asyncio_detailed(
    usergroup_id: str,
    *,
    client: AuthenticatedClient,
) -> Response[HTTPValidationError | UserGroupOut]:
    """Get Usergroup

     Get user group

    Args:
        usergroup_id (str): User group ID or usergroup name

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and
        Client.raise_on_unexpected_status is True.
        httpx2.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[HTTPValidationError | UserGroupOut]
    """

    kwargs = _get_kwargs(
        usergroup_id=usergroup_id,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    usergroup_id: str,
    *,
    client: AuthenticatedClient,
) -> HTTPValidationError | UserGroupOut | None:
    """Get Usergroup

     Get user group

    Args:
        usergroup_id (str): User group ID or usergroup name

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and
        Client.raise_on_unexpected_status is True.
        httpx2.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        HTTPValidationError | UserGroupOut
    """

    return (
        await asyncio_detailed(
            usergroup_id=usergroup_id,
            client=client,
        )
    ).parsed

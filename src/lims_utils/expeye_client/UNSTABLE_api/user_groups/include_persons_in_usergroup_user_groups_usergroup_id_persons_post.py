from http import HTTPStatus
from typing import Any
from urllib.parse import quote

import httpx2

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.http_validation_error import HTTPValidationError
from ...models.paged_user_group_has_person_out import PagedUserGroupHasPersonOut
from ...models.person_list_numeric import PersonListNumeric
from ...models.person_list_str import PersonListStr
from ...models.person_list_uuid import PersonListUuid
from ...types import Response


def _get_kwargs(
    usergroup_id: str,
    *,
    body: PersonListNumeric | PersonListStr | PersonListUuid,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/user-groups/{usergroup_id}/persons".format(
            usergroup_id=quote(str(usergroup_id), safe=""),
        ),
    }

    if isinstance(body, PersonListNumeric):
        _kwargs["json"] = body.to_dict()
    elif isinstance(body, PersonListUuid):
        _kwargs["json"] = body.to_dict()
    else:
        _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx2.Response
) -> HTTPValidationError | PagedUserGroupHasPersonOut | None:
    if response.status_code == 201:
        response_201 = PagedUserGroupHasPersonOut.from_dict(response.json())

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
) -> Response[HTTPValidationError | PagedUserGroupHasPersonOut]:
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
    body: PersonListNumeric | PersonListStr | PersonListUuid,
) -> Response[HTTPValidationError | PagedUserGroupHasPersonOut]:
    """Include Persons In Usergroup

     Add users to user group

    Args:
        usergroup_id (str): User group ID or usergroup name
        body (PersonListNumeric | PersonListStr | PersonListUuid):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx2.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[HTTPValidationError | PagedUserGroupHasPersonOut]
    """

    kwargs = _get_kwargs(
        usergroup_id=usergroup_id,
        body=body,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    usergroup_id: str,
    *,
    client: AuthenticatedClient,
    body: PersonListNumeric | PersonListStr | PersonListUuid,
) -> HTTPValidationError | PagedUserGroupHasPersonOut | None:
    """Include Persons In Usergroup

     Add users to user group

    Args:
        usergroup_id (str): User group ID or usergroup name
        body (PersonListNumeric | PersonListStr | PersonListUuid):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx2.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        HTTPValidationError | PagedUserGroupHasPersonOut
    """

    return sync_detailed(
        usergroup_id=usergroup_id,
        client=client,
        body=body,
    ).parsed


async def asyncio_detailed(
    usergroup_id: str,
    *,
    client: AuthenticatedClient,
    body: PersonListNumeric | PersonListStr | PersonListUuid,
) -> Response[HTTPValidationError | PagedUserGroupHasPersonOut]:
    """Include Persons In Usergroup

     Add users to user group

    Args:
        usergroup_id (str): User group ID or usergroup name
        body (PersonListNumeric | PersonListStr | PersonListUuid):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx2.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[HTTPValidationError | PagedUserGroupHasPersonOut]
    """

    kwargs = _get_kwargs(
        usergroup_id=usergroup_id,
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    usergroup_id: str,
    *,
    client: AuthenticatedClient,
    body: PersonListNumeric | PersonListStr | PersonListUuid,
) -> HTTPValidationError | PagedUserGroupHasPersonOut | None:
    """Include Persons In Usergroup

     Add users to user group

    Args:
        usergroup_id (str): User group ID or usergroup name
        body (PersonListNumeric | PersonListStr | PersonListUuid):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx2.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        HTTPValidationError | PagedUserGroupHasPersonOut
    """

    return (
        await asyncio_detailed(
            usergroup_id=usergroup_id,
            client=client,
            body=body,
        )
    ).parsed

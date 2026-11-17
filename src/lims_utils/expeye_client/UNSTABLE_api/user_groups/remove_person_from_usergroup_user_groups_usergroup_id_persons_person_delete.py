from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx2

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.http_validation_error import HTTPValidationError
from ...models.remove_person_from_usergroup_user_groups_usergroup_id_persons_person_delete_personas import (
    RemovePersonFromUsergroupUserGroupsUsergroupIdPersonsPersonDeletePersonas,
)
from ...types import UNSET, Response


def _get_kwargs(
    usergroup_id: str,
    person: str,
    *,
    person_as: RemovePersonFromUsergroupUserGroupsUsergroupIdPersonsPersonDeletePersonas,
) -> dict[str, Any]:

    params: dict[str, Any] = {}

    json_person_as = person_as.value
    params["personAs"] = json_person_as

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "delete",
        "url": "/user-groups/{usergroup_id}/persons/{person}".format(
            usergroup_id=quote(str(usergroup_id), safe=""),
            person=quote(str(person), safe=""),
        ),
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx2.Response
) -> Any | HTTPValidationError | None:
    if response.status_code == 204:
        response_204 = cast(Any, None)
        return response_204

    if response.status_code == 422:
        response_422 = HTTPValidationError.from_dict(response.json())

        return response_422

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx2.Response
) -> Response[Any | HTTPValidationError]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    usergroup_id: str,
    person: str,
    *,
    client: AuthenticatedClient,
    person_as: RemovePersonFromUsergroupUserGroupsUsergroupIdPersonsPersonDeletePersonas,
) -> Response[Any | HTTPValidationError]:
    """Remove Person From Usergroup

     Remove user from user group

    Args:
        usergroup_id (str): User group ID or usergroup name
        person (str):
        person_as (RemovePersonFromUsergroupUserGroupsUsergroupIdPersonsPersonDeletePersonas):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx2.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | HTTPValidationError]
    """

    kwargs = _get_kwargs(
        usergroup_id=usergroup_id,
        person=person,
        person_as=person_as,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    usergroup_id: str,
    person: str,
    *,
    client: AuthenticatedClient,
    person_as: RemovePersonFromUsergroupUserGroupsUsergroupIdPersonsPersonDeletePersonas,
) -> Any | HTTPValidationError | None:
    """Remove Person From Usergroup

     Remove user from user group

    Args:
        usergroup_id (str): User group ID or usergroup name
        person (str):
        person_as (RemovePersonFromUsergroupUserGroupsUsergroupIdPersonsPersonDeletePersonas):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx2.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | HTTPValidationError
    """

    return sync_detailed(
        usergroup_id=usergroup_id,
        person=person,
        client=client,
        person_as=person_as,
    ).parsed


async def asyncio_detailed(
    usergroup_id: str,
    person: str,
    *,
    client: AuthenticatedClient,
    person_as: RemovePersonFromUsergroupUserGroupsUsergroupIdPersonsPersonDeletePersonas,
) -> Response[Any | HTTPValidationError]:
    """Remove Person From Usergroup

     Remove user from user group

    Args:
        usergroup_id (str): User group ID or usergroup name
        person (str):
        person_as (RemovePersonFromUsergroupUserGroupsUsergroupIdPersonsPersonDeletePersonas):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx2.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | HTTPValidationError]
    """

    kwargs = _get_kwargs(
        usergroup_id=usergroup_id,
        person=person,
        person_as=person_as,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    usergroup_id: str,
    person: str,
    *,
    client: AuthenticatedClient,
    person_as: RemovePersonFromUsergroupUserGroupsUsergroupIdPersonsPersonDeletePersonas,
) -> Any | HTTPValidationError | None:
    """Remove Person From Usergroup

     Remove user from user group

    Args:
        usergroup_id (str): User group ID or usergroup name
        person (str):
        person_as (RemovePersonFromUsergroupUserGroupsUsergroupIdPersonsPersonDeletePersonas):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx2.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | HTTPValidationError
    """

    return (
        await asyncio_detailed(
            usergroup_id=usergroup_id,
            person=person,
            client=client,
            person_as=person_as,
        )
    ).parsed

from http import HTTPStatus
from typing import Any
from urllib.parse import quote
from uuid import UUID

import httpx2

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.http_validation_error import HTTPValidationError
from ...models.person_optional import PersonOptional
from ...models.person_out import PersonOut
from ...types import Response


def _get_kwargs(
    person_id: int | UUID,
    *,
    body: PersonOptional,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "patch",
        "url": "/persons/{person_id}".format(
            person_id=quote(str(person_id), safe=""),
        ),
    }

    _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx2.Response
) -> HTTPValidationError | PersonOut | None:
    if response.status_code == 200:
        response_200 = PersonOut.from_dict(response.json())

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
) -> Response[HTTPValidationError | PersonOut]:
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
    body: PersonOptional,
) -> Response[HTTPValidationError | PersonOut]:
    """Update Person

     Update person

    Args:
        person_id (int | UUID):
        body (PersonOptional):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx2.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[HTTPValidationError | PersonOut]
    """

    kwargs = _get_kwargs(
        person_id=person_id,
        body=body,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    person_id: int | UUID,
    *,
    client: AuthenticatedClient,
    body: PersonOptional,
) -> HTTPValidationError | PersonOut | None:
    """Update Person

     Update person

    Args:
        person_id (int | UUID):
        body (PersonOptional):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx2.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        HTTPValidationError | PersonOut
    """

    return sync_detailed(
        person_id=person_id,
        client=client,
        body=body,
    ).parsed


async def asyncio_detailed(
    person_id: int | UUID,
    *,
    client: AuthenticatedClient,
    body: PersonOptional,
) -> Response[HTTPValidationError | PersonOut]:
    """Update Person

     Update person

    Args:
        person_id (int | UUID):
        body (PersonOptional):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx2.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[HTTPValidationError | PersonOut]
    """

    kwargs = _get_kwargs(
        person_id=person_id,
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    person_id: int | UUID,
    *,
    client: AuthenticatedClient,
    body: PersonOptional,
) -> HTTPValidationError | PersonOut | None:
    """Update Person

     Update person

    Args:
        person_id (int | UUID):
        body (PersonOptional):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx2.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        HTTPValidationError | PersonOut
    """

    return (
        await asyncio_detailed(
            person_id=person_id,
            client=client,
            body=body,
        )
    ).parsed

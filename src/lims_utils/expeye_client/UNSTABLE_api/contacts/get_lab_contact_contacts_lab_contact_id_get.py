from http import HTTPStatus
from typing import Any
from urllib.parse import quote

import httpx2

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.http_validation_error import HTTPValidationError
from ...models.lab_contact_out import LabContactOut
from ...types import Response


def _get_kwargs(
    lab_contact_id: int,
) -> dict[str, Any]:

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/contacts/{lab_contact_id}".format(
            lab_contact_id=quote(str(lab_contact_id), safe=""),
        ),
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx2.Response
) -> HTTPValidationError | LabContactOut | None:
    if response.status_code == 200:
        response_200 = LabContactOut.from_dict(response.json())

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
) -> Response[HTTPValidationError | LabContactOut]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    lab_contact_id: int,
    *,
    client: AuthenticatedClient,
) -> Response[HTTPValidationError | LabContactOut]:
    """Get Lab Contact

     Get lab contact information

    Args:
        lab_contact_id (int):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and
            Client.raise_on_unexpected_status is True.
        httpx2.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[HTTPValidationError | LabContactOut]
    """

    kwargs = _get_kwargs(
        lab_contact_id=lab_contact_id,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    lab_contact_id: int,
    *,
    client: AuthenticatedClient,
) -> HTTPValidationError | LabContactOut | None:
    """Get Lab Contact

     Get lab contact information

    Args:
        lab_contact_id (int):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and
            Client.raise_on_unexpected_status is True.
        httpx2.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        HTTPValidationError | LabContactOut
    """

    return sync_detailed(
        lab_contact_id=lab_contact_id,
        client=client,
    ).parsed


async def asyncio_detailed(
    lab_contact_id: int,
    *,
    client: AuthenticatedClient,
) -> Response[HTTPValidationError | LabContactOut]:
    """Get Lab Contact

     Get lab contact information

    Args:
        lab_contact_id (int):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and
            Client.raise_on_unexpected_status is True.
        httpx2.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[HTTPValidationError | LabContactOut]
    """

    kwargs = _get_kwargs(
        lab_contact_id=lab_contact_id,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    lab_contact_id: int,
    *,
    client: AuthenticatedClient,
) -> HTTPValidationError | LabContactOut | None:
    """Get Lab Contact

     Get lab contact information

    Args:
        lab_contact_id (int):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and
            Client.raise_on_unexpected_status is True.
        httpx2.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        HTTPValidationError | LabContactOut
    """

    return (
        await asyncio_detailed(
            lab_contact_id=lab_contact_id,
            client=client,
        )
    ).parsed

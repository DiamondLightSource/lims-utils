from http import HTTPStatus
from typing import Any
from urllib.parse import quote

import httpx2

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.http_validation_error import HTTPValidationError
from ...models.paged_person_out import PagedPersonOut
from ...models.person_id_with_role import PersonIdWithRole
from ...types import Response


def _get_kwargs(
    proposal_reference: str,
    visit_number: int,
    *,
    body: list[PersonIdWithRole],
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "patch",
        "url": "/proposals/{proposal_reference}/sessions/{visit_number}/persons".format(
            proposal_reference=quote(str(proposal_reference), safe=""),
            visit_number=quote(str(visit_number), safe=""),
        ),
    }

    _kwargs["json"] = []
    for body_item_data in body:
        body_item = body_item_data.to_dict()
        _kwargs["json"].append(body_item)

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
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
    proposal_reference: str,
    visit_number: int,
    *,
    client: AuthenticatedClient,
    body: list[PersonIdWithRole],
) -> Response[HTTPValidationError | PagedPersonOut]:
    """Include Persons In Session

     Create persons in session

    Args:
        proposal_reference (str):
        visit_number (int):
        body (list[PersonIdWithRole]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx2.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[HTTPValidationError | PagedPersonOut]
    """

    kwargs = _get_kwargs(
        proposal_reference=proposal_reference,
        visit_number=visit_number,
        body=body,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    proposal_reference: str,
    visit_number: int,
    *,
    client: AuthenticatedClient,
    body: list[PersonIdWithRole],
) -> HTTPValidationError | PagedPersonOut | None:
    """Include Persons In Session

     Create persons in session

    Args:
        proposal_reference (str):
        visit_number (int):
        body (list[PersonIdWithRole]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx2.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        HTTPValidationError | PagedPersonOut
    """

    return sync_detailed(
        proposal_reference=proposal_reference,
        visit_number=visit_number,
        client=client,
        body=body,
    ).parsed


async def asyncio_detailed(
    proposal_reference: str,
    visit_number: int,
    *,
    client: AuthenticatedClient,
    body: list[PersonIdWithRole],
) -> Response[HTTPValidationError | PagedPersonOut]:
    """Include Persons In Session

     Create persons in session

    Args:
        proposal_reference (str):
        visit_number (int):
        body (list[PersonIdWithRole]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx2.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[HTTPValidationError | PagedPersonOut]
    """

    kwargs = _get_kwargs(
        proposal_reference=proposal_reference,
        visit_number=visit_number,
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    proposal_reference: str,
    visit_number: int,
    *,
    client: AuthenticatedClient,
    body: list[PersonIdWithRole],
) -> HTTPValidationError | PagedPersonOut | None:
    """Include Persons In Session

     Create persons in session

    Args:
        proposal_reference (str):
        visit_number (int):
        body (list[PersonIdWithRole]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx2.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        HTTPValidationError | PagedPersonOut
    """

    return (
        await asyncio_detailed(
            proposal_reference=proposal_reference,
            visit_number=visit_number,
            client=client,
            body=body,
        )
    ).parsed

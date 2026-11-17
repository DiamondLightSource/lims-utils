from http import HTTPStatus
from typing import Any
from urllib.parse import quote

import httpx2

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.http_validation_error import HTTPValidationError
from ...models.protein_with_crystals_in import ProteinWithCrystalsIn
from ...models.protein_with_crystals_out import ProteinWithCrystalsOut
from ...types import UNSET, Response, Unset


def _get_kwargs(
    proposal_reference: str,
    *,
    body: list[ProteinWithCrystalsIn],
    reference_by_name: bool | Unset = False,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    params: dict[str, Any] = {}

    params["referenceByName"] = reference_by_name

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/proposals/{proposal_reference}/crystals".format(
            proposal_reference=quote(str(proposal_reference), safe=""),
        ),
        "params": params,
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
) -> HTTPValidationError | list[ProteinWithCrystalsOut] | None:
    if response.status_code == 201:
        response_201 = []
        _response_201 = response.json()
        for response_201_item_data in _response_201:
            response_201_item = ProteinWithCrystalsOut.from_dict(response_201_item_data)

            response_201.append(response_201_item)

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
) -> Response[HTTPValidationError | list[ProteinWithCrystalsOut]]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    proposal_reference: str,
    *,
    client: AuthenticatedClient,
    body: list[ProteinWithCrystalsIn],
    reference_by_name: bool | Unset = False,
) -> Response[HTTPValidationError | list[ProteinWithCrystalsOut]]:
    """Create Crystals

     Create new shipment and its children from JSON

    Args:
        proposal_reference (str):
        reference_by_name (bool | Unset): Whether to reference proteins by name or ID Default:
            False.
        body (list[ProteinWithCrystalsIn]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx2.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[HTTPValidationError | list[ProteinWithCrystalsOut]]
    """

    kwargs = _get_kwargs(
        proposal_reference=proposal_reference,
        body=body,
        reference_by_name=reference_by_name,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    proposal_reference: str,
    *,
    client: AuthenticatedClient,
    body: list[ProteinWithCrystalsIn],
    reference_by_name: bool | Unset = False,
) -> HTTPValidationError | list[ProteinWithCrystalsOut] | None:
    """Create Crystals

     Create new shipment and its children from JSON

    Args:
        proposal_reference (str):
        reference_by_name (bool | Unset): Whether to reference proteins by name or ID Default:
            False.
        body (list[ProteinWithCrystalsIn]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx2.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        HTTPValidationError | list[ProteinWithCrystalsOut]
    """

    return sync_detailed(
        proposal_reference=proposal_reference,
        client=client,
        body=body,
        reference_by_name=reference_by_name,
    ).parsed


async def asyncio_detailed(
    proposal_reference: str,
    *,
    client: AuthenticatedClient,
    body: list[ProteinWithCrystalsIn],
    reference_by_name: bool | Unset = False,
) -> Response[HTTPValidationError | list[ProteinWithCrystalsOut]]:
    """Create Crystals

     Create new shipment and its children from JSON

    Args:
        proposal_reference (str):
        reference_by_name (bool | Unset): Whether to reference proteins by name or ID Default:
            False.
        body (list[ProteinWithCrystalsIn]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx2.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[HTTPValidationError | list[ProteinWithCrystalsOut]]
    """

    kwargs = _get_kwargs(
        proposal_reference=proposal_reference,
        body=body,
        reference_by_name=reference_by_name,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    proposal_reference: str,
    *,
    client: AuthenticatedClient,
    body: list[ProteinWithCrystalsIn],
    reference_by_name: bool | Unset = False,
) -> HTTPValidationError | list[ProteinWithCrystalsOut] | None:
    """Create Crystals

     Create new shipment and its children from JSON

    Args:
        proposal_reference (str):
        reference_by_name (bool | Unset): Whether to reference proteins by name or ID Default:
            False.
        body (list[ProteinWithCrystalsIn]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx2.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        HTTPValidationError | list[ProteinWithCrystalsOut]
    """

    return (
        await asyncio_detailed(
            proposal_reference=proposal_reference,
            client=client,
            body=body,
            reference_by_name=reference_by_name,
        )
    ).parsed

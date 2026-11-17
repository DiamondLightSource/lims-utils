from http import HTTPStatus
from typing import Any
from urllib.parse import quote

import httpx2

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.http_validation_error import HTTPValidationError
from ...models.registered_dewar_has_proposal_in import RegisteredDewarHasProposalIn
from ...models.registered_dewar_has_proposal_out import RegisteredDewarHasProposalOut
from ...types import UNSET, Response, Unset


def _get_kwargs(
    proposal_reference: str,
    barcode_or_id: int | str,
    *,
    body: RegisteredDewarHasProposalIn,
    is_barcode: bool | Unset = True,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    params: dict[str, Any] = {}

    params["isBarcode"] = is_barcode

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "put",
        "url": "/proposals/{proposal_reference}/dewar-registry/{barcode_or_id}".format(
            proposal_reference=quote(str(proposal_reference), safe=""),
            barcode_or_id=quote(str(barcode_or_id), safe=""),
        ),
        "params": params,
    }

    _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx2.Response
) -> HTTPValidationError | RegisteredDewarHasProposalOut | None:
    if response.status_code == 200:
        response_200 = RegisteredDewarHasProposalOut.from_dict(response.json())

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
) -> Response[HTTPValidationError | RegisteredDewarHasProposalOut]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    proposal_reference: str,
    barcode_or_id: int | str,
    *,
    client: AuthenticatedClient,
    body: RegisteredDewarHasProposalIn,
    is_barcode: bool | Unset = True,
) -> Response[HTTPValidationError | RegisteredDewarHasProposalOut]:
    """Create Dewar Registry Has Proposal Entry

     Create/update dewar registry entry's relationship to a proposal

    Args:
        proposal_reference (str):
        barcode_or_id (int | str):
        is_barcode (bool | Unset):  Default: True.
        body (RegisteredDewarHasProposalIn):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and
            Client.raise_on_unexpected_status is True.
        httpx2.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[HTTPValidationError | RegisteredDewarHasProposalOut]
    """

    kwargs = _get_kwargs(
        proposal_reference=proposal_reference,
        barcode_or_id=barcode_or_id,
        body=body,
        is_barcode=is_barcode,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    proposal_reference: str,
    barcode_or_id: int | str,
    *,
    client: AuthenticatedClient,
    body: RegisteredDewarHasProposalIn,
    is_barcode: bool | Unset = True,
) -> HTTPValidationError | RegisteredDewarHasProposalOut | None:
    """Create Dewar Registry Has Proposal Entry

     Create/update dewar registry entry's relationship to a proposal

    Args:
        proposal_reference (str):
        barcode_or_id (int | str):
        is_barcode (bool | Unset):  Default: True.
        body (RegisteredDewarHasProposalIn):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and
            Client.raise_on_unexpected_status is True.
        httpx2.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        HTTPValidationError | RegisteredDewarHasProposalOut
    """

    return sync_detailed(
        proposal_reference=proposal_reference,
        barcode_or_id=barcode_or_id,
        client=client,
        body=body,
        is_barcode=is_barcode,
    ).parsed


async def asyncio_detailed(
    proposal_reference: str,
    barcode_or_id: int | str,
    *,
    client: AuthenticatedClient,
    body: RegisteredDewarHasProposalIn,
    is_barcode: bool | Unset = True,
) -> Response[HTTPValidationError | RegisteredDewarHasProposalOut]:
    """Create Dewar Registry Has Proposal Entry

     Create/update dewar registry entry's relationship to a proposal

    Args:
        proposal_reference (str):
        barcode_or_id (int | str):
        is_barcode (bool | Unset):  Default: True.
        body (RegisteredDewarHasProposalIn):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and
            Client.raise_on_unexpected_status is True.
        httpx2.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[HTTPValidationError | RegisteredDewarHasProposalOut]
    """

    kwargs = _get_kwargs(
        proposal_reference=proposal_reference,
        barcode_or_id=barcode_or_id,
        body=body,
        is_barcode=is_barcode,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    proposal_reference: str,
    barcode_or_id: int | str,
    *,
    client: AuthenticatedClient,
    body: RegisteredDewarHasProposalIn,
    is_barcode: bool | Unset = True,
) -> HTTPValidationError | RegisteredDewarHasProposalOut | None:
    """Create Dewar Registry Has Proposal Entry

     Create/update dewar registry entry's relationship to a proposal

    Args:
        proposal_reference (str):
        barcode_or_id (int | str):
        is_barcode (bool | Unset):  Default: True.
        body (RegisteredDewarHasProposalIn):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and
            Client.raise_on_unexpected_status is True.
        httpx2.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        HTTPValidationError | RegisteredDewarHasProposalOut
    """

    return (
        await asyncio_detailed(
            proposal_reference=proposal_reference,
            barcode_or_id=barcode_or_id,
            client=client,
            body=body,
            is_barcode=is_barcode,
        )
    ).parsed

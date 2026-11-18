from http import HTTPStatus
from typing import Any
from urllib.parse import quote

import httpx2

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.http_validation_error import HTTPValidationError
from ...models.registered_container_has_proposal_in import RegisteredContainerHasProposalIn
from ...models.registered_container_has_proposal_out import RegisteredContainerHasProposalOut
from ...types import UNSET, Response, Unset


def _get_kwargs(
    proposal_reference: str,
    barcode_or_id: int | str,
    *,
    body: RegisteredContainerHasProposalIn,
    is_barcode: bool | Unset = True,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    params: dict[str, Any] = {}

    params["isBarcode"] = is_barcode

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/proposals/{proposal_reference}/container-registry/{barcode_or_id}".format(
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
) -> HTTPValidationError | RegisteredContainerHasProposalOut | None:
    if response.status_code == 201:
        response_201 = RegisteredContainerHasProposalOut.from_dict(response.json())

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
) -> Response[HTTPValidationError | RegisteredContainerHasProposalOut]:
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
    body: RegisteredContainerHasProposalIn,
    is_barcode: bool | Unset = True,
) -> Response[HTTPValidationError | RegisteredContainerHasProposalOut]:
    """Create Container Registry Has Proposal Entry

     Assign container registry entry to proposal

    Args:
        proposal_reference (str):
        barcode_or_id (int | str):
        is_barcode (bool | Unset):  Default: True.
        body (RegisteredContainerHasProposalIn):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and
        Client.raise_on_unexpected_status is True.
        httpx2.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[HTTPValidationError | RegisteredContainerHasProposalOut]
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
    body: RegisteredContainerHasProposalIn,
    is_barcode: bool | Unset = True,
) -> HTTPValidationError | RegisteredContainerHasProposalOut | None:
    """Create Container Registry Has Proposal Entry

     Assign container registry entry to proposal

    Args:
        proposal_reference (str):
        barcode_or_id (int | str):
        is_barcode (bool | Unset):  Default: True.
        body (RegisteredContainerHasProposalIn):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and
        Client.raise_on_unexpected_status is True.
        httpx2.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        HTTPValidationError | RegisteredContainerHasProposalOut
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
    body: RegisteredContainerHasProposalIn,
    is_barcode: bool | Unset = True,
) -> Response[HTTPValidationError | RegisteredContainerHasProposalOut]:
    """Create Container Registry Has Proposal Entry

     Assign container registry entry to proposal

    Args:
        proposal_reference (str):
        barcode_or_id (int | str):
        is_barcode (bool | Unset):  Default: True.
        body (RegisteredContainerHasProposalIn):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and
        Client.raise_on_unexpected_status is True.
        httpx2.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[HTTPValidationError | RegisteredContainerHasProposalOut]
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
    body: RegisteredContainerHasProposalIn,
    is_barcode: bool | Unset = True,
) -> HTTPValidationError | RegisteredContainerHasProposalOut | None:
    """Create Container Registry Has Proposal Entry

     Assign container registry entry to proposal

    Args:
        proposal_reference (str):
        barcode_or_id (int | str):
        is_barcode (bool | Unset):  Default: True.
        body (RegisteredContainerHasProposalIn):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and
        Client.raise_on_unexpected_status is True.
        httpx2.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        HTTPValidationError | RegisteredContainerHasProposalOut
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

from http import HTTPStatus
from typing import Any

import httpx2

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.body_create_full_shipment_from_file import BodyCreateFullShipmentFromFile
from ...models.http_validation_error import HTTPValidationError
from ...models.proposal_with_children_out import ProposalWithChildrenOut
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    body: BodyCreateFullShipmentFromFile | Unset = UNSET,
    queue_container: bool | Unset = False,
    allow_missing_facility_code: bool | Unset = False,
    reuse_shipments: bool | Unset = False,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    params: dict[str, Any] = {}

    params["queueContainer"] = queue_container

    params["allowMissingFacilityCode"] = allow_missing_facility_code

    params["reuseShipments"] = reuse_shipments

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/shipments/upload",
        "params": params,
    }

    if not isinstance(body, Unset):
        _kwargs["files"] = body.to_multipart()

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx2.Response
) -> HTTPValidationError | ProposalWithChildrenOut | None:
    if response.status_code == 201:
        response_201 = ProposalWithChildrenOut.from_dict(response.json())

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
) -> Response[HTTPValidationError | ProposalWithChildrenOut]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient,
    body: BodyCreateFullShipmentFromFile | Unset = UNSET,
    queue_container: bool | Unset = False,
    allow_missing_facility_code: bool | Unset = False,
    reuse_shipments: bool | Unset = False,
) -> Response[HTTPValidationError | ProposalWithChildrenOut]:
    """Create Full Shipment From File

     Create new full shipment from file

    Args:
        queue_container (bool | Unset): Queue container for UDC Default: False.
        allow_missing_facility_code (bool | Unset): Ignore facility code if it's not provided or
            invalid Default: False.
        reuse_shipments (bool | Unset): Reuse existing shipments/dewars if they match the provided
            shipments/dewars in the file Default: False.
        body (BodyCreateFullShipmentFromFile | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and
        Client.raise_on_unexpected_status is True.
        httpx2.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[HTTPValidationError | ProposalWithChildrenOut]
    """

    kwargs = _get_kwargs(
        body=body,
        queue_container=queue_container,
        allow_missing_facility_code=allow_missing_facility_code,
        reuse_shipments=reuse_shipments,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: AuthenticatedClient,
    body: BodyCreateFullShipmentFromFile | Unset = UNSET,
    queue_container: bool | Unset = False,
    allow_missing_facility_code: bool | Unset = False,
    reuse_shipments: bool | Unset = False,
) -> HTTPValidationError | ProposalWithChildrenOut | None:
    """Create Full Shipment From File

     Create new full shipment from file

    Args:
        queue_container (bool | Unset): Queue container for UDC Default: False.
        allow_missing_facility_code (bool | Unset): Ignore facility code if it's not provided or
            invalid Default: False.
        reuse_shipments (bool | Unset): Reuse existing shipments/dewars if they match the provided
            shipments/dewars in the file Default: False.
        body (BodyCreateFullShipmentFromFile | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and
        Client.raise_on_unexpected_status is True.
        httpx2.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        HTTPValidationError | ProposalWithChildrenOut
    """

    return sync_detailed(
        client=client,
        body=body,
        queue_container=queue_container,
        allow_missing_facility_code=allow_missing_facility_code,
        reuse_shipments=reuse_shipments,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    body: BodyCreateFullShipmentFromFile | Unset = UNSET,
    queue_container: bool | Unset = False,
    allow_missing_facility_code: bool | Unset = False,
    reuse_shipments: bool | Unset = False,
) -> Response[HTTPValidationError | ProposalWithChildrenOut]:
    """Create Full Shipment From File

     Create new full shipment from file

    Args:
        queue_container (bool | Unset): Queue container for UDC Default: False.
        allow_missing_facility_code (bool | Unset): Ignore facility code if it's not provided or
            invalid Default: False.
        reuse_shipments (bool | Unset): Reuse existing shipments/dewars if they match the provided
            shipments/dewars in the file Default: False.
        body (BodyCreateFullShipmentFromFile | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and
        Client.raise_on_unexpected_status is True.
        httpx2.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[HTTPValidationError | ProposalWithChildrenOut]
    """

    kwargs = _get_kwargs(
        body=body,
        queue_container=queue_container,
        allow_missing_facility_code=allow_missing_facility_code,
        reuse_shipments=reuse_shipments,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient,
    body: BodyCreateFullShipmentFromFile | Unset = UNSET,
    queue_container: bool | Unset = False,
    allow_missing_facility_code: bool | Unset = False,
    reuse_shipments: bool | Unset = False,
) -> HTTPValidationError | ProposalWithChildrenOut | None:
    """Create Full Shipment From File

     Create new full shipment from file

    Args:
        queue_container (bool | Unset): Queue container for UDC Default: False.
        allow_missing_facility_code (bool | Unset): Ignore facility code if it's not provided or
            invalid Default: False.
        reuse_shipments (bool | Unset): Reuse existing shipments/dewars if they match the provided
            shipments/dewars in the file Default: False.
        body (BodyCreateFullShipmentFromFile | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and
        Client.raise_on_unexpected_status is True.
        httpx2.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        HTTPValidationError | ProposalWithChildrenOut
    """

    return (
        await asyncio_detailed(
            client=client,
            body=body,
            queue_container=queue_container,
            allow_missing_facility_code=allow_missing_facility_code,
            reuse_shipments=reuse_shipments,
        )
    ).parsed

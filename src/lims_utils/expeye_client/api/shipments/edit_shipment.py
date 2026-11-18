from http import HTTPStatus
from typing import Any
from urllib.parse import quote

import httpx2

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.http_validation_error import HTTPValidationError
from ...models.shipment_optional import ShipmentOptional
from ...models.shipment_out import ShipmentOut
from ...types import Response


def _get_kwargs(
    shipment_id: int,
    *,
    body: ShipmentOptional,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "patch",
        "url": "/shipments/{shipment_id}".format(
            shipment_id=quote(str(shipment_id), safe=""),
        ),
    }

    _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx2.Response
) -> HTTPValidationError | ShipmentOut | None:
    if response.status_code == 200:
        response_200 = ShipmentOut.from_dict(response.json())

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
) -> Response[HTTPValidationError | ShipmentOut]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    shipment_id: int,
    *,
    client: AuthenticatedClient,
    body: ShipmentOptional,
) -> Response[HTTPValidationError | ShipmentOut]:
    """Edit Shipment

     Edit shipment

    Args:
        shipment_id (int):
        body (ShipmentOptional):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and
        Client.raise_on_unexpected_status is True.
        httpx2.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[HTTPValidationError | ShipmentOut]
    """

    kwargs = _get_kwargs(
        shipment_id=shipment_id,
        body=body,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    shipment_id: int,
    *,
    client: AuthenticatedClient,
    body: ShipmentOptional,
) -> HTTPValidationError | ShipmentOut | None:
    """Edit Shipment

     Edit shipment

    Args:
        shipment_id (int):
        body (ShipmentOptional):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and
        Client.raise_on_unexpected_status is True.
        httpx2.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        HTTPValidationError | ShipmentOut
    """

    return sync_detailed(
        shipment_id=shipment_id,
        client=client,
        body=body,
    ).parsed


async def asyncio_detailed(
    shipment_id: int,
    *,
    client: AuthenticatedClient,
    body: ShipmentOptional,
) -> Response[HTTPValidationError | ShipmentOut]:
    """Edit Shipment

     Edit shipment

    Args:
        shipment_id (int):
        body (ShipmentOptional):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and
        Client.raise_on_unexpected_status is True.
        httpx2.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[HTTPValidationError | ShipmentOut]
    """

    kwargs = _get_kwargs(
        shipment_id=shipment_id,
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    shipment_id: int,
    *,
    client: AuthenticatedClient,
    body: ShipmentOptional,
) -> HTTPValidationError | ShipmentOut | None:
    """Edit Shipment

     Edit shipment

    Args:
        shipment_id (int):
        body (ShipmentOptional):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and
        Client.raise_on_unexpected_status is True.
        httpx2.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        HTTPValidationError | ShipmentOut
    """

    return (
        await asyncio_detailed(
            shipment_id=shipment_id,
            client=client,
            body=body,
        )
    ).parsed

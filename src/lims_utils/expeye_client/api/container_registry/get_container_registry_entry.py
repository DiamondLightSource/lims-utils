from http import HTTPStatus
from typing import Any
from urllib.parse import quote

import httpx2

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.http_validation_error import HTTPValidationError
from ...models.registered_container_out import RegisteredContainerOut
from ...types import UNSET, Response, Unset


def _get_kwargs(
    barcode_or_id: int | str,
    *,
    is_barcode: bool | Unset = True,
) -> dict[str, Any]:

    params: dict[str, Any] = {}

    params["isBarcode"] = is_barcode

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/container-registry/{barcode_or_id}".format(
            barcode_or_id=quote(str(barcode_or_id), safe=""),
        ),
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx2.Response
) -> HTTPValidationError | RegisteredContainerOut | None:
    if response.status_code == 200:
        response_200 = RegisteredContainerOut.from_dict(response.json())

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
) -> Response[HTTPValidationError | RegisteredContainerOut]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    barcode_or_id: int | str,
    *,
    client: AuthenticatedClient,
    is_barcode: bool | Unset = True,
) -> Response[HTTPValidationError | RegisteredContainerOut]:
    """Get Container Registry Entry

     Get container registry information

    Args:
        barcode_or_id (int | str):
        is_barcode (bool | Unset):  Default: True.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and
        Client.raise_on_unexpected_status is True.
        httpx2.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[HTTPValidationError | RegisteredContainerOut]
    """

    kwargs = _get_kwargs(
        barcode_or_id=barcode_or_id,
        is_barcode=is_barcode,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    barcode_or_id: int | str,
    *,
    client: AuthenticatedClient,
    is_barcode: bool | Unset = True,
) -> HTTPValidationError | RegisteredContainerOut | None:
    """Get Container Registry Entry

     Get container registry information

    Args:
        barcode_or_id (int | str):
        is_barcode (bool | Unset):  Default: True.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and
        Client.raise_on_unexpected_status is True.
        httpx2.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        HTTPValidationError | RegisteredContainerOut
    """

    return sync_detailed(
        barcode_or_id=barcode_or_id,
        client=client,
        is_barcode=is_barcode,
    ).parsed


async def asyncio_detailed(
    barcode_or_id: int | str,
    *,
    client: AuthenticatedClient,
    is_barcode: bool | Unset = True,
) -> Response[HTTPValidationError | RegisteredContainerOut]:
    """Get Container Registry Entry

     Get container registry information

    Args:
        barcode_or_id (int | str):
        is_barcode (bool | Unset):  Default: True.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and
        Client.raise_on_unexpected_status is True.
        httpx2.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[HTTPValidationError | RegisteredContainerOut]
    """

    kwargs = _get_kwargs(
        barcode_or_id=barcode_or_id,
        is_barcode=is_barcode,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    barcode_or_id: int | str,
    *,
    client: AuthenticatedClient,
    is_barcode: bool | Unset = True,
) -> HTTPValidationError | RegisteredContainerOut | None:
    """Get Container Registry Entry

     Get container registry information

    Args:
        barcode_or_id (int | str):
        is_barcode (bool | Unset):  Default: True.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and
        Client.raise_on_unexpected_status is True.
        httpx2.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        HTTPValidationError | RegisteredContainerOut
    """

    return (
        await asyncio_detailed(
            barcode_or_id=barcode_or_id,
            client=client,
            is_barcode=is_barcode,
        )
    ).parsed

from http import HTTPStatus
from typing import Any
from urllib.parse import quote

import httpx2

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.container_inspection_optional import ContainerInspectionOptional
from ...models.container_inspection_out import ContainerInspectionOut
from ...models.http_validation_error import HTTPValidationError
from ...types import Response


def _get_kwargs(
    container_inspection_id: int,
    *,
    body: ContainerInspectionOptional,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "patch",
        "url": "/container-inspections/{container_inspection_id}".format(
            container_inspection_id=quote(str(container_inspection_id), safe=""),
        ),
    }

    _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx2.Response
) -> ContainerInspectionOut | HTTPValidationError | None:
    if response.status_code == 200:
        response_200 = ContainerInspectionOut.from_dict(response.json())

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
) -> Response[ContainerInspectionOut | HTTPValidationError]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    container_inspection_id: int,
    *,
    client: AuthenticatedClient,
    body: ContainerInspectionOptional,
) -> Response[ContainerInspectionOut | HTTPValidationError]:
    """Update Container Inspection

     Update container inspection entry

    Args:
        container_inspection_id (int):
        body (ContainerInspectionOptional):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx2.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ContainerInspectionOut | HTTPValidationError]
    """

    kwargs = _get_kwargs(
        container_inspection_id=container_inspection_id,
        body=body,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    container_inspection_id: int,
    *,
    client: AuthenticatedClient,
    body: ContainerInspectionOptional,
) -> ContainerInspectionOut | HTTPValidationError | None:
    """Update Container Inspection

     Update container inspection entry

    Args:
        container_inspection_id (int):
        body (ContainerInspectionOptional):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx2.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ContainerInspectionOut | HTTPValidationError
    """

    return sync_detailed(
        container_inspection_id=container_inspection_id,
        client=client,
        body=body,
    ).parsed


async def asyncio_detailed(
    container_inspection_id: int,
    *,
    client: AuthenticatedClient,
    body: ContainerInspectionOptional,
) -> Response[ContainerInspectionOut | HTTPValidationError]:
    """Update Container Inspection

     Update container inspection entry

    Args:
        container_inspection_id (int):
        body (ContainerInspectionOptional):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx2.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ContainerInspectionOut | HTTPValidationError]
    """

    kwargs = _get_kwargs(
        container_inspection_id=container_inspection_id,
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    container_inspection_id: int,
    *,
    client: AuthenticatedClient,
    body: ContainerInspectionOptional,
) -> ContainerInspectionOut | HTTPValidationError | None:
    """Update Container Inspection

     Update container inspection entry

    Args:
        container_inspection_id (int):
        body (ContainerInspectionOptional):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx2.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ContainerInspectionOut | HTTPValidationError
    """

    return (
        await asyncio_detailed(
            container_inspection_id=container_inspection_id,
            client=client,
            body=body,
        )
    ).parsed

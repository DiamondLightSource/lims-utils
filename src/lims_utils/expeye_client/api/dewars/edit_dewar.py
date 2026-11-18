from http import HTTPStatus
from typing import Any
from urllib.parse import quote

import httpx2

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.dewar_optional import DewarOptional
from ...models.dewar_out import DewarOut
from ...models.http_validation_error import HTTPValidationError
from ...types import UNSET, Response, Unset


def _get_kwargs(
    dewar_id: int,
    *,
    body: DewarOptional,
    merge_json: bool | Unset = False,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    params: dict[str, Any] = {}

    params["mergeJson"] = merge_json

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "patch",
        "url": "/dewars/{dewar_id}".format(
            dewar_id=quote(str(dewar_id), safe=""),
        ),
        "params": params,
    }

    _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx2.Response
) -> DewarOut | HTTPValidationError | None:
    if response.status_code == 200:
        response_200 = DewarOut.from_dict(response.json())

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
) -> Response[DewarOut | HTTPValidationError]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    dewar_id: int,
    *,
    client: AuthenticatedClient,
    body: DewarOptional,
    merge_json: bool | Unset = False,
) -> Response[DewarOut | HTTPValidationError]:
    """Edit Dewar

     Edit dewar

    Args:
        dewar_id (int):
        merge_json (bool | Unset): Merge JSON in comments field instead of replacing Default:
            False.
        body (DewarOptional):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and
        Client.raise_on_unexpected_status is True.
        httpx2.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[DewarOut | HTTPValidationError]
    """

    kwargs = _get_kwargs(
        dewar_id=dewar_id,
        body=body,
        merge_json=merge_json,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    dewar_id: int,
    *,
    client: AuthenticatedClient,
    body: DewarOptional,
    merge_json: bool | Unset = False,
) -> DewarOut | HTTPValidationError | None:
    """Edit Dewar

     Edit dewar

    Args:
        dewar_id (int):
        merge_json (bool | Unset): Merge JSON in comments field instead of replacing Default:
            False.
        body (DewarOptional):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and
        Client.raise_on_unexpected_status is True.
        httpx2.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        DewarOut | HTTPValidationError
    """

    return sync_detailed(
        dewar_id=dewar_id,
        client=client,
        body=body,
        merge_json=merge_json,
    ).parsed


async def asyncio_detailed(
    dewar_id: int,
    *,
    client: AuthenticatedClient,
    body: DewarOptional,
    merge_json: bool | Unset = False,
) -> Response[DewarOut | HTTPValidationError]:
    """Edit Dewar

     Edit dewar

    Args:
        dewar_id (int):
        merge_json (bool | Unset): Merge JSON in comments field instead of replacing Default:
            False.
        body (DewarOptional):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and
        Client.raise_on_unexpected_status is True.
        httpx2.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[DewarOut | HTTPValidationError]
    """

    kwargs = _get_kwargs(
        dewar_id=dewar_id,
        body=body,
        merge_json=merge_json,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    dewar_id: int,
    *,
    client: AuthenticatedClient,
    body: DewarOptional,
    merge_json: bool | Unset = False,
) -> DewarOut | HTTPValidationError | None:
    """Edit Dewar

     Edit dewar

    Args:
        dewar_id (int):
        merge_json (bool | Unset): Merge JSON in comments field instead of replacing Default:
            False.
        body (DewarOptional):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and
        Client.raise_on_unexpected_status is True.
        httpx2.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        DewarOut | HTTPValidationError
    """

    return (
        await asyncio_detailed(
            dewar_id=dewar_id,
            client=client,
            body=body,
            merge_json=merge_json,
        )
    ).parsed

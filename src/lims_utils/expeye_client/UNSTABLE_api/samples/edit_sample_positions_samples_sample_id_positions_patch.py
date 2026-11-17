from http import HTTPStatus
from typing import Any
from urllib.parse import quote

import httpx2

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.http_validation_error import HTTPValidationError
from ...models.paged_sample_position_out import PagedSamplePositionOut
from ...models.sample_position_optional import SamplePositionOptional
from ...types import UNSET, Response, Unset


def _get_kwargs(
    sample_id: int,
    *,
    body: SamplePositionOptional,
    position_type: None | str | Unset = UNSET,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    params: dict[str, Any] = {}

    json_position_type: None | str | Unset
    if isinstance(position_type, Unset):
        json_position_type = UNSET
    else:
        json_position_type = position_type
    params["positionType"] = json_position_type

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "patch",
        "url": "/samples/{sample_id}/positions".format(
            sample_id=quote(str(sample_id), safe=""),
        ),
        "params": params,
    }

    _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx2.Response
) -> HTTPValidationError | PagedSamplePositionOut | None:
    if response.status_code == 200:
        response_200 = PagedSamplePositionOut.from_dict(response.json())

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
) -> Response[HTTPValidationError | PagedSamplePositionOut]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    sample_id: int,
    *,
    client: AuthenticatedClient,
    body: SamplePositionOptional,
    position_type: None | str | Unset = UNSET,
) -> Response[HTTPValidationError | PagedSamplePositionOut]:
    """Edit Sample Positions

     Edit multiple sample positions in a sample simultaneously

    Args:
        sample_id (int):
        position_type (None | str | Unset):
        body (SamplePositionOptional):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and
            Client.raise_on_unexpected_status is True.
        httpx2.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[HTTPValidationError | PagedSamplePositionOut]
    """

    kwargs = _get_kwargs(
        sample_id=sample_id,
        body=body,
        position_type=position_type,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    sample_id: int,
    *,
    client: AuthenticatedClient,
    body: SamplePositionOptional,
    position_type: None | str | Unset = UNSET,
) -> HTTPValidationError | PagedSamplePositionOut | None:
    """Edit Sample Positions

     Edit multiple sample positions in a sample simultaneously

    Args:
        sample_id (int):
        position_type (None | str | Unset):
        body (SamplePositionOptional):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and
            Client.raise_on_unexpected_status is True.
        httpx2.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        HTTPValidationError | PagedSamplePositionOut
    """

    return sync_detailed(
        sample_id=sample_id,
        client=client,
        body=body,
        position_type=position_type,
    ).parsed


async def asyncio_detailed(
    sample_id: int,
    *,
    client: AuthenticatedClient,
    body: SamplePositionOptional,
    position_type: None | str | Unset = UNSET,
) -> Response[HTTPValidationError | PagedSamplePositionOut]:
    """Edit Sample Positions

     Edit multiple sample positions in a sample simultaneously

    Args:
        sample_id (int):
        position_type (None | str | Unset):
        body (SamplePositionOptional):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and
            Client.raise_on_unexpected_status is True.
        httpx2.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[HTTPValidationError | PagedSamplePositionOut]
    """

    kwargs = _get_kwargs(
        sample_id=sample_id,
        body=body,
        position_type=position_type,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    sample_id: int,
    *,
    client: AuthenticatedClient,
    body: SamplePositionOptional,
    position_type: None | str | Unset = UNSET,
) -> HTTPValidationError | PagedSamplePositionOut | None:
    """Edit Sample Positions

     Edit multiple sample positions in a sample simultaneously

    Args:
        sample_id (int):
        position_type (None | str | Unset):
        body (SamplePositionOptional):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and
            Client.raise_on_unexpected_status is True.
        httpx2.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        HTTPValidationError | PagedSamplePositionOut
    """

    return (
        await asyncio_detailed(
            sample_id=sample_id,
            client=client,
            body=body,
            position_type=position_type,
        )
    ).parsed

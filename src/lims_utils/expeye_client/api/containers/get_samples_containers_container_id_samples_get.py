from http import HTTPStatus
from typing import Any
from urllib.parse import quote

import httpx2

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.http_validation_error import HTTPValidationError
from ...models.paged_sample_out import PagedSampleOut
from ...types import UNSET, Response, Unset


def _get_kwargs(
    container_id: int,
    *,
    loaded: bool | None | Unset = UNSET,
    is_in_sample_changer: bool | None | Unset = UNSET,
    page: int | Unset = 0,
    limit: int | Unset = 25,
) -> dict[str, Any]:

    params: dict[str, Any] = {}

    json_loaded: bool | None | Unset
    if isinstance(loaded, Unset):
        json_loaded = UNSET
    else:
        json_loaded = loaded
    params["loaded"] = json_loaded

    json_is_in_sample_changer: bool | None | Unset
    if isinstance(is_in_sample_changer, Unset):
        json_is_in_sample_changer = UNSET
    else:
        json_is_in_sample_changer = is_in_sample_changer
    params["isInSampleChanger"] = json_is_in_sample_changer

    params["page"] = page

    params["limit"] = limit

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/containers/{container_id}/samples".format(
            container_id=quote(str(container_id), safe=""),
        ),
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx2.Response
) -> HTTPValidationError | PagedSampleOut | None:
    if response.status_code == 200:
        response_200 = PagedSampleOut.from_dict(response.json())

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
) -> Response[HTTPValidationError | PagedSampleOut]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    container_id: int,
    *,
    client: AuthenticatedClient,
    loaded: bool | None | Unset = UNSET,
    is_in_sample_changer: bool | None | Unset = UNSET,
    page: int | Unset = 0,
    limit: int | Unset = 25,
) -> Response[HTTPValidationError | PagedSampleOut]:
    """Get Samples

     Get samples in container

    Args:
        container_id (int):
        loaded (bool | None | Unset): Only return samples have been/have not been loaded into the
            beamline(i.e. have a RobotAction entry or not)
        is_in_sample_changer (bool | None | Unset):
        page (int | Unset): Page number/Results to skip. Negative numbers count backwards from the
            last page Default: 0.
        limit (int | Unset): Number of results to show Default: 25.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx2.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[HTTPValidationError | PagedSampleOut]
    """

    kwargs = _get_kwargs(
        container_id=container_id,
        loaded=loaded,
        is_in_sample_changer=is_in_sample_changer,
        page=page,
        limit=limit,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    container_id: int,
    *,
    client: AuthenticatedClient,
    loaded: bool | None | Unset = UNSET,
    is_in_sample_changer: bool | None | Unset = UNSET,
    page: int | Unset = 0,
    limit: int | Unset = 25,
) -> HTTPValidationError | PagedSampleOut | None:
    """Get Samples

     Get samples in container

    Args:
        container_id (int):
        loaded (bool | None | Unset): Only return samples have been/have not been loaded into the
            beamline(i.e. have a RobotAction entry or not)
        is_in_sample_changer (bool | None | Unset):
        page (int | Unset): Page number/Results to skip. Negative numbers count backwards from the
            last page Default: 0.
        limit (int | Unset): Number of results to show Default: 25.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx2.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        HTTPValidationError | PagedSampleOut
    """

    return sync_detailed(
        container_id=container_id,
        client=client,
        loaded=loaded,
        is_in_sample_changer=is_in_sample_changer,
        page=page,
        limit=limit,
    ).parsed


async def asyncio_detailed(
    container_id: int,
    *,
    client: AuthenticatedClient,
    loaded: bool | None | Unset = UNSET,
    is_in_sample_changer: bool | None | Unset = UNSET,
    page: int | Unset = 0,
    limit: int | Unset = 25,
) -> Response[HTTPValidationError | PagedSampleOut]:
    """Get Samples

     Get samples in container

    Args:
        container_id (int):
        loaded (bool | None | Unset): Only return samples have been/have not been loaded into the
            beamline(i.e. have a RobotAction entry or not)
        is_in_sample_changer (bool | None | Unset):
        page (int | Unset): Page number/Results to skip. Negative numbers count backwards from the
            last page Default: 0.
        limit (int | Unset): Number of results to show Default: 25.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx2.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[HTTPValidationError | PagedSampleOut]
    """

    kwargs = _get_kwargs(
        container_id=container_id,
        loaded=loaded,
        is_in_sample_changer=is_in_sample_changer,
        page=page,
        limit=limit,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    container_id: int,
    *,
    client: AuthenticatedClient,
    loaded: bool | None | Unset = UNSET,
    is_in_sample_changer: bool | None | Unset = UNSET,
    page: int | Unset = 0,
    limit: int | Unset = 25,
) -> HTTPValidationError | PagedSampleOut | None:
    """Get Samples

     Get samples in container

    Args:
        container_id (int):
        loaded (bool | None | Unset): Only return samples have been/have not been loaded into the
            beamline(i.e. have a RobotAction entry or not)
        is_in_sample_changer (bool | None | Unset):
        page (int | Unset): Page number/Results to skip. Negative numbers count backwards from the
            last page Default: 0.
        limit (int | Unset): Number of results to show Default: 25.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx2.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        HTTPValidationError | PagedSampleOut
    """

    return (
        await asyncio_detailed(
            container_id=container_id,
            client=client,
            loaded=loaded,
            is_in_sample_changer=is_in_sample_changer,
            page=page,
            limit=limit,
        )
    ).parsed

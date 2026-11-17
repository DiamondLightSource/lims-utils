from http import HTTPStatus
from typing import Any
from urllib.parse import quote

import httpx2

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.http_validation_error import HTTPValidationError
from ...models.paged_image_quality_indicator_out import PagedImageQualityIndicatorOut
from ...types import Response


def _get_kwargs(
    data_collection_id: int,
) -> dict[str, Any]:

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/data-collections/{data_collection_id}/image-quality-indicators".format(
            data_collection_id=quote(str(data_collection_id), safe=""),
        ),
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx2.Response
) -> HTTPValidationError | PagedImageQualityIndicatorOut | None:
    if response.status_code == 200:
        response_200 = PagedImageQualityIndicatorOut.from_dict(response.json())

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
) -> Response[HTTPValidationError | PagedImageQualityIndicatorOut]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    data_collection_id: int,
    *,
    client: AuthenticatedClient,
) -> Response[HTTPValidationError | PagedImageQualityIndicatorOut]:
    """Get Image Quality Indicators

     Get image quality indicators

    Args:
        data_collection_id (int):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and
            Client.raise_on_unexpected_status is True.
        httpx2.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[HTTPValidationError | PagedImageQualityIndicatorOut]
    """

    kwargs = _get_kwargs(
        data_collection_id=data_collection_id,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    data_collection_id: int,
    *,
    client: AuthenticatedClient,
) -> HTTPValidationError | PagedImageQualityIndicatorOut | None:
    """Get Image Quality Indicators

     Get image quality indicators

    Args:
        data_collection_id (int):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and
            Client.raise_on_unexpected_status is True.
        httpx2.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        HTTPValidationError | PagedImageQualityIndicatorOut
    """

    return sync_detailed(
        data_collection_id=data_collection_id,
        client=client,
    ).parsed


async def asyncio_detailed(
    data_collection_id: int,
    *,
    client: AuthenticatedClient,
) -> Response[HTTPValidationError | PagedImageQualityIndicatorOut]:
    """Get Image Quality Indicators

     Get image quality indicators

    Args:
        data_collection_id (int):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and
            Client.raise_on_unexpected_status is True.
        httpx2.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[HTTPValidationError | PagedImageQualityIndicatorOut]
    """

    kwargs = _get_kwargs(
        data_collection_id=data_collection_id,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    data_collection_id: int,
    *,
    client: AuthenticatedClient,
) -> HTTPValidationError | PagedImageQualityIndicatorOut | None:
    """Get Image Quality Indicators

     Get image quality indicators

    Args:
        data_collection_id (int):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and
            Client.raise_on_unexpected_status is True.
        httpx2.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        HTTPValidationError | PagedImageQualityIndicatorOut
    """

    return (
        await asyncio_detailed(
            data_collection_id=data_collection_id,
            client=client,
        )
    ).parsed

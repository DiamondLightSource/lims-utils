from http import HTTPStatus
from typing import Any
from urllib.parse import quote

import httpx2

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.data_collection_comment_in import DataCollectionCommentIn
from ...models.data_collection_comment_out import DataCollectionCommentOut
from ...models.http_validation_error import HTTPValidationError
from ...types import Response


def _get_kwargs(
    data_collection_id: int,
    *,
    body: DataCollectionCommentIn,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/data-collections/{data_collection_id}/comments".format(
            data_collection_id=quote(str(data_collection_id), safe=""),
        ),
    }

    _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx2.Response
) -> DataCollectionCommentOut | HTTPValidationError | None:
    if response.status_code == 201:
        response_201 = DataCollectionCommentOut.from_dict(response.json())

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
) -> Response[DataCollectionCommentOut | HTTPValidationError]:
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
    body: DataCollectionCommentIn,
) -> Response[DataCollectionCommentOut | HTTPValidationError]:
    """Create Comment

     Create new data collection comment

    Args:
        data_collection_id (int):
        body (DataCollectionCommentIn):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and
            Client.raise_on_unexpected_status is True.
        httpx2.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[DataCollectionCommentOut | HTTPValidationError]
    """

    kwargs = _get_kwargs(
        data_collection_id=data_collection_id,
        body=body,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    data_collection_id: int,
    *,
    client: AuthenticatedClient,
    body: DataCollectionCommentIn,
) -> DataCollectionCommentOut | HTTPValidationError | None:
    """Create Comment

     Create new data collection comment

    Args:
        data_collection_id (int):
        body (DataCollectionCommentIn):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and
            Client.raise_on_unexpected_status is True.
        httpx2.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        DataCollectionCommentOut | HTTPValidationError
    """

    return sync_detailed(
        data_collection_id=data_collection_id,
        client=client,
        body=body,
    ).parsed


async def asyncio_detailed(
    data_collection_id: int,
    *,
    client: AuthenticatedClient,
    body: DataCollectionCommentIn,
) -> Response[DataCollectionCommentOut | HTTPValidationError]:
    """Create Comment

     Create new data collection comment

    Args:
        data_collection_id (int):
        body (DataCollectionCommentIn):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and
            Client.raise_on_unexpected_status is True.
        httpx2.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[DataCollectionCommentOut | HTTPValidationError]
    """

    kwargs = _get_kwargs(
        data_collection_id=data_collection_id,
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    data_collection_id: int,
    *,
    client: AuthenticatedClient,
    body: DataCollectionCommentIn,
) -> DataCollectionCommentOut | HTTPValidationError | None:
    """Create Comment

     Create new data collection comment

    Args:
        data_collection_id (int):
        body (DataCollectionCommentIn):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and
            Client.raise_on_unexpected_status is True.
        httpx2.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        DataCollectionCommentOut | HTTPValidationError
    """

    return (
        await asyncio_detailed(
            data_collection_id=data_collection_id,
            client=client,
            body=body,
        )
    ).parsed

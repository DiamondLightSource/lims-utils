from http import HTTPStatus
from typing import Any
from urllib.parse import quote

import httpx2

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.http_validation_error import HTTPValidationError
from ...models.processing_job_parameters_in import ProcessingJobParametersIn
from ...models.processing_job_parameters_out import ProcessingJobParametersOut
from ...types import Response


def _get_kwargs(
    processing_job_id: int,
    *,
    body: ProcessingJobParametersIn,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "put",
        "url": "/processing-jobs/{processing_job_id}/parameters".format(
            processing_job_id=quote(str(processing_job_id), safe=""),
        ),
    }

    _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx2.Response
) -> HTTPValidationError | ProcessingJobParametersOut | None:
    if response.status_code == 200:
        response_200 = ProcessingJobParametersOut.from_dict(response.json())

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
) -> Response[HTTPValidationError | ProcessingJobParametersOut]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    processing_job_id: int,
    *,
    client: AuthenticatedClient,
    body: ProcessingJobParametersIn,
) -> Response[HTTPValidationError | ProcessingJobParametersOut]:
    """Upsert Processing Job Parameters

     Upsert processing job parameters

    Args:
        processing_job_id (int):
        body (ProcessingJobParametersIn):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and
            Client.raise_on_unexpected_status is True.
        httpx2.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[HTTPValidationError | ProcessingJobParametersOut]
    """

    kwargs = _get_kwargs(
        processing_job_id=processing_job_id,
        body=body,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    processing_job_id: int,
    *,
    client: AuthenticatedClient,
    body: ProcessingJobParametersIn,
) -> HTTPValidationError | ProcessingJobParametersOut | None:
    """Upsert Processing Job Parameters

     Upsert processing job parameters

    Args:
        processing_job_id (int):
        body (ProcessingJobParametersIn):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and
            Client.raise_on_unexpected_status is True.
        httpx2.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        HTTPValidationError | ProcessingJobParametersOut
    """

    return sync_detailed(
        processing_job_id=processing_job_id,
        client=client,
        body=body,
    ).parsed


async def asyncio_detailed(
    processing_job_id: int,
    *,
    client: AuthenticatedClient,
    body: ProcessingJobParametersIn,
) -> Response[HTTPValidationError | ProcessingJobParametersOut]:
    """Upsert Processing Job Parameters

     Upsert processing job parameters

    Args:
        processing_job_id (int):
        body (ProcessingJobParametersIn):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and
            Client.raise_on_unexpected_status is True.
        httpx2.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[HTTPValidationError | ProcessingJobParametersOut]
    """

    kwargs = _get_kwargs(
        processing_job_id=processing_job_id,
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    processing_job_id: int,
    *,
    client: AuthenticatedClient,
    body: ProcessingJobParametersIn,
) -> HTTPValidationError | ProcessingJobParametersOut | None:
    """Upsert Processing Job Parameters

     Upsert processing job parameters

    Args:
        processing_job_id (int):
        body (ProcessingJobParametersIn):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and
            Client.raise_on_unexpected_status is True.
        httpx2.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        HTTPValidationError | ProcessingJobParametersOut
    """

    return (
        await asyncio_detailed(
            processing_job_id=processing_job_id,
            client=client,
            body=body,
        )
    ).parsed

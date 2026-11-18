from http import HTTPStatus
from typing import Any
from urllib.parse import quote

import httpx2

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.http_validation_error import HTTPValidationError
from ...models.paged_processing_job_with_auto_proc_program_out import PagedProcessingJobWithAutoProcProgramOut
from ...models.processing_job_combinator import ProcessingJobCombinator
from ...types import UNSET, Response, Unset


def _get_kwargs(
    proposal_reference: str,
    *,
    body: ProcessingJobCombinator | Unset = UNSET,
    page: int | Unset = 0,
    limit: int | Unset = 25,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    params: dict[str, Any] = {}

    params["page"] = page

    params["limit"] = limit

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/proposals/{proposal_reference}/processing-jobs".format(
            proposal_reference=quote(str(proposal_reference), safe=""),
        ),
        "params": params,
    }

    if not isinstance(body, Unset):
        _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx2.Response
) -> HTTPValidationError | PagedProcessingJobWithAutoProcProgramOut | None:
    if response.status_code == 200:
        response_200 = PagedProcessingJobWithAutoProcProgramOut.from_dict(response.json())

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
) -> Response[HTTPValidationError | PagedProcessingJobWithAutoProcProgramOut]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    proposal_reference: str,
    *,
    client: AuthenticatedClient,
    body: ProcessingJobCombinator | Unset = UNSET,
    page: int | Unset = 0,
    limit: int | Unset = 25,
) -> Response[HTTPValidationError | PagedProcessingJobWithAutoProcProgramOut]:
    """Get Processing Jobs Advanced

     Get processing jobs that belong to the proposal

    Args:
        proposal_reference (str):
        page (int | Unset): Page number/Results to skip. Negative numbers count backwards from the
            last page Default: 0.
        limit (int | Unset): Number of results to show Default: 25.
        body (ProcessingJobCombinator | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and
        Client.raise_on_unexpected_status is True.
        httpx2.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[HTTPValidationError | PagedProcessingJobWithAutoProcProgramOut]
    """

    kwargs = _get_kwargs(
        proposal_reference=proposal_reference,
        body=body,
        page=page,
        limit=limit,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    proposal_reference: str,
    *,
    client: AuthenticatedClient,
    body: ProcessingJobCombinator | Unset = UNSET,
    page: int | Unset = 0,
    limit: int | Unset = 25,
) -> HTTPValidationError | PagedProcessingJobWithAutoProcProgramOut | None:
    """Get Processing Jobs Advanced

     Get processing jobs that belong to the proposal

    Args:
        proposal_reference (str):
        page (int | Unset): Page number/Results to skip. Negative numbers count backwards from the
            last page Default: 0.
        limit (int | Unset): Number of results to show Default: 25.
        body (ProcessingJobCombinator | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and
        Client.raise_on_unexpected_status is True.
        httpx2.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        HTTPValidationError | PagedProcessingJobWithAutoProcProgramOut
    """

    return sync_detailed(
        proposal_reference=proposal_reference,
        client=client,
        body=body,
        page=page,
        limit=limit,
    ).parsed


async def asyncio_detailed(
    proposal_reference: str,
    *,
    client: AuthenticatedClient,
    body: ProcessingJobCombinator | Unset = UNSET,
    page: int | Unset = 0,
    limit: int | Unset = 25,
) -> Response[HTTPValidationError | PagedProcessingJobWithAutoProcProgramOut]:
    """Get Processing Jobs Advanced

     Get processing jobs that belong to the proposal

    Args:
        proposal_reference (str):
        page (int | Unset): Page number/Results to skip. Negative numbers count backwards from the
            last page Default: 0.
        limit (int | Unset): Number of results to show Default: 25.
        body (ProcessingJobCombinator | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and
        Client.raise_on_unexpected_status is True.
        httpx2.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[HTTPValidationError | PagedProcessingJobWithAutoProcProgramOut]
    """

    kwargs = _get_kwargs(
        proposal_reference=proposal_reference,
        body=body,
        page=page,
        limit=limit,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    proposal_reference: str,
    *,
    client: AuthenticatedClient,
    body: ProcessingJobCombinator | Unset = UNSET,
    page: int | Unset = 0,
    limit: int | Unset = 25,
) -> HTTPValidationError | PagedProcessingJobWithAutoProcProgramOut | None:
    """Get Processing Jobs Advanced

     Get processing jobs that belong to the proposal

    Args:
        proposal_reference (str):
        page (int | Unset): Page number/Results to skip. Negative numbers count backwards from the
            last page Default: 0.
        limit (int | Unset): Number of results to show Default: 25.
        body (ProcessingJobCombinator | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and
        Client.raise_on_unexpected_status is True.
        httpx2.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        HTTPValidationError | PagedProcessingJobWithAutoProcProgramOut
    """

    return (
        await asyncio_detailed(
            proposal_reference=proposal_reference,
            client=client,
            body=body,
            page=page,
            limit=limit,
        )
    ).parsed

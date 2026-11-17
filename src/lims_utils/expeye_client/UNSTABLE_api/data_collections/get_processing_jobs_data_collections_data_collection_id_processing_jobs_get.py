from http import HTTPStatus
from typing import Any
from urllib.parse import quote

import httpx2

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.http_validation_error import HTTPValidationError
from ...models.paged_processing_job_with_auto_proc_program_out import PagedProcessingJobWithAutoProcProgramOut
from ...models.processing_status import ProcessingStatus
from ...types import UNSET, Response, Unset


def _get_kwargs(
    data_collection_id: int,
    *,
    search: str | Unset = "",
    min_completeness: float | None | Unset = UNSET,
    max_completeness: float | None | Unset = UNSET,
    min_mean_i_over_sigma: float | None | Unset = UNSET,
    max_mean_i_over_sigma: float | None | Unset = UNSET,
    min_res_i_over_sigma: float | None | Unset = UNSET,
    max_res_i_over_sigma: float | None | Unset = UNSET,
    low_resolution_cutoff: float | None | Unset = UNSET,
    high_resolution_cutoff: float | None | Unset = UNSET,
    space_group: None | str | Unset = UNSET,
    downstream: bool | None | Unset = UNSET,
    processing_type: None | str | Unset = UNSET,
    status: list[ProcessingStatus] | None | Unset = UNSET,
    page: int | Unset = 0,
    limit: int | Unset = 25,
) -> dict[str, Any]:

    params: dict[str, Any] = {}

    params["search"] = search

    json_min_completeness: float | None | Unset
    if isinstance(min_completeness, Unset):
        json_min_completeness = UNSET
    else:
        json_min_completeness = min_completeness
    params["minCompleteness"] = json_min_completeness

    json_max_completeness: float | None | Unset
    if isinstance(max_completeness, Unset):
        json_max_completeness = UNSET
    else:
        json_max_completeness = max_completeness
    params["maxCompleteness"] = json_max_completeness

    json_min_mean_i_over_sigma: float | None | Unset
    if isinstance(min_mean_i_over_sigma, Unset):
        json_min_mean_i_over_sigma = UNSET
    else:
        json_min_mean_i_over_sigma = min_mean_i_over_sigma
    params["minMeanIOverSigma"] = json_min_mean_i_over_sigma

    json_max_mean_i_over_sigma: float | None | Unset
    if isinstance(max_mean_i_over_sigma, Unset):
        json_max_mean_i_over_sigma = UNSET
    else:
        json_max_mean_i_over_sigma = max_mean_i_over_sigma
    params["maxMeanIOverSigma"] = json_max_mean_i_over_sigma

    json_min_res_i_over_sigma: float | None | Unset
    if isinstance(min_res_i_over_sigma, Unset):
        json_min_res_i_over_sigma = UNSET
    else:
        json_min_res_i_over_sigma = min_res_i_over_sigma
    params["minResIOverSigma"] = json_min_res_i_over_sigma

    json_max_res_i_over_sigma: float | None | Unset
    if isinstance(max_res_i_over_sigma, Unset):
        json_max_res_i_over_sigma = UNSET
    else:
        json_max_res_i_over_sigma = max_res_i_over_sigma
    params["maxResIOverSigma"] = json_max_res_i_over_sigma

    json_low_resolution_cutoff: float | None | Unset
    if isinstance(low_resolution_cutoff, Unset):
        json_low_resolution_cutoff = UNSET
    else:
        json_low_resolution_cutoff = low_resolution_cutoff
    params["lowResolutionCutoff"] = json_low_resolution_cutoff

    json_high_resolution_cutoff: float | None | Unset
    if isinstance(high_resolution_cutoff, Unset):
        json_high_resolution_cutoff = UNSET
    else:
        json_high_resolution_cutoff = high_resolution_cutoff
    params["highResolutionCutoff"] = json_high_resolution_cutoff

    json_space_group: None | str | Unset
    if isinstance(space_group, Unset):
        json_space_group = UNSET
    else:
        json_space_group = space_group
    params["spaceGroup"] = json_space_group

    json_downstream: bool | None | Unset
    if isinstance(downstream, Unset):
        json_downstream = UNSET
    else:
        json_downstream = downstream
    params["downstream"] = json_downstream

    json_processing_type: None | str | Unset
    if isinstance(processing_type, Unset):
        json_processing_type = UNSET
    else:
        json_processing_type = processing_type
    params["processingType"] = json_processing_type

    json_status: list[str] | None | Unset
    if isinstance(status, Unset):
        json_status = UNSET
    elif isinstance(status, list):
        json_status = []
        for status_type_0_item_data in status:
            status_type_0_item = status_type_0_item_data.value
            json_status.append(status_type_0_item)

    else:
        json_status = status
    params["status"] = json_status

    params["page"] = page

    params["limit"] = limit

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/data-collections/{data_collection_id}/processing-jobs".format(
            data_collection_id=quote(str(data_collection_id), safe=""),
        ),
        "params": params,
    }

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
    data_collection_id: int,
    *,
    client: AuthenticatedClient,
    search: str | Unset = "",
    min_completeness: float | None | Unset = UNSET,
    max_completeness: float | None | Unset = UNSET,
    min_mean_i_over_sigma: float | None | Unset = UNSET,
    max_mean_i_over_sigma: float | None | Unset = UNSET,
    min_res_i_over_sigma: float | None | Unset = UNSET,
    max_res_i_over_sigma: float | None | Unset = UNSET,
    low_resolution_cutoff: float | None | Unset = UNSET,
    high_resolution_cutoff: float | None | Unset = UNSET,
    space_group: None | str | Unset = UNSET,
    downstream: bool | None | Unset = UNSET,
    processing_type: None | str | Unset = UNSET,
    status: list[ProcessingStatus] | None | Unset = UNSET,
    page: int | Unset = 0,
    limit: int | Unset = 25,
) -> Response[HTTPValidationError | PagedProcessingJobWithAutoProcProgramOut]:
    """Get Processing Jobs

     Get processing jobs that belong to the data collection

    Args:
        data_collection_id (int):
        search (str | Unset):  Default: ''.
        min_completeness (float | None | Unset):
        max_completeness (float | None | Unset):
        min_mean_i_over_sigma (float | None | Unset):
        max_mean_i_over_sigma (float | None | Unset):
        min_res_i_over_sigma (float | None | Unset):
        max_res_i_over_sigma (float | None | Unset):
        low_resolution_cutoff (float | None | Unset):
        high_resolution_cutoff (float | None | Unset):
        space_group (None | str | Unset):
        downstream (bool | None | Unset): If True, only return processing jobs that are downstream
            of another processing job. If False, only return processing jobs that are not downstream
            of another processing job. If None, return all processing jobs.
        processing_type (None | str | Unset):
        status (list[ProcessingStatus] | None | Unset):
        page (int | Unset): Page number/Results to skip. Negative numbers count backwards from the
            last page Default: 0.
        limit (int | Unset): Number of results to show Default: 25.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and
            Client.raise_on_unexpected_status is True.
        httpx2.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[HTTPValidationError | PagedProcessingJobWithAutoProcProgramOut]
    """

    kwargs = _get_kwargs(
        data_collection_id=data_collection_id,
        search=search,
        min_completeness=min_completeness,
        max_completeness=max_completeness,
        min_mean_i_over_sigma=min_mean_i_over_sigma,
        max_mean_i_over_sigma=max_mean_i_over_sigma,
        min_res_i_over_sigma=min_res_i_over_sigma,
        max_res_i_over_sigma=max_res_i_over_sigma,
        low_resolution_cutoff=low_resolution_cutoff,
        high_resolution_cutoff=high_resolution_cutoff,
        space_group=space_group,
        downstream=downstream,
        processing_type=processing_type,
        status=status,
        page=page,
        limit=limit,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    data_collection_id: int,
    *,
    client: AuthenticatedClient,
    search: str | Unset = "",
    min_completeness: float | None | Unset = UNSET,
    max_completeness: float | None | Unset = UNSET,
    min_mean_i_over_sigma: float | None | Unset = UNSET,
    max_mean_i_over_sigma: float | None | Unset = UNSET,
    min_res_i_over_sigma: float | None | Unset = UNSET,
    max_res_i_over_sigma: float | None | Unset = UNSET,
    low_resolution_cutoff: float | None | Unset = UNSET,
    high_resolution_cutoff: float | None | Unset = UNSET,
    space_group: None | str | Unset = UNSET,
    downstream: bool | None | Unset = UNSET,
    processing_type: None | str | Unset = UNSET,
    status: list[ProcessingStatus] | None | Unset = UNSET,
    page: int | Unset = 0,
    limit: int | Unset = 25,
) -> HTTPValidationError | PagedProcessingJobWithAutoProcProgramOut | None:
    """Get Processing Jobs

     Get processing jobs that belong to the data collection

    Args:
        data_collection_id (int):
        search (str | Unset):  Default: ''.
        min_completeness (float | None | Unset):
        max_completeness (float | None | Unset):
        min_mean_i_over_sigma (float | None | Unset):
        max_mean_i_over_sigma (float | None | Unset):
        min_res_i_over_sigma (float | None | Unset):
        max_res_i_over_sigma (float | None | Unset):
        low_resolution_cutoff (float | None | Unset):
        high_resolution_cutoff (float | None | Unset):
        space_group (None | str | Unset):
        downstream (bool | None | Unset): If True, only return processing jobs that are downstream
            of another processing job. If False, only return processing jobs that are not downstream
            of another processing job. If None, return all processing jobs.
        processing_type (None | str | Unset):
        status (list[ProcessingStatus] | None | Unset):
        page (int | Unset): Page number/Results to skip. Negative numbers count backwards from the
            last page Default: 0.
        limit (int | Unset): Number of results to show Default: 25.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and
            Client.raise_on_unexpected_status is True.
        httpx2.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        HTTPValidationError | PagedProcessingJobWithAutoProcProgramOut
    """

    return sync_detailed(
        data_collection_id=data_collection_id,
        client=client,
        search=search,
        min_completeness=min_completeness,
        max_completeness=max_completeness,
        min_mean_i_over_sigma=min_mean_i_over_sigma,
        max_mean_i_over_sigma=max_mean_i_over_sigma,
        min_res_i_over_sigma=min_res_i_over_sigma,
        max_res_i_over_sigma=max_res_i_over_sigma,
        low_resolution_cutoff=low_resolution_cutoff,
        high_resolution_cutoff=high_resolution_cutoff,
        space_group=space_group,
        downstream=downstream,
        processing_type=processing_type,
        status=status,
        page=page,
        limit=limit,
    ).parsed


async def asyncio_detailed(
    data_collection_id: int,
    *,
    client: AuthenticatedClient,
    search: str | Unset = "",
    min_completeness: float | None | Unset = UNSET,
    max_completeness: float | None | Unset = UNSET,
    min_mean_i_over_sigma: float | None | Unset = UNSET,
    max_mean_i_over_sigma: float | None | Unset = UNSET,
    min_res_i_over_sigma: float | None | Unset = UNSET,
    max_res_i_over_sigma: float | None | Unset = UNSET,
    low_resolution_cutoff: float | None | Unset = UNSET,
    high_resolution_cutoff: float | None | Unset = UNSET,
    space_group: None | str | Unset = UNSET,
    downstream: bool | None | Unset = UNSET,
    processing_type: None | str | Unset = UNSET,
    status: list[ProcessingStatus] | None | Unset = UNSET,
    page: int | Unset = 0,
    limit: int | Unset = 25,
) -> Response[HTTPValidationError | PagedProcessingJobWithAutoProcProgramOut]:
    """Get Processing Jobs

     Get processing jobs that belong to the data collection

    Args:
        data_collection_id (int):
        search (str | Unset):  Default: ''.
        min_completeness (float | None | Unset):
        max_completeness (float | None | Unset):
        min_mean_i_over_sigma (float | None | Unset):
        max_mean_i_over_sigma (float | None | Unset):
        min_res_i_over_sigma (float | None | Unset):
        max_res_i_over_sigma (float | None | Unset):
        low_resolution_cutoff (float | None | Unset):
        high_resolution_cutoff (float | None | Unset):
        space_group (None | str | Unset):
        downstream (bool | None | Unset): If True, only return processing jobs that are downstream
            of another processing job. If False, only return processing jobs that are not downstream
            of another processing job. If None, return all processing jobs.
        processing_type (None | str | Unset):
        status (list[ProcessingStatus] | None | Unset):
        page (int | Unset): Page number/Results to skip. Negative numbers count backwards from the
            last page Default: 0.
        limit (int | Unset): Number of results to show Default: 25.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and
            Client.raise_on_unexpected_status is True.
        httpx2.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[HTTPValidationError | PagedProcessingJobWithAutoProcProgramOut]
    """

    kwargs = _get_kwargs(
        data_collection_id=data_collection_id,
        search=search,
        min_completeness=min_completeness,
        max_completeness=max_completeness,
        min_mean_i_over_sigma=min_mean_i_over_sigma,
        max_mean_i_over_sigma=max_mean_i_over_sigma,
        min_res_i_over_sigma=min_res_i_over_sigma,
        max_res_i_over_sigma=max_res_i_over_sigma,
        low_resolution_cutoff=low_resolution_cutoff,
        high_resolution_cutoff=high_resolution_cutoff,
        space_group=space_group,
        downstream=downstream,
        processing_type=processing_type,
        status=status,
        page=page,
        limit=limit,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    data_collection_id: int,
    *,
    client: AuthenticatedClient,
    search: str | Unset = "",
    min_completeness: float | None | Unset = UNSET,
    max_completeness: float | None | Unset = UNSET,
    min_mean_i_over_sigma: float | None | Unset = UNSET,
    max_mean_i_over_sigma: float | None | Unset = UNSET,
    min_res_i_over_sigma: float | None | Unset = UNSET,
    max_res_i_over_sigma: float | None | Unset = UNSET,
    low_resolution_cutoff: float | None | Unset = UNSET,
    high_resolution_cutoff: float | None | Unset = UNSET,
    space_group: None | str | Unset = UNSET,
    downstream: bool | None | Unset = UNSET,
    processing_type: None | str | Unset = UNSET,
    status: list[ProcessingStatus] | None | Unset = UNSET,
    page: int | Unset = 0,
    limit: int | Unset = 25,
) -> HTTPValidationError | PagedProcessingJobWithAutoProcProgramOut | None:
    """Get Processing Jobs

     Get processing jobs that belong to the data collection

    Args:
        data_collection_id (int):
        search (str | Unset):  Default: ''.
        min_completeness (float | None | Unset):
        max_completeness (float | None | Unset):
        min_mean_i_over_sigma (float | None | Unset):
        max_mean_i_over_sigma (float | None | Unset):
        min_res_i_over_sigma (float | None | Unset):
        max_res_i_over_sigma (float | None | Unset):
        low_resolution_cutoff (float | None | Unset):
        high_resolution_cutoff (float | None | Unset):
        space_group (None | str | Unset):
        downstream (bool | None | Unset): If True, only return processing jobs that are downstream
            of another processing job. If False, only return processing jobs that are not downstream
            of another processing job. If None, return all processing jobs.
        processing_type (None | str | Unset):
        status (list[ProcessingStatus] | None | Unset):
        page (int | Unset): Page number/Results to skip. Negative numbers count backwards from the
            last page Default: 0.
        limit (int | Unset): Number of results to show Default: 25.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and
            Client.raise_on_unexpected_status is True.
        httpx2.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        HTTPValidationError | PagedProcessingJobWithAutoProcProgramOut
    """

    return (
        await asyncio_detailed(
            data_collection_id=data_collection_id,
            client=client,
            search=search,
            min_completeness=min_completeness,
            max_completeness=max_completeness,
            min_mean_i_over_sigma=min_mean_i_over_sigma,
            max_mean_i_over_sigma=max_mean_i_over_sigma,
            min_res_i_over_sigma=min_res_i_over_sigma,
            max_res_i_over_sigma=max_res_i_over_sigma,
            low_resolution_cutoff=low_resolution_cutoff,
            high_resolution_cutoff=high_resolution_cutoff,
            space_group=space_group,
            downstream=downstream,
            processing_type=processing_type,
            status=status,
            page=page,
            limit=limit,
        )
    ).parsed

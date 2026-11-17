from http import HTTPStatus
from typing import Any
from urllib.parse import quote

import httpx2

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.get_tomograms_for_dcg_data_groups_group_id_tomograms_get_sort_by_type_0 import (
    GetTomogramsForDcgDataGroupsGroupIdTomogramsGetSortByType0,
)
from ...models.http_validation_error import HTTPValidationError
from ...models.paged_tomogram_out import PagedTomogramOut
from ...types import UNSET, Response, Unset


def _get_kwargs(
    group_id: int,
    *,
    sort_by: GetTomogramsForDcgDataGroupsGroupIdTomogramsGetSortByType0
    | None
    | Unset = GetTomogramsForDcgDataGroupsGroupIdTomogramsGetSortByType0.DATE,
    search: None | str | Unset = UNSET,
    page: int | Unset = 0,
    limit: int | Unset = 25,
) -> dict[str, Any]:

    params: dict[str, Any] = {}

    json_sort_by: None | str | Unset
    if isinstance(sort_by, Unset):
        json_sort_by = UNSET
    elif isinstance(sort_by, GetTomogramsForDcgDataGroupsGroupIdTomogramsGetSortByType0):
        json_sort_by = sort_by.value
    else:
        json_sort_by = sort_by
    params["sortBy"] = json_sort_by

    json_search: None | str | Unset
    if isinstance(search, Unset):
        json_search = UNSET
    else:
        json_search = search
    params["search"] = json_search

    params["page"] = page

    params["limit"] = limit

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/data-groups/{group_id}/tomograms".format(
            group_id=quote(str(group_id), safe=""),
        ),
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx2.Response
) -> HTTPValidationError | PagedTomogramOut | None:
    if response.status_code == 200:
        response_200 = PagedTomogramOut.from_dict(response.json())

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
) -> Response[HTTPValidationError | PagedTomogramOut]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    group_id: int,
    *,
    client: AuthenticatedClient,
    sort_by: GetTomogramsForDcgDataGroupsGroupIdTomogramsGetSortByType0
    | None
    | Unset = GetTomogramsForDcgDataGroupsGroupIdTomogramsGetSortByType0.DATE,
    search: None | str | Unset = UNSET,
    page: int | Unset = 0,
    limit: int | Unset = 25,
) -> Response[HTTPValidationError | PagedTomogramOut]:
    """Get Tomograms For Dcg

     List Tomograms belonging to a data collection group

    Args:
        group_id (int):
        sort_by (GetTomogramsForDcgDataGroupsGroupIdTomogramsGetSortByType0 | None | Unset):
            Default: GetTomogramsForDcgDataGroupsGroupIdTomogramsGetSortByType0.DATE.
        search (None | str | Unset):
        page (int | Unset): Page number/Results to skip. Negative numbers count backwards from the
            last page Default: 0.
        limit (int | Unset): Number of results to show Default: 25.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and
            Client.raise_on_unexpected_status is True.
        httpx2.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[HTTPValidationError | PagedTomogramOut]
    """

    kwargs = _get_kwargs(
        group_id=group_id,
        sort_by=sort_by,
        search=search,
        page=page,
        limit=limit,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    group_id: int,
    *,
    client: AuthenticatedClient,
    sort_by: GetTomogramsForDcgDataGroupsGroupIdTomogramsGetSortByType0
    | None
    | Unset = GetTomogramsForDcgDataGroupsGroupIdTomogramsGetSortByType0.DATE,
    search: None | str | Unset = UNSET,
    page: int | Unset = 0,
    limit: int | Unset = 25,
) -> HTTPValidationError | PagedTomogramOut | None:
    """Get Tomograms For Dcg

     List Tomograms belonging to a data collection group

    Args:
        group_id (int):
        sort_by (GetTomogramsForDcgDataGroupsGroupIdTomogramsGetSortByType0 | None | Unset):
            Default: GetTomogramsForDcgDataGroupsGroupIdTomogramsGetSortByType0.DATE.
        search (None | str | Unset):
        page (int | Unset): Page number/Results to skip. Negative numbers count backwards from the
            last page Default: 0.
        limit (int | Unset): Number of results to show Default: 25.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and
            Client.raise_on_unexpected_status is True.
        httpx2.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        HTTPValidationError | PagedTomogramOut
    """

    return sync_detailed(
        group_id=group_id,
        client=client,
        sort_by=sort_by,
        search=search,
        page=page,
        limit=limit,
    ).parsed


async def asyncio_detailed(
    group_id: int,
    *,
    client: AuthenticatedClient,
    sort_by: GetTomogramsForDcgDataGroupsGroupIdTomogramsGetSortByType0
    | None
    | Unset = GetTomogramsForDcgDataGroupsGroupIdTomogramsGetSortByType0.DATE,
    search: None | str | Unset = UNSET,
    page: int | Unset = 0,
    limit: int | Unset = 25,
) -> Response[HTTPValidationError | PagedTomogramOut]:
    """Get Tomograms For Dcg

     List Tomograms belonging to a data collection group

    Args:
        group_id (int):
        sort_by (GetTomogramsForDcgDataGroupsGroupIdTomogramsGetSortByType0 | None | Unset):
            Default: GetTomogramsForDcgDataGroupsGroupIdTomogramsGetSortByType0.DATE.
        search (None | str | Unset):
        page (int | Unset): Page number/Results to skip. Negative numbers count backwards from the
            last page Default: 0.
        limit (int | Unset): Number of results to show Default: 25.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and
            Client.raise_on_unexpected_status is True.
        httpx2.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[HTTPValidationError | PagedTomogramOut]
    """

    kwargs = _get_kwargs(
        group_id=group_id,
        sort_by=sort_by,
        search=search,
        page=page,
        limit=limit,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    group_id: int,
    *,
    client: AuthenticatedClient,
    sort_by: GetTomogramsForDcgDataGroupsGroupIdTomogramsGetSortByType0
    | None
    | Unset = GetTomogramsForDcgDataGroupsGroupIdTomogramsGetSortByType0.DATE,
    search: None | str | Unset = UNSET,
    page: int | Unset = 0,
    limit: int | Unset = 25,
) -> HTTPValidationError | PagedTomogramOut | None:
    """Get Tomograms For Dcg

     List Tomograms belonging to a data collection group

    Args:
        group_id (int):
        sort_by (GetTomogramsForDcgDataGroupsGroupIdTomogramsGetSortByType0 | None | Unset):
            Default: GetTomogramsForDcgDataGroupsGroupIdTomogramsGetSortByType0.DATE.
        search (None | str | Unset):
        page (int | Unset): Page number/Results to skip. Negative numbers count backwards from the
            last page Default: 0.
        limit (int | Unset): Number of results to show Default: 25.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and
            Client.raise_on_unexpected_status is True.
        httpx2.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        HTTPValidationError | PagedTomogramOut
    """

    return (
        await asyncio_detailed(
            group_id=group_id,
            client=client,
            sort_by=sort_by,
            search=search,
            page=page,
            limit=limit,
        )
    ).parsed

from http import HTTPStatus
from typing import Any
from urllib.parse import quote

import httpx2

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.auto_proc_program_attachment_optional import AutoProcProgramAttachmentOptional
from ...models.http_validation_error import HTTPValidationError
from ...models.paged_auto_proc_program_attachment_out import PagedAutoProcProgramAttachmentOut
from ...types import UNSET, Response, Unset


def _get_kwargs(
    proposal_reference: str,
    visit_number: int,
    *,
    body: AutoProcProgramAttachmentOptional,
    file_path: None | str | Unset = UNSET,
    file_name: None | str | Unset = UNSET,
    legacy_join: bool | Unset = False,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    params: dict[str, Any] = {}

    json_file_path: None | str | Unset
    if isinstance(file_path, Unset):
        json_file_path = UNSET
    else:
        json_file_path = file_path
    params["filePath"] = json_file_path

    json_file_name: None | str | Unset
    if isinstance(file_name, Unset):
        json_file_name = UNSET
    else:
        json_file_name = file_name
    params["fileName"] = json_file_name

    params["legacyJoin"] = legacy_join

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "patch",
        "url": "/proposals/{proposal_reference}/sessions/{visit_number}/processing-programs/attachments".format(
            proposal_reference=quote(str(proposal_reference), safe=""),
            visit_number=quote(str(visit_number), safe=""),
        ),
        "params": params,
    }

    _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx2.Response
) -> HTTPValidationError | PagedAutoProcProgramAttachmentOut | None:
    if response.status_code == 200:
        response_200 = PagedAutoProcProgramAttachmentOut.from_dict(response.json())

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
) -> Response[HTTPValidationError | PagedAutoProcProgramAttachmentOut]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    proposal_reference: str,
    visit_number: int,
    *,
    client: AuthenticatedClient,
    body: AutoProcProgramAttachmentOptional,
    file_path: None | str | Unset = UNSET,
    file_name: None | str | Unset = UNSET,
    legacy_join: bool | Unset = False,
) -> Response[HTTPValidationError | PagedAutoProcProgramAttachmentOut]:
    """Update Processing Program Attachments

     List processing program attachments belonging to a session. Multiple items can be updated at once.

    Args:
        proposal_reference (str):
        visit_number (int):
        file_path (None | str | Unset): File path to filter by
        file_name (None | str | Unset): File name to filter by
        legacy_join (bool | Unset): Also join through AutoProcIntegration where attachments don't
            have a parent processing job. Useful for attachments created before 2018, but slows down
            execution significantly Default: False.
        body (AutoProcProgramAttachmentOptional):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and
            Client.raise_on_unexpected_status is True.
        httpx2.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[HTTPValidationError | PagedAutoProcProgramAttachmentOut]
    """

    kwargs = _get_kwargs(
        proposal_reference=proposal_reference,
        visit_number=visit_number,
        body=body,
        file_path=file_path,
        file_name=file_name,
        legacy_join=legacy_join,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    proposal_reference: str,
    visit_number: int,
    *,
    client: AuthenticatedClient,
    body: AutoProcProgramAttachmentOptional,
    file_path: None | str | Unset = UNSET,
    file_name: None | str | Unset = UNSET,
    legacy_join: bool | Unset = False,
) -> HTTPValidationError | PagedAutoProcProgramAttachmentOut | None:
    """Update Processing Program Attachments

     List processing program attachments belonging to a session. Multiple items can be updated at once.

    Args:
        proposal_reference (str):
        visit_number (int):
        file_path (None | str | Unset): File path to filter by
        file_name (None | str | Unset): File name to filter by
        legacy_join (bool | Unset): Also join through AutoProcIntegration where attachments don't
            have a parent processing job. Useful for attachments created before 2018, but slows down
            execution significantly Default: False.
        body (AutoProcProgramAttachmentOptional):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and
            Client.raise_on_unexpected_status is True.
        httpx2.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        HTTPValidationError | PagedAutoProcProgramAttachmentOut
    """

    return sync_detailed(
        proposal_reference=proposal_reference,
        visit_number=visit_number,
        client=client,
        body=body,
        file_path=file_path,
        file_name=file_name,
        legacy_join=legacy_join,
    ).parsed


async def asyncio_detailed(
    proposal_reference: str,
    visit_number: int,
    *,
    client: AuthenticatedClient,
    body: AutoProcProgramAttachmentOptional,
    file_path: None | str | Unset = UNSET,
    file_name: None | str | Unset = UNSET,
    legacy_join: bool | Unset = False,
) -> Response[HTTPValidationError | PagedAutoProcProgramAttachmentOut]:
    """Update Processing Program Attachments

     List processing program attachments belonging to a session. Multiple items can be updated at once.

    Args:
        proposal_reference (str):
        visit_number (int):
        file_path (None | str | Unset): File path to filter by
        file_name (None | str | Unset): File name to filter by
        legacy_join (bool | Unset): Also join through AutoProcIntegration where attachments don't
            have a parent processing job. Useful for attachments created before 2018, but slows down
            execution significantly Default: False.
        body (AutoProcProgramAttachmentOptional):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and
            Client.raise_on_unexpected_status is True.
        httpx2.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[HTTPValidationError | PagedAutoProcProgramAttachmentOut]
    """

    kwargs = _get_kwargs(
        proposal_reference=proposal_reference,
        visit_number=visit_number,
        body=body,
        file_path=file_path,
        file_name=file_name,
        legacy_join=legacy_join,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    proposal_reference: str,
    visit_number: int,
    *,
    client: AuthenticatedClient,
    body: AutoProcProgramAttachmentOptional,
    file_path: None | str | Unset = UNSET,
    file_name: None | str | Unset = UNSET,
    legacy_join: bool | Unset = False,
) -> HTTPValidationError | PagedAutoProcProgramAttachmentOut | None:
    """Update Processing Program Attachments

     List processing program attachments belonging to a session. Multiple items can be updated at once.

    Args:
        proposal_reference (str):
        visit_number (int):
        file_path (None | str | Unset): File path to filter by
        file_name (None | str | Unset): File name to filter by
        legacy_join (bool | Unset): Also join through AutoProcIntegration where attachments don't
            have a parent processing job. Useful for attachments created before 2018, but slows down
            execution significantly Default: False.
        body (AutoProcProgramAttachmentOptional):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and
            Client.raise_on_unexpected_status is True.
        httpx2.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        HTTPValidationError | PagedAutoProcProgramAttachmentOut
    """

    return (
        await asyncio_detailed(
            proposal_reference=proposal_reference,
            visit_number=visit_number,
            client=client,
            body=body,
            file_path=file_path,
            file_name=file_name,
            legacy_join=legacy_join,
        )
    ).parsed

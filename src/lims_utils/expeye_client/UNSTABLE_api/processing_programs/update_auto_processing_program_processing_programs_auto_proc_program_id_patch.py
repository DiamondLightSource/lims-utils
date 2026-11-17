from http import HTTPStatus
from typing import Any
from urllib.parse import quote

import httpx2

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.auto_proc_program_optional import AutoProcProgramOptional
from ...models.auto_proc_program_out import AutoProcProgramOut
from ...models.http_validation_error import HTTPValidationError
from ...types import Response


def _get_kwargs(
    auto_proc_program_id: int,
    *,
    body: AutoProcProgramOptional,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "patch",
        "url": "/processing-programs/{auto_proc_program_id}".format(
            auto_proc_program_id=quote(str(auto_proc_program_id), safe=""),
        ),
    }

    _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx2.Response
) -> AutoProcProgramOut | HTTPValidationError | None:
    if response.status_code == 200:
        response_200 = AutoProcProgramOut.from_dict(response.json())

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
) -> Response[AutoProcProgramOut | HTTPValidationError]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    auto_proc_program_id: int,
    *,
    client: AuthenticatedClient,
    body: AutoProcProgramOptional,
) -> Response[AutoProcProgramOut | HTTPValidationError]:
    """Update Auto Processing Program

     Update processing program

    Args:
        auto_proc_program_id (int):
        body (AutoProcProgramOptional):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and
            Client.raise_on_unexpected_status is True.
        httpx2.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[AutoProcProgramOut | HTTPValidationError]
    """

    kwargs = _get_kwargs(
        auto_proc_program_id=auto_proc_program_id,
        body=body,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    auto_proc_program_id: int,
    *,
    client: AuthenticatedClient,
    body: AutoProcProgramOptional,
) -> AutoProcProgramOut | HTTPValidationError | None:
    """Update Auto Processing Program

     Update processing program

    Args:
        auto_proc_program_id (int):
        body (AutoProcProgramOptional):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and
            Client.raise_on_unexpected_status is True.
        httpx2.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        AutoProcProgramOut | HTTPValidationError
    """

    return sync_detailed(
        auto_proc_program_id=auto_proc_program_id,
        client=client,
        body=body,
    ).parsed


async def asyncio_detailed(
    auto_proc_program_id: int,
    *,
    client: AuthenticatedClient,
    body: AutoProcProgramOptional,
) -> Response[AutoProcProgramOut | HTTPValidationError]:
    """Update Auto Processing Program

     Update processing program

    Args:
        auto_proc_program_id (int):
        body (AutoProcProgramOptional):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and
            Client.raise_on_unexpected_status is True.
        httpx2.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[AutoProcProgramOut | HTTPValidationError]
    """

    kwargs = _get_kwargs(
        auto_proc_program_id=auto_proc_program_id,
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    auto_proc_program_id: int,
    *,
    client: AuthenticatedClient,
    body: AutoProcProgramOptional,
) -> AutoProcProgramOut | HTTPValidationError | None:
    """Update Auto Processing Program

     Update processing program

    Args:
        auto_proc_program_id (int):
        body (AutoProcProgramOptional):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and
            Client.raise_on_unexpected_status is True.
        httpx2.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        AutoProcProgramOut | HTTPValidationError
    """

    return (
        await asyncio_detailed(
            auto_proc_program_id=auto_proc_program_id,
            client=client,
            body=body,
        )
    ).parsed

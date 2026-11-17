from http import HTTPStatus
from typing import Any
from urllib.parse import quote

import httpx2

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.admin_var_in import AdminVarIn
from ...models.admin_var_out import AdminVarOut
from ...models.http_validation_error import HTTPValidationError
from ...types import Response


def _get_kwargs(
    admin_var_name: str,
    *,
    body: AdminVarIn,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "patch",
        "url": "/admin-vars/{admin_var_name}".format(
            admin_var_name=quote(str(admin_var_name), safe=""),
        ),
    }

    _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx2.Response
) -> AdminVarOut | HTTPValidationError | None:
    if response.status_code == 200:
        response_200 = AdminVarOut.from_dict(response.json())

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
) -> Response[AdminVarOut | HTTPValidationError]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    admin_var_name: str,
    *,
    client: AuthenticatedClient,
    body: AdminVarIn,
) -> Response[AdminVarOut | HTTPValidationError]:
    """Update Admin Var

     Update admin variable value

    Args:
        admin_var_name (str):
        body (AdminVarIn):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx2.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[AdminVarOut | HTTPValidationError]
    """

    kwargs = _get_kwargs(
        admin_var_name=admin_var_name,
        body=body,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    admin_var_name: str,
    *,
    client: AuthenticatedClient,
    body: AdminVarIn,
) -> AdminVarOut | HTTPValidationError | None:
    """Update Admin Var

     Update admin variable value

    Args:
        admin_var_name (str):
        body (AdminVarIn):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx2.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        AdminVarOut | HTTPValidationError
    """

    return sync_detailed(
        admin_var_name=admin_var_name,
        client=client,
        body=body,
    ).parsed


async def asyncio_detailed(
    admin_var_name: str,
    *,
    client: AuthenticatedClient,
    body: AdminVarIn,
) -> Response[AdminVarOut | HTTPValidationError]:
    """Update Admin Var

     Update admin variable value

    Args:
        admin_var_name (str):
        body (AdminVarIn):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx2.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[AdminVarOut | HTTPValidationError]
    """

    kwargs = _get_kwargs(
        admin_var_name=admin_var_name,
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    admin_var_name: str,
    *,
    client: AuthenticatedClient,
    body: AdminVarIn,
) -> AdminVarOut | HTTPValidationError | None:
    """Update Admin Var

     Update admin variable value

    Args:
        admin_var_name (str):
        body (AdminVarIn):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx2.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        AdminVarOut | HTTPValidationError
    """

    return (
        await asyncio_detailed(
            admin_var_name=admin_var_name,
            client=client,
            body=body,
        )
    ).parsed

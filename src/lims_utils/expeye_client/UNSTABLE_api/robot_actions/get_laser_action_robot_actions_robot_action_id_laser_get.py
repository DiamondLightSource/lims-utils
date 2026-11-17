from http import HTTPStatus
from typing import Any
from urllib.parse import quote

import httpx2

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.http_validation_error import HTTPValidationError
from ...models.laser_action_out import LaserActionOut
from ...types import Response


def _get_kwargs(
    robot_action_id: int,
) -> dict[str, Any]:

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/robot-actions/{robot_action_id}/laser".format(
            robot_action_id=quote(str(robot_action_id), safe=""),
        ),
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx2.Response
) -> HTTPValidationError | LaserActionOut | None:
    if response.status_code == 200:
        response_200 = LaserActionOut.from_dict(response.json())

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
) -> Response[HTTPValidationError | LaserActionOut]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    robot_action_id: int,
    *,
    client: AuthenticatedClient,
) -> Response[HTTPValidationError | LaserActionOut]:
    """Get Laser Action

     Get laser points and parameters

    Args:
        robot_action_id (int):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx2.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[HTTPValidationError | LaserActionOut]
    """

    kwargs = _get_kwargs(
        robot_action_id=robot_action_id,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    robot_action_id: int,
    *,
    client: AuthenticatedClient,
) -> HTTPValidationError | LaserActionOut | None:
    """Get Laser Action

     Get laser points and parameters

    Args:
        robot_action_id (int):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx2.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        HTTPValidationError | LaserActionOut
    """

    return sync_detailed(
        robot_action_id=robot_action_id,
        client=client,
    ).parsed


async def asyncio_detailed(
    robot_action_id: int,
    *,
    client: AuthenticatedClient,
) -> Response[HTTPValidationError | LaserActionOut]:
    """Get Laser Action

     Get laser points and parameters

    Args:
        robot_action_id (int):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx2.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[HTTPValidationError | LaserActionOut]
    """

    kwargs = _get_kwargs(
        robot_action_id=robot_action_id,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    robot_action_id: int,
    *,
    client: AuthenticatedClient,
) -> HTTPValidationError | LaserActionOut | None:
    """Get Laser Action

     Get laser points and parameters

    Args:
        robot_action_id (int):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx2.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        HTTPValidationError | LaserActionOut
    """

    return (
        await asyncio_detailed(
            robot_action_id=robot_action_id,
            client=client,
        )
    ).parsed

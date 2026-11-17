from http import HTTPStatus
from typing import Any
from urllib.parse import quote

import httpx2

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.full_movie_optional import FullMovieOptional
from ...models.full_movie_out import FullMovieOut
from ...models.http_validation_error import HTTPValidationError
from ...types import Response


def _get_kwargs(
    motion_correction_id: int,
    *,
    body: FullMovieOptional,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "patch",
        "url": "/motion-correction/{motion_correction_id}".format(
            motion_correction_id=quote(str(motion_correction_id), safe=""),
        ),
    }

    _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx2.Response
) -> FullMovieOut | HTTPValidationError | None:
    if response.status_code == 200:
        response_200 = FullMovieOut.from_dict(response.json())

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
) -> Response[FullMovieOut | HTTPValidationError]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    motion_correction_id: int,
    *,
    client: AuthenticatedClient,
    body: FullMovieOptional,
) -> Response[FullMovieOut | HTTPValidationError]:
    """Update Motion Correction

     Update a movie, motion correction, CTF and optional tilt alignment bundle.
                        Omit TiltImageAlignment to leave alignments unchanged.
                        Setting TiltImageAlignment to null deletes the alignment.

    Args:
        motion_correction_id (int):
        body (FullMovieOptional):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and
            Client.raise_on_unexpected_status is True.
        httpx2.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[FullMovieOut | HTTPValidationError]
    """

    kwargs = _get_kwargs(
        motion_correction_id=motion_correction_id,
        body=body,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    motion_correction_id: int,
    *,
    client: AuthenticatedClient,
    body: FullMovieOptional,
) -> FullMovieOut | HTTPValidationError | None:
    """Update Motion Correction

     Update a movie, motion correction, CTF and optional tilt alignment bundle.
                        Omit TiltImageAlignment to leave alignments unchanged.
                        Setting TiltImageAlignment to null deletes the alignment.

    Args:
        motion_correction_id (int):
        body (FullMovieOptional):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and
            Client.raise_on_unexpected_status is True.
        httpx2.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        FullMovieOut | HTTPValidationError
    """

    return sync_detailed(
        motion_correction_id=motion_correction_id,
        client=client,
        body=body,
    ).parsed


async def asyncio_detailed(
    motion_correction_id: int,
    *,
    client: AuthenticatedClient,
    body: FullMovieOptional,
) -> Response[FullMovieOut | HTTPValidationError]:
    """Update Motion Correction

     Update a movie, motion correction, CTF and optional tilt alignment bundle.
                        Omit TiltImageAlignment to leave alignments unchanged.
                        Setting TiltImageAlignment to null deletes the alignment.

    Args:
        motion_correction_id (int):
        body (FullMovieOptional):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and
            Client.raise_on_unexpected_status is True.
        httpx2.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[FullMovieOut | HTTPValidationError]
    """

    kwargs = _get_kwargs(
        motion_correction_id=motion_correction_id,
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    motion_correction_id: int,
    *,
    client: AuthenticatedClient,
    body: FullMovieOptional,
) -> FullMovieOut | HTTPValidationError | None:
    """Update Motion Correction

     Update a movie, motion correction, CTF and optional tilt alignment bundle.
                        Omit TiltImageAlignment to leave alignments unchanged.
                        Setting TiltImageAlignment to null deletes the alignment.

    Args:
        motion_correction_id (int):
        body (FullMovieOptional):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and
            Client.raise_on_unexpected_status is True.
        httpx2.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        FullMovieOut | HTTPValidationError
    """

    return (
        await asyncio_detailed(
            motion_correction_id=motion_correction_id,
            client=client,
            body=body,
        )
    ).parsed

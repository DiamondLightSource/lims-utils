from http import HTTPStatus
from typing import Any
from urllib.parse import quote

import httpx2

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.fluorescence_spectrum_optional import FluorescenceSpectrumOptional
from ...models.fluorescence_spectrum_out import FluorescenceSpectrumOut
from ...models.http_validation_error import HTTPValidationError
from ...types import Response


def _get_kwargs(
    fluorescence_spectrum_id: int,
    *,
    body: FluorescenceSpectrumOptional,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "patch",
        "url": "/fluorescence-spectrums/{fluorescence_spectrum_id}".format(
            fluorescence_spectrum_id=quote(str(fluorescence_spectrum_id), safe=""),
        ),
    }

    _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx2.Response
) -> FluorescenceSpectrumOut | HTTPValidationError | None:
    if response.status_code == 200:
        response_200 = FluorescenceSpectrumOut.from_dict(response.json())

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
) -> Response[FluorescenceSpectrumOut | HTTPValidationError]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    fluorescence_spectrum_id: int,
    *,
    client: AuthenticatedClient,
    body: FluorescenceSpectrumOptional,
) -> Response[FluorescenceSpectrumOut | HTTPValidationError]:
    """Update Fluorescence Spectrum

     Update existing fluorescence spectrum params

    Args:
        fluorescence_spectrum_id (int):
        body (FluorescenceSpectrumOptional):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and
            Client.raise_on_unexpected_status is True.
        httpx2.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[FluorescenceSpectrumOut | HTTPValidationError]
    """

    kwargs = _get_kwargs(
        fluorescence_spectrum_id=fluorescence_spectrum_id,
        body=body,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    fluorescence_spectrum_id: int,
    *,
    client: AuthenticatedClient,
    body: FluorescenceSpectrumOptional,
) -> FluorescenceSpectrumOut | HTTPValidationError | None:
    """Update Fluorescence Spectrum

     Update existing fluorescence spectrum params

    Args:
        fluorescence_spectrum_id (int):
        body (FluorescenceSpectrumOptional):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and
            Client.raise_on_unexpected_status is True.
        httpx2.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        FluorescenceSpectrumOut | HTTPValidationError
    """

    return sync_detailed(
        fluorescence_spectrum_id=fluorescence_spectrum_id,
        client=client,
        body=body,
    ).parsed


async def asyncio_detailed(
    fluorescence_spectrum_id: int,
    *,
    client: AuthenticatedClient,
    body: FluorescenceSpectrumOptional,
) -> Response[FluorescenceSpectrumOut | HTTPValidationError]:
    """Update Fluorescence Spectrum

     Update existing fluorescence spectrum params

    Args:
        fluorescence_spectrum_id (int):
        body (FluorescenceSpectrumOptional):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and
            Client.raise_on_unexpected_status is True.
        httpx2.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[FluorescenceSpectrumOut | HTTPValidationError]
    """

    kwargs = _get_kwargs(
        fluorescence_spectrum_id=fluorescence_spectrum_id,
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    fluorescence_spectrum_id: int,
    *,
    client: AuthenticatedClient,
    body: FluorescenceSpectrumOptional,
) -> FluorescenceSpectrumOut | HTTPValidationError | None:
    """Update Fluorescence Spectrum

     Update existing fluorescence spectrum params

    Args:
        fluorescence_spectrum_id (int):
        body (FluorescenceSpectrumOptional):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and
            Client.raise_on_unexpected_status is True.
        httpx2.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        FluorescenceSpectrumOut | HTTPValidationError
    """

    return (
        await asyncio_detailed(
            fluorescence_spectrum_id=fluorescence_spectrum_id,
            client=client,
            body=body,
        )
    ).parsed

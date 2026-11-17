from http import HTTPStatus
from typing import Any
from urllib.parse import quote

import httpx2

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.http_validation_error import HTTPValidationError
from ...models.sample_in_with_crystal_and_diffraction_plan import SampleInWithCrystalAndDiffractionPlan
from ...models.sample_out import SampleOut
from ...types import Response


def _get_kwargs(
    container_id: int,
    *,
    body: list[SampleInWithCrystalAndDiffractionPlan] | SampleInWithCrystalAndDiffractionPlan,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/containers/{container_id}/samples".format(
            container_id=quote(str(container_id), safe=""),
        ),
    }

    if isinstance(body, SampleInWithCrystalAndDiffractionPlan):
        _kwargs["json"] = body.to_dict()
    else:
        _kwargs["json"] = []
        for body_type_1_item_data in body:
            body_type_1_item = body_type_1_item_data.to_dict()
            _kwargs["json"].append(body_type_1_item)

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx2.Response
) -> HTTPValidationError | list[SampleOut] | SampleOut | None:
    if response.status_code == 201:

        def _parse_response_201(data: object) -> list[SampleOut] | SampleOut:
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                response_201_type_0 = SampleOut.from_dict(data)

                return response_201_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            if not isinstance(data, list):
                raise TypeError()
            response_201_type_1 = []
            _response_201_type_1 = data
            for response_201_type_1_item_data in _response_201_type_1:
                response_201_type_1_item = SampleOut.from_dict(response_201_type_1_item_data)

                response_201_type_1.append(response_201_type_1_item)

            return response_201_type_1

        response_201 = _parse_response_201(response.json())

        return response_201

    if response.status_code == 422:
        response_422 = HTTPValidationError.from_dict(response.json())

        return response_422

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx2.Response
) -> Response[HTTPValidationError | list[SampleOut] | SampleOut]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    container_id: int,
    *,
    client: AuthenticatedClient,
    body: list[SampleInWithCrystalAndDiffractionPlan] | SampleInWithCrystalAndDiffractionPlan,
) -> Response[HTTPValidationError | list[SampleOut] | SampleOut]:
    """Create Sample

     Create new sample

    Args:
        container_id (int):
        body (list[SampleInWithCrystalAndDiffractionPlan] |
            SampleInWithCrystalAndDiffractionPlan):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx2.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[HTTPValidationError | list[SampleOut] | SampleOut]
    """

    kwargs = _get_kwargs(
        container_id=container_id,
        body=body,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    container_id: int,
    *,
    client: AuthenticatedClient,
    body: list[SampleInWithCrystalAndDiffractionPlan] | SampleInWithCrystalAndDiffractionPlan,
) -> HTTPValidationError | list[SampleOut] | SampleOut | None:
    """Create Sample

     Create new sample

    Args:
        container_id (int):
        body (list[SampleInWithCrystalAndDiffractionPlan] |
            SampleInWithCrystalAndDiffractionPlan):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx2.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        HTTPValidationError | list[SampleOut] | SampleOut
    """

    return sync_detailed(
        container_id=container_id,
        client=client,
        body=body,
    ).parsed


async def asyncio_detailed(
    container_id: int,
    *,
    client: AuthenticatedClient,
    body: list[SampleInWithCrystalAndDiffractionPlan] | SampleInWithCrystalAndDiffractionPlan,
) -> Response[HTTPValidationError | list[SampleOut] | SampleOut]:
    """Create Sample

     Create new sample

    Args:
        container_id (int):
        body (list[SampleInWithCrystalAndDiffractionPlan] |
            SampleInWithCrystalAndDiffractionPlan):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx2.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[HTTPValidationError | list[SampleOut] | SampleOut]
    """

    kwargs = _get_kwargs(
        container_id=container_id,
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    container_id: int,
    *,
    client: AuthenticatedClient,
    body: list[SampleInWithCrystalAndDiffractionPlan] | SampleInWithCrystalAndDiffractionPlan,
) -> HTTPValidationError | list[SampleOut] | SampleOut | None:
    """Create Sample

     Create new sample

    Args:
        container_id (int):
        body (list[SampleInWithCrystalAndDiffractionPlan] |
            SampleInWithCrystalAndDiffractionPlan):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx2.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        HTTPValidationError | list[SampleOut] | SampleOut
    """

    return (
        await asyncio_detailed(
            container_id=container_id,
            client=client,
            body=body,
        )
    ).parsed

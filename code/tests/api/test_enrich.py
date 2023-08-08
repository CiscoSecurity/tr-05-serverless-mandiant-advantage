from http import HTTPStatus
from unittest.mock import patch

from pytest import fixture

from code.tests.api.utils import get_headers
from code.tests.conftest import mock_api_response
from code.tests.payloads_for_tests import (
    EXPECTED_RELAY_RESPONSE,
    EXPECTED_RESPONSE_OF_JWKS_ENDPOINT,
    EXPECTED_RESPONSE_OF_TEMPLATE,
)


def routes():
    yield "/deliberate/observables"
    yield "/observe/observables"
    yield "/refer/observables"


def ids():
    yield "40909883-cb4c-4473-b2ca-d87553de9198"


@fixture(scope="module", params=routes(), ids=lambda route: f"POST {route}")
def route(request):
    return request.param


@fixture(scope="module")
def invalid_json_value():
    return [{"type": "sha1", "value": ""}]


@patch("requests.get")
def test_enrich_call_with_valid_jwt_but_invalid_json_value(
    mock_request,
    route,
    client,
    valid_jwt,
    invalid_json_value,
    invalid_json_expected_payload,
):
    mock_request.return_value = mock_api_response(
        payload=EXPECTED_RESPONSE_OF_JWKS_ENDPOINT
    )
    response = client.post(
        route, headers=get_headers(valid_jwt()), json=invalid_json_value
    )
    assert response.status_code == HTTPStatus.OK
    assert response.json == invalid_json_expected_payload(
        "{0: {'value': ['Field may not be blank.']}}"
    )


@fixture(scope="module")
def valid_json():
    return [
        {"type": "sha1", "value": "654477f623a09fda1b04fcba854734fb20a30e11"}
    ]


@patch("api.mapping.uuid4")
@patch("requests.request")
@patch("requests.get")
def test_enrich_call_success(
    mock_get, mock_request, mock_id, route, client, valid_jwt, valid_json
):
    mock_get.return_value = mock_api_response(
        payload=EXPECTED_RESPONSE_OF_JWKS_ENDPOINT
    )
    mock_request.return_value = mock_api_response(
        payload=EXPECTED_RESPONSE_OF_TEMPLATE
    )
    mock_id.side_effect = ids()
    response = client.post(
        route, headers=get_headers(valid_jwt()), json=valid_json
    )
    assert response.status_code == HTTPStatus.OK
    if route == "/observe/observables":
        assert response.json == EXPECTED_RELAY_RESPONSE

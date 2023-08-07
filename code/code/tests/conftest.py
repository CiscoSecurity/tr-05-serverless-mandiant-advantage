from http import HTTPStatus
from unittest.mock import MagicMock

import jwt
from pytest import fixture

from code.api.errors import INVALID_ARGUMENT
from code.app import app
from code.tests.payloads_for_tests import PRIVATE_KEY


@fixture(scope="session")
def client():
    app.rsa_private_key = PRIVATE_KEY
    app.testing = True

    with app.test_client() as client:
        yield client


@fixture(scope="session")
def valid_jwt(client):
    def _make_jwt(
        api_key="some_key",
        host="some_host.com",
        limit=1,
        jwks_host="visibility.amp.cisco.com",
        aud="http://localhost",
        kid="02B1174234C29F8EFB69911438F597FF3FFEE6B7",
        wrong_structure=False,
        wrong_jwks_host=False,
    ):
        payload = {
            "api_key": api_key,
            "host": host,
            "CTR_ENTITIES_LIMIT": limit,
            "jwks_host": jwks_host,
            "aud": aud,
        }

        if wrong_jwks_host:
            payload.pop("jwks_host")

        if wrong_structure:
            payload.pop("api_key")

        return jwt.encode(
            payload,
            client.application.rsa_private_key,
            algorithm="RS256",
            headers={"kid": kid},
        )

    return _make_jwt


@fixture(scope="module")
def invalid_json_expected_payload():
    def _make_message(message):
        error = {"code": INVALID_ARGUMENT, "message": message, "type": "fatal"}
        return {"errors": [error]}

    return _make_message


def mock_api_response(status_code=HTTPStatus.OK, payload=None):
    mock_response = MagicMock()

    mock_response.status_code = status_code
    mock_response.ok = status_code == HTTPStatus.OK
    mock_response.json = lambda: payload

    return mock_response


@fixture(scope="module")
def connection_error_expected_relay_response():
    return {
        "errors": [
            {
                "code": "connection error",
                "message": "Unable to connect to SentinelOne, "
                "validate the configured API endpoint: "
                "https://some_host.com/web/api/v2.1/threats",
                "type": "fatal",
            }
        ]
    }

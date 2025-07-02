from http import HTTPStatus
from unittest.mock import MagicMock

from tests.utils.crypto import generate_rsa_key_pair
import jwt
from pytest import fixture

from api.errors import INVALID_ARGUMENT
from app import app


@fixture(scope="session")
def test_keys_and_token():
    private_pem, jwks, kid = generate_rsa_key_pair()
    wrong_private_pem, wrong_jwks, _ = generate_rsa_key_pair()

    return {
        "private_key": private_pem,
        "jwks": jwks,
        "kid": kid,
        "wrong_private_key": wrong_private_pem,
        "wrong_jwks": wrong_jwks,
    }


@fixture(scope="session")
def client(test_keys_and_token):
    app.rsa_private_key = test_keys_and_token["private_key"]
    app.testing = True

    with app.test_client() as client:
        yield client


@fixture(scope="session")
def valid_jwt(client):
    def _make_jwt(
        api_key="some_key",
        api_secret="some_secret",
        host="some_host.com",
        limit=1,
        jwks_host="visibility.amp.cisco.com",
        aud="http://localhost",
        wrong_structure=False,
        wrong_jwks_host=False,
        kid=None,
        private_key=None,
    ):
        payload = {
            "API_KEY": api_key,
            "API_SECRET": api_secret,
            "host": host,
            "CTR_ENTITIES_LIMIT": limit,
            "jwks_host": jwks_host,
            "aud": aud,
        }

        if wrong_jwks_host:
            payload.pop("jwks_host")

        if wrong_structure:
            payload.pop("API_KEY")

        signing_key = private_key or app.rsa_private_key
        signing_kid = kid or "02B1174234C29F8EFB69911438F597FF3FFEE6B7"

        return jwt.encode(
            payload,
            signing_key,
            algorithm="RS256",
            headers={"kid": signing_kid},
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

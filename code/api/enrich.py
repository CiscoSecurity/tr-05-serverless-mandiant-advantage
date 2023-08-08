from functools import partial
from uuid import uuid4
from api.mapping import Mapping
from api.schemas import ObservableSchema
from api.errors import MandiantKeyError
from api.utils import (
    get_json,
    get_auth_token,
    get_credentials,
    get_public_key,
    jsonify_errors,
    jsonify_data,
)
from flask import Blueprint, current_app, g

enrich_api = Blueprint("enrich", __name__)

get_observables = partial(get_json, schema=ObservableSchema(many=True))


@enrich_api.route("/deliberate/observables", methods=["POST"])
def deliberate_observables():
    _ = get_credentials()
    _ = get_observables()
    return jsonify_data({})


@enrich_api.route("/observe/observables", methods=["POST"])
def observe_observables():
    credentials = get_credentials()
    observables = get_observables()

    ui_url = current_app.config['UI_URL']

    try:
        for observable in observables:
            print(observable)
    except KeyError:
        jsonify_errors(MandiantKeyError())

    return jsonify_data({})


@enrich_api.route("/refer/observables", methods=["POST"])
def refer_observables():
    _ = get_credentials()
    _ = get_observables()
    return jsonify_data([])

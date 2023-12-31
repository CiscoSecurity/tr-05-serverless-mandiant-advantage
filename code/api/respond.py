from functools import partial

from api.schemas import ActionFormParamsSchema, ObservableSchema
from api.utils import get_credentials, get_json, jsonify_data
from flask import Blueprint

respond_api = Blueprint("respond", __name__)

get_observables = partial(get_json, schema=ObservableSchema(many=True))
get_action_form_params = partial(get_json, schema=ActionFormParamsSchema())


@respond_api.route("/respond/observables", methods=["POST"])
def respond_observables():
    _ = get_credentials()
    _ = get_observables()
    return jsonify_data([])


@respond_api.route("/respond/trigger", methods=["POST"])
def respond_trigger():
    _ = get_credentials()
    _ = get_action_form_params()
    return jsonify_data({"status": "success"})

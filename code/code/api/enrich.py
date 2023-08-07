from functools import partial

from api.client import TemplateClient
from api.mapping import Sighting
from api.schemas import ObservableSchema
from api.utils import (
    filter_observables,
    get_credentials,
    get_json,
    jsonify_data,
    jsonify_result,
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
    _ = get_credentials()
    observables = filter_observables(get_observables())

    g.sightings = []
    limit = current_app.config["CTR_ENTITIES_LIMIT"]
    client = TemplateClient()

    for observable in observables:
        threats = client.get_threats()
        sighting_mapping = Sighting(observable)

        if len(threats) > limit:
            threats = threats[:limit]
        for threat in threats:
            mapped_sighting = sighting_mapping.extract(threat)
            g.sightings.append(mapped_sighting)

    return jsonify_result()


@enrich_api.route("/refer/observables", methods=["POST"])
def refer_observables():
    _ = get_credentials()
    _ = get_observables()
    return jsonify_data([])

from api.utils import get_credentials, jsonify_data
from flask import Blueprint

health_api = Blueprint("health", __name__)


@health_api.route("/health", methods=["POST"])
def health():
    _ = get_credentials()
    return jsonify_data({"status": "ok"})

import traceback

from flask import Flask, jsonify

from api.enrich import enrich_api
from api.health import health_api
from api.respond import respond_api
from api.utils import jsonify_errors, get_json
from api.version import version_api
from api.watchdog import watchdog_api

app = Flask(__name__)

app.url_map.strict_slashes = False
app.config.from_object("config.Config")

for bp in [enrich_api, health_api, respond_api, version_api, watchdog_api]:
    app.register_blueprint(bp)

if __name__ == "__main__":
    app.run()

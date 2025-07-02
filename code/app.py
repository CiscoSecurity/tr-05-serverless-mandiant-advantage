import traceback

from api.errors import CTRBaseError
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


@app.errorhandler(Exception)
def handle_error(exception):
    code = getattr(exception, "code", 500)
    message = getattr(exception, "description", "Something went wrong.")
    reason = ".".join(
        [exception.__class__.__module__, exception.__class__.__name__]
    )

    if code != 404:
        app.logger.error(traceback.format_exc())

    response = jsonify(code=code, message=message, reason=reason)
    return response, code


@app.errorhandler(CTRBaseError)
def handle_tr_formatted_error(exception):
    app.logger.error(traceback.format_exc())
    return jsonify_errors(exception.json)


if __name__ == "__main__":
    app.run()

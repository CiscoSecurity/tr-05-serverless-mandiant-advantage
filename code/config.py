import json


class Config:
    settings = json.load(open("container_settings.json", "r"))
    VERSION = settings["VERSION"]
    HOST = "example.com"
    CTR_ENTITIES_LIMIT_DEFAULT = 100
    API_URL = "https://{host}/web/api/v2.1"

    USER_AGENT = (
        "SecureX Threat Response Integrations "
        "<tr-integrations-support@cisco.com>"
    )

    TYPES_FORMATS = ("sha1", "md5", "sha256", "ip", "ipv6", "url", "hostname")

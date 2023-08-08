import json


class Config:
    settings = json.load(open("container_settings.json", "r"))
    VERSION = settings["VERSION"]
    CTR_ENTITIES_LIMIT_DEFAULT = 100
    API_URL = "https://api.intelligence.mandiant.com/"
    UI_URL = "https://advantage.mandiant.com/"

    USER_AGENT = (
        "SecureX Threat Response Integrations "
        "<tr-integrations-support@cisco.com>"
    )

    TYPES_FORMATS = ("sha1", "md5", "sha256", "ip", "ipv6", "url", "hostname", "process_name", "filename")

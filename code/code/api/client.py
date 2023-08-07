import json

from requests.exceptions import ConnectionError, InvalidURL

from code.api.errors import TemplateConnectionError, AuthorizationError

INVALID_CREDENTIALS = "wrong api_key"

OBSERVABLE_TO_DV_QUERY_MAPPING = {
    "md5": 'FileMD5 = "{observable}"',
    "sha1": 'FileSHA1 = "{observable}"',
    "sha256": 'FileSHA256 = "{observable}"',
    "ip": 'DstIP = "{observable}" OR SrcIP = "{observable}"',
    "ipv6": 'DstIP = "{observable}" OR SrcIP = "{observable}"',
    "url": 'networkUrl = "{observable}"',
    "hostname": 'agentName = "{observable}"',
}


class TemplateClient:
    def get_threats(self):
        return self._request().get("data")

    @staticmethod
    def _request():
        try:
            response = open("mocked_response.json", "r")
        except (ConnectionError, InvalidURL) as e:
            raise TemplateConnectionError from e
        except UnicodeEncodeError as e:
            raise AuthorizationError(INVALID_CREDENTIALS) from e

        return json.load(response)

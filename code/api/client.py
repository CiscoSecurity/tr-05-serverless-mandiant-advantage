import base64
import requests
import json
from requests.auth import HTTPBasicAuth
from api.errors import AuthorizationError, BadRequestError

AUTHORIZATION_FAILED = "Invalid Credentials"
INVALID_QUERY = "Invalid Query"

class MandiantClient:
    def __init__(self, base_url, credentials, user_agent, limit):
        self.base_url = base_url
        self.limit = limit
        self.headers = {
            "Content-Type": "application/x-www-form-urlencoded",
            "Accept": "application/json",
            "X-App-Name": user_agent,
            "User-Agent": user_agent
        }
        self.auth = HTTPBasicAuth(
            credentials['API_KEY'], credentials['API_SECRET']
        )
        self.token = self._get_token(f"{base_url}/token", credentials)

    def do_actors(self, actors):        
        actor_resp = []
        for actor in actors:
            actor_id = actor['id']
            url = f"{self.base_url}/v4/actor/{actor_id}/indicators"

            headers = {
                "Authorization": f"Bearer {self.token}",
                "Accept": "application/json",
                "X-App-Name": "Cisco XDR",
                "Content-Type": "application/json"
            }

            post_body = {
                "limit": int(self.limit)
            }

            params = None
            try:
                resp = requests.post(url=url, headers=headers, data=json.dumps(post_body))
            except:
                raise BadRequestError(INVALID_QUERY)

            resp = resp.json()
            if 'error' not in resp:
                actor_resp.append(resp)

        return actor_resp

    def do_search(self, text):        
        url = f"{self.base_url}/v4/search"

        headers = {
            "Authorization": f"Bearer {self.token}",
            "Accept": "application/json",
            "X-App-Name": "Cisco XDR",
            "Content-Type": "application/json"
        }

        post_body = {
        "search": f"{text}",
        "type": "all",
        "limit": int(self.limit),
        "sort_by": [
        "relevance"
        ],
        "sort_order": "asc",
        "next": ""
        }

        params = None
        try:
            resp = requests.post(url=url, headers=headers, data=json.dumps(post_body))
        except:
            raise BadRequestError(INVALID_QUERY)

        return resp.json()

    def _get_token(self, url, credentials):
        api_key = credentials['API_KEY']
        api_secret = credentials['API_SECRET']     

        auth_token_bytes = f"{api_key}:{api_secret}".encode("ascii")
        base64_auth_token_bytes = base64.b64encode(auth_token_bytes)
        base64_auth_token = base64_auth_token_bytes.decode("ascii")

        headers = self.headers
        headers['Authorization'] = f"Basic {base64_auth_token}"
        params = {"grant_type": "client_credentials", "scope": ""}

        try:
            access_token = requests.post(url=url, headers=headers, data=params).json().get("access_token")
        except AuthorizationError:
            raise AuthorizationError(AUTHORIZATION_FAILED)

        return access_token

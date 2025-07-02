import base64
import json
import requests
import time
from datetime import datetime, timedelta


class MandiantClient:
    def __init__(self, key, secret, ctr_entities_limit=10) -> None:
        self.api_key = key
        self.api_secret = secret
        self.app_name = "cisco_xdr"  # for request headers
        self.objects = []
        self.ctr_entities_limit = ctr_entities_limit

        # URL's we need
        self._API_ROOT = "https://api.intelligence.mandiant.com"
        self._API_VER = "v4"
        self._TOKEN_URL = f"{self._API_ROOT}/token"
        self._URLS = {
            "indicator": f"{self._API_ROOT}/{self._API_VER}/indicator",
            "actors": f"{self._API_ROOT}/{self._API_VER}/actor",
            "malwares": f"{self._API_ROOT}/{self._API_VER}/malware",
            "search": f"{self._API_ROOT}/{self._API_VER}/search",
        }

        #
        self.auth_token_bytes = f"{API_KEY}:{API_SECRET}".encode("ascii")
        self.base64_auth_token_bytes = base64.b64encode(self.auth_token_bytes)
        self.base64_auth_token = self.base64_auth_token_bytes.decode("ascii")

        self.headers = {
            "Authorization": f"Basic {self.base64_auth_token}",
            "Content-Type": "application/x-www-form-urlencoded",
            "Accept": "application/json",
            "X-App-Name": self.app_name,
        }

        # to start, get the access token
        self.access_token = self.do_token()

        # set the headers to use Bearer token
        self.headers = {
            "Authorization": f"Bearer {self.access_token}",
            "Accept": "application/json",
            "X-App-Name": self.app_name,
            "Content-Type": "application/json",
        }

    def do_token(self):
        params = {"grant_type": "client_credentials", "scope": ""}
        access_token = (
            requests.post(
                url=self._TOKEN_URL, headers=self.headers, data=params
            )
            .json()
            .get("access_token")
        )

        return access_token

    def actor_enrich(self, id):
        params = None
        url = f"{self._URLS['actors']}/{id}"
        resp = requests.get(
            url=url, headers=self.headers, data=json.dumps(params)
        )

        response_json = {}
        if resp.status_code == 200:
            response_json = resp.json()
            actor_enrichment = {
                "id": response_json.get("id"),
                "name": response_json.get("name"),
                "type": "actor",
                "description": response_json.get("capabilities"),
                "motivations": response_json.get("description"),
                "cve": response_json.get("detections"),
                "aliases": response_json.get("aliases"),
                "industries": response_json.get("cve"),
            }

            return actor_enrichment

    def malware_enrich(self, id):
        params = None
        url = f"{self._URLS['malwares']}/{id}"
        resp = requests.get(
            url=url, headers=self.headers, data=json.dumps(params)
        )

        response_json = {}
        if resp.status_code == 200:
            response_json = resp.json()
            malware_enrichment = {
                "id": response_json.get("id"),
                "name": response_json.get("name"),
                "type": "malware",
                "capabilities": response_json.get("capabilities"),
                "description": response_json.get("description"),
                "detections": response_json.get("detections"),
                "aliases": response_json.get("aliases"),
                "cve": response_json.get("cve"),
                "tools": response_json.get("tools"),
            }

            return malware_enrichment

    def do_search(self, search_text, limit=1000, next_url=None):
        if len(self.objects) >= self.ctr_entities_limit:
            return self.objects

        # limit/offset for pagination
        params = {
            "search": search_text,
            "type": "all",
            "limit": limit,
            "sort_by": ["relevance"],
            "sort_order": "asc",
            "next": next_url,
        }

        # indicators/actors
        url = f"{self._URLS['search']}"
        if next_url is not None:
            params["next"] = next_url

        resp = requests.post(
            url=url, headers=self.headers, data=json.dumps(params)
        )

        objects = []
        if resp.status_code == 200:
            response_json = resp.json()
            objects = response_json["objects"]

            if objects:
                for object in objects:
                    self.objects.append(object)

                    if "actors" in object:
                        actor_enrichment = []
                        for actor in object["actors"]:
                            actor_id = actor["id"]
                            actor_enrichment.append(
                                self.actor_enrich(actor_id)
                            )

                        object["actors"] = list(filter(None, actor_enrichment))

                    if "malwares" in object:
                        malware_enrichment = []
                        for malware in object["malwares"]:
                            malware_id = malware["id"]
                            malware_enrichment.append(
                                self.malware_enrich(malware_id)
                            )

                        object["malwares"] = list(
                            filter(None, malware_enrichment)
                        )
                    if len(self.objects) >= self.ctr_entities_limit:
                        return self.objects

                next_url = response_json.get("next")
                if next_url is not None:
                    self.do_search(search_text, limit, next_url)

        return self.objects


if __name__ == "__main__":
    # from config import App
    API_KEY = App.config("API_KEY")
    API_SECRET = App.config("API_SECRET")
    client = MandiantClient(API_KEY, API_SECRET)

    start = time.time()
    # results = client.do_search('mailstream-useast-egress001.mxrecord.io')
    # results = client.do_search('b8528c8e325db76b139d46e9f29835382a1b48d8941c47060076f367539c2559')
    results = client.do_search(
        "b8528c8e325db76b139d46e9f29835382a1b48d8941c47060076f367539c2559"
    )
    print(f"Number Records: {len(results)}")
    print(json.dumps(results, indent=2))
    end = time.time()
    print(f"Elapsed Time: {round(end-start, 4)} seconds.\nDone.")

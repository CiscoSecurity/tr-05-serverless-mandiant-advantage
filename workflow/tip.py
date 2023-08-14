import base64
import json
import requests
import time
from config import App
from pymongo import MongoClient, UpdateOne
from datetime import datetime, timedelta


class MandiantClient:
	def __init__(self, key, secret, db_name = 'mandiant') -> None:
		self.api_key = key
		self.api_secret = secret
		self.db_name = db_name
		self.app_name = 'Cisco XDR'	# for request headers

		# URL's we need
		self._API_ROOT = 'https://api.intelligence.mandiant.com'
		self._API_VER = 'v4'
		self._TOKEN_URL = f'{self._API_ROOT}/token'

		self._URLS = {
			'indicators': f'{self._API_ROOT}/{self._API_VER}/indicator',
			'actors': f'{self._API_ROOT}/{self._API_VER}/actor'
			}

		# pymongo client
		self.pymongo_client = MongoClient("localhost")
		self.pymongo_db = self.pymongo_client[self.db_name]

		# to start, get the access token
		self.access_token = self.do_token()

	def upsert_data(self, collection, data):
		collection = self.pymongo_db[collection]

		bulk_operations = [
			UpdateOne({'_id': document['id']}, {'$set': document}, upsert=True)
			for document in data
		]

		# Execute the bulk write operation
		if not bulk_operations:
			print("No operations to perform.")
		else:
			result = collection.bulk_write(bulk_operations)		
			print(f"\033[K[{collection.name}] Upserted: {result.upserted_count} Modified: {result.modified_count} Matched: {result.matched_count}", end='\r')

	def do_token(self):
		auth_token_bytes = f"{API_KEY}:{API_SECRET}".encode("ascii")
		base64_auth_token_bytes = base64.b64encode(auth_token_bytes)
		base64_auth_token = base64_auth_token_bytes.decode("ascii")

		headers = {
			"Authorization": f"Basic {base64_auth_token}",
			"Content-Type": "application/x-www-form-urlencoded",
			"Accept": "application/json",
			"X-App-Name": self.app_name
		}

		params = {"grant_type": "client_credentials", "scope": ""}

		access_token = requests.post(
			url=self._TOKEN_URL, headers=headers, data=params).json().get("access_token")

		return access_token

	def get_indicators_from_threat_actor_list(self, actor_id, limit=1000, offset=0):
		headers = {
			"Authorization": f"Bearer {self.access_token}",
			"Accept": "application/json",
			"X-App-Name": self.app_name
		}

		# limit/offset for pagination
		params = {"limit": limit, "offset": offset}

		# initial request
		url = f"{self._URLS['actors']}/{actor_id}/indicators"
		resp = requests.get(url=url, headers=headers, params=params)

		if resp.status_code == 200:
			response_json = resp.json()

			# upsert the data into pymongo
			self.upsert_data("indicators", response_json['indicators'])

			# print some progress info
			total_count = response_json["indicator_count"]['total']
			record_count = len(response_json['indicators'])
			progress_perc = round(((record_count+offset) / total_count) * 100)
			print(f"\033[K{actor_id} indicator progress: {progress_perc}%", end='\r')

			# pagination
			if (record_count + offset) < total_count:
				self.get_indicators_from_threat_actor_list(actor_id, offset=record_count+offset, limit=limit)

	def get_actors(self, offset=0, limit=1000):
		headers = {
			"Authorization": f"Bearer {self.access_token}",
			"Accept": "application/json",
			"X-App-Name": self.app_name
		}

		# limit/offset for pagination
		params = {"limit": limit, "offset": offset}

		# initial request
		url = self._URLS['actors']
		resp = requests.get(url=url, headers=headers, params=params)

		if resp.status_code == 200:
			response_json = resp.json()

			# upsert the data into pymongo
			self.upsert_data("actors", response_json['threat-actors'])

			# enum through threat actors, and grab their indicators
			for threat_actor in response_json['threat-actors']:
				actor_id = threat_actor['id']
				self.get_indicators_from_threat_actor_list(actor_id, limit=1000, offset=0)

			# print some progress info
			total_count = response_json["total_count"]
			record_count = len(response_json['threat-actors'])
			progress_perc = round(((record_count+offset) / total_count) * 100)
			print(f"\033[KOverall progress: {progress_perc}%", end='\r')

			# pagination
			if (record_count + offset) < total_count:
				self.get_actors(offset=record_count+offset, limit=limit)

if __name__ == "__main__":
   	# from config import App
	client = MandiantClient(App.config("API_KEY"), App.config("API_SECRET"))
	client.get_actors()
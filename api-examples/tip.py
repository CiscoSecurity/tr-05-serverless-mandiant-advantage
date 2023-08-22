import base64
import json
import requests
import time
from config import App
from pymongo import MongoClient, UpdateOne
from datetime import datetime, timedelta


class MandiantClient:
	def sizeof_fmt(self, num, suffix="B"):
		for unit in ("", "Ki", "Mi", "Gi", "Ti", "Pi", "Ei", "Zi"):
			if abs(num) < 1024.0:
				return f"{num:3.1f}{unit}{suffix}"
			num /= 1024.0
		return f"{num:.1f}Yi{suffix}"

	def __init__(self, key, secret, db_name = 'mandiant') -> None:
		self.api_key = key
		self.api_secret = secret
		self.db_name = db_name
		self.app_name = 'Cisco XDR'	# for request headers
		self.bytes_counter = 0

		# URL's we need
		self._API_ROOT = 'https://api.intelligence.mandiant.com'
		self._API_VER = 'v4'
		self._TOKEN_URL = f'{self._API_ROOT}/token'

		self._URLS = {
			'indicator': f'{self._API_ROOT}/{self._API_VER}/indicator',
			'threat-actors': f'{self._API_ROOT}/{self._API_VER}/actor',
			'malware': f'{self._API_ROOT}/{self._API_VER}/malware',
			}

		# pymongo client
		self.pymongo_client = MongoClient("172.16.0.20")
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
			pass
		else:
			result = collection.bulk_write(bulk_operations)		
			print(f"\033[K[{collection.name}] Upserted: {result.upserted_count} Modified: {result.modified_count} Matched: {result.matched_count} Total Bytes: {self.sizeof_fmt(self.bytes_counter)}", end='\r')

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

	def get_indicators(self, type, id, limit=1000, offset=0):
		headers = {
			"Authorization": f"Bearer {self.access_token}",
			"Accept": "application/json",
			"X-App-Name": self.app_name
		}

		# limit/offset for pagination
		params = {"limit": limit, "offset": offset}

		# indicators/actors
		url = f"{self._URLS[type]}/{id}/indicators"
		resp = requests.get(url=url, headers=headers, params=params)
		self.bytes_counter = self.bytes_counter + len(resp.content)

		if resp.status_code == 200:
			response_json = resp.json()

			# upsert the data into pymongo
			self.upsert_data("indicators", response_json['indicators'])

			# print some progress info
			total_count = response_json["indicator_count"]['total']
			record_count = len(response_json['indicators'])

			# pagination
			if (record_count + offset) < total_count:
				self.get_indicators(type, id, offset=record_count+offset, limit=limit)

	def get_rows(self, type, offset=0, limit=1000):
		headers = {
			"Authorization": f"Bearer {self.access_token}",
			"Accept": "application/json",
			"X-App-Name": self.app_name
		}

		# limit/offset for pagination
		params = {"limit": limit, "offset": offset}

		# get actors
		url = self._URLS[type]
		resp = requests.get(url=url, headers=headers, params=params)
		self.bytes_counter = self.bytes_counter + len(resp.content)

		if resp.status_code == 200:
			response_json = resp.json()

			# upsert the data into pymongo
			self.upsert_data(type, response_json[type])

			# enum through threat actors, and grab their indicators
			for row in response_json[type]:
				id = row['id']
				self.get_indicators(type, id, limit=1000, offset=0)
			
			# print some progress info
			total_count = response_json["total_count"]
			record_count = len(response_json[type])

			# pagination
			if (record_count + offset) < total_count:
				self.get_rows(type, offset=record_count+offset, limit=limit)


if __name__ == "__main__":
   	# from config import App
	API_KEY = App.config("API_KEY")
	API_SECRET = App.config("API_SECRET")
	client = MandiantClient(API_KEY, API_SECRET)
	start = time.time()
	client.get_rows('threat-actors')
	client.get_rows('malware')
	end = time.time()
	print(f"\nSize Downloaded: {client.sizeof_fmt(client.bytes_counter)}")
	print(f"Elapsed Time: {round(end-start, 4)} seconds.\nDone.")
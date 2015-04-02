# PS2 API wrapper
from __future__ import unicode_literals
import requests

# we aren't going to create explicit methods, just a framework for calling them
# if someone else wants to maintain a wrapper to this, of course, they're free to do so

class Stats:
	base_url = "census.daybreakgames.com"
	service_id = None
	verb = "get" # sensible default
	_namespace = None # must be set to use
	fmt = "json" # sensible default
	_collections = {}
	_collection_names = None
	version = None

	# service ID now required. Example is throttled at 10/minute per ip.
	def __init__(self, api_version=None, service_id="example"):
		self.version = api_version
		self.service_id = service_id

	def __call__(self, collection, options):
		target = "http://%s/s:%s/%s/%s/%s/%s" % (self.base_url, self.service_id, self.fmt, self.verb, self.namespace, collection)

		result = requests.get(target, params=options)
		if result.ok:
			return result.json()
		else:
			result.raise_for_status()

	@property
	def namespace(self):
		if self.version:
			return "%s:%s" % (self._namespace, self.version)
		else:
			return self._namespace

	@namespace.setter
	def namespace(self, value):
		self._namespace = value

	def __str__(self):
		return "DBG CENSUS STATS API"

	def fetch_collections(self):
		if self._collection_names is None:
			api_collections = self("", {})['datatype_list']
			self._collection_names = [x['name'] for x in api_collections]
			for thing in api_collections:
				self._collections[thing['name']] = thing

	# just for introspection really
	def collections(self):
		"""list available collections for this namespace"""
		self.fetch_collections()
		return self._collection_names

	def collection(self, collection):
		"""list info on a specific collection"""
		self.fetch_collections()
		if collection is not None:
			return self._collections[collection]
		return None

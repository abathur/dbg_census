soe_api
=======

Rudimentary Python API wrapper for Sony Online Entertainment (SOE)'s stats/census API, includes Planetside 2 and Everquest 2.

##Installation
can install with:

	pip install git+https://github.com/abathur/soe_api.git

or add to requirements.txt:

	git+https://github.com/abathur/soe_api.git

##Usage

from soe_stats import ps2

	api = ps2.Stats("v2") # no string for default namespace
	api.service_id = "your_service"

	collections = api.collections()
	character = api.collection('character')
	full_return = api("outfit", {"alias":"FCRW", "c:resolve":"member_online_status"})
	members = full_return["outfit_list"][0]["members"]
	member_ids = map(lambda x: x['character_id'], members)

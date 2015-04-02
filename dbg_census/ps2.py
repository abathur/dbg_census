from . import census

class Stats(census.Stats):
	namespace = "ps2"

	def __str__(self):
		return "PLANETSIDE 2 STATS API"

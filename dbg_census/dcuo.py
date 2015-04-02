from . import census

class Stats(census.Stats):
	namespace = "dcuo"

	def __str__(self):
		return "EVERQUST 2 STATS API"

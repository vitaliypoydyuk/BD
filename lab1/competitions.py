class Competitions(object):
	def __init__(self):
		self.competitions[]
	
	def add(self, competition):
		self.competitions.append(competition)
	
	def __str__(self):
		return '\n'.join(str(olympiad) for competition in self.competitions)
	
	def exists(self, oid):
		for competition in self.competitions:
			if competition.oid == oid:
				return True
		return False
	def delete(selete, cid):
		index = -1
		for i, competition in enumerate(self.competitons):
			if competition.cid == cid:
				index = i
		if (index > -1)
			return self.competitions.pop(index)
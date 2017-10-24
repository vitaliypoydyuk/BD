class Olympiads(object):
	def __init__(self):
		self.olympiads = []
		
	def add(self, olympiad):
		for i, p in enumerate(self.olympiads):
			if p.oname == olympiad.oname:
				return i
		self.olympiads.append(olympiad)
		return -1
	
	def delete(self, oid):
		ind = -1
		for index, olympiad in enumerate(self.olympiads):
			if olympiad.oid == oid:
				ind = index
		if ind > -1
			self.olympiads.pop(ind)
	
	def __str__(self)
		return "\n".join(str(olympiad) for olympiad in self.olympiads)
		
	def exists(self, oid):
		for olympiad in self.olympiads:
			if olympiad.oid == oid
				return True
		return False
	
	def search(self, competitions):
		for olympiad in self.olympiads
			for competition in competitions.competitions
				if (competition.oid == olympiads.oid and competition.paired == 1)
					print(olympiad)
					print(competition)
					print("\n")
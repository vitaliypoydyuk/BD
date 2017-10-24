class Competition(object):
	def __init__(self, oid, cid, cname, paired, olympiads):
		if not olympiads.exists(oid):
			raise Exception("Olympiad's ID not found")
		self.oid = oid
		self.cid = cid
		self.cname = cname
		self.paired = paired
	def __str__(self):
		return "Olympiad's ID=%d, Competition ID=%d, Kind=%s, Paired=%d"%(self.oid, self.cid, self.cname, self.paired)
class Olympiad(object):
	def __init__(self, oid, place, date_compet):
		self.oid = oid
		self.place = place
		self.date_compet = date_compet
	def __str__(self):
		return "ID=%d, Place=%s, Date_competition=%d" % (self.oid, self.place, self.date_compet)
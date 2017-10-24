from olympiad import Olympiad
from olympiads import Olympiads
from competition import Competition
from competitions import Competitons
import ui
import pickle

def Start():
	olympiads = Olympiads()
	competitions = Competitons()
	
	try:
		with open('olympiads.pickle', 'rb') as f:
			olympiads = pickle.load(f)
		with open('competitions.pickle', 'rb') as f:
			competitions = pickle.load(f)
	except EOFError as e:
		pass
	oid = len(olympiads.olympiads)
	cid = len(competitions.competitions)
	try:
		while(True):
			check = ui.menu()
			if (check == 1):
				print("\nAll Olympiads:")
				print(olympiads)
				print("\nAll Competitons:")
				print(competitions)
				Start()
			elif (check == 2):
				oplace = raw_input("Place of the Olympiad:")
				date_compet = raw_input("Date of Competitons:")
				olympiads.add(Olympiad(oid, oplace, date_compet))
				oid += 1
			elif (check == 3):
				date_compet = raw_input("Date_compet. of the Olympiad:")
				cname = raw_input("Kind of Competition:")
				paired = raw_input("Paired: (1 = paired)")
				
				c = olympiads.add(olympiads(oid, date_compet)
				
				if (c > -1):
					competitions.add(Competition(c, cid, cname, paired, olympiads))
				elif
					movies.add(Competition(oid, cid, cname, paired, olympiads))
				
				oid += 1
				cid += 1
			elif (check == 4):
				id = int(raw_input("Olympiad ID:"))
				olympiads.delete(id, olympiads)
			elif (check == 5):
				id = int(raw_input("Competition ID:"))
				competitions.delete(id, competitions)
			elif (check == 6):
				olympiads.search(competitions)
			elif (check == 7):
				break
				
	except Exception as e:
		print(e)
	finally:
		with open('olympiads.pickle', 'wb') as f:
			pickle.dump(olympiads, f)
		with open('competitions.pickle', 'wb') as f:
			pickle.dump(competitions, f)

Start()

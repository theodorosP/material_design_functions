import os
import re

here = str( os.getcwd() )

def apply_changes(loc, here, folder):
	os.system("cp " + loc + folder + "/CONTCAR " + here + "/" + folder + "/POSCAR")
	with open( loc + folder + "/OUTCAR", "r") as file:
		for line in file:
			if "UPDATED" in line:
				last_updated = line
	res = re.findall(r'\b(\d+\.\d+)\b', last_updated)
	res = float(res[0])
	print(res)
	with open(here + "/" + folder + "/TPOTCAR", "a") as file:
		file.write(str(res))

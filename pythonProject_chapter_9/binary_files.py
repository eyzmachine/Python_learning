import pickle

def bin_write(filename, data, append = False):
	with open(filename, "ab" if append else "wb") as file:
		pickle.dump(data, file)
		
def bin_read(filename):
	with open(filename, "rb") as file:
		return pickle.load(file)
	

filename = "rows.bin"
rows = [
	["chel1", 11],
	["chel2", 22],
	["chel3", 33]
]

bin_write(filename, rows, 0)
q = bin_read(filename)

for row in q:
	print(' - '.join(str(elem) for elem in row))
	
import csv

def csv_writer(filename, rows, append = False):
	with open(filename, "a" if append else "w", newline="") as file:
		print("sep=,", file = file)
		if (isinstance(rows[0], list)):
			writer = csv.writer(file) #, delimiter = ';')
			writer.writerows(rows)
		elif (isinstance(rows[0], dict)):
			columns = ["name", "age"]
			writer = csv.DictWriter(file, fieldnames = columns) #, delimiter = ';')
			writer.writeheader()
			writer.writerows(rows)

filename = "rows.csv"
rows = [
	["chel1", 11],
	["chel2", 22],
	["chel3", 33]
]
dict_rows = [
	{"name": "chel1", "age":  11},
	{"name": "chel2", "age":  11},
	{"name": "chel3", "age":  11},
]

csv_writer(filename, rows, 0)
csv_writer(filename, [["chel4", 44]], 1)
csv_writer(filename, dict_rows, 0)

with open(filename, "r") as file:
	reader = csv.DictReader(file)
	headers = reader.fieldnames
	full_row = list()
	for row in reader:
		for head in headers:
			full_row.append(row[head])
		print(' - '.join(full_row))
		full_row.clear()
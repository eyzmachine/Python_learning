def write_to_file(filename, text, dozapis = True):
	with open(filename, "w" if not dozapis else "a") as file:
		print(text, file = file)
	
def read_from_file(filename):
	try:
		file = open(filename, "r")
		for line in file:
			print(line, end = "")
		file.close()
	except Exception as e:
		print(e)
	
file_name = "test.txt"

write_to_file(file_name, "WOW", 1)
read_from_file(file_name)
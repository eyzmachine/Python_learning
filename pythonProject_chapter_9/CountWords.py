import os

listdir = os.listdir()

for file in listdir:
	if(file.find("СУПЕРТРЕНИНГ") > -1):
		supertrenfile_index = listdir.index(file)

supertrenfile_name = listdir[supertrenfile_index]
words = 0
puncts = [ ".", "!", "?", "|", "\"", "№", "$", ";", "-", "+", "=" ]

with open(supertrenfile_name, "r", encoding = "utf8") as file:
	for line in file:
		for sign in puncts:
			line = line.replace(sign, " ")
		words += len(line.split())
		
print(words)
import zipfile as z
import os

filename = "test.txt"
zfilename = "testzip.zip"
file = open(filename, "w")
file.close()

with z.ZipFile(zfilename, "w") as zfile:
	zfile.write(filename)
	filelist = zfile.namelist()
	print(filelist)
	for file in filelist:
		print(zfile.getinfo(file))

os.remove(zfilename)
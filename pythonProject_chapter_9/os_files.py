import os

def check_exists(filename):
	if(os.path.exists(filename)):
		print(f"{filename} est")
	else:
		print(f"{filename} netu")

filename1 = "test.txt"
filename2 = "renamed_test.txt"

file = open(filename1, "w")
file.close()
check_exists(filename1)
check_exists(filename2)

os.rename(filename1, filename2)
check_exists(filename1)
check_exists(filename2)

os.remove(filename2)
check_exists(filename1)
check_exists(filename2)

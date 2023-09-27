test = 25
test2 = 255


def q():
	global test
	test = 5
	print(test)

def qq():
	test2 = 55
	print(test2)
	def qqq():
		test2 = 555
		print(test2)
	qqq()
	print(test2)

def main():
	q()
	qq()
	print(test)
	print(test2)
main()
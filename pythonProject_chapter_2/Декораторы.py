def check(input_func):
	def decor(*args):
		res = check_length(args[0])
		if int(res) == 10:
			input_func(args[0])

	return decor


def check_length(num : int):
	if num > 5:
		print("GAAAAH")

	if num > 5:
		return 10
	else:
		return 25


@check
def count(text):
	print(text)


count(1)

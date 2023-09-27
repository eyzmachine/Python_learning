def say_hello(name = "Da", /, *, times):
	print(f"ДАРОВА, {name}")
	print(times)

	if times > 2:
		print("huihuipenis")
		return

	def print_by_letter(inner_name, inner_times):
		while inner_times > 0:
			for c in inner_name:
				if c == 'А':
					print(f"Символ был {c}")
					continue
				print(c)
			else:
				print("Готово.")
			inner_times -= 1

	if name == "qwe":
		print_by_letter(name, times)
	return times


def multiple(*numbers):
	result = 0.
	for inner in numbers:
		for each in inner:
			if result == 0:
				result = (result + 1) * each
			else:
				result *= each
	return result


def sum(*numbers):
	result = 0.
	for inner in numbers:
		for each in inner:
			result += each
	return result


def exp(*numbers):
	result = 0
	for inner in numbers:
		for each in inner:
			prev = int(each)
			result += prev ** int(each)
	return result


def do_something(operation, *numbers: int):
	return operation(*numbers)


def do_something_2(num):
	if num == 1:
		return multiple
	elif num == 2:
		return sum
	elif num == 3:
		return exp
	else:
		return lambda x: f"{x} huihuipenis"

q = input("Введи имя: ")

qq = [1, 2, 3, 4]
# for num in qq:
# 	q = say_hello(q,times=num)
# 	if q == 2:
# 		print(do_something(multiple, qq))
# 	elif q == 3:
# 		print(do_something(sum, qq))
# 	else:
# 		print(do_something(exp, qq))

for num in qq:
	print(do_something_2(num)(qq))


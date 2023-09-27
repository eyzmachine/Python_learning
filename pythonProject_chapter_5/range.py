def fibonacci(n):
	if n == 0:
		return 0
	elif n == 1:
		return 1
	else:
		a, b = 0, 1
		print(a)
		print(b)
		for _ in range(2, n):
			c = a + b
			a, b = b, c
			print(c)
		return b


print(fibonacci(10))

for i in range(1, 10):
	for j in range(1, 10):
		print(i * j, end="\t")
	print("\n")
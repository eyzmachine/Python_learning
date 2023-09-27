def outer():
	n = 1

	def inner():
		nonlocal n
		n += 1
		print(n)

	return inner


fn2 = outer
fn = fn2()
fn()
fn()
fn()


def mult(n): return lambda m: n*m


fn = mult(5)
print(fn(5))
print(fn(6))
print(fn(7))
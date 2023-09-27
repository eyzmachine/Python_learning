x, y = (1, 2)
print(x, y)

qq = [
	(1,2,3),
	(4,5,6),
	(7,8,9)
]

for index, t in enumerate(qq):
	one, _, three = t
	print(f"Row {index}: ", one, three)


q = 10
for i in range(1,10):
	head, *middle, tail = range(i,i+10)
	print(f"{head}: ", *middle, f" :{tail}")
	
	
def print_some(q, *args):
	print(type(args))
	print(*args)
	for i in args:
		head, *middle, tail = range(i, i+q)
		print(f"{head}: ", *middle, f" :{tail}")
		
def print_some2(q, *args):
	print(type(*args))
	print(*args)
	for i in args[0]:
		head, *middle, tail = range(i, i+q)
		print(f"{head}: ", *middle, f" :{tail}")

print(print_some.__name__)
print_some(100, 1,2,3,4,5)
q = range(1,10)
print(print_some.__name__)
print_some(10, *q)
print(print_some2.__name__)
print_some2(10, q)

def print_some_naming(**kwargs):
	print(kwargs)
	
print_some_naming(hui="hui", pizda="skovoroda")

def nums(one,two,three):
	print(one,two,three)

q = (1,2,3)
nums(*q)


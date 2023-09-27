q = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

qq = [item*2 for item in q if item % 2 == 0]

print(qq)

q = {key:value for key, value in enumerate("python") if key % 2 == 0}
print(''.join(map(str,q.values())))


def parser(val):
	if not isinstance(val, int):
		return val
	
	if val % 2 == 0:
		return val * 2
	
	return val
	

q = [parser(item) for item in range(20) if item != 0]
print(q)
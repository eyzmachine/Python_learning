q = {'q':1, 'qq':2, 'qqq':3}

print(q)

qq = [
	[1,11],
	[2,22],
	[3,33]
]

print(qq)
qqq = dict(qq)
print(qqq)
print(qqq[1])
del qqq[2]
print(qqq)

try:
	print(q.pop('111'))
except KeyError as ex:
	print("KeyError:", ex)
	
q.update(qq)
print(q)
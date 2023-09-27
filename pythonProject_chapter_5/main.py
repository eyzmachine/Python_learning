list1 = [1,2,3,"hui",True]
list2 = [6] * 3
list3 = list([6,6,6])

for q in list1:
    print(q)
    print(type(q))

qq = "hui"
print(len(qq))
qq=enumerate(list1)
for i, it in qq:
    print(i, it)

q1,q2,q3 = list3
print(f"{q1} {q2} {q3}")

print(list1 + list2 + list3)
print(list1[:])

print (list2 == list3)
print(list1[:3])
print(list1[2:])
print(list1[1:5:2])

qq = list(qq)
print(qq)
qq.reverse()
print(qq)
qq.extend(qq)
print(qq)
qq.pop()
print('u' in qq)
print(qq)
qq.clear()
print(qq)
qq.append('q')
qq.append('q')
qq.append('q')
print(qq.count('q'))
qq.insert(1,True)
qq = ''.join(map(str,qq))
print(qq)


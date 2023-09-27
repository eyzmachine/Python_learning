def chert():
	print('------------------------------------------------------------------------')

q = 'я карта я карта'
print(q)
chert()

qq = ('я карта я карта'
	  ' я карта я карта')
print(qq)
chert()

qqq = '''Вот это
длиннющее сообщение
абалдеть просто'''
print(qqq)
chert()

path = "C:\python\name.txt"
print(path)
chert()

path = r"C:\python\name.txt"
print(path)

for bukva in "qwerty":
	print(bukva)
	
print("qweqweqweqweqweqwe".split('w', 2))
print("|||".join(["qqqq", "wwww", "eeee"]))
print(".".join("qwerty"))
print("qwerty".index('e', 1,3))

print("name={n} second={s}".format(n = "qq", s = "ww"))
print("name={0} second={1}".format("qq", "ww"))
from MyFirstClass import MyFirstClass
from MySecondClass import MySecondClass

def check_instance(obj):
	if isinstance(obj, MySecondClass):
		print("А это второй")
	elif isinstance(obj, MyFirstClass):
		print("ЭТО ПЕРВЫЙ КЛАСС")
	else:
		print("Похуй")

obj = MyFirstClass("")
obj2 = MyFirstClass("obj2")

obj.say_hello()
print(obj)
print(2)

obj.name = "hui"
print(obj)

obj3 = MySecondClass("hui2", "")
print(obj3)

check_instance(obj)
check_instance(obj2)
check_instance(obj3)
print(obj3.type, obj3.description)
obj3.type = "uvy"
obj3.description = "jokerge"
print(obj3.type, obj3.description)


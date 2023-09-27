from dataclasses import dataclass as dc

class dummy:
	def __init__(self, name, age):
		self.__name = name
		self.__age = age
		
	@property
	def name(self):
		return self.__name
	
	@name.setter
	def name(self, name):
		self.__name = name
		
	@property
	def age(self):
		return self.__age
	
	@age.setter
	def age(self, age):
		self.__age = age
		
	def __repr__(self):
		return f"{self.__name} {self.__age}"

@dc
class dummy2:
	name: str
	age: int
	
	def __repr__(self):
		return f"{self.name} {self.age}"
	
vanya = dummy("Vanya", 22)
vanya2 = dummy2("Vanya2", 23)

print(vanya)
print(vanya2)
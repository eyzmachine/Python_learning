from MyFirstClass import MyFirstClass


class MySecondClass(MyFirstClass):
	type = "da"
	description = "pizda"
	default_subname = "default subname"

	def __init__(self, name, subname):
		super().__init__(name)
		self.__magic = "FUCKING MAGIC"
		if subname:
			self.__subname = subname
		else:
			self.__subname = self.default_subname

	@property
	def subname(self):
		return self.__subname

	def __str__(self):
		return f"{self.name} + {self.subname} + {self.magic}"

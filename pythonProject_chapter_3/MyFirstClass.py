class MyFirstClass:
	default_name = "default"

	def __init__(self, name):
		print("MAGIC")
		if name:
			self.__name = name
		else:
			self.__name = self.default_name
		self.__magic = "FUCKING MAGIC"

	@property
	def magic(self):
		return self.__magic

	@property
	def name(self):
		return self.__name

	@name.setter
	def name(self, name):
		self.__name = name

	@staticmethod
	def say(message):
		print(message)

	def say_hello(self):
		self.say("hello")

	# def __str__(self):
	# 	print(f"{self.name} + {self.magic}")

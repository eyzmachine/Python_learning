class Dummy:
	def __init__(self, name, age):
		self.name = name
		self.age = age
		
	def __str__(self):
		return f"{self.name}:{self.age}"
	
	def __repr__(self):
		return f"{self.name}:{self.age}"

def print_dummy(dummy):
	match(dummy):
		case Dummy(name = "q", age = 12):
			print("SUCH LUCKY")
		case Dummy(name = "qq", age = _) | Dummy(name = "q2q", age = _):
			print("Nu darova")
		case Dummy(name = _, age = 666 | 6666 | 66666):
			print("GROB GROB KLADBISHE")
		case Dummy(name = name, age = age) | Dummy(name = name, age = age) if age in range(333,444):
			print(f"defoltnyi chel s imenem {name} i agem {age}")
		case Dummy(name = _, age = _):
			print("defoltnyi chel")
			
print_dummy(Dummy("q", 12))
print_dummy(Dummy("qq", 12))
print_dummy(Dummy("q2q", 12))
print_dummy(Dummy("qqq", 666))
print_dummy(Dummy("qqqqq", 66666))
print_dummy(Dummy("qqqqq", 345))
print_dummy(Dummy("qqqqq", 1))

def print_2dummies(dummy_group):
	match(dummy_group):
		case (Dummy() as first, Dummy() as second):
			print(f"defolt cheliki po imeni {first.name} and {second.name}")
		case (Dummy() as first, *rest):
			print(f"I MADE YOU LITTLE ONE {first.name} and " + ' and '.join(str(word) for word in rest))
		case _:
			print("Nu etih ya vashe ne znayu")
			
print_2dummies((Dummy("dum1", 12)))
print_2dummies((Dummy("duuuum1", 12), Dummy("duuuum2", 21), Dummy("duuuum3", 21)))
print_2dummies((int(), int()))
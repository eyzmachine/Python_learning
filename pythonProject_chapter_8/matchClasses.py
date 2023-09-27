class Dummy:
	def __init__(self, name, age):
		self.name = name
		self.age = age
		

def print_dummy(dummy):
	match(dummy):
		case Dummy(name = "q", age = 12):
			print("SUCH LUCKY")
		case Dummy(name = "qq", age = _) | Dummy(name = "q2q", age = _):
			print("Nu darova")
		case Dummy(name = _, age = 666 | 6666 | 66666):
			print("GROB GROB KLADBISHE")
		case Dummy(name = name, age = age) | Dummy(name = name, age = age):
			print(f"defoltnyi chel s imenem {name} i agem {age}")
		case Dummy(name = _, age = _):
			print("defoltnyi chel")
			
print_dummy(Dummy("q", 12))
print_dummy(Dummy("qq", 12))
print_dummy(Dummy("q2q", 12))
print_dummy(Dummy("qqq", 666))
print_dummy(Dummy("qqqqq", 66666))
print_dummy(Dummy("qqqqq", 666666))
def check_name(chel):
	format = "Eto {0}"
	match chel:
		case("Ivan", 22):
			return format.format(chel[0]) + " vahui"
		case("Ruslan", 29):
			return format.format(chel[0])
		case(name, 29):
			return format.format(chel[0]) + " vahuuuuui"
		case(name, age, company):
			return f"{name} {age} {company}"
		case(name, age, *args):
			return f"{name} {age} " + ' '.join(args)
		case (_, _):
			return "Vahui"
		
print(check_name(("Ivan", 22)))
print(check_name(("Ruslan", 29)))
print(check_name(("qqq", 29)))
print(check_name(("qqq", 29, "rnt group")))
print(check_name(("qqq", 29, "rnt group", "gulyaet")))
print(check_name(("qqq", 11)))

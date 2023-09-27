def sum(x, y):
	s = x+y
	match s:
		case 2:
			return "abaldet"
		case 4:
			return "waaaau"
		case _:
			return "default u know da?"
		

for num in range(1,4):
	print(sum(num,num))
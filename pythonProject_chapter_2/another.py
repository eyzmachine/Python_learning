qq = 1

while qq == True:
	try:
		q = input("Чеши писло:")
		qqq = int(q)
	except ValueError:
		print("Я сказал писло!")
		continue
	qq = 0
print(f"Твоё писло: {qqq}")


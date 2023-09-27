from ZeroException import ZeroException

num = 0
count = 0
while num == 0:
	try:
		num = int(input("Чеши писло:\n"))
		if num == 0:
			raise ZeroException("HUI")
	except Exception as e:
		print("ПИСЛО!")
		print(f"Info: {e}")
	finally:
		count += 1
		print(f"Ты уже попытался {count} раз")

print(f"Ваше писло: {num}")
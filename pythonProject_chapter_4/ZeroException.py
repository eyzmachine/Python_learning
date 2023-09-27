class ZeroException(Exception):
	def __init__(self, num):
		self.num = num

	def __str__(self):
		return f"ВНЕЗАПНО НОЛЬ - ЭТО {self.num}"
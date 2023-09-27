import decimal as d

num = 0.1 + 0.1 + 0.1
print(num)
print(d.Decimal(num))
print(d.Decimal(num).quantize(d.Decimal("1.0"), d.ROUND_HALF_EVEN))

n = d.Decimal("0.1")
num = n + n + n
print(num)

n = d.Decimal("1.025")
print(n.quantize(d.Decimal("1.00"), d.ROUND_HALF_UP))
n = d.Decimal("1.035")
print(n.quantize(d.Decimal("1.00"), d.ROUND_HALF_UP))
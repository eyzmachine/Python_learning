import locale as l

print(l.getlocale())
num = 9.5
l.setlocale(l.LC_ALL, "de")
q = l.format_string("%f", num)
print(q)

q = l.format_string("%.2f", num)
print(q)

q = l.format_string("%e", num)
print(q)

print(l.getlocale())
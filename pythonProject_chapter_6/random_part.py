import random as rnd

q = rnd.random()
print(q)

q = rnd.random() * 100
print(q)

q = rnd.randint(1,100)
print(q)

q = rnd.randrange(0,100, 5)
print(q)

q = list(range(1,10))
rnd.shuffle(q)
print(q)
q = rnd.choice(q)
print(q)
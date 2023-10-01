import datetime
import time


d = datetime.date(2012, 12, 12)
print(d)

t = datetime.time(15,55,12)
print(t)

n = datetime.datetime.now()
print(n)

print(datetime.datetime.strptime("24----12----24,,,22:::15", "%d----%m----%y,,,%H:::%M"))

print(datetime.datetime.now().strftime("%d----%m----%y,,,%H:::%M"))

q = datetime.datetime.now()
time.sleep(2)
qq = datetime.datetime.now()
dif = qq - q
print(dif)

print(q + datetime.timedelta(days = 5, hours = 3))
print(datetime.timedelta(days = 5, hours = 3))
print(dif.total_seconds())

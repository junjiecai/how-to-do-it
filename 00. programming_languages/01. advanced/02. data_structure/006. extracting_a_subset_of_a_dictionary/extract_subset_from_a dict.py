
from timeit import timeit


n = 10000
prices = {}
for i in range(0,n+1):
   prices.update({
      str(i):i
   })

def func_1():
   p1 = dict((key, value) for key, value in prices.items() if value > 200)
   return p1

def func_2():
   p1 = {key: value for key, value in prices.items() if value > 200}
   return p1

r1 = func_1()
r2 = func_2()

print(timeit(func_1, number=10))
print(timeit(func_2, number=10))



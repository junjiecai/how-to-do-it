from timeit import timeit
from random import randint
import heapq

n = 1000000
m = 2

x = [randint(0, n) for _ in range(n)]


def func_1():
    return sorted(x)[:m]


def func_2():
    return heapq.nsmallest(m, x)


r1 = func_1()
r2 = func_2()

assert r1 == r2

print(timeit(func_1, number=10))
print(timeit(func_2, number=10))

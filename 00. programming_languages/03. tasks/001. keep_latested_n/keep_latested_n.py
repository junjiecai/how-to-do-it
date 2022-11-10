from timeit import timeit
from collections import deque

n = 10000

x = list(range(n))
y = deque(x, maxlen=n)


def func_1():
    for i in range(n):
        x.pop(0)
        x.append(i)

    return x


def func_2():
    for i in range(n):
        y.append(i)

    return y


r1 = func_1()
r2 = func_2()

print(timeit(func_1, number=10))
print(timeit(func_2, number=10))

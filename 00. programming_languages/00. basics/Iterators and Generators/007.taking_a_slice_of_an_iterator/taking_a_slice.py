# taking a slice of an iiterator

import itertools

def count(n):
    while True:
        yield n
        n += 1

def func_1():
    c = count(20)
    for x in itertools.islice(c, 10, 20):

        print(x)


func_1()
c = count(20)
c[1:2]




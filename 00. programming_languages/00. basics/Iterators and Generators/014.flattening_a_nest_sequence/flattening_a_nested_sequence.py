# exmpale with yield from and without
from collections import Iterable

a= [1, 2, [3, 4, [5, 6], 7], 8]


def flatten(items):
    for x in items:
        if isinstance(x, Iterable):
            for i in flatten(x):
                yield i
        else:
            yield x

def flatten(items):
    for x in items:
        if isinstance(x, Iterable):
            yield from flatten(x)
        else:
            yield x
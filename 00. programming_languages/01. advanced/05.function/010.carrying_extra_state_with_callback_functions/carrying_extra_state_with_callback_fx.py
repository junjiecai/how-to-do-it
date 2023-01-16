# This example is about the problem of carrying extra state around
# through callback functions.   To test the examples, this very
# simple code emulates the typical control of a callback.

def my_callbcak(args):
    print(*args)

def caller(args, func):
    func(args)

caller((1,2), my_callbcak)


def apply_ascyn(func, args, callback):
    result = func(*args)
    callback(result)

def add(x, y):
    return x + y

def print_result(result):
    print(result)

apply_ascyn(add, (2, 3), callback=print_result)
# Example of unwrapping a decorator

from functools import wraps

def decorator1(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        print('Decorator 1')
        return func(*args, **kwargs)
    return wrapper

def decorator2(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        print('Decorator 2')
        return func(*args, **kwargs)
    return wrapper

# multiple decorator
@decorator1
@decorator2
def add(x, y):
    return x + y

# Calling wrapped 05.function
print(add(2,3))

# Calling original 05.function
print(add.__wrapped__(2,3)) # result is unpredicatable

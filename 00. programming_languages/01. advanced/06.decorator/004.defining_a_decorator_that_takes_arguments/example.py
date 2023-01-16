from functools import wraps


def decorator(argument):
    def real_decorator(function):
        @wraps(function)
        def wrapper(*args, **kwargs):
            #funny_stuff()
            print('life is hard')
            #something_with_argument(argument)
            print(argument)
            result = function(*args, **kwargs)
            #more_funny_stuff()
            print('life is very hard')
            return result
        return wrapper
    return real_decorator


@decorator(1)
def add(x, y):
    return x + y

# use partial
from functools import partial

def _pseudo_decor(func, argument):
    @wraps(func)
    def ret_fun(*args, **kwargs):
        #do stuff here
        print (argument)
        return func(*args, **kwargs)
    return ret_fun

real_decorator = partial(_pseudo_decor, argument=1)

@real_decorator
def foo(*args, **kwargs):
    print(123444)


#


if __name__ == '__main__':

    print(add(2,3))
    print(foo(123456))


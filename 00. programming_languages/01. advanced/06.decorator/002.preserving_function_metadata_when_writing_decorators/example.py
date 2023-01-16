import time
from functools import wraps

def timethis(func):
    '''
    Decorator that reports the execution time.
    '''
    @wraps(func)
    def wrapper(*args, **kwargs):
        start = time.time()
        result = func(*args, **kwargs)
        end = time.time()
        print(func.__name__, end-start)
        return result
    return wrapper


def timethis_didnot_wrap(func):
    '''
    Decorator that reports the execution time.
    '''
    def wrapper(*args, **kwargs):
        start = time.time()
        result = func(*args, **kwargs)
        end = time.time()
        print(func.__name__, end-start)
        return result
    return wrapper

if __name__ == '__main__':
    @timethis
    def countdown(n:int):
        '''
        Counts down
        '''
        while n > 0:
            n -= 1
    @timethis_didnot_wrap
    def countdown_1(n:int):
        '''
        Counts down
        '''
        while n > 0:
            n -= 1

    countdown(100000)
    print('Name:', countdown.__name__)
    print('Docstring:', repr(countdown.__doc__))
    print('Annotations:', countdown.__annotations__)
    print(countdown.__wrapped__(100000))

    countdown_1(100000)
    print('Name:', countdown_1.__name__)
    print('Docstring:', repr(countdown_1.__doc__))
    print('Annotations:', countdown_1.__annotations__)
    print(countdown_1.__wrapped__(100000))

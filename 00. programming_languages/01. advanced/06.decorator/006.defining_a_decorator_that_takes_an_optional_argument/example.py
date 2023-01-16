from functools import wraps, partial


def sleep(func=None, *, seconds=None, msg=None):
    if func is None:
        return partial(sleep, seconds=seconds, msg=msg)

    seconds = seconds if seconds else 1
    msg = msg if msg else 'Sleeping for {} seconds'.format(seconds)

    @wraps(func)
    def wrapper(*args, **kwargs):
        print(msg)
        return func(*args, **kwargs)
    return wrapper


# Example use
@sleep
def add(x, y):
    return x + y

@sleep(seconds=2)
def sub(x, y):
    return x - y

@sleep()
def multiple(x, y):
    return x * y



if __name__ == '__main__':

    add(2,3)
    sub(2,3)
    multiple(2, 3)



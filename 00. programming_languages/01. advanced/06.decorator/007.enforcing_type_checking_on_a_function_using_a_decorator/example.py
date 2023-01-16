from inspect import signature
from functools import wraps

def Type_Check(*ty_args, **ty_kwargs):
    def decorator(func):
        # If in optimized mode, disable type checking
        if not __debug__:
            return func

        # Map function argument names to supplied types
        sig = signature(func)
        bound_types = sig.bind_partial(*ty_args, **ty_kwargs).arguments


        @wraps(func)
        def wrapper(*args, **kwargs):
            bound_values = sig.bind(*args, **kwargs)
            # Enforce type assertions across supplied arguments
            for name, value in bound_values.arguments.items():
                if name in bound_types:
                    if not isinstance(value, bound_types[name]):
                        raise TypeError(
                            'Argument {} must be {}'.format(name, bound_types[name])
                            )
            return func(*args, **kwargs)
        return wrapper
    return decorator

# Examples

@Type_Check(int,int)
def add(x, y):
    return x + y

@Type_Check(str)
def first_Letter(word):
    return word[0]

if __name__ == '__main__':
    print(add(2,3))
    print(add('www','www'))
    print(first_Letter('diane'))



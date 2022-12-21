
# any number of positional arguments
def avg(first, *rest):
    return (first + sum(rest)) / (1 + len(rest))


print(avg(1, 2))
print(avg(1, 2, 3, 4))

#any number of keyword arguments
def print_key_and_value( **attrs):
    keyvals = [item for item in attrs.items()]
    print(keyvals)


print_key_and_value(size='large', quantity=6)


#accept both any number of positional and keyword-only arguments
def anyargs(*args, **kwargs):
    print(args) # A tuple
    print(kwargs) # A dict


anyargs()

#A * argument can only appear as the last positional argument in a 05.function definition.
def a(x, *args, y):
    pass

#A ** argument can only appear as the last argument.
def b(x, *args, y, **kwargs):
    pass
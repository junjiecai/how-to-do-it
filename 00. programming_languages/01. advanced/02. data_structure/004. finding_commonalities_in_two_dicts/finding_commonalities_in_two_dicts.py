
def func_1():
    a = {
        'x': 1,
        'y': 2,
        'z': 3
    }

    b = {
        'w': 10,
        'x': 11,
        'y': 2
    }

    # Find keys in common
    common = a.keys() & b.keys()
    # Find keys in a that are not in b
    difference = a.keys() - b.keys()
    # Find (key,value) pairs in common
    common_pair = a.items() & b.items()

    return common, difference,common_pair

print(func_1())
from collections import defaultdict

def func_1():
    a = defaultdict(list)
    a['movie'].append(1)
    a['movie'].append(1)
    a['director'].append(1)

    return a

def func_2():
    a = defaultdict(set)
    a['movie'].add(1)
    a['movie'].add(1)
    a['director'].add(1)

    return a


def func_3():
    a = {}
    a.setdefault('movie',set())
    a.setdefault('director',[])
    a['movie'].add(1)
    a['movie'].add(1)
    a['director'].append(1)

    return a

def func_4():
    pairs = [('movie',1),('movie',1),('director',1)]
    d = {}
    for key, value in pairs:
        if key not in d:
            d[key] = []
        d[key].append(value)

    return d

def func_5():
    pairs = [('movie',1),('movie',1),('director',1)]
    d = defaultdict(list)
    for key, value in pairs:
        d[key].append(value)

    return d

a1 = func_1()
a2 = func_2()
a3 = func_3()
a4 = func_4()
a5 = func_5()

print(a1)
print(a2)
print(a3)
print(a4)
print(a5)
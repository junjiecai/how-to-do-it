from collections import OrderedDict
from collections import defaultdict

def func_1():
    d = OrderedDict()
    d['foo'] = 1
    d['bar'] = 2
    d['spam'] = 3

    for key in d:
        print(key, d[key])




def func_2():
    d = defaultdict(int)
    d['foo'] = 1
    d['bar'] = 2
    d['spam'] = 3

    for key in d:
        print(key, d[key])

def func_3():
    pass
    a = [
        {'x': 2, 'y': 3},
        {'x': 1, 'y': 4},
        {'x': 2, 'y': 3},
        {'x': 2, 'y': 3},
        {'x': 10, 'y': 15}
        ]
    # ordered_dict 用于保留 list of dict 中 key 的顺序

func_1()
func_2()

assert {'x':1,'y':2} == {'y':2,'x':1}
assert OrderedDict({'x':1,'y':2}) == OrderedDict({'y':2,'x':1})
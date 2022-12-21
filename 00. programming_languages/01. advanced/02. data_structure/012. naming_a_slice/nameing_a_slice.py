
def func_1():
    q = [0, 1, 2, 3, 4, 5, 6]
    a = slice(2, 4)
    print(q(a))


def func_2():
    q = [0, 1, 2, 3, 4, 5, 6]
    print(q[2:4])


def func_3():
    q = [0, 1, 2, 3, 4, 5, 6]
    a = slice(2, 4)
    q[a] = [10,11]
    print(a)


def func_4():
    q = [0, 1, 2, 3, 4, 5, 6]
    a = slice(2, 4)
    del q[a]
    print(a)



func_1()
func_2()
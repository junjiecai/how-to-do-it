

def func_1():
    choices = ['http:', 'ftp:']
    url = 'http://www.python.org'
    print(url.startswith(tuple(choices)))

def func_2():
    choices = 'http:'
    url = 'http://www.python.org'
    print(url.startswith(choices))

def func_3():
    filenames = ['Makefile', 'foo.c', 'bar.py', 'spam.c', 'spam.h']
    new_names = [name for name in filenames if name.endswith(('.c', '.h'))]
    print(new_names)


func_1()
func_2()
func_3()

# Examples of simple regular expression matching

import re
text = 'Today is 11/27/2012. PyCon starts 3/13/2013.'

def func_1():

    # (a) Find all matching dates
    datepat = re.compile(r'\d+/\d+/\d+')
    print(datepat.findall(text))


def func_2():
    # (b) Find all matching dates with capture groups
    datepat = re.compile(r'(\d+)/(\d+)/(\d+)')
    for month, day, year in datepat.findall(text):
        print('{}-{}-{}'.format(year, month, day))


def func_3():
    # (c) Iterative search
    datepat = re.compile(r'(\d+)/(\d+)/(\d+)')
    for m in datepat.finditer(text):
        print(m.groups())


func_1()
func_2()
func_3()


# Examples of simple regular expression substitution

import re

def fun_1():
    text = 'yeah, but no, but yeah, but no, but yeah'
    text.replace('yeah', 'yep')
    print(text)

def func_2():
    text = 'Today is 11/27/2012. PyCon starts 3/13/2013.'
    datepat = re.compile(r'(\d+)/(\d+)/(\d+)')

    # (a) Simple substitution
    print(datepat.sub(r'\3-\1-\2', text))

def func_3():
    text = 'Today is 11/27/2012. PyCon starts 3/13/2013.'
    re.sub(r'(?P<month>\d+)/(?P<day>\d+)/(?P<year>\d+)', r'\g<year>-\g<month>-\g<day>', text)

    print(text)


def func_4():
    text = 'Today is 11/27/2012. PyCon starts 3/13/2013.'
    from calendar import month_abbr
    datepat = re.compile(r'(\d+)/(\d+)/(\d+)')

    def change_date(m):
        mon_name = month_abbr[int(m.group(1))]
        return '{} {} {}'.format(m.group(2), mon_name, m.group(3))

    print(datepat.sub(change_date, text))

fun_1()
func_2()
func_3()
func_4()
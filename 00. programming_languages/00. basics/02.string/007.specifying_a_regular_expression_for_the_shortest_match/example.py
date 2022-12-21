

# Example of a regular expression that finds shortest matches

import re

# Sample text
text = 'Computer says "no." Phone says "yes."'

def func_1():
    # (a) Regex that finds quoted strings - longest match
    str_pat = re.compile(r'\"(.*)\"')
    print(str_pat.findall(text))

def func_2():
    # (b) Regex that finds quoted strings - shortest match
    str_pat = re.compile(r'\"(.*?)\"')
    print(str_pat.findall(text))

func_1()
func_2()



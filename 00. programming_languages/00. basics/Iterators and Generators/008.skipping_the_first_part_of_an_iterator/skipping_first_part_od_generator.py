# use dropwhile and islice to skip first part of an iterator

from itertools import dropwhile
with open('/etc/passwd') as f:
    for line in dropwhile(lambda line: not line.startswith('#'), f):
        print(line, end='')

from itertools import islice
items = ['a', 'b', 'c', 1, 4, 10, 15]
for x in islice(items, 3, None):
    print(x)
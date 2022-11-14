
# Sort a list of a dicts on a common key

rows = [
    {'fname': 'B', 'lname': 'Jones', 'uid': 1},
    {'fname': 'D', 'lname': 'lalaland', 'uid': 2},
    {'fname': 'J', 'lname': 'Cleese', 'uid': 3},
    {'fname': 'Big', 'lname': 'Jones', 'uid': 4}
]

from operator import itemgetter

rows_by_fname = sorted(rows, key=itemgetter('fname'))
rows_by_uid = sorted(rows, key=itemgetter('uid'))

from pprint import pprint

print("Sorted by fname:")
pprint(rows_by_fname)

print("Sorted by uid:")
pprint(rows_by_uid)

rows_by_lfname = sorted(rows, key=itemgetter('lname','fname'))
print("Sorted by lname,fname:")
pprint(rows_by_lfname)

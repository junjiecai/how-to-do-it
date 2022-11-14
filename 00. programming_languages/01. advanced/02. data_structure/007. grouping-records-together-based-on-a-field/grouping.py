rows = [
    {'address': '1', 'date': '07/01/2012'},
    {'address': '2', 'date': '07/04/2012'},
    {'address': '3', 'date': '07/02/2012'},
    {'address': '4', 'date': '07/03/2012'},
    {'address': '5', 'date': '07/02/2012'},
    {'address': '6', 'date': '07/02/2012'},
    {'address': '7', 'date': '07/01/2012'},
    {'address': '8', 'date': '07/04/2012'},
]

from itertools import groupby

# 全局groupby 需要先sort，非全局不需要sort
rows.sort(key=lambda r: r['date'])
for date, items in groupby(rows, key=lambda r: r['date']):
    print(date)
    for i in items:
        print('    ', i)


from collections import defaultdict
rows_by_date = defaultdict(list)
for row in rows:
    rows_by_date[row['date']].append(row)

for r in rows_by_date['07/01/2012']:
    print(r)


    




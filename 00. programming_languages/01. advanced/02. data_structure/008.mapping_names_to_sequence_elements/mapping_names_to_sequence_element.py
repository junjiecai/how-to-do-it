
"""
todo: compare namedtuple to class and dict
"""
from collections import namedtuple

Stock = namedtuple('Stock', ['name', 'shares', 'price'])

stock = Stock('APPLE','99','11')


#unmutable
stock.price = 12

#
#stock = stock._replace(price = 12)

print(stock)




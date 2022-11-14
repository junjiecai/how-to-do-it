

def func_1():
   nums = [1, 2, 3, 4, 5]
   s = sum(x * x for x in nums)
   print(s)

def func_2():
   nums = [1, 2, 3, 4, 5]
   s = sum((x * x for x in nums))
   print(s)


def func_3():
   portfolio = [
      {'name':'GOOG', 'shares': 50},
      {'name':'YHOO', 'shares': 75},
      {'name':'AOL', 'shares': 20},
      {'name':'SCOX', 'shares': 65}
   ]
   min_shares = min(s['shares'] for s in portfolio)
   print(min_shares)

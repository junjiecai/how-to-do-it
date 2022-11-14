
# Example of calculating with dictionaries

prices = {
   'ACME': 45,
   'AAPL': 612,
   'IBM': 205,
   'HPQ': 37,
   'FB': 10
}

# Find min and max price
min_price = min(prices.values())
max_price = max(prices.values())

print('min price:', min_price)
print('max price:', max_price)

prices_sorted = sorted(zip(prices.values(), prices.keys()))
for price, name in prices_sorted:
    print('    ', name, price)



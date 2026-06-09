prices = [7,6,4,3,1]

min_price = float('inf')
max_price = 0

print(min_price)

for price in prices:
    if price < min_price:
        min_price = price
    elif price - min_price > max_price:
        max_price = price - min_price

print(max_price)

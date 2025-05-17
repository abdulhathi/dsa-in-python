def max_profit(price, start, end):
  if end <= start:
    return 0
  profit = 0
  for i in range(start, end-1):
    for j in range(i+1, end):
      if price[j] > price[i]:
        curr_profit = price[j] - price[i] + \
            max_profit(price, start, i-1) + max_profit(price, j+1, end)
        profit = max(curr_profit, profit)
  return profit


print(max_profit([1, 5, 3, 8, 12], 0, 5))

def max_profit_efficient(price):
  profit = 0
  for i in range(1,len(price)):
    if price[i] > price[i-1]:
      profit += price[i] - price[i-1]
  return profit


print(max_profit_efficient([1, 5, 3, 8, 12]))

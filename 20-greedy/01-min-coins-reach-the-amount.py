from collections import defaultdict

def min_coins_reach_amount(coins, amount):
  coins.sort(reverse=True)
  coins_res = defaultdict(int)
  count = 0
  while amount > 0:
    for coin in coins:
      if amount < coin:
        continue
      num_of_this_coin = amount // coin
      amount -= coin * num_of_this_coin
      coins_res[coin] += num_of_this_coin
      count += num_of_this_coin

  return count, coins_res


res = min_coins_reach_amount([2, 10, 5, 1], 52)
res = min_coins_reach_amount([2, 10, 5, 1], 58)

print(res)


import heapq

# * Time: O(n) +O(count*logn) Space: O(1)
def purchasing_maximum_items(items, sum):
  count = 0
  while sum > 0:
    item = heapq.heappop(items)
    if item > sum:
      break
    count += 1
    sum -= item
  return count


res = purchasing_maximum_items([1, 12, 5, 111, 200], 10)
print(res)

res = purchasing_maximum_items([20, 10, 5, 30, 100], 35)
print(res)

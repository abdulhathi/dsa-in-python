from collections import deque

# * Time: O(n) Space: O(n)
def next_greater_element(nums):
  n = len(nums)
  q, res = deque([n-1]), deque([-1])
  for i in range(n-2, -1, -1):
    num = nums[i]
    while q and nums[q[0]] <= num:
      q.popleft()
    if q:
      res.appendleft(nums[q[0]])
    else:
      res.appendleft(-1)
    q.appendleft(i)
  return list(res)


res = next_greater_element([5, 15, 10, 8, 6, 12, 9, 18])
print(res)
res = next_greater_element([10,15,20,25])
print(res)
res = next_greater_element([25,20,15,10])
print(res)

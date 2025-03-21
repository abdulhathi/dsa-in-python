import math


def largest_element(nums):
  max_elem = -math.inf
  for num in nums:
    max_elem = max(max_elem, num)
  return max_elem if max_elem != -math.inf else None


res = largest_element([10, 5, 20, 8])
print(res)

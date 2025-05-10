import math
from typing import List


def max_diff_in_array(nums: List[int]) -> List[int]:
  n = len(nums)
  last_largest_elem = nums[n-1]
  max_diff = -math.inf
  for i in range(n-2, -1, -1):
    max_diff = max(max_diff, last_largest_elem - nums[i])
    last_largest_elem = max(last_largest_elem, nums[i])
  return max_diff


print(max_diff_in_array([2, 3, 10, 6, 4, 8, 1]))

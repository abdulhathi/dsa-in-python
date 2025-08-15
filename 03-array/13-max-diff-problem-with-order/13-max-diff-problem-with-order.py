import math
from typing import List

# * Time: O(n) Space: O(1)
def max_diff_in_array(nums: List[int]) -> List[int]:
  minElem = nums[0]
  maxDiff = -math.inf
  for i in range(1, len(nums)):
    maxDiff = max(maxDiff, nums[i] - minElem)
    minElem = min(minElem, nums[i])
  return maxDiff


print(max_diff_in_array([2, 3, 10, 6, 4, 8, 1]))
print(max_diff_in_array([7, 9, 5, 6, 3, 2]))
print(max_diff_in_array([10, 20, 30]))
print(max_diff_in_array([30, 10, 8, 2]))

from collections import defaultdict
from typing import List


class Solution:
  def canPartition(self, nums: List[int]) -> bool:
    n = len(nums)
    total = sum(nums)
    if n == 1 or total % 2 != 0:
      return False
    dp = defaultdict(bool)

    def equal_subset(i, total_sum, curr_sum):
      if i >= n:
        return False
      if total_sum == curr_sum:
        return True
      if (i, total_sum, curr_sum) not in dp:
        dp[(i, total_sum, curr_sum)] = equal_subset(i+1, total_sum,
                                                    curr_sum) or equal_subset(i+1, total_sum - nums[i], curr_sum + nums[i])
      return dp[(i, total_sum, curr_sum)]

    return equal_subset(0, total, 0)

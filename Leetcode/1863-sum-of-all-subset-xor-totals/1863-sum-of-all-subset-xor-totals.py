from typing import List


class Solution:
  def subsetXORSum(self, nums: List[int]) -> int:
    n = len(nums)

    def subset(i, curr_sum):
      if i == n:
        return curr_sum
      return subset(i+1, curr_sum) + subset(i+1, curr_sum ^ nums[i])

    return subset(0, 0)


print(Solution().subsetXORSum([5, 1, 6]))
print(Solution().subsetXORSum([3, 4, 5, 6, 7, 8]))

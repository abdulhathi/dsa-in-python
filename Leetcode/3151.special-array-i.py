#
# @lc app=leetcode id=3151 lang=python3
#
# [3151] Special Array I
#

# @lc code=start
class Solution:
  def isArraySpecial(self, nums: List[int]) -> bool:
    n = len(nums)
    if n <= 1:
      return True
    for i in range(n-1):
      if (nums[i] % 2 == nums[i+1] % 2):
        return False
    return True
# @lc code=end
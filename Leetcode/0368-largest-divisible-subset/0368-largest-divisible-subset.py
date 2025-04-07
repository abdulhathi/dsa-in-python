# Time: (nlogn) + N^2  Space: O(n^2)
from collections import defaultdict
from typing import List


class Solution:
  def largestDivisibleSubset(self, nums: List[int]) -> List[int]:
    nums.sort()
    n = len(nums)
    dp = defaultdict(list)

    def dfs(i):
      if i not in dp:
        dp[i] = [nums[i]]
        for j in range(i+1, n):
          if nums[j] % nums[i] != 0:
            continue
          next_subset = dfs(j)
          if len(next_subset) + 1 > len(dp[i]):
            dp[i] = [nums[i]] + next_subset
      return dp[i]

    largest_subset = []
    for i in range(n-1, -1, -1):
      subset = dfs(i)
      if len(subset) > len(largest_subset):
        largest_subset = subset
    return largest_subset

print(Solution().largestDivisibleSubset([1, 2,3]))
print(Solution().largestDivisibleSubset([1, 2, 3,4,5,6,7,8,9,10,11]))
print(Solution().largestDivisibleSubset([5, 9, 18,54,108,540,90,180,360,720]))
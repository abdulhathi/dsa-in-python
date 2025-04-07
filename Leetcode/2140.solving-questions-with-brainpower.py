#
# @lc app=leetcode id=2140 lang=python3
#
# [2140] Solving Questions With Brainpower
#

# @lc code=start
# from collections import defaultdict


from collections import defaultdict


class Solution:
  def mostPoints(self, questions: List[List[int]]) -> int:
    memo = defaultdict(int)
    n = len(questions)

    def dfs(ind):
      if ind >= n:
        return 0
      if not ind in memo:
        power, skip = questions[ind]
        memo[ind] = max(dfs(ind+1), dfs(ind+skip+1) + power)
      return memo[ind]

    return dfs(0)
# @lc code=end

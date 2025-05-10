from typing import List


def fixed_array_with_range_of_queries(nums: List[int], queries: List[tuple]) -> List[int]:
  ps, prev = [], 0
  for num in nums:
    prev = prev + num
    ps.append(prev)

  res = []
  for query in queries:
    si, ei = query
    res.append(ps[ei] - (ps[si-1] if si > 0 else 0))
  return res


res = fixed_array_with_range_of_queries(
    [2, 8, 3, 9, 6, 5, 4], [(0, 2), (1, 3), (2, 6)])
print(res)

from typing import List

# * Time: O(n) Space: O(n) CodingTime: 10min


def merge_subarrays(nums: List[int], low: int, mid: int, high: int) -> List[int]:
  x, y = low, mid+1
  m, n = mid+1, high+1
  res = []
  while x < m and y < n:
    if nums[x] < nums[y]:
      res.append(nums[x])
      x += 1
    else:
      res.append(nums[y])
      y += 1

  while x < m:
    res.append(nums[x])
    x += 1

  while y < n:
    res.append(nums[y])
    y += 1

  return res


print(merge_subarrays([10, 15, 20, 11, 13], 0, 2, 4))
print(merge_subarrays([5, 8, 12, 14, 7], 0, 3, 4))

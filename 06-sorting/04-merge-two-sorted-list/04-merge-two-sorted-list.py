from typing import List

# * Time: O(max(m, n)) Space: O(m+n) Coding_Time: 10min
def merge_two_sorted_list(nums1: List[int], nums2: List[int]) -> List[int]:
  x, y = 0, 0
  m, n = len(nums1), len(nums2)
  res = []
  while x < m and y < n:
    if nums1[x] < nums2[y]:
      res.append(nums1[x])
      x += 1
    else:
      res.append(nums2[y])
      y += 1

  while x < m:
    res.append(nums1[x])
    x += 1

  while y < n:
    res.append(nums2[y])
    y += 1

  return res


print(merge_two_sorted_list([10, 15, 20], [5, 6, 6, 30]))
print(merge_two_sorted_list([1, 1, 2], [3]))

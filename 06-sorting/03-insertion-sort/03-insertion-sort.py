from typing import List

# * Time: O(n^2) Space: O(1) Coding-time: 11min


def insertion_sort(nums: List[int]) -> List[int]:
  n = len(nums)
  for i in range(1, n):
    elem = nums[i]
    j = i-1
    while j >= 0 and nums[j] > elem:
      nums[j+1] = nums[j]
      j -= 1
    nums[j+1] = elem
  return nums


print(insertion_sort([20, 5, 40, 60, 10, 30]))

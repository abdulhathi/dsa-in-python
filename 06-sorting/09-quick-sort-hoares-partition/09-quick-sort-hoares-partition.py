from typing import List


def hoares_partition(nums: List[int], l: int, h: int) -> List[int]:
  pivot = nums[l]
  i, j = l-1, h+1
  while True:
    i = i + 1
    while nums[i] < pivot:
      i = i + 1
    j = j - 1
    while nums[j] > pivot:
      j = j - 1
    if i >= j:
      return j, nums
    nums[i], nums[j] = nums[j], nums[i]


print(hoares_partition([5, 3, 8, 4, 2, 7, 1, 10], 0, 7))

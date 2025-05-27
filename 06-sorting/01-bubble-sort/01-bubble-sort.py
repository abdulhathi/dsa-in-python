from typing import List

# * Time: O(n^2) Space: O(1)


def bubble_sort(nums: List[int]) -> List[int]:
  n = len(nums)
  for i in range(n-1):
    swapped = False
    for j in range(1, n-i):
      if nums[j-1] > nums[j]:
        nums[j-1], nums[j] = nums[j], nums[j-1]
        swapped = True
    if not swapped:
      return nums
  return nums


print(bubble_sort([2, 10, 8, 7]))
print(bubble_sort([10, 8, 20, 5]))
print(bubble_sort([6, 8, 6, 6]))

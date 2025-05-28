from typing import List


def quick_sort_naive_partition(nums: List[int], p: int) -> List[int]:
  n = len(nums)
  nums[n-1], nums[p] = nums[p], nums[n-1]
  temp = []
  for num in nums:
    if num <= nums[n-1]:
      temp.append(num)
  for num in nums:
    if num > nums[n-1]:
      temp.append(num)
  for i in range(len(nums)):
    nums[i] = temp[i]
  return nums

print(quick_sort_naive_partition([5, 13, 6, 9, 12, 8, 11], 5))

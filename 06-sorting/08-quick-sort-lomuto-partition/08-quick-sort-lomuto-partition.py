from typing import List

# * Time: O(n) Space: O(1) CodingTime: 10min
def lomuto_partition(nums: List[int]) -> List[int]:
  n = len(nums)
  pivot, i = nums[n-1], -1
  for j in range(n-1):
    if nums[j] < pivot:
      i = i + 1
      nums[i], nums[j] = nums[j], nums[i]
  nums[i+1], nums[n-1] = nums[n-1], nums[i+1]
  return i+1


print(lomuto_partition([10, 80, 30, 90, 50, 70]))

from typing import List


def remove_duplicates_from_sorted_array(nums: List[int]) -> List[int]:
  n = len(nums)
  j = 1
  for i in range(1,n):
    if nums[j-1] != nums[i]:
      nums[j] = nums[i]
      j += 1
  return nums


res = remove_duplicates_from_sorted_array([10, 20, 20, 30, 30, 30, 30])
print(res)

res = remove_duplicates_from_sorted_array([10, 20, 30, 40, 50, 50])
print(res)
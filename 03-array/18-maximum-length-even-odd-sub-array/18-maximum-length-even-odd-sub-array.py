from typing import List


def maximum_length_even_odd_subarray(nums: List[int]) -> int:
  n = len(nums)
  maxLength, currMaxLength = 0, 0
  for i in range(n):
    if nums[i-1] % 2 != 0 and nums[i] % 2 == 0:
      currMaxLength += 1
    elif nums[i-1] % 2 == 0 and nums[i] % 2 != 0:
      currMaxLength += 1
    else:
      maxLength = max(currMaxLength, maxLength)
      currMaxLength = 0
  return max(currMaxLength, maxLength)


print(maximum_length_even_odd_subarray([10, 12, 14, 7, 8]))
print(maximum_length_even_odd_subarray([7, 10, 13, 14]))
print(maximum_length_even_odd_subarray([10, 12, 8, 4]))

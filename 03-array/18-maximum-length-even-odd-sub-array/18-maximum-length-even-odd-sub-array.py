from typing import List


def maximum_length_even_odd_subarray(nums: List[int]) -> int:
  max_len, curr_max_len = 1, 1
  is_even = False if nums[0] % 2 == 0 else True
  for i in range(1, len(nums)):
    num = nums[i]
    if (is_even and num % 2 == 0) or not is_even and num % 2 != 0:
      curr_max_len += 1
      is_even = not is_even
    else:
      max_len = max(max_len, curr_max_len)
      curr_max_len = 0
      is_even = True
  return max(max_len, curr_max_len)


print(maximum_length_even_odd_subarray([10, 12, 14, 7, 8]))
print(maximum_length_even_odd_subarray([7, 10, 13, 14]))
print(maximum_length_even_odd_subarray([10, 12, 8, 4]))

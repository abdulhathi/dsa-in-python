from typing import List


def maximum_subarray_sum(nums: List[int]) -> int:
  max_sub_arr_sum, curr_max_sub_arr_sum = nums[0], nums[0]
  n = len(nums)
  for i in range(1, n):
    if curr_max_sub_arr_sum + nums[i] > nums[i]:
      curr_max_sub_arr_sum += nums[i]
    else:
      curr_max_sub_arr_sum = nums[i]
    max_sub_arr_sum = max(max_sub_arr_sum, curr_max_sub_arr_sum)
  return max_sub_arr_sum


print(maximum_subarray_sum([-5, 1, -2, 3, -1, 2, -2]))

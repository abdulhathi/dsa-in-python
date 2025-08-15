from typing import List

# * The idea is max of i is the maximum of (i-1 value + i th value) or i th value
# * Time: O(n) Space: O(1)
def maximum_subarray_sum(nums: List[int]) -> int:
  max_sub_arr_sum, curr_max_sub_arr_sum = nums[0], nums[0]
  n = len(nums)
  for i in range(1, n):
    curr_max_sub_arr_sum = max(curr_max_sub_arr_sum + nums[i], nums[i])
    max_sub_arr_sum = max(max_sub_arr_sum, curr_max_sub_arr_sum)
  return max_sub_arr_sum


print(maximum_subarray_sum([-5, 1, -2, 3, -1, 2, -2]))

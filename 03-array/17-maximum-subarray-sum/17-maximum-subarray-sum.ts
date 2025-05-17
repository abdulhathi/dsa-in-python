const max_subarray_sum = (nums: number[]): number => {
  let [curr_max_sub_arr_sum, max_sub_arr_sum] = [nums[0], nums[0]]
  for (let i = 1; i < nums.length; i++) {
    if (curr_max_sub_arr_sum + nums[i] > nums[i]) {
      curr_max_sub_arr_sum += nums[i]
    } else {
      curr_max_sub_arr_sum = nums[i]
    }
    max_sub_arr_sum = Math.max(curr_max_sub_arr_sum, max_sub_arr_sum)
  }
  return max_sub_arr_sum
}

console.log(max_subarray_sum([-5, 1, -2, 3, -1, 2, -2]))

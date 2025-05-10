const move_all_zeros_to_end = (nums: number[]): number[] => {
  let zero_pos = 0
  for (let i = 0; i < nums.length; i++) {
    if (nums[i] !== 0) {
      if (i !== zero_pos) {
        const temp = nums[i]
        nums[i] = nums[zero_pos]
        nums[zero_pos] = temp
      }
      zero_pos++
    }
  }
  return nums
}

console.log(move_all_zeros_to_end([10, 15, 0, 20, 0, 25]))

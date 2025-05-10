const remove_dups_from_sorted_array = (nums: number[]): number[] => {
  let j = 1
  for (let i = 1; i < nums.length; i++) {
    if (nums[i] != nums[j - 1]) {
      nums[j] = nums[i]
      j += 1
    }
  }
  return nums
}

console.log(remove_dups_from_sorted_array([10, 20, 20, 30, 30, 30, 30]))

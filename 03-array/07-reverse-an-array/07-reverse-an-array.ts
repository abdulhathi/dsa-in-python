const reverse_an_array = (nums: number[]): number[] => {
  let lp = 0
  let rp = nums.length - 1
  while (lp < rp) {
    const temp = nums[lp]
    nums[lp] = nums[rp]
    nums[rp] = temp
    lp += 1
    rp -= 1
  }
  return nums
}

console.log(reverse_an_array([10, 20, 30]))

console.log(reverse_an_array([10, 20, 30, 40, 50]))

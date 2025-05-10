const check_if_an_array_sorted = (nums: number[]): boolean => {
  const n = nums.length
  for (let i = 1; i < n; i++) {
    if (nums[i-1] > nums[i])
      return false
  }
  return true
}


let res = check_if_an_array_sorted([8, 12, 15])
console.log(res)
res = check_if_an_array_sorted([8, 10, 10, 12])
console.log(res)
res = check_if_an_array_sorted([100])
console.log(res)
res = check_if_an_array_sorted([100, 20, 200])
console.log(res)

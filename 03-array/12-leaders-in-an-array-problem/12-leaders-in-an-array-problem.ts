const leaders_in_an_array = (nums: number[]): number[] => {
  const leaders = []
  let last_max = -Infinity
  for (let i = nums.length - 1; i >= 0; i--) {
    const num = nums[i]
    if (num > last_max) {
      leaders.unshift(num)
      last_max = num
    }
  }
  return leaders
}

console.log(leaders_in_an_array([7, 10, 4, 10, 6, 5, 2]))

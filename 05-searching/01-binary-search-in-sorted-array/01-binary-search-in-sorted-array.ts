const binary_search_in_sorted_array = (numbers: number[], key: number) => {
  let left = 0
  let right = numbers.length - 1
  while (left <= right) {
    const mid = Math.floor((left + right) / 2)
    if (numbers[mid] === key) return true
    else [left, right] = key < numbers[mid] ? [left, mid - 1] : [mid + 1, right]
  }
  return false
}

console.log(binary_search_in_sorted_array([10, 20, 30, 40, 50, 60], 20))

console.log(binary_search_in_sorted_array([10, 20, 30, 40, 50, 60], 70))

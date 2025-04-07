const bubble_sort = (numbers: number[]) => {
  const n = numbers.length
  for (let i = 0; i < n; i++) {
    let [largest_ind, largest_one] = [0, numbers[0]]
    for (let j = 1; j < n - i; j++) {
      if (numbers[j] > largest_one) {
        largest_ind = j
        largest_one = numbers[j]
      }
    }
    const temp = numbers[n - i - 1]
    numbers[n - i - 1] = largest_one
    numbers[largest_ind] = temp
  }
  return numbers
}

console.log(bubble_sort([30, 20, 60, 50, 40]))
console.log(bubble_sort([2, 10, 8, 7]))
console.log(bubble_sort([2]))

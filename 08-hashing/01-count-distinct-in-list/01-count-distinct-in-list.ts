const count_distinct_elements_in_list = (numbers: number[]) => {
  const set = new Set()
  for (const number of numbers)
    set.add(number)
  return set.size
}

console.log(count_distinct_elements_in_list([10, 20, 10, 30, 30, 20]))
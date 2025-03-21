const ts_sum_of_n_natural_numbers = (n: number): number => {
  let result = 0
  for (let i = 1; i <= n; i++) {
    result += i
  }
  return result
}

console.log(ts_sum_of_n_natural_numbers(5))

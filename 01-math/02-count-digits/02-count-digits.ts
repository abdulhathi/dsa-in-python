const count_digits = (num: number) => {
  let count = 0
  while (num > 0) {
    count += 1
    num = Math.round(num / 10)
  }
  return count
}

console.log(count_digits(1000))

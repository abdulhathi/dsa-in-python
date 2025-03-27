
const print_one_to_n = (n: number) => {
  const res = []
  const print = (n: number) => {
    if (n === 0) return
    print(n-1)
    res.push(n)
  }
  print(n)
  return res
}

console.log(print_one_to_n(5))
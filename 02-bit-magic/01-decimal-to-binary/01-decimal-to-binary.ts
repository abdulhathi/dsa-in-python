const decimal_to_binary = (num: number) => {
  let res = ''
  while (num > 0) {
    res = `${num % 2}` + res
    num = Math.floor(num / 2)
  }
  return res
}

console.log(decimal_to_binary(7))

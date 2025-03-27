const factorial_of_a_number = (num: number) => {
  let res = 1
  for(let i = 1; i <= num; i++)
    res *= i
  return res
}

console.log(factorial_of_a_number(4))
console.log(factorial_of_a_number(6))
console.log(factorial_of_a_number(0))
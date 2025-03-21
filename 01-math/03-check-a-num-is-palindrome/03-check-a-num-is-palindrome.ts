const check_a_num_is_palindrome = (num: number) => {
  let reversed = 0
  let temp = num
  while (temp > 0) {
    reversed *= 10
    reversed += temp % 10
    temp = Math.floor(temp / 10)
  }
  return reversed === num
}

console.log(check_a_num_is_palindrome(9999))
console.log(check_a_num_is_palindrome(9998))

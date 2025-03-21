def is_palindrome(num):
  temp = num
  revere_num = 0
  while temp > 0:
    revere_num *= 10
    revere_num += temp % 10
    temp //= 10
  return num == revere_num


print(is_palindrome(78987))
print(is_palindrome(7))

print(is_palindrome(77))

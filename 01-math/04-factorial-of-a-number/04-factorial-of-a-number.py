def factorial_of_a_number(num):
  res = 1
  for i in range(1, num+1):
    res *= i
  return res


print(factorial_of_a_number(4))
print(factorial_of_a_number(6))

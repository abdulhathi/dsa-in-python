def nth_fib_number_by_tabulation(n):
  table = [0] * (n+1)
  table[1] = 1
  for i in range(2, n+1):
    table[i] = table[i-1] + table[i-2]
  return table[n]


print(nth_fib_number_by_tabulation(5))
print(nth_fib_number_by_tabulation(6))

def count_good_numbers(n: int) -> int:
  mod = (10**9)+7
  def power(x, n):
    if n == 0:
      return 1
    temp = power(x, n//2)
    temp = (temp * temp) % mod
    return (temp if n % 2 == 0 else temp * x) % mod
    
  n1, n2 = (n+1)//2, n//2
  
  return (power(5, n1) * power(4, n2)) % mod


print(count_good_numbers(1))
print(count_good_numbers(2))
print(count_good_numbers(4))
print(count_good_numbers(50))
print(count_good_numbers(806166225460393))

def check_kth_bit_is_set(num, k):
  temp = k-1
  for _ in range(temp):
    num = num // 2
  return num & 1 == 1

res = check_kth_bit_is_set(10, 3)
print(res)


def binary_to_decimal(bin):
  n, res = len(bin), 0
  for i, c in enumerate(bin):
    res += int(c) * (2**(n-1-i))
  return res


print(binary_to_decimal("10010"))
print(binary_to_decimal("101"))

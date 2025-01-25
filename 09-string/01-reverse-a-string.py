def reverse_a_string(str):
  res = list(str)
  l, r = 0, len(str)-1
  while l < r:
    res[l], res[r] = res[r], res[l]
    l, r = l+1, r-1
  return "".join(res)


res = reverse_a_string('geek')
print(res)

res = reverse_a_string('abbac')
print(res)

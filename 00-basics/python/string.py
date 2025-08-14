s = "lee(t(c)o)de)"

n = len(s)
l, r = 0, n-1
left, right = '', ''
while l <= r:
  if l == r and (s[l] != '(' or s[r] != ')'):
    left += s[l]
  else:
    while s[l] != '(':
      left += s[l]
      l += 1
    while s[r] != ')':
      right = s[r] + right
      r -= 1
    left, right = left+s[l], s[r]+right
  l, r = l+1, r-1


def palindrome_check(s):
  lp, rp = 0, len(s)-1
  while lp < rp:
    if s[lp] != s[rp]:
      return False
    lp, rp = lp+1, rp-1
  return True


print(palindrome_check('abba'))
print(palindrome_check('abcba'))
print(palindrome_check('geek'))
print(palindrome_check('a'))
print(palindrome_check('abA'))

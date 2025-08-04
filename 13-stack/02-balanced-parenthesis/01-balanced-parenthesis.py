def balanced_parenthesis(parenthesis):
  st = []
  dic = {'}': '{', ')': '(', ']': '['}
  for p in parenthesis:
    if p in dic:
      if not st:
        return False
      if dic[p] != st.pop():
        return False
      continue
    st.append(p)
  return st == []


print(balanced_parenthesis('([])'))
print(balanced_parenthesis('((())'))
print(balanced_parenthesis('([)]'))
print(balanced_parenthesis('{}([()])'))
print(balanced_parenthesis('(()))'))

def balanced_parenthesis(paranthesis):
  st = []
  dic = {'}': '{', ')': '(', ']': '['}
  for p in paranthesis:
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

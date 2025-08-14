from collections import deque


def infix_to_postfix(infix):
  dq = deque()
  precedence_dic = {'(': 0, '-': 1, '+': 1, '/': 2, '*': 2, '^': 3}
  postfix = ''
  for val in infix:
    if val.isalpha():
      postfix += val
    elif val == ')':
      while dq:
        if dq[0] == '(':
          dq.popleft()
          break
        postfix += dq.popleft()
    elif dq and precedence_dic[dq[0]] < precedence_dic[val]:
      dq.appendleft(val)
    else:
      while dq and precedence_dic[dq[0]] > precedence_dic[val]:
        postfix += dq.popleft()
      dq.appendleft(val)

  while dq:
    postfix += dq.popleft()

  return postfix


print(infix_to_postfix('a+b*c'))
print(infix_to_postfix('a+b/c-d*e'))
print(infix_to_postfix('(a+b)*c'))
print(infix_to_postfix('a*b/c'))

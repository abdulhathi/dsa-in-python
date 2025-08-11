from collections import deque


def generate_k_nums_with_given_digits(digits, k):
  q = deque()
  for digit in digits:
    q.append(str(digit))

  res = []
  while k > 0 and q:
    k -= 1
    curr = q.popleft()
    res.append(curr)
    for digit in digits:
      q.append(f"{digit}{curr}")
  return res


res = generate_k_nums_with_given_digits([5, 6], 10)
print(res)

from collections import defaultdict


def nth_fib_num_memoization(n):
  dic = defaultdict(int)
  dic[0], dic[1] = 0, 1

  def fib(n):
    if n in dic:
      return dic[n]
    res = fib(n-1) + fib(n-2)
    dic[n] = res
    return dic[n]

  res = fib(n)
  return res


res = nth_fib_num_memoization(6)
print(res)

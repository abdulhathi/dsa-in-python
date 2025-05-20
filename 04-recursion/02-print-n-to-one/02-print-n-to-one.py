from typing import List


def print_n_to_one(n: int) -> List[int]:
  if n == 0:
    return []
  return [n] + print_n_to_one(n-1)

print(print_n_to_one(3))
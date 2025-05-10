from typing import List


def check_if_an_array_sorted(nums: List[int]) -> bool:
  n = len(nums)
  for i in range(1, n):
    if nums[i-1] > nums[i]:
      return False
  return True

res = check_if_an_array_sorted([8,12,15])
print(res)
res = check_if_an_array_sorted([8, 10, 10, 12])
print(res)
res = check_if_an_array_sorted([100])
print(res)
res = check_if_an_array_sorted([100, 20, 200])
print(res)

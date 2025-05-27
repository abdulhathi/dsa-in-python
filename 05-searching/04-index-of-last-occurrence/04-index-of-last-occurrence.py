from typing import List


def index_of_last_occurrence(nums: List[int], x: int) -> int:
  n = len(nums)
  lp, rp = 0, n-1
  while lp <= rp:
    mid = (lp+rp)//2
    if nums[mid] == x and (mid == n-1 or nums[mid+1] > x):
      return mid
    else:
      lp, rp = [mid+1, rp] if nums[mid] <= x else [lp, mid-1]
  return -1


print(index_of_last_occurrence([10, 15, 20, 20, 40, 40], 20))
print(index_of_last_occurrence([5, 8, 8, 10, 10], 10))
print(index_of_last_occurrence([8, 10, 10, 12], 7))

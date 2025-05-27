from typing import List


def index_of_first_occurrence(nums: List[int], x: int) -> int:
  lp, rp = 0, len(nums)-1
  while lp <= rp:
    mid = (lp+rp)//2
    if nums[mid] == x and (mid == 0 or nums[mid-1] < x):
      return mid
    else:
      lp, rp = [lp, mid-1] if nums[mid] >= x else [mid+1, rp]
  return -1


print(index_of_first_occurrence([5, 10, 10, 20, 20], 10))
print(index_of_first_occurrence([5, 10, 10, 20, 20], 20))

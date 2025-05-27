from typing import List


def count_occurrences_in_a_sorted_array(nums: List[int], x: int) -> int:
  n = len(nums)
  lp, rp = 0, n-1
  while lp <= rp:
    mid = (lp+rp)//2
    if nums[mid] == x:
      left, right = mid, mid
      while left-1 >= 0 and nums[left-1] == x:
        left -= 1
      while right+1 <= n-1 and nums[right+1] == x:
        right += 1
      return (right - left) + 1
    else:
      lp, rp = [lp, mid-1] if nums[mid] > x else [mid+1, rp]
  return 0


print(count_occurrences_in_a_sorted_array([10, 20, 20, 20, 30, 30], 20))
print(count_occurrences_in_a_sorted_array([10, 20, 20, 20, 30, 30], 30))
print(count_occurrences_in_a_sorted_array([10, 20, 20, 20, 30, 30], 10))

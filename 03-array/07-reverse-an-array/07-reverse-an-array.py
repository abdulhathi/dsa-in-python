from typing import List


def reverse_an_array(nums: List[int]) -> List[int]:
  lp, rp = 0, len(nums)-1
  while lp < rp:
    nums[lp], nums[rp] = nums[rp], nums[lp]
    lp, rp = lp+1, rp-1
  return nums


res = reverse_an_array([10, 5, 7, 30])
print(res)


res = reverse_an_array([30, 20, 5])
print(res)

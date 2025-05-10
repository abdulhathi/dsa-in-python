from typing import List


def left_rotate_an_array_by_one_pos(nums: List[int]) -> List[int]:
  lp, rp = 1, len(nums) - 1
  while lp < rp:
    nums[lp], nums[rp] = nums[rp], nums[lp]
    lp, rp = lp+1, rp-1

  lp, rp = 0, len(nums) - 1
  while lp < rp:
    nums[lp], nums[rp] = nums[rp], nums[lp]
    lp, rp = lp+1, rp-1

  return nums


print(left_rotate_an_array_by_one_pos([1, 2, 3, 4, 5]))
from typing import List


def left_rotate_an_array_by_d_places(nums: List[int], d: int) -> List[int]:
  def reverse(nums, lp, rp):
    while lp < rp:
      nums[lp], nums[rp] = nums[rp], nums[lp]
      lp, rp = lp+1, rp-1

  reverse(nums, 0, d-1)
  reverse(nums, d, len(nums)-1)
  reverse(nums, 0, len(nums)-1)
  return nums


print(left_rotate_an_array_by_d_places([1, 2, 3, 4, 5], 2))
print(left_rotate_an_array_by_d_places([10,5,13,15], 3))

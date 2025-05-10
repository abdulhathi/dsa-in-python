from typing import List


def move_all_zeros_to_end(nums: List[int]):
  zero_pos = 0
  for i in range(len(nums)):
    if nums[i] != 0:
      if i != zero_pos:
        nums[i], nums[zero_pos] = nums[zero_pos], nums[i]
      zero_pos += 1
  return nums

print(move_all_zeros_to_end([8, 5, 0, 10, 0, 20]))
print(move_all_zeros_to_end([0, 0, 0, 10, 0]))

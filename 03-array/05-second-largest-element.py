import math

def second_largest_element(nums):
  if not nums:
    return None
  first_largest, second_largest = nums[0], -math.inf
  for num in nums:
    if num > first_largest:
      first_largest = max(first_largest, num) 
      second_largest = first_largest
      continue
    second_largest = max(second_largest, num)
  return None if second_largest == -math.inf else second_largest


print(second_largest_element([10, 5, 8, 20]))
print(second_largest_element([20, 10, 20, 8, 12]))
print(second_largest_element([10, 10, 10]))

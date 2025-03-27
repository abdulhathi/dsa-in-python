def binary_search_in_sorted_array(nums, key):
  left, right = 0, len(nums)-1

  while left <= right:
    mid = (left + right) // 2
    if key < nums[mid]:
      right = mid - 1
    elif key > nums[mid]:
      left = mid + 1
    return True
  return False


res = binary_search_in_sorted_array([10, 20, 30, 40, 50, 60], 20)
print(res)
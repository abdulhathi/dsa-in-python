def recursive_binary_search(nums, key):

  def binary_search(nums, l, r):
    if l > r:
      return False
    mid = (l+r) // 2
    if key < nums[mid]:
      return binary_search(nums, l, mid-1)
    elif key > nums[mid]:
      return binary_search(nums, mid+1, r)
    else:
      return True

  return binary_search(nums, 0, len(nums)-1)


res = recursive_binary_search([10, 20, 30, 40, 50, 60, 70], 70)
print(res)

res = recursive_binary_search([10, 20, 30, 40, 50, 60, 70], 65)
print(res)

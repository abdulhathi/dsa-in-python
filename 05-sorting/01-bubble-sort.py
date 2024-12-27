def bubble_sort(nums):
  n = len(nums)
  for i in range(n):
    large_val_pos = 0
    for j in range(n-i):
      if nums[j] > nums[large_val_pos]:
        large_val_pos = j
    nums[n-1-i], nums[large_val_pos] = nums[large_val_pos], nums[n-1-i]
  return nums

res = bubble_sort([2,10,8,7])
print(res)
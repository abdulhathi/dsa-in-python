def majorityElement(nums):
  res, count = nums[0], 1
  for i in range(1, len(nums)):
    count += 1 if nums[i] == res else -1
    if count == 0:
      res, count = nums[i], 1

  count = 0
  for num in nums:
    if num == res:
      count += 1

  return res if count > len(nums)//2 else -1


res = majorityElement([8, 3, 4, 8, 8])
print(res)

res = majorityElement([3, 7, 4, 7, 7, 5])
print(res)

res = majorityElement([20, 20, 20, 40, 30, 50, 20])
print(res)

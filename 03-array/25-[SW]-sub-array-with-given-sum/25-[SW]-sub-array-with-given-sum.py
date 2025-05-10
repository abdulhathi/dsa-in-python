def sub_array_with_given_sum(nums, target_sum):
  curr_sum, s = 0, 0
  for num in nums:
    curr_sum += num
    while target_sum < curr_sum:
      curr_sum -= nums[s]
      s += 1
    if curr_sum == target_sum:
      return True

  return False


res = sub_array_with_given_sum([1, 4, 20, 3, 10, 5], 33)
print(res)

res = sub_array_with_given_sum([1, 4, 0, 0, 3, 10, 5], 7)
print(res)

res = sub_array_with_given_sum([2, 4, 3], 3)
print(res)

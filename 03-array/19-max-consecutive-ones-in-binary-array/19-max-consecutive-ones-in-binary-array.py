def max_consecutive_ones_in_binary_array(binary):
  maxCount = 0
  currCount = 0
  for num in binary:
    if num == 1:
      currCount += 1
    else:
      maxCount = max(maxCount, currCount)
      currCount = 0

  return max(maxCount, currCount)


res = max_consecutive_ones_in_binary_array([0, 1, 1, 0, 1, 0])
print(res)

res = max_consecutive_ones_in_binary_array([1, 1, 1, 1])
print(res)

res = max_consecutive_ones_in_binary_array([1, 0, 1, 1, 1, 1, 0, 1, 1])
print(res)

res = max_consecutive_ones_in_binary_array([0, 0, 0])
print(res)

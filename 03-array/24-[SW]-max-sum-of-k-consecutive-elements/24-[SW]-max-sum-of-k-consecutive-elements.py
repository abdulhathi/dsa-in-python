def max_sum_of_k_consecutive_elements(nums, k):
  n = len(nums)
  sum_of_k = sum([nums[i] for i in range(k)])
  largest_sum = sum_of_k
  for i in range(k, n):
    sum_of_k -= nums[i-k]
    sum_of_k += nums[i]
    largest_sum = max(sum_of_k, largest_sum)
  return largest_sum


res = max_sum_of_k_consecutive_elements([1, 8, 30, -5, 20, 7], 3)
print(res)

res = max_sum_of_k_consecutive_elements([5, -10, 6, 90, 3], 2)
print(res)

import heapq

# * Differences between each value in the nums array compare with x and it's index value to find the first k elements
# * Time O(n) + O(n-k logk) Space: O(k)


def k_closest_to_given_element(nums, k, x):
  closest = [[-abs(nums[i]-x), i] for i in range(k)]
  
  for i in range(k, len(nums)):
    diff = abs(nums[i]-x)
    if diff >= abs(closest[0][0]):
      continue
    heapq.heappushpop(closest, [-diff, i])

  return [nums[i] for _, i in closest]


res = k_closest_to_given_element([10, 15, 7, 3, 4], 2, 8)
print(res)
res = k_closest_to_given_element([100, 80, 10, 5, 70], 3, 2)
print(res)
res = k_closest_to_given_element([20, 40, 5, 100, 150], 3, 100)
print(res)

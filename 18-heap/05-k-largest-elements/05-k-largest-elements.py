import heapq

# * Time: O((k+(n-k)) * log k) Space: O(k)
def k_largest_elements(nums, k):
  n = len(nums)
  largest = []
  for i in range(0, k):
    heapq.heappush(largest, nums[i])
  for i in range(k, n):
    if largest[0] < nums[i]:
      heapq.heappushpop(largest, nums[i])
  return largest


print(k_largest_elements([5, 15, 10, 20, 8], 2))
print(k_largest_elements([8, 6, 4, 10, 9], 2))
print(k_largest_elements([5, 15, 10, 20, 8, 25, 18], 3))

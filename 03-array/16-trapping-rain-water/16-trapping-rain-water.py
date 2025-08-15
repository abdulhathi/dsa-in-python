
# * Time: O(n) Space: O(n)
def trapping_rain_water(nums):
  n = len(nums)
  leftMax, rightMax = [0] * n, [0] * n
  leftMax[0], rightMax[n-1] = nums[0], nums[n-1]

  for i in range(1, n):
    leftMax[i] = max(nums[i], leftMax[i-1])

  for i in range(n-2, -1, -1):
    rightMax[i] = max(nums[i], rightMax[i+1])

  maxWater = 0
  for i in range(n):
    maxWater += min(leftMax[i], rightMax[i]) - nums[i]

  return maxWater


res = trapping_rain_water([3, 0, 1, 2, 5])
print(res)

res = trapping_rain_water([2, 0, 2])
print(res)

res = trapping_rain_water([3, 0, 1, 2, 5])
print(res)

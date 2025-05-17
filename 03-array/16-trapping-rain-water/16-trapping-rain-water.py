def trapping_rain_water(nums):
  n = len(nums)
  trapped_water = 0
  for i in range(1, n-1):
    lmax = 0
    for j in range(0, i):
      lmax = max(lmax, nums[j])
    rmax = 0
    for k in range(i+1, n):
      rmax = max(rmax, nums[k])

    trapped_water += min(lmax, rmax) - nums[i]
  return trapped_water


print(trapping_rain_water([3, 0, 1, 2, 5]))

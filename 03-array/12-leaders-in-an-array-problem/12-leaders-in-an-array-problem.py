from typing import List


def leaders_in_an_array_problem(nums: List[int]) -> List[int]:
  n = len(nums)
  last_largest_elem = nums[n-1]
  leaders = [last_largest_elem]
  for i in range(n-2, -1, -1):
    if nums[i] > last_largest_elem:
      leaders.append(nums[i])
      last_largest_elem = nums[i]

  res = [leaders[i] for i in range(len(leaders)-1, -1, -1)]
  return res


print(leaders_in_an_array_problem([7, 10, 4, 3, 6, 5, 2]))
print(leaders_in_an_array_problem([7, 10, 4, 10, 6, 5, 2]))
print(leaders_in_an_array_problem([10, 20, 30]))
print(leaders_in_an_array_problem([30, 20, 10]))


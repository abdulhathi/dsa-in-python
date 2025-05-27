from typing import List

# * Time: O(n^2) Space: O(1) Coding_Time: 4min
def selection_sort(nums: List[int]) -> List[int]:
  n = len(nums)
  for i in range(n-1):
    min_elem_ind = i
    for j in range(i+1, n):
      if nums[j] < nums[min_elem_ind]:
        min_elem_ind = j
    nums[i], nums[min_elem_ind] = nums[min_elem_ind], nums[i]
  return nums


print(selection_sort([10, 5, 8, 20, 2, 18]))

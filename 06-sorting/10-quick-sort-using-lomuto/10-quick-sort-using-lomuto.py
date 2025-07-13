from typing import List

# * Time: O(nlogn) Space: O(logn) CodingTime: 10min
def quick_sort_using_lomuto(nums: List[int]) -> List[int]:
  def lomuto_partition(l: int, h: int):
    pivot, i = nums[h], l - 1
    for j in range(l, h):
      if nums[j] < pivot:
        i = i + 1
        nums[i], nums[j] = nums[j], nums[i]
    nums[i+1], nums[h] = nums[h], nums[i+1]
    return i+1

  def quick_sort(l: int, h: int):
    if l < h:
      p = lomuto_partition(l, h)
      quick_sort(l, p-1)
      quick_sort(p+1, h)

  quick_sort(0, len(nums)-1)
  return nums


print(quick_sort_using_lomuto([8, 4, 7, 9, 3, 10, 5]))

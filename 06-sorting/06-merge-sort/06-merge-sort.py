from typing import List

# * Time: O(nlogn) Space: O(n)
def merge_sort(nums: List[int], low: int, high: int) -> List[int]:
  if low < high:
    mid = (low+high)//2
    merge_sort(nums, low, mid)
    merge_sort(nums, mid+1, high)
    merge_subarrays(nums, low, mid, high)
  return nums


def merge_subarrays(nums: List[int], low: int, mid: int, high: int) -> List[int]:
  nums1, nums2 = nums[low: mid+1], nums[mid+1: high+1]
  i, j, k = 0, 0, low
  m, n = len(nums1), len(nums2)
  while i < m and j < n:
    if nums1[i] < nums2[j]:
      nums[k] = nums1[i]
      i += 1
    else:
      nums[k] = nums2[j]
      j += 1
    k += 1
  nums[k:high+1] = nums1[i:] if i < m else nums2[j:]


print(merge_sort([10, 5, 30, 15, 7], 0, 4))

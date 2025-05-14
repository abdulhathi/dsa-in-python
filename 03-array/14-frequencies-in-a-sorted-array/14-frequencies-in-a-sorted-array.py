from typing import List
from collections import Counter, defaultdict


def frequencies_in_a_sorted_array(nums: List[int]) -> dict:
  dic = defaultdict(int)
  for num in nums:
    dic[num] += 1
  return dic

  # return Counter(nums)


print(frequencies_in_a_sorted_array([10, 10, 10, 25, 30, 30]))
print(frequencies_in_a_sorted_array([10, 10, 10, 10]))
print(frequencies_in_a_sorted_array([10, 20, 30]))

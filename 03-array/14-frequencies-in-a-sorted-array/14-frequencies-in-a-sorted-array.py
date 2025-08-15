from typing import List


def frequencies_in_a_sorted_array(nums: List[int]) -> dict:
  freq = [[nums[0], 1]]
  for i in range(1, len(nums)):
    if freq[len(freq)-1][0] != nums[i]:
      freq.append([nums[i], 1])
    else:
      freq[len(freq)-1][1] += 1
  return freq

  # return Counter(nums)


print(frequencies_in_a_sorted_array([10, 10, 10, 25, 30, 30]))
print(frequencies_in_a_sorted_array([10, 10, 10, 10]))
print(frequencies_in_a_sorted_array([10, 20, 30]))

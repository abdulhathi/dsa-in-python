def count_distinct_element_in_list(nums):
  s = set()
  for num in nums:
    s.add(num)
  return len(s)

res = count_distinct_element_in_list([10, 20, 10, 30, 30, 20])
print(res)
def get_smaller_elements(nums: list[int], key):
  return [num for num in nums if num < key]


res = get_smaller_elements([8, 100, 20, 40, 3, 7], 10)
print(res)

res = get_smaller_elements([100, 20, 40, 60, 80, 200], 60)
print(res)

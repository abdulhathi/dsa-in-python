def seperate_even_and_odd(nums):
  even, odd = [], []
  for num in nums:
    if num % 2 == 0:
      even.append(num)
    else:
      odd.append(num)
  return even, odd

res = seperate_even_and_odd([10, 41, 30, 15, 80])
print(res)

res = seperate_even_and_odd([10, 20, 30])
print(res)



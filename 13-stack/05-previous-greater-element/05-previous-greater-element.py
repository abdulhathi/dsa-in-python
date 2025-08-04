def previous_greater_element(nums):
  st, res = [0], [-1]
  n = len(nums)
  for i in range(1, n):
    num = nums[i]
    while st and nums[st[len(st)-1]] <= num:
      st.pop()
    if st:
      res.append(nums[st[len(st)-1]])
    else:
      res.append(-1)
    st.append(i)
  return res


res = previous_greater_element([15, 10, 18, 12, 4, 6, 2, 8])
print(res)

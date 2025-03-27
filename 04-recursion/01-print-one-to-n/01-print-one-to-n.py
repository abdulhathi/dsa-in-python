def print_one_to_n(num):
  res = []
  def dfs_one_to_n(num):
    if num == 0:
      return
    dfs_one_to_n(num-1)
    res.append(num)
  dfs_one_to_n(num)
  return res

res = print_one_to_n(5)
print(res)
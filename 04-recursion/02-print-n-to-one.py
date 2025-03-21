def print_n_to_one(n):
  res = []
  def print(n):
    if n >= 1:
      res.append(n)
      print(n-1)
  
  print(n)
  return res

res = print_n_to_one(10)
print(res)
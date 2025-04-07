def geneate_subsets(s):
  res = []

  def subset(s, i, sub_set):
    if i == len(s):
      res.append(sub_set)
      return
    subset(s, i+1, sub_set)
    subset(s, i+1, sub_set+s[i])

  subset(s, 0, "")
  return res

res = geneate_subsets('ABC')
print(res)
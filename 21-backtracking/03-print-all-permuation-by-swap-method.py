def print_all_perms(s):
  n, res = len(s), []

  def dfs(perm, l, r):
    if l == r:
      res.append("".join(perm))
    else:
      for i in range(l, r+1):
        perm[i], perm[l] = perm[l], perm[i]
        dfs(perm, l+1, r)
        perm[i], perm[l] = perm[l], perm[i]
  dfs(list(s), 0, n-1)
  return res


res = print_all_perms('ABC')
print(res)

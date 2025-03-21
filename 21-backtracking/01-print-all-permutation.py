# DFS
def print_all_permutations(s):
  n = len(s)
  visited = [False] * n
  res = []
  def dfs(perm):
    if len(perm) == n:
      res.append(perm)
    else:
      for i in range(n):
        if visited[i]:
          continue
        visited[i] = True
        dfs(perm+s[i])
        visited[i] = False

  dfs('')
  return res

res = print_all_permutations('ABC')
print(res)
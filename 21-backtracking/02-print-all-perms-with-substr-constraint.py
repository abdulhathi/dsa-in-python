def print_all_perms_substr_constaint(s, sub_str):
  n = len(s)
  visited, res = [False] * n, []
  def dfs(perm, sub_str_in_perm):
    if "".join(sub_str_in_perm) == sub_str:
      return
    elif len(perm) == n:
      res.append(perm)
    else:
      for i in range(n):
        if visited[i]:
          continue
        visited[i] = True
        ss_len = len(sub_str_in_perm)
        if ss_len == 0 or sub_str_in_perm[ss_len-1] != sub_str[ss_len-1]:
          sub_str_in_perm = [s[i]]
        else:
          sub_str_in_perm.append(s[i])
        dfs(perm+s[i], sub_str_in_perm)
        visited[i] = False
        sub_str_in_perm = []
  dfs('', [])
  return res

res = print_all_perms_substr_constaint('ABC', 'AB')
print(res)

def dfsDisconnectedGraph(adjList):
  visited = set()
  res = []

  def dfs(u):
    visited.add(u)
    res.append(u)
    for v in adjList[u]:
      if v in visited:
        continue
      dfs(v)
  
  for u in range(len(adjList)):
    if u in visited:
      continue
    dfs(u)
  
  return res


res = dfsDisconnectedGraph([[1,2],[0,2],[0,1],[4],[3]])
print(res)
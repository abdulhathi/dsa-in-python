import math

def bridgesInGraph(adjList, s):
  n = len(adjList)
  visited, dt, lt, bridges = set(), [0] * n, [math.inf] * n, set()
  discTime = 0

  def dfs(u, p):
    nonlocal discTime
    visited.add(u)
    discTime += 1
    dt[u] = discTime
    lt[u] = discTime
    for v in adjList[u]:
      if v in visited:
        if v != p:
          lt[u] = min(lt[u], dt[v])
        continue
      dfs(v, u)
      lt[u] = min(lt[u], lt[v])
      if lt[v] > dt[u]:
        bridges.add((u,v))
  
  dfs(s, None)
  return bridges, dt, lt

adjList = [[1,2],[0,2,3],[0,1],[1,4],[3]]
res = bridgesInGraph(adjList, 0)
print(res)
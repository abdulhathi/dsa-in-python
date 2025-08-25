import math

# * Discovery time        D(V)
# * Lowwes Discovery time L(V)
def articulationPoint(adjList, s):
  n = len(adjList)
  visited, dt, lt, ap = set(), [0] * n, [math.inf] * n, set()
  discTime = 0
  def dfs(u, parent):
    nonlocal discTime
    visited.add(u)
    discTime += 1
    dt[u] = discTime
    lt[u] = discTime
    childCount = 0
    for v in adjList[u]:
      if v in visited:
        if v != parent:
          lt[u] = min(lt[u], dt[v])
        continue
      childCount += 1
      dfs(v, u)
      lt[u] = min(lt[v], lt[u])
      if lt[v] >= dt[u]:
        if parent == None and childCount < 2:
          continue
        ap.add(u)

  dfs(s, None)
  return list(ap),dt,lt

adjList = [[1,3],[0,2,4],[1,3],[0,2],[1,5,6],[4,6],[4,5]]
res = articulationPoint(adjList, 1)
print(res)

adjList = [[1],[0,2,3],[1],[1]]
print(articulationPoint(adjList, 3))

adjList = [[1,3],[2,0],[1,3,4,5],[0,2],[2,5],[2,4]]
print(articulationPoint(adjList, 0))

adjList = [[3], [3], [3], [0, 1, 2, 4], [3, 5], [4]]
print(articulationPoint(adjList, 0))

adjList = [[1, 2, 3], [0], [0], [0, 4], [3, 5], [4]]
print(articulationPoint(adjList, 0))

# * dfs(1)
# * |-dfs(0)
# *   |-dfs(3)
# *     |-dfs(2)
# *     
# * 
# * 
# * 
# * 
# * 

import math


def topologicalSortByDFS(adjList):
  st = []
  visited = set()

  def dfs(u):
    visited.add(u)
    for v in adjList[u]:
      if v in visited:
        continue
      dfs(v)
    st.append(u)

  for u in range(len(adjList)):
    if u in visited:
      continue
    dfs(u)

  return st[::-1]


def shortestPathByTopoSort(adjListWithWeight, s):
  n = len(adjListWithWeight)
  adjList = []
  for u, adj in enumerate(adjListWithWeight):
    adjList.append([v for v, w in adj])
  ts = topologicalSortByDFS(adjList)
  dist = [math.inf] * n
  dist[s] = 0
  for u in ts:
    for v, w in adjListWithWeight[u]:
      if dist[v] > dist[u] + w:
        dist[v] = dist[u]+w
  return dist

adjListWithWeight = [
  [[1,2],[4,1]],
  [[2,3]],
  [[3,6]],
  [],
  [[2,2],[5,4]],
  [[3,1]]]
res = shortestPathByTopoSort(adjListWithWeight, 0)
print(res)

adjListWithWeight = [[[1,1]],[[2,3],[3,2]],[[3,4]],[]]
res = shortestPathByTopoSort(adjListWithWeight, 1)
print(res)

# *
# *     (0)------2------->(1) 
# *      |                 |
# *      1                 3  
# *      |                 |
# *      V                 V
# *     (4)------2------->(2)
# *      |                 |
# *      4                 6
# *      |                 |
# *      V                 V
# *     (5)------1------->(3)

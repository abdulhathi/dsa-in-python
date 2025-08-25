import heapq


def kruskalsMST(adjList):
  n = len(adjList)
  parent = [i for i in range(n)]
  rank = [0] * n
  minHeap = []
  for u in range(n):
    for v, w in adjList[u]:
      heapq.heappush(minHeap, [w, u, v])

  def union(x, y):
    xp, yp = parent[x], parent[y]
    if rank[xp] > rank[yp]:
      parent[y] = xp
    elif rank[yp] > rank[xp]:
      parent[x] = yp
    else:
      parent[y] = xp
      rank[xp] += 1

  def findParent(x):
    if x == parent[x]:
      return parent[x]
    parent[x] = findParent(parent[x])
    return parent[x]

  res = 0
  while minHeap:
    w, u, v = heapq.heappop(minHeap)
    up, vp = findParent(u), findParent(v)
    if up == vp:
      continue
    union(up, vp)
    res += w
  return res


adjList = [
    [[1, 10], [2, 8]],
    [[0, 10], [2, 5], [3, 3]],
    [[0, 8], [1, 5], [3, 4]],
    [[1, 3], [2, 4], [4, 15]],
    [[2, 12], [3, 15]]
]
print(kruskalsMST(adjList))

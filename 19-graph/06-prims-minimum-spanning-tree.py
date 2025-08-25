import heapq, math

# * Time : O(v+e) Space:O(e)
def primsMST(adjList):
  n = len(adjList)
  minHeap = []
  visited = set()
  heapq.heappush(minHeap, [0, 0])
  dist = [math.inf] * n
  dist[0] = [0]
  res = 0
  while minHeap:
    w, u = heapq.heappop(minHeap)
    if u in visited:
      continue
    res += w
    visited.add(u)
    for v, w in adjList[u]:
      if v in visited:
        continue
      if dist[v] > w:
        dist[v] = w
        heapq.heappush(minHeap, [w, v])

  return res


adjList = [
    [[1, 3], [3, 1]],
    [[0, 3], [2, 1], [3, 3]],
    [[1, 1], [3, 1], [4, 5], [5, 4]],
    [[0, 1], [1, 3], [2, 1], [4, 6]],
    [[3, 6], [2, 5], [5, 2]],
    [[2, 4], [4, 2]]
]
print(primsMST(adjList))


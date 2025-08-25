import heapq
import math

# * Time: O(v+e) Space: O(v)
def dijkstrasMinShortestPath(adjList):
  n = len(adjList)
  visited = set()
  dist = [math.inf] * n
  dist[0] = 0
  minHeap = [[0,0]]
  isNormalized = False
  while minHeap and not isNormalized:
    isNormalized = True
    _,u = heapq.heappop(minHeap)
    visited.add(u)
    for v, cost in adjList[u]:
      if v in visited:
        continue
      if dist[v] > dist[u] + cost:
        dist[v] = dist[u] + cost
        heapq.heappush(minHeap,[dist[v], v])
        isNormalized = False
  return dist

adjList = [
  [[1,4],[2,8]],
  [[0,4],[2,11],[3,8]],
  [[0,8],[1,11],[4,7],[5,1]],
  [[1,8],[4,2],[7,4],[6,7]],
  [[2,7],[5,6],[3,2]],
  [[2,1],[4,6],[7,2]],
  [[3,7],[7,14],[8,9]],
  [[5,2],[3,4],[6,14],[8,10]],
  [[6,9],[7,10]]
  ]
res = dijkstrasMinShortestPath(adjList)
print(res)
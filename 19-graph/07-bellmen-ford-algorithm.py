import math

# * Time: O(v * v * e) or O(n^3) Space: O(v)
def bellmenFordAlgorithm(adjList):
  n = len(adjList)
  dist = [math.inf] * n
  dist[0] = 0
  isNormalized = False
  temp = n
  while temp and not isNormalized:
    temp -= 1
    isNormalized = True
    for u in range(n):
      for v,w in adjList[u]:
        if dist[v] > dist[u] + w:
          dist[v] = dist[u] + w
          isNormalized = False

  negativeWeightCycleDetected = temp <= 0
  return negativeWeightCycleDetected, dist


adjList = [
  [[1,6],[2,5],[3,5]],
  [[4,-1]],
  [[1,-2],[4,1]],
  [[2,-2],[5,-1]],
  [[6,3]],
  [[6,3]],
  []
]
res = bellmenFordAlgorithm(adjList)
print(res)

adjList = [
  [[1,4],[3,5]],
  [[3,5]],
  [[1,-10]],
  [[2,3]]
]
res = bellmenFordAlgorithm(adjList)
print(res)
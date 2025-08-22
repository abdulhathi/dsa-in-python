from collections import deque

def cycleDetectionByKhansBFS(adjList):
  n = len(adjList)
  indegree = [0] * n
  for u in range(n):
    for v in adjList[u]:
      indegree[v] += 1
  
  q = deque([u for u, deg in enumerate(indegree) if deg == 0])

  count = 0
  while q:
    u = q.popleft()
    count += 1
    for v in adjList[u]:
      indegree[v] -= 1
      if indegree[v] == 0:
        q.append(v)
  
  return count != n

adjList = [[1],[2],[3],[1],[1]]
res = cycleDetectionByKhansBFS(adjList)
print(res)

res = cycleDetectionByKhansBFS([[2,3],[3,4],[],[],[]])
print(res)
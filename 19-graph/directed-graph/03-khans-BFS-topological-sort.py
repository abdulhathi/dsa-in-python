from collections import deque


def khansTopoLogicalSorting(adjList):
  res = []
  n = len(adjList)
  indegree = [0] * n
  for u in range(n):
    for v in adjList[u]:
      indegree[v] += 1

  q = deque([i for i, d in enumerate(indegree) if d == 0])
  while q:
    u = q.popleft()
    res.append(u)
    for v in adjList[u]:
      indegree[v] -= 1
      if indegree[v] == 0:
        q.append(v)
  
  return res


res = khansTopoLogicalSorting([[2,3],[3,4],[],[],[]])
print(res)

res = khansTopoLogicalSorting([[2,3],[3,4],[3],[],[]])
print(res)
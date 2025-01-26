from collections import deque

def bfs(adjList):
  vertices_count = len(adjList)
  count = 0
  visited = set()
  for v in range(vertices_count):
    if v in visited:
      continue
    q = deque([v])
    visited.add(v)
    count += 1
    while q:
      curr_v = q.popleft()
      for adj_v in adjList[curr_v]:
        if adj_v in visited:
          continue
        visited.add(adj_v)
        q.append(adj_v)
  return count

adjList = [[1,2],[0,2],[0,1],[4],[3],[6,7],[5],[5]]
res = bfs(adjList)
print(res)
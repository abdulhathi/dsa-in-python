from collections import deque

def breadth_first_search(adjList):
  vertices_count = len(adjList)
  visited = [False] * vertices_count
  res = []
  for v in range(vertices_count):
    if visited[v]:
      continue
    q = deque([v])
    visited[v] = True
    while q:
      curr_v = q.popleft()
      res.append(curr_v)
      for adj_v in adjList[curr_v]:
        if visited[adj_v]:
          continue
        visited[adj_v] = True
        q.append(adj_v)
  return res

adjList = [[1,5,2],[0,3],[0,4],[1,5],[2,5],[3,0,4]]
res = breadth_first_search(adjList)
print(res)


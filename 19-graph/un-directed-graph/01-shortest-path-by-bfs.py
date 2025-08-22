from collections import defaultdict, deque

# * Time: O(v+e) Space: O(v)
def shortestPathByBFS(adjList, s):
  dist = defaultdict(int)
  visited = set()

  def bfs(u):
    q = deque([u])
    visited.add(u)
    dist[u] = 0
    while q:
      u = q.popleft()
      for v in adjList[u]:
        if v in visited:
          continue
        dist[v] = dist[u] + 1
        visited.add(v)
        q.append(v)
  bfs(s)      
  return dist

adjList = [[1,2],[0,2,3],[0,1,3],[1,2]]
print(shortestPathByBFS(adjList, 0))

# *              ------------- 
# *             /             \
# *   (0)-----(1)-----(2)-----(3)
# *     \             /
# *      -------------
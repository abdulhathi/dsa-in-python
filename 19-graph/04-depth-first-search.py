
# * Time: O(v+e) Space: O(v)
def depthFirstSearch(adjList, s):
  visited = set()
  res = []
  def dfs(u):
    visited.add(u)
    res.append(u)
    for v in adjList[u]:
      if v in visited:
        continue
      dfs(v)
  
  dfs(s)
  return res

adjList = [[1,4],[2],[3],[2],[0,5,6],[4,6],[4,5]]
res = depthFirstSearch(adjList, 0)
print(res)

adjList = [[1,2],[0,3,4],[0,3],[1,2],[1,5],[4]]
res = depthFirstSearch(adjList, 0)
print(res)

# * Time: O(v+e) Space: O(v)
def topologicalSortByDFS(adjList):
  st = []
  visited = set()

  def dfs(u):
    visited.add(u)
    for v in adjList[u]:
      if v in visited:
        continue
      dfs(v)
    st.append(u)

  for u in range(len(adjList)):
    if u in visited:
      continue
    dfs(u)

  return st[::-1]

adjList = [[1],[3],[3,4],[4],[]]
res = topologicalSortByDFS(adjList)
print(res)
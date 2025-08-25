
# * Kosarajus Strongly connected components
# * Time: O(v+e) Space: O(v+e)
def kosarajusSCC(adjList):

  def getStackResOfDFS(adjList, visited, u):
    st = []
    def dfs(u):
      visited.add(u)
      for v in adjList[u]:
        if v in visited:
          continue
        dfs(v)
      st.append(u)

    dfs(u)
    return st

  st = getStackResOfDFS(adjList, set(), 0)

  # * Transpose graph
  n = len(adjList)
  adjList1 = [[] for _ in range(n)]

  for u in range(n):
    for v in adjList[u]:
      adjList1[v].append(u)

  res = []
  visited = set()
  while st:
    u = st.pop()
    if u in visited:
      continue
    res.append(getStackResOfDFS(adjList1,visited, u))
  
  return res
    
adjList = [
  [1],
  [2,3],
  [0],
  [4],
  []
]
res = kosarajusSCC(adjList)
print(res)

# * Time: O(v+e) Space: O(v)
def cycleDetectionByDFS(adjList):
  visited = set()
  recursionSt = set()

  def dfs(u):
    visited.add(u)
    recursionSt.add(u)
    for v in adjList[u]:
      if v in visited and v not in recursionSt:
        continue
      if v in visited and v in recursionSt:
        return True
      if dfs(v):
        return True
    recursionSt.remove(u)
    return False

  for u in range(len(adjList)):
    if u in visited:
      continue
    if dfs(u):
      return True

  return False

adjList = [[1], [], [1, 3], [4], [5], [3]]
print(cycleDetectionByDFS(adjList))

adjList = [[1], [3], [1, 3], []]
print(cycleDetectionByDFS(adjList))
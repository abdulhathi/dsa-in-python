
# * Time: O(v+e) Space: O(v)
def detectCycleByDFS(adjList, s):
  visited = set()

  def dfs(u, parent):
    visited.add(u)
    for v in adjList[u]:
      if v in visited and v == parent:
        continue
      if v in visited and v != parent:
        return True
      if dfs(v, u):
        return True
    return False

  return dfs(s, None)

adjList = [[1], [0, 2, 4], [1, 3], [2], [1]]
print(detectCycleByDFS(adjList, 0))

adjList = [[1], [0, 2, 3], [1, 3], [1, 2]]
print(detectCycleByDFS(adjList, 0))

# *
# *   (0)---(1)---(2)
# *          |     | 
# *         (4)   (3)
# *
# *   (0)---(1)---(2)   
# *           \   /  
# *            (3)
# *

def create_graph(v):
  adjList = [[] for _ in range(v)]
  return adjList

def add_edge(adjList, u, v):
  adjList[u].append(v)
  adjList[v].append(u)

def print_graph(adjList):
  for i in range(len(adjList)):
    print(adjList[i])

adjList =create_graph(4)  
add_edge(adjList,1, 2)
add_edge(adjList, 0, 2)
add_edge(adjList, 1, 3)
add_edge(adjList, 0, 1)
print_graph(adjList)
add_edge(adjList,2,3)
print_graph(adjList)


abcdefghijklmnopqrstuvwzyz
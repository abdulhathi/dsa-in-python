
class DisjointSet:
  def __init__(self, n):
    self.Parent = [i for i in range(n)]
    self.Rank = [0] * n

  def union(self, x, y):
    rank, parent = self.Rank, self.Parent
    xp, yp = parent[x], parent[y]
    if rank[xp] > rank[yp]:
      parent[yp] = xp
    elif rank[yp] > rank[xp]:
      parent[xp] = yp
    else:
      parent[yp] = xp
      rank[xp] += 1

  def findParent(self, x):
    parent = self.Parent
    if x == parent[x]:
      return x
    parent[x] = self.findParent(parent[x])
    return parent[x]

  def __str__(self):
    parent = [str(x) for x in self.Parent]
    rank = [str(x) for x in self.Rank]
    return f'[{",".join(parent)}] \n[{",".join(rank)}]'


ds = DisjointSet(7)
print(ds)

ds.union(0,1)
print(ds)

ds.union(4,5)
print(ds)


ds.union(5,1)
print(ds)

import math


class MyMinHeap:
  def __init__(self, items=[]):
    self.arr = items

  def leftIndex(self, i):
    return (2*i)+1

  def rightIndex(self, i):
    return (2*i)+2

  def parentIndex(self, i):
    return (i-1)//2

  # Time : O(n)
  def buildHeap(self):
    n = len(self.arr) // 2
    for i in range(n-1, -1, -1):
      self.minHeapify(i)

  # Time : log(n)
  def insert(self, key):
    arr = self.arr
    i = len(arr)
    arr.append(key)
    p = self.parentIndex(i)
    while i > 0 and arr[p] > arr[i]:
      arr[p], arr[i] = arr[i], arr[p]
      i = p
      p = self.parentIndex(i)

  # Time : O(logN)
  def minHeapify(self, i):
    arr = self.arr
    p, n = i, len(arr) - 1
    l, r = self.leftIndex(p), self.rightIndex(p)
    min_val_ind = r if r <= n and arr[r] < arr[l] else l
    while p < n and l <= n and arr[p] > arr[min_val_ind]:
      arr[p], arr[min_val_ind] = arr[min_val_ind], arr[p]
      p = min_val_ind
      l, r = self.leftIndex(p), self.rightIndex(p)
      min_val_ind = r if r <= n and arr[r] < arr[l] else l

  # Time : O(logN)
  def extractMin(self):
    arr, n = self.arr, len(self.arr)
    if n == 0:
      return None
    min_val = arr[0]
    arr[0] = arr[n-1]
    arr.pop()
    self.minHeapify(0)
    return min_val

  # Time : O(logN)
  def decreaseKey(self, i, val):
    arr = self.arr
    arr[i] = val
    p = self.parentIndex(i)
    while p >= 0 and arr[p] > arr[i]:
      arr[p], arr[i] = arr[i], arr[p]
      i = p
      p = self.parentIndex(i)

  # Time : O(logN)
  def delete(self, i):
    self.decreaseKey(i, -math.inf)
    self.extractMin()

  def __str__(self):
    return ", ".join([str(x) for x in self.arr])


minHeap = MyMinHeap([45, 25, 100, 50, 40, 15, 20, 10])
minHeap.insert(12)
print(minHeap)
print(minHeap.extractMin())
print(minHeap)
minHeap.decreaseKey(5, 1)
print(minHeap)
minHeap.delete(4)
print(minHeap)
minHeap.delete(6)
print(minHeap)
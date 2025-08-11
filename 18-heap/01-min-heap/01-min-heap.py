import math


class MinHeap:
  def __init__(self, nums):
    self.arr = nums

  def insert(self, val):
    arr = self.arr
    arr.append(val)
    ci = len(arr)-1
    pi = self.__parent(ci)
    while pi >= 0 and arr[ci] < arr[pi]:
      arr[ci], arr[pi] = arr[pi], arr[ci]
      ci, pi = pi, self.__parent(pi)

  def extract_min(self):
    arr = self.arr
    if not arr:
      return -math.inf
    n = len(self.arr)
    pi, li = 0, n-1
    arr[pi], arr[li] = arr[li], arr[pi]
    min_val = arr.pop()
    self.__min_heapify(pi)
    return min_val

  def decrease_key(self, ci, new_val):
    arr = self.arr
    pi = self.__parent(ci)
    arr[ci] = new_val
    while pi >= 0 and arr[ci] < arr[pi]:
      arr[ci], arr[pi] = arr[pi], arr[ci]
      ci, pi = pi, self.__parent(pi)

  def delete(self, ci):
    if ci >= len(self.arr):
      return
    self.decrease_key(ci, -math.inf)
    self.extract_min()

  def build_heap(self):
    n = len(self.arr)
    ci = (n-2)//2
    while ci >= 0:
      self.__min_heapify(ci)
      ci -= 1

  def __str__(self):
    return ",".join(map(str, self.arr))

  # * Private functions
  def __left_child(self, pi):
    return (pi*2)+1

  def __right_child(self, pi):
    return (pi*2)+2

  def __parent(self, ci):
    return (ci-1)//2

  # * Normalize the complete binary tree from parent to child and it's child (Top to bottom)
  def __min_heapify(self, pi):
    arr = self.arr
    lc, rc, n = self.__left_child(pi), self.__right_child(pi), len(arr)
    mci = lc if rc >= n or arr[lc] < arr[rc] else rc
    while mci < n and arr[pi] > arr[mci]:
      arr[pi], arr[mci] = arr[mci], arr[pi]
      pi = mci
      lc, rc = self.__left_child(pi), self.__right_child(pi)
      mci = lc if rc >= n or arr[lc] < arr[rc] else rc
    # print(arr)


minHeap = MinHeap([10, 20, 15, 40, 50, 100, 25, 45])
print(minHeap)

# minHeap.insert(12)
# print(minHeap)
# # while True:
# #   min_val = minHeap.extract_min()
# #   print('min_val', min_val)
# #   if min_val == -math.inf:
# #     break

# minHeap.decrease_key(5, 5)
# print(minHeap)

# minHeap.delete(4)
# print(minHeap)

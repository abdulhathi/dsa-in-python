def min_heapify(arr, n, pi):
  li, ri = (pi*2)+1, (pi*2)+2
  mci = li if ri >= n or arr[li] < arr[ri] else ri
  while mci < n and arr[pi] > arr[mci]:
    arr[pi], arr[mci] = arr[mci], arr[pi]
    pi = mci
    li, ri = (pi*2)+1, (pi*2)+2
    mci = li if ri >= n or arr[li] < arr[ri] else ri


def max_heapify(arr, n, pi):
  li, ri = (pi*2)+1, (pi*2)+2
  mci = li if ri >= n or arr[li] > arr[ri] else ri
  while mci < n and arr[pi] < arr[mci]:
    arr[pi], arr[mci] = arr[mci], arr[pi]
    pi = mci
    li, ri = (pi*2)+1, (pi*2)+2
    mci = li if ri >= n or arr[li] > arr[ri] else ri


def build_heap(arr, n):
  ci = (n-2)//2
  while ci >= 0:
    max_heapify(arr, n, ci)
    ci -= 1
  return arr


def heap_sort(arr):
  n = len(arr)
  arr = build_heap(arr, n)
  print(arr)
  for i in range(n-1, -1, -1):
    arr[0], arr[i] = arr[i], arr[0]
    max_heapify(arr, i, 0)
  return arr


print(heap_sort([10, 15, 50, 4, 20]))

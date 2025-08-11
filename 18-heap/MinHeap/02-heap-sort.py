def heap_sort(arr):

  def li(i):
    return (2*i)+1

  def ri(i):
    return (2*i)+2

  def max_heapify(arr, n, pi):
    l, r = li(pi), ri(pi)
    while ((l < n and arr[l] > arr[pi]) or (r < n and arr[r] > arr[pi])):
      ci = r if r < n and arr[r] > arr[l] else l
      arr[pi], arr[ci] = arr[ci], arr[pi]
      pi = ci
      l, r = li(pi), ri(pi)

  length = len(arr)
  n = (length//2)
  for i in range(n-1, -1, -1):
    max_heapify(arr, length-1, i)

  for i in range(length-1, 0, -1):
    arr[i], arr[0] = arr[0], arr[i]
    max_heapify(arr, i, 0)

  return arr


res = heap_sort([10, 15, 50, 4, 20])
print(res)

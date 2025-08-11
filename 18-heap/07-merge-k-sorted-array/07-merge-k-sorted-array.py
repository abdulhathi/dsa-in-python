import heapq

# * Time: O((m*n)*logm) Space: O(m)
def merge_k_sorted_array(arr_list):
  n = len(arr_list)
  min_heap = []
  for i in range(n):
    heapq.heappush(min_heap, [arr_list[i][0], i, 0])

  res = []
  while min_heap:
    val, i, j = heapq.heappop(min_heap)
    res.append(val)
    if j+1 < len(arr_list[i]):
      heapq.heappush(min_heap, [arr_list[i][j+1], i, j+1])
  return res


res = merge_k_sorted_array([[10, 20],
                            [5, 15],
                            [4, 9, 11]])
print(res)

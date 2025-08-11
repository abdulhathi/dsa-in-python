import heapq


def median_of_a_stream(stream):
  if not stream:
    return []
  max_heap, min_heap = [-stream[0]], []
  res = [stream[0]]
  for i in range(1, len(stream)):
    val = stream[i]
    if len(max_heap) == len(min_heap):
      if val > -max_heap[0]:
        heapq.heappush(min_heap, val)
        heapq.heappush(max_heap, -heapq.heappop(min_heap))
      else:
        heapq.heappush(max_heap, -val)
    else:
      if val > -max_heap[0]:
        heapq.heappush(min_heap, val)
      else:
        heapq.heappush(max_heap, -val)
        heapq.heappush(min_heap, -heapq.heappop(max_heap))

    median = -max_heap[0] if len(max_heap) > len(
        min_heap) else (-max_heap[0] + min_heap[0])/2
    res.append(median)

  return res


res = median_of_a_stream([12, 15, 10, 5, 8, 7, 16])
print(res)
import heapq

# arr = [10, 5, 2, 20, 1]
# heapq.heapify(arr)
# print(arr)

# 40, 15, 5, 11, 12
# heapq.heappush(arr, 40)
# print(arr)

# print(heapq.heappop(arr))
# print(arr)

# print(heapq.nlargest(2, arr))
# print(heapq.nsmallest(2, arr))

# print(heapq.heappushpop(arr, 1))
# print(arr)

# print(heapq.heapreplace(arr, -1))
# print(arr)

arr = [[10, 0], [15, 1], [7, 2], [3, 3], [4, 4]]
heapq.heapify(arr)
print(arr)
print(heapq.heappop(arr))
print(heapq.heappop(arr))
print(heapq.heappop(arr))
print(heapq.heappop(arr))
print(heapq.heappop(arr))

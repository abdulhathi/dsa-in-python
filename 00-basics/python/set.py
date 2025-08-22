
import heapq


s = set([3, 5, 6, 7, 10, 8])

# s.add(20)
# s.add(10)

# s.discard(30)\

l = list(s)
heapq.heapify(l)
print(l)

print(s.update(set([20])))
print(s)

s.update(set([30,40]))
print(s)
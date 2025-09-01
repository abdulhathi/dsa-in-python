
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

s1 = set(['A','B'])
s2 = set(['B','C'])
s3 = set(['A'])

print(s1.intersection(s2))
print(s1 & s2)

print(s3.issubset(s1))

print(s1.union(s2))

print(s1.difference(s2))
print(s2.difference(s1))

s1.remove('B')
print(s1)

mySet = {'a','b','c','c'}
print(mySet)

while mySet:
  print(mySet.pop())

# print(1=2)

print('a'=='A')
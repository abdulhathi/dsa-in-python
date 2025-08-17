from collections import deque

q = deque()

if q:
  print('q is valid')

q.appendleft(10)
q.appendleft(20)
q.appendleft(30)

print(q[0])

while q and str(q[0]).isnumeric():
  print(q.popleft())

q = deque()
q.appendleft(1)
q.appendleft(2)
q.appendleft(3)
for val in q:
  print(val)

l = [1, 2, 3, 4, 5, 6, 7]
dq = deque()

dq.append(l[0])
dq.append(l[1])

for x in l[2:]:
  dq.append(x)
print(dq)

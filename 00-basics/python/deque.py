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

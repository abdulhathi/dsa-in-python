from collections import deque


class StackUsingQueue:
  def __init__(self):
    self.q1, self.q2 = deque(), deque()

  def push(self, val):
    self.q2, self.q1 = self.q1, self.q2
    self.q1.append(val)
    while self.q2:
      self.q1.append(self.q2.popleft())

  def pop(self):
    return self.q1.popleft() if self.q1 else None

  def peek(self):
    return self.q1[0] if self.q1 else None

  def size(self):
    return len(self.q1)

  def __str__(self):
    res = []
    for item in self.q1:
      res.append(str(item))
    return ",".join(res)


stack = StackUsingQueue()
stack.push(10)
stack.push(20)
stack.push(30)
print(stack)
print(stack.pop())
print(stack)
print(stack.peek())
print(stack.size())

import sys
import os
sys.path.append(os.getcwd())
from PythonDataStructures.SinglyLinkedList.ListNode import ListNode

class MyStack:
  def __init__(self):
    self.head = None
    self._size = 0

  def push(self, key):
    node = ListNode(key, self.head)
    self.head = node
    self._size += 1

  def pop(self):
    temp = self.head
    if temp:
      self.head = temp.next
      self._size -= 1
      return temp.val
    else:
      return ''

  def peek(self):
    return self.head.val if self.head else None

  def size(self):
    return self._size

  def __str__(self):
    temp = self.head
    res = []
    while temp:
      res.append(str(temp.val))
      temp = temp.next
    return ",".join(res)

stack = MyStack()
print(stack.pop())

stack.push(10)
stack.push(20)
stack.push(30)
print(stack)

print(stack.pop())
print(stack.pop())
print(stack)

print(stack.size())

stack.push(200)
stack.push(300)
print(stack.peek())
print(stack)
while stack.size() > 0:
  stack.pop()
print(stack.peek())
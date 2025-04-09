import sys
import os
sys.path.append(os.getcwd())
from PythonDataStructures.DoublyLinkedList.ListNode import ListNode

# First In First Out (FIFO)
class StackByLinkedList:
  def __init__(self):
    self.head = None
    self.tail = None
    self._size = 0

  # Time : O(1) Space : O(1)
  def push(self, key):
    node = ListNode(key)
    if not self.head:
      self.head = self.tail = node
    else:
      node.prev = self.tail
      self.tail.next = node
      self.tail = self.tail.next
    self._size += 1
    return self.tail

  # Time : O(1)
  def pop(self):
    if not self.tail:
      return None
    tail = self.tail
    if not tail.prev:
      self.head = self.tail = None
    else:
      self.tail = tail.prev
      self.tail.next = None
    tail.prev = None
    self._size -= 1
    return tail
  
  # Time : O(1)
  def peek(self):
    return self.tail
  
  # Time : O(1)
  def size(self):
    return self._size
  
st = StackByLinkedList()
st.push(10)
st.push(20)
st.push(30)

print(st.peek())
print(st.pop())
print(st.size())
print(st.peek())
st.push(40)
print(st.peek())
print(st.size())

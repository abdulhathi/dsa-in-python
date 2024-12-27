from DoublyLinkedList import ListNode


class StackByLinkedList:
  def __init__(self):
    self.head = None
    self.tail = None
    self._size = 0

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

  def pop(self):
    tail = self.tail
    if self.tail:
      if self.tail == self.head:
        self.head = self.tail.perv
        self.head.prev = None
      self.tail = self.tail.prev
      self.tail.next = None
      self._size -= 1
    return tail
  
  def peek(self):
    return self.tail
  
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

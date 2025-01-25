from DoublyLinkedList import ListNode

class DequeByDoublyLinkedList:
  def __init__(self):
    self.head = None
    self.tail = None
    self._size = 0
    
  def insert_front(self, key):
    node = ListNode(key, None, self.head)
    if not self.head:
      self.head = self.tail = node
    else:
      self.head.prev = node
      self.head = node
    self._size += 1
    return node
  
  def insert_rear(self, key):
    node = ListNode(key, self.tail, None)
    if not self.tail:
      self.head = self.tail = node
    else:
      self.tail.next = node
      self.tail = node
    self._size += 1
    return node
  
  def delete_front(self):
    if not self.head:
      return None
    head = self.head
    if not head.next:
      self.head = self.tail = None
    else:
      self.head = head.next
      self.head.prev = None
    head.next = None
    self._size -= 1
    return head
    
  def delete_rear(self):
    if not self.tail:
      return None
    tail = self.tail
    if not tail.prev:
      self.head = self.tail = None
    else:
      self.tail = tail.prev
      self.tail.next = None
    self._size -= 1
    tail.prev = None
    return tail
  
  def get_front(self):
    return self.head
  
  def get_rear(self):
    return self.tail
  
  def isEmpty(self):
    return self._size == 0
  
  def size(self):
    return self._size
    

dq = DequeByDoublyLinkedList()
dq.insert_front(10)
dq.insert_front(20)
dq.insert_front(30)
print(dq.get_front())
print(dq.delete_front())

dq.insert_rear(40)
dq.insert_rear(50)
print(dq.get_front())
print(dq.delete_rear())

print(dq.size())
print(dq.isEmpty())
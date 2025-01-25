from DoublyLinkedList import ListNode

# Last In First Out (LIFO)
class QueueByLinkedList:
  def __init__(self):
    self.head = None
    self.tail = None
    self._size = 0

  def enque(self, key):
    node = ListNode(key)
    if not self.head:
      self.head = self.tail = node
    else:
      node.prev = self.tail
      self.tail.next = node
      self.tail = node
    self._size += 1
    return self.tail

  def deque(self):
    if not self.head:
      return None
    head = self.head
    if not head.next:
      self.head = self.tail = None
    else:
      self.head = head.next
      self.head.prev = None
    self._size -= 1
    head.next = None
    return head

  def size(self):
    return self._size

  def getFront(self):
    return self.head

  def getRear(self):
    return self.tail

  def isEmpty(self):
    return self._size == 0

q = QueueByLinkedList()
q.enque(10)
q.enque(20)
q.enque(30)
print(q.deque())
print(q.size())
q.enque(40)
print(q.getFront())
print(q.getRear())

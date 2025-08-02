import sys
import os
sys.path.append(os.getcwd())
from PythonDataStructures.DoublyLinkedList.ListNode import ListNode

def reverse_a_doubly_linked_list(head):
  curr = head
  last = None
  while curr:
    last = curr
    curr.next, curr.prev = curr.prev, curr.next
    curr = curr.prev

  return last

head = ListNode.create([10,20,30])
res = reverse_a_doubly_linked_list(head)
print(res)

head = ListNode.create([10])
res = reverse_a_doubly_linked_list(head)
print(res)

head = ListNode.create([])
res = reverse_a_doubly_linked_list(head)
print(res)

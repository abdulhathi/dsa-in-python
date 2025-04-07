import sys
import os
sys.path.append(os.getcwd())
from PythonDataStructures.SinglyLinkedList.ListNode import ListNode

def traverse_linked_list(head):
  res = []
  while head:
    res.append(head.val)
    head = head.next
  return res


head = ListNode(
    1, ListNode(2, ListNode(3, ListNode(4))))
res = traverse_linked_list(head)
print(res)

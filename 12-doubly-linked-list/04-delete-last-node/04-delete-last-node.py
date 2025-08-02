import sys
import os
sys.path.append(os.getcwd())
from PythonDataStructures.DoublyLinkedList.ListNode import ListNode

def delete_last_node(head):
  if not head or not head.next:
    return None
  temp = head
  while temp.next:
    temp = temp.next

  temp.prev.next = None
  return head

head = ListNode.create([10,20,30])
res = delete_last_node(head)
print(res)

head = ListNode.create([10])
res = delete_last_node(head)
print(res)

head = ListNode.create([])
res = delete_last_node(head)
print(res)

head = ListNode.create([10,20])
res = delete_last_node(head)
print(res)

import sys
import os
sys.path.append(os.getcwd())
from PythonDataStructures.DoublyLinkedList.ListNode import ListNode

def delete_head_node(head):
  if not head or not head.next:
    return None
  head = head.next
  head.prev = None
  return head


head = ListNode.create([10,20,30])
res = delete_head_node(head)
print(res)

head = ListNode.create([10])
res = delete_head_node(head)
print(res)

head = ListNode.create([])
res = delete_head_node(head)
print(res)

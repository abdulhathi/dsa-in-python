import sys
import os
sys.path.append(os.getcwd())
from PythonDataStructures.SinglyLinkedList.ListNode import ListNode

def delete_last_node(head):
  dummy = ListNode(0, head)
  temp = dummy
  while temp.next and temp.next.next:
    temp = temp.next
  
  temp.next = None
  return dummy.next

head = ListNode.create([])
res = delete_last_node(head)
print(res)

head = ListNode.create([10,20,30])
res = delete_last_node(head)
print(res)

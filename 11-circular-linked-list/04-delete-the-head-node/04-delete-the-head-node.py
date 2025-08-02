import sys
import os
sys.path.append(os.getcwd())
from PythonDataStructures.CircularLinkedList.ListNode import ListNode

def delete_the_head_node(head):
  if head.next == head:
    return None
  temp = head
  while temp.next != head:
    temp = temp.next
  
  temp.next = temp.next.next
  return temp.next

head = ListNode.create([10,20,30])
res = delete_the_head_node(head)
print(res)

head = ListNode.create([20, 30])
res = delete_the_head_node(head)
print(res)

head = ListNode.create([10])
res = delete_the_head_node(head)
print(res)

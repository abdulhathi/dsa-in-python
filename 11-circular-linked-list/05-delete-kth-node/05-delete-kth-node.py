import sys
import os
sys.path.append(os.getcwd())
from PythonDataStructures.CircularLinkedList.ListNode import ListNode

def delete_kth_node(head, k):
  if not head:
    return None
  elif k == 1:
    temp = head
    while temp.next != head:
      temp = temp.next
    temp.next = temp.next.next
    return temp.next
  else:
    temp = head
    for _ in range(k-2):
      temp = temp.next
    temp.next = temp.next.next
    return head
  
head = ListNode.create([10,20,15,30])
res = delete_kth_node(head, 4)
print(res)

head = ListNode.create([10, 20, 15, 30])
res = delete_kth_node(head, 1)
print(res)

head = ListNode.create([10, 20, 15, 30])
res = delete_kth_node(head, 3)
print(res)

import sys
import os
sys.path.append(os.getcwd())
from PythonDataStructures.SinglyLinkedList.ListNode import ListNode

def reverse_linked_lis_by_k_groups(head, k):
  prev, curr = None, head
  groups = []
  while curr:
    n = k
    tail = curr
    while n > 0 and curr:
      next = curr.next
      curr.next = prev
      prev = curr
      curr = next
      n -= 1
    groups.append([prev, tail])
    prev = None
  
  head, tail = groups.pop()
  while groups:
    newHead, newTail = groups.pop()
    newTail.next = head
    head = newHead
  return head
        

head = ListNode.create([10,20,30,40,50,60])
res = reverse_linked_lis_by_k_groups(head, 3)
print(res)

head = ListNode.create([10, 20, 30, 40, 50, 60])
res = reverse_linked_lis_by_k_groups(head, 2)
print(res)

head = ListNode.create([10, 20, 30, 40, 50, 60])
res = reverse_linked_lis_by_k_groups(head, 1)
print(res)

head = ListNode.create([10, 20, 30, 40, 50])
res = reverse_linked_lis_by_k_groups(head, 3)
print(res)

head = ListNode.create([10, 20, 30])
res = reverse_linked_lis_by_k_groups(head, 4)
print(res)


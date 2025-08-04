import sys
import os
sys.path.append(os.getcwd())
from PythonDataStructures.SinglyLinkedList.ListNode import ListNode


def nth_node_from_last(head, n):
  length = 0
  temp = head
  while temp:
    length += 1
    temp = temp.next
  node_ind = length+1-n
  if n > length:
    return None
  for _ in range(node_ind-1):
    head = head.next
  return head

head = ListNode.create([10,20,30,40,50])
res = nth_node_from_last(head, 2)
print(res)

head = ListNode.create([10, 20, 30, 40, 50])
res = nth_node_from_last(head, 1)
print(res)

head = ListNode.create([10, 20, 30, 40, 50])
res = nth_node_from_last(head, 5)
print(res)

head = ListNode.create([10, 20, 30, 40, 50])
res = nth_node_from_last(head, 6)
print(res)

head = ListNode.create([10, 20, 30, 40, 50])
res = nth_node_from_last(head, 0)
print(res)

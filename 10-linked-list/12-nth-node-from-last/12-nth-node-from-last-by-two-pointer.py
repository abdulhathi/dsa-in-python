import sys
import os
sys.path.append(os.getcwd())
from PythonDataStructures.SinglyLinkedList.ListNode import ListNode

# * Time: O(n) Space: O(1)
def nth_node_by_two_pointer(head, n):
  first, second = head, head
  for _ in range(n):
    if not first:
      return None
    first = first.next
  
  while first:
    first = first.next
    second = second.next
  return second

head = ListNode.create([10,20,30,40,50,60,70])
res = nth_node_by_two_pointer(head, 3)
print(res)

head = ListNode.create([10, 20, 30, 40, 50, 60, 70])
res = nth_node_by_two_pointer(head, 2)
print(res)

head = ListNode.create([10])
res = nth_node_by_two_pointer(head, 2)
print(res)

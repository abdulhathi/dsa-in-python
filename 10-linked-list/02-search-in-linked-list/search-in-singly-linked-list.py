import sys
import os
sys.path.append(os.getcwd())
from PythonDataStructures.SinglyLinkedList.ListNode import ListNode


def search_in_singly_linked_list(head, key):
  ind = 0
  while head:
    if head.val == key:
      return ind
    head = head.next
    ind += 1
  return -1


head = ListNode.create([10, 5, 20, 15])
print(search_in_singly_linked_list(head, 20))
print(search_in_singly_linked_list(ListNode.create([10, 15]), 20))
print(search_in_singly_linked_list(ListNode.create([10, 5, 30]), 10))

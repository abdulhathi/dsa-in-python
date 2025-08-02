import sys
import os
sys.path.append(os.getcwd())
from PythonDataStructures.SinglyLinkedList.ListNode import ListNode


def sorted_insert_in_linked_list(head, key):
  dummy = ListNode(0, head)
  temp = dummy
  while temp.next:
    if temp.next.val > key:
      break
    temp = temp.next
  temp.next = ListNode(key, temp.next)
  return dummy.next


head = ListNode.create([10, 20, 30, 40])
res = sorted_insert_in_linked_list(head, 25)
print(res)

head = ListNode.create([10, 25])
res = sorted_insert_in_linked_list(head, 5)
print(res)

head = ListNode.create([10, 20])
res = sorted_insert_in_linked_list(head, 30)
print(res)

head = ListNode.create([])
res = sorted_insert_in_linked_list(head, 30)
print(res)

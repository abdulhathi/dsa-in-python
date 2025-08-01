import sys
import os
sys.path.append(os.getcwd())
from PythonDataStructures.SinglyLinkedList.ListNode import ListNode


def insert_at_the_beginning_of_the_linked_list(head, key):
  return ListNode(key, head)


head = None
res = insert_at_the_beginning_of_the_linked_list(head, 10)
print(res)

head = ListNode.create([10, 20, 30])
res = insert_at_the_beginning_of_the_linked_list(head, 5)
print(res)


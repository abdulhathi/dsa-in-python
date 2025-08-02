import sys
import os
sys.path.append(os.getcwd())
from PythonDataStructures.CircularLinkedList.ListNode import ListNode

def insert_at_the_beginning(head, key):
  temp = head
  while temp.next != head:
    temp = temp.next
  temp.next = ListNode(key, temp.next)
  return temp.next

head = ListNode.create([10,20,30])
res = insert_at_the_beginning(head, 5)
print(res)
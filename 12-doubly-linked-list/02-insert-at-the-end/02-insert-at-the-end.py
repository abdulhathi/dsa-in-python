import sys
import os
sys.path.append(os.getcwd())
from PythonDataStructures.DoublyLinkedList.ListNode import ListNode

def insert_at_the_end(head, key):
  temp = head
  while temp.next:
    temp = temp.next
  temp.next = ListNode(key, temp)
  return head

head = ListNode.create([10,20,30])
res = insert_at_the_end(head, 40)
print(res)
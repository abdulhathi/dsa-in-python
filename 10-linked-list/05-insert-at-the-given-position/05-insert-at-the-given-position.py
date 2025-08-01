import sys
import os
sys.path.append(os.getcwd())
from PythonDataStructures.SinglyLinkedList.ListNode import ListNode

def insert_at_the_given_position(head, key, index):
  dummy = ListNode(0, head)
  temp = dummy
  pos = 1
  while temp.next:
    if pos == index:
      break
    temp = temp.next
    pos += 1
  temp.next = ListNode(key, temp.next)
  return dummy.next

head = ListNode.create([10,30,50,70])
res = insert_at_the_given_position(head, 20, 2)
print(res)

head = ListNode.create([5,15,25,25])
res = insert_at_the_given_position(head, 10, 5)
print(res)

import sys, os
sys.path.append(os.getcwd())
from PythonDataStructures.SinglyLinkedList.ListNode import ListNode

def insert_at_the_end_of_the_linked_list(head, key):
  dummy = ListNode(0, head)
  temp = dummy
  while temp.next:
    temp = temp.next
  temp.next = ListNode(key)
  return dummy.next

head = ListNode.create([10,20,30])
res = insert_at_the_end_of_the_linked_list(head, 35)
print(res)

head = ListNode.create([])
res = insert_at_the_end_of_the_linked_list(head, 10)
print(res)

head = ListNode.create([10])
res = insert_at_the_end_of_the_linked_list(head, 20)
print(res)

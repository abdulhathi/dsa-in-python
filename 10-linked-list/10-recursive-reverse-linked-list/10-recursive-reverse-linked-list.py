import sys
import os
sys.path.append(os.getcwd())
from PythonDataStructures.SinglyLinkedList.ListNode import ListNode

def recursive_reverse_linked_list(head):
  def reverse(curr, prev):
    if not curr:
      return prev
    next = curr.next
    curr.next = prev
    return reverse(next, curr)
  
  return reverse(head, None)

head = ListNode.create([10,20,30])
res = recursive_reverse_linked_list(head)
print(res)
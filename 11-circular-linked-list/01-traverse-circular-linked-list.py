import sys
import os
sys.path.append(os.getcwd())
from PythonDataStructures.CircularLinkedList.ListNode import ListNode

def traverse_circular_linked_list(head):
  temp, res = head, []
  if temp:
    res.append(f" -> {temp.val}")
    temp = temp.next
    while temp != head:
      res.append(str(temp.val))
      temp = temp.next
  return " -> ".join(res) + " -> "


head = ListNode(1, ListNode(2, ListNode(3, ListNode(4))))
head.next.next.next.next = head
res = traverse_circular_linked_list(head)
print(res)

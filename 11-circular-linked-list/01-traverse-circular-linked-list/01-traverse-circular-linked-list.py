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
  return f"{' -> '.join(res)} -> "


head = ListNode.create([1, 2, 3, 4])
res = traverse_circular_linked_list(head)
print(res)

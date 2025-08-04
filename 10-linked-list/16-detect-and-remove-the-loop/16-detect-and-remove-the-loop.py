import sys
import os
sys.path.append(os.getcwd())
from PythonDataStructures.SinglyLinkedList.ListNode import ListNode


# * Floyd cycle detection
def detect_and_remove_the_loop(head):
  if not head or not head.next:
    return head
  slow, fast = head, head
  while fast and fast.next:
    slow = slow.next
    fast = fast.next.next
    if slow == fast:
      break
  if slow != fast:
    return head
  
  slow = head
  while slow.next != fast.next:
    slow = slow.next
    fast = fast.next
  fast.next = None
  return head

head = ListNode.create([10,20,30,40])
head.next.next.next.next = head.next
res = detect_and_remove_the_loop(head)
print(res)
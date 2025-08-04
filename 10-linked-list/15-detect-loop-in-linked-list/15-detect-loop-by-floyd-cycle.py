import sys
import os
sys.path.append(os.getcwd())
from PythonDataStructures.SinglyLinkedList.ListNode import ListNode

# * Detect the loop by slow and fast pointer. When it meets both on same node then loop exist.
# * Time: O(n) Space: O(1)
def detect_loop_by_floyd_cycle(head):
  if not head or not head.next:
    return False
  if head == head.next:
    return True
  slow, fast = head, head
  while fast and fast.next:
    slow = slow.next
    fast = fast.next.next
    if slow == fast:
      return True
  return False

head = ListNode.create([10,15,12,20])
head.next.next.next.next = head.next
res = detect_loop_by_floyd_cycle(head)
print(res)

head = ListNode.create([10, 15, 12, 20])
res = detect_loop_by_floyd_cycle(head)
print(res)

head = ListNode.create([10])
res = detect_loop_by_floyd_cycle(head)
print(res)

head = ListNode.create([])
res = detect_loop_by_floyd_cycle(head)
print(res)

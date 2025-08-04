import sys
import os
sys.path.append(os.getcwd())
from PythonDataStructures.SinglyLinkedList.ListNode import ListNode

# * Detect the loop by assign the next node each node to the dummy node. So if loop exist the node which already pointing to the next node is dummy node then loop exist.
# * Time: O(n) Space: O(1)
def detect_loop_by_pointing_dummy_node(head):
  dummy = ListNode(0)
  while head:
    if head.next == dummy:
      return True
    next = head.next
    head.next = dummy
    head = next
  return False

head = ListNode.create([10,15,12,20])
head.next.next.next.next = head.next
res = detect_loop_by_pointing_dummy_node(head)
print(res)

head = ListNode.create([10, 15, 12, 20])
res = detect_loop_by_pointing_dummy_node(head)
print(res)

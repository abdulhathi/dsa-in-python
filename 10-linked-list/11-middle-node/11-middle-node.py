import sys
import os
sys.path.append(os.getcwd())
from PythonDataStructures.SinglyLinkedList.ListNode import ListNode

# * Time : O(n) Space : O(1)
def middle_node(head):
  slow, fast = head, head
  while fast and fast.next:
    fast = fast.next.next
    slow = slow.next
  return slow


# ^ Even node
head = ListNode.create([10,20,30,40,50,60])
res = middle_node(head)
print(res)

# ^ Even node
head = ListNode.create([10, 20, 30, 40, 50,60,70])
res = middle_node(head)
print(res)

# ^ Zero node
head = ListNode.create([])
res = middle_node(head)
print(res)

# ^ one node
head = ListNode.create([10])
res = middle_node(head)
print(res)

# ^ two node
head = ListNode.create([10,20])
res = middle_node(head)
print(res)

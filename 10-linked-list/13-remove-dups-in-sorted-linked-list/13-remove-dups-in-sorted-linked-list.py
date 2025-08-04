import sys
import os
sys.path.append(os.getcwd())
from PythonDataStructures.SinglyLinkedList.ListNode import ListNode

# * Time: O(n) Space: O(1)
def remove_duplicates_in_sorted_linked_list(head):
  if not head or not head.next:
    return head
  
  temp = head
  while temp:
    while temp.next and temp.val == temp.next.val:
      temp.next = temp.next.next
    temp = temp.next
  return head

head = ListNode.create([10,10,20,20,30,30,30])
res = remove_duplicates_in_sorted_linked_list(head)
print(res)

head = ListNode.create([10, 10])
res = remove_duplicates_in_sorted_linked_list(head)
print(res)

head = ListNode.create([10])
res = remove_duplicates_in_sorted_linked_list(head)
print(res)

head = ListNode.create([])
res = remove_duplicates_in_sorted_linked_list(head)
print(res)

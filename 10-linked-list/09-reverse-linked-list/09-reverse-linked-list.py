import sys
import os
sys.path.append(os.getcwd())
from PythonDataStructures.SinglyLinkedList.ListNode import ListNode

def reverse_linked_list(head):
  prev, curr = None, head
  while curr:
    next = curr.next
    curr.next = prev
    prev = curr
    curr = next
  return prev

head = ListNode.create([10,20,30])
res = reverse_linked_list(head)
print(res)

# ^   p = N  c = 10 -> 20 -> 30 -> N 
# ^   n = 20 -> 30 -> N   p = 10 -> N               c = n
# ^   n = 30 -> N         p = 20 -> 10 -> n         c = n
# ^   n = N               p = 30 -> 20 -> 10 -> n   c = n
# ^   return p

def reverse_linked_list_by_stack(head):
  st, temp = [], head
  while temp:
    st.append(temp.val)
    temp = temp.next
  temp = head
  while st:
    temp.val = st.pop()
    temp = temp.next
  return head


head = ListNode.create([10, 20, 30])
res = reverse_linked_list_by_stack(head)
print(res)

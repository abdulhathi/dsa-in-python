from DoublyLinkedList import ListNode


def insert_at_beginning_of_doubly_linked_list(head, x):
  node = ListNode(x, None, head)
  if head:
    head.prev = node
  return node


head = ListNode.create([10, 15, 20])
# print(head)
res = insert_at_beginning_of_doubly_linked_list(head, 5)
print(res)

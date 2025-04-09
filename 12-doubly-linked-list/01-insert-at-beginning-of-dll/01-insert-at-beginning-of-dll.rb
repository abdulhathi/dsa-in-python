require_relative '../../RubyDataStructure/DoublyLinkedList/ListNode.rb'

def insert_at_beginning_of_doubly_linked_list(head, key)
  return ListNode.new(key, head)
end

l1 = ListNode.new(10)
l2 = ListNode.new(20, nil, l1)
l1.next = l2

res = insert_at_beginning_of_doubly_linked_list l1, 5
while res
  print "#{res.val} "
  res = res.next
end
require_relative '../../RubyDataStructure/CircularLinkedList/ListNode.rb'

def traverse_circular_linked_list(head)
  return [] if !head
  temp = head
  res = [temp.val]
  temp = temp.next
  while temp != head
    res.append(temp.val)
    temp = temp.next
  end
  return res
end

head = ListNode.new(1, ListNode.new(2, ListNode.new(3, ListNode.new(4))))
head.next.next.next.next = head

print traverse_circular_linked_list head
require_relative '../../RubyDataStructure/SinglyLinkedList/ListNode.rb'

def traverse_linked_list(node)
  res = []
  while node
    res.append(node.val)
    node = node.next
  end
  res
end

node = ListNode.new(10, ListNode.new(20, ListNode.new(30)))
print traverse_linked_list(node)
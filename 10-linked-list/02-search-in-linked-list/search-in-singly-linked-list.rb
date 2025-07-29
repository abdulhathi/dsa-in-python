require_relative '../../RubyDataStructure/SinglyLinkedList/ListNode'

def search_in_singly_linked_list(head, key)
  ind = 0
  while head
    return ind if head.val == key
    ind += 1
    head = head.next
  end
  -1
end

puts search_in_singly_linked_list(ListNode.create([10,5,20,15]), 20)
puts search_in_singly_linked_list(ListNode.create([10,15]), 20)
puts search_in_singly_linked_list(ListNode.create([10,5,30]), 10)
import { ListNode } from '../../TypeScriptDataStructure/SinglyLinkedList/ListNode'

const search_in_singly_linked_list = (head: ListNode, key: number) => {
  let ind = 0
  while (head) {
    if (head.val === key) return ind
    ind += 1
    head = head.next
  }
  return -1
}

console.log(search_in_singly_linked_list(ListNode.create([10, 5, 20, 15]), 20))
console.log(search_in_singly_linked_list(ListNode.create([10, 15]), 20))
console.log(search_in_singly_linked_list(ListNode.create([10, 5, 30]), 10))

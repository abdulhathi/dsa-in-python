import { ListNode } from '../../TypeScriptDataStructure/SinglyLinkedList/ListNode'

const traverse_linked_list = (head: ListNode) => {
  const res = []
  while (head) {
    res.push(head.val)
    head = head.next
  }
  return res
}

const node = new ListNode(10, new ListNode(20))
console.log(traverse_linked_list(node))

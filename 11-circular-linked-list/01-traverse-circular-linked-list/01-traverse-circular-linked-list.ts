import { ListNode } from '../../TypeScriptDataStructure/CircularLinkedList/ListNode'

const traverse_circular_linked_list = (head: ListNode) => {
  if (head === null)
    return []
  let temp = head
  const res = [temp.val]
  temp = temp.next
  while (temp !== head) {
    res.push(temp.val)
    temp = temp.next
  }
  return res
}

const head = new ListNode(10, new ListNode(20, new ListNode(30, new ListNode(40))))
head.next.next.next.next = head
console.log(traverse_circular_linked_list(head))

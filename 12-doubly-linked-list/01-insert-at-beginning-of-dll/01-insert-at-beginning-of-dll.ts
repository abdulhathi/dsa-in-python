import { ListNode } from '../../TypeScriptDataStructure/DoublyLinkedList/ListNode'

const insert_at_beginning_of_dll = (head: ListNode, key: number) => {
  const new_head = new ListNode(key, null, head)
  head.prev = new_head
  return new_head
}

const head = new ListNode(10, null, new ListNode(20))
head.next.prev = head

console.log(insert_at_beginning_of_dll(head, 30))
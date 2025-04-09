export class ListNode {
  val: number
  next: ListNode
  prev: ListNode

  constructor(val = 0, prev = null, next = null) {
    this.val = val
    this.prev = prev
    this.next = next
  }
}

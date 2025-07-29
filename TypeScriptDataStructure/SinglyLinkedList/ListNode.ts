export class ListNode {
  val: number
  next: ListNode | null

  constructor(val?: number, next?: ListNode | null) {
    this.val = val
    this.next = next
  }

  static create(arr: number[]) {
    const dummy = new ListNode(0)
    let temp = dummy
    for (const num of arr) {
      temp.next = new ListNode(num)
      temp = temp.next
    }
    return dummy.next
  }
}

class ListNode:
  def __init__(self, val=0, prev=None, next=None):
    self.val = val
    self.next = next
    self.prev = prev

  def create(items=[]):
    n = len(items)
    if n == 0:
      return None
    head = ListNode(items[0])
    temp = head
    for i in range(1, n):
      temp.next = ListNode(items[i], temp, None)
      temp = temp.next
    return head

  def __str__(self):
    head = self
    res = []
    while head:
      res.append(str(head.val))
      head = head.next
    return f"None <- {' <=> '.join(res)} -> None"

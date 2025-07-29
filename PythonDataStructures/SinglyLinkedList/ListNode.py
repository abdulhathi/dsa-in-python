class ListNode:
  def __init__(self, val=0, next=None):
    self.val = val
    self.next = next

  def __str__(self):
    head = self
    res = []
    while head:
      res.append(str(head.val))
      head = head.next
    return " -> ".join(res)

  @staticmethod
  def create(nums):
    dummy = ListNode(0)
    temp = dummy
    for num in nums:
      temp.next = ListNode(num)
      temp = temp.next
    self = dummy.next
    return self
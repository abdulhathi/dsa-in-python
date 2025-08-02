class ListNode:
  def __init__(self, val=0, next=None):
    self.val = val
    self.next = next

  def __str__(self):
    temp, res = self, []
    while temp.next != self:
      res.append(str(temp.val))
      temp = temp.next
    res.append(str(temp.val))
    return f"{' -> '.join(res)} -> {temp.next.val}"

  @staticmethod
  def create(nums):
    dummy = ListNode(0)
    temp = dummy
    for num in nums:
      temp.next = ListNode(num)
      temp = temp.next
    temp.next = dummy.next
    return dummy.next

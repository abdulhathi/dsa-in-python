from collections import deque


class TreeNode:
  def __init__(self, val=0, left=None, right=None):
    self.val = val
    self.left = left
    self.right = right

  def create(items=[]):
    if not items:
      return None
    root, i, n = TreeNode(items[0]), 1, len(items)
    q = deque([root])
    while i < n:
      curr = q.popleft()
      curr.left, i = TreeNode(items[i]) if items[i] else None, i+1
      if curr.left:
        q.append(curr.left)
      if i < n:
        curr.right, i = TreeNode(items[i]) if items[i] else None, i+1
        if curr.right:
          q.append(curr.right)
    return root

  def __str__(self):
    root = self
    q, res = deque([root]), []
    while q:
      curr = q.popleft()
      if not curr:
        continue
      res.append(str(curr.val))
      q.append(curr.left)
      q.append(curr.right)
    return "["+",".join(res)+"]"
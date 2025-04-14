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
      q.append(curr.left)
      if i < n:
        curr.right, i = TreeNode(items[i]) if items[i] else None, i+1
        q.append(curr.right)
    return root

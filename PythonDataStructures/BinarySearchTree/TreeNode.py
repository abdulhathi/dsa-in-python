from collections import deque


class TreeNode:
  def __init__(self, val=0, left=None, right=None):
    self.val = val
    self.left = left
    self.right = right

  def create(items=[]):
    def create_bst(root, key):
      if not root:
        return TreeNode(key)
      elif key < root.val:
        root.left = create_bst(root.left, key)
      else:
        root.right = create_bst(root.right, key)
      return root

    root = None
    for item in items:
      if not item:
        continue
      root = create_bst(root, item)
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
    return ",".join(res)

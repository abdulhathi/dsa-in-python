from BinaryTree import TreeNode


def iterative_pre_order_traversal(root):
  st, res = [], []
  while st or root:
    if root:
      st.append(root)
      res.append(root.val)
      root = root.left
    else:
      root = st.pop()
      root = root.right
  return res


root = TreeNode.create([10, 20, 30, None, None, 40, 50])
res = iterative_pre_order_traversal(root)
print(res)
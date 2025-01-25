from BinaryTree import TreeNode


def iterative_post_order_traversal(root):
  st, res = [], []
  while st or root:
    if root:
      st.append((root, False))
      root = root.left
    else:
      curr, flag = st.pop()
      if flag:
        res.append(curr.val)
      else:
        st.append((curr, True))
        root = curr.right
  return res


root = TreeNode.create([10, 20, 30, None, None, 40, 50])
res = iterative_post_order_traversal(root)
print(res)

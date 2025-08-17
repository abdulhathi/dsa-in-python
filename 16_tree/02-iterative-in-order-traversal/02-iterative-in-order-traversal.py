import sys, os
sys.path.append(os.getcwd())
from PythonDataStructures.BinaryTree.TreeNode import TreeNode


def iterative_in_order_traversal(root):
  st, res = [], []
  while st or root:
    if root:
      st.append(root)
      root = root.left
    else:
      root = st.pop()
      res.append(root.val)
      root = root.right
  return res 


root = TreeNode.create([10, 20, 30, None, None, 40, 50])
res = iterative_in_order_traversal(root)
print(res)
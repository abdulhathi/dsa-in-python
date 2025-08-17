import sys, os
sys.path.append(os.getcwd())
from PythonDataStructures.BinaryTree.TreeNode import TreeNode


def preOrderTraversal(root):
  if not root:
    return []
  return [root.val] + preOrderTraversal(root.left) + preOrderTraversal(root.right)

root = TreeNode.create([10, 20, 30, None, None, 40, 50])
res = preOrderTraversal(root)
print(res)
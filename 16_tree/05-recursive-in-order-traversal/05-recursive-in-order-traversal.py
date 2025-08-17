import sys, os
sys.path.append(os.getcwd())
from PythonDataStructures.BinaryTree.TreeNode import TreeNode

def inOrderTraversal(root):
  if not root:
    return []
  return inOrderTraversal(root.left) + [root.val] + inOrderTraversal(root.right)


root = TreeNode.create([10, 20, 30, None, None, 40, 50])
res = inOrderTraversal(root)
print(res)

import sys, os
sys.path.append(os.getcwd())
from PythonDataStructures.BinaryTree.TreeNode import TreeNode

def postOrderTraversal(root):
  if not root:
    return []
  return postOrderTraversal(root.left) + postOrderTraversal(root.right) + [root.val]


root = TreeNode.create([10, 20, 30, None, None, 40, 50])
res = postOrderTraversal(root)
print(res)
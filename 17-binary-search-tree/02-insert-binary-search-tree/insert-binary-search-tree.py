import sys, os
sys.path.append(os.getcwd())
from PythonDataStructures.BinarySearchTree.TreeNode import TreeNode

def insertBST(root, val):
  if not root:
    return TreeNode(val)
  elif val < root.val:
    root.left = insertBST(root.left, val)  
  elif val > root.val:
    root.right = insertBST(root.right, val)
  else:
    return root
  return root

root = TreeNode.create([10,15,12,18])
root = insertBST(root, 20)
print(root)

root = TreeNode.create([])
root = insertBST(root, 20)
print(root)

root = TreeNode.create([8,2,10])
res = insertBST(root, 10)
print(res)
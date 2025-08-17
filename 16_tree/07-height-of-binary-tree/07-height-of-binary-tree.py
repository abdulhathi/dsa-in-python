import sys, os
sys.path.append(os.getcwd())
from PythonDataStructures.BinaryTree.TreeNode import TreeNode

def height(root):
  if not root:
    return 0
  return 1 + max(height(root.left), height(root.right))

root = TreeNode.create([10,8,30,None,None,40,50,None,None,70])
print(height(root))

root = TreeNode.create([30,40,20,70,None,None,None,None,80])
print(height(root))

root = TreeNode.create([10])
print(height(root))

root = TreeNode.create([])
print(height(root))

root = TreeNode.create([10,20,None,30])
print(height(root))
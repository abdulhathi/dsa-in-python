import sys, os
sys.path.append(os.getcwd())
from PythonDataStructures.BinaryTree.TreeNode import TreeNode

# * Time: O(n) Space: O(n)
def sizeOfTheBinaryTree(root):
  if not root:
    return 0
  return sizeOfTheBinaryTree(root.left) + sizeOfTheBinaryTree(root.right) + 1

root = TreeNode.create([10,80,70,40,50])
print(sizeOfTheBinaryTree(root))

root = TreeNode.create([])
print(sizeOfTheBinaryTree(root))

root = TreeNode.create([10,None,20,None,30])
print(sizeOfTheBinaryTree(root))

root = TreeNode.create([10])
print(sizeOfTheBinaryTree(root))
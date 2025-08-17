import sys, os
sys.path.append(os.getcwd())
from PythonDataStructures.BinaryTree.TreeNode import TreeNode
import math

# * Time: O(n) Space: O(n)
def maxOfBinaryTree(root):
  if not root:
    return -math.inf
  return max(root.val, maxOfBinaryTree(root.left), maxOfBinaryTree(root.right))

root = TreeNode.create([10,30,5,90,None,80,70])
print(maxOfBinaryTree(root))
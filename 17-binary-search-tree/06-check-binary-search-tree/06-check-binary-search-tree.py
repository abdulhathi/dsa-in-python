import sys, os
sys.path.append(os.getcwd())
from PythonDataStructures.BinaryTree.TreeNode import TreeNode
import math

def checkBST(root):
  def isBST(root, leftMax = -math.inf, rightMax = math.inf):
    if not root:
      return True
    if not leftMax < root.val < rightMax:
      return False
    return isBST(root.left, leftMax, root.val) and isBST(root.right, root.val, rightMax)
            
  return isBST(root)

root = TreeNode.create([10,8,20,None,None,13,24])
print(checkBST(root))

root = TreeNode.create([20,8,30,None,None,18,35])
# print(root.left.left, root.left.right)
print(checkBST(root))

# *           (20)
# *     (8)           (30)
# *                 (18)  (35)
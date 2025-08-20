import sys, os
sys.path.append(os.getcwd())
from PythonDataStructures.BinarySearchTree.TreeNode import TreeNode

def createBST(nums):

  def create(root, val):
    if not root:
      return TreeNode(val)
    elif val < root.val:
      root.left = create(root.left, val)
    elif val > root.val:
      root.right = create(root.right, val)
    else:
      return root
    return root


  root = None
  for num in nums:
    root = create(root, num)
  return root

root = createBST([20,15,30,40,50,12,18,35,80,7])
print(root)
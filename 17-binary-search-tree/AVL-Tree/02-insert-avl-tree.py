import sys, os
sys.path.append(os.getcwd())
from PythonDataStructures.BinarySearchTree.TreeNode import TreeNode

def clockWiseRotation(root):
  rootRight = root
  root = root.left
  rootRight.left = root.right
  root.right = rootRight
  return root

def antiClickWiseRotation(root):
  rootLeft = root
  root = root.right
  rootLeft.right = root.left
  root.left = rootLeft
  return root
  
def balanceFactor(root):
  def height(root):
    if not root:
      return 0
    return max(height(root.left), height(root.right)) + 1
  
  return (height(root.left) - height(root.right))

def insertAVLTree(root, key):
  if not root:
    return TreeNode(key)
  elif root.val > key:
    root.left = insertAVLTree(root.left, key)
  elif root.val <  key:
    root.right = insertAVLTree(root.right, key)
  else:
    return root
  
  bf = balanceFactor(root)
  if bf == 2:
    bfLeft = balanceFactor(root.left)
    if bfLeft == 1:
      root = clockWiseRotation(root)
    elif bfLeft == -1:
      root.left = antiClickWiseRotation(root.left)
      root = clockWiseRotation(root)
  elif bf == -2:
    bfRight = balanceFactor(root.right)
    if bfRight == -1:
      root = antiClickWiseRotation(root)
    elif bfRight == 1:
      root.right = clockWiseRotation(root.right)
      root = antiClickWiseRotation(root)
      
  return root

nums = [20,15,5,40,50,18]
root = None
for num in nums:
  root = insertAVLTree(root, num)
  print(root.left, root.right)
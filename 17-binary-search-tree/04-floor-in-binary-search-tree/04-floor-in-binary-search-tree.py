import sys, os
sys.path.append(os.getcwd())
from PythonDataStructures.BinarySearchTree.TreeNode import TreeNode

def floorInBST(root, key):
  if not root:
    return None
  if key == root.val:
    return root
  elif root.val < key:
    res = floorInBST(root.right, key) 
    return root if not res or root.val > res.val else res
  elif root.val > key:
    return floorInBST(root.left, key)
  
root = TreeNode.create([50,30,70,20,40,60,80,None,None,None,None,55,65])
print(floorInBST(root, 28))
print(floorInBST(root, 58))
print(floorInBST(root, 65))




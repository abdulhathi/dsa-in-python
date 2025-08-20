import sys, os
sys.path.append(os.getcwd())
from PythonDataStructures.BinarySearchTree.TreeNode import TreeNode

# * Approach: Iterative Time: O(n) Space: O(h)
def floorInBST(root, key):
  res = None
  while root:
    if root.val == key:
      return root
    elif root.val < key:
      res = root
      root = root.right
    else:
      root = root.left
  return res


root = TreeNode.create([50,30,70,20,40,60,80,None,None,None,None,55,65])
print(floorInBST(root, 28))
print(floorInBST(root, 58))
print(floorInBST(root, 65))
print(floorInBST(root, 18))
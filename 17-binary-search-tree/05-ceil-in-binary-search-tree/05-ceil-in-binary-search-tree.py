import sys, os
sys.path.append(os.getcwd())
from PythonDataStructures.BinarySearchTree.TreeNode import TreeNode

# * Approach: Iterative Time: O(n) Space: O(h)
def ceilInBST(root, key):
  res = None
  while root:
    if root.val == key:
      return root
    elif root.val > key:
      res = root
      root = root.left
    else:
      root = root.right
  return res


root = TreeNode.create([50,30,70,20,40,60,80,None,None,None,None,55,65])
print(ceilInBST(root, 28))
print(ceilInBST(root, 58))
print(ceilInBST(root, 65))
print(ceilInBST(root, 18))
print(ceilInBST(root, 90))
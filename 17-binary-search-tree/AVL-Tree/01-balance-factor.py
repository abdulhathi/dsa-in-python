import sys, os
sys.path.append(os.getcwd())
from PythonDataStructures.BinarySearchTree.TreeNode import TreeNode

# * Time: O(n) Space: O(h)
def balanceFactor(root):
  def height(root):
    if not root:
      return 0
    return max(height(root.left), height(root.right)) + 1
  
  return abs(height(root.left) - height(root.right))

root = TreeNode.create([18,12,None,8,None])
print(balanceFactor(root))

root = TreeNode.create([18,6,20,2,None,19,None])
print(balanceFactor(root))
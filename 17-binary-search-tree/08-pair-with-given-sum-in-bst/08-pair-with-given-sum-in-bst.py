import sys, os
sys.path.append(os.getcwd())
from PythonDataStructures.BinarySearchTree.TreeNode import TreeNode

# * Time: O(n) Space: O(n)
def pairWithGivenSumInBST(root, sum):
  s = set()
  
  def dfs(root):
    if not root:
      return False
    if sum - root.val in s:
      return True
    s.add(root.val)
    return dfs(root.left) or dfs(root.right)
  
  return dfs(root)

root = TreeNode.create([10,8,20,4,9,11,30,None,None,None,None,None,None,25])
res = pairWithGivenSumInBST(root, 33)
print(res)

root = TreeNode.create([20,8,40,None,None,35])
res = pairWithGivenSumInBST(root, 49)
print(res)
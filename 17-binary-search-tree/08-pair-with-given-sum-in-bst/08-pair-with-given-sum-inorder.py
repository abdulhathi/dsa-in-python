import sys, os
sys.path.append(os.getcwd())
from PythonDataStructures.BinarySearchTree.TreeNode import TreeNode

# * Time: O(n) Space: O(n)
def pairWithGivenSumInBST(root, sum):
  inOrderRes = []
  def inOrder(root):
    if root:
      inOrder(root.left)
      inOrderRes.append(root.val)
      inOrder(root.right)

  inOrder(root)
  lp, rp = 0, len(inOrderRes) - 1
  while lp < rp:
    pair = inOrderRes[lp] + inOrderRes[rp]
    if pair == sum:
      return True
    elif pair < sum:
      lp += 1
    else:
      rp -= 1
  return False

root = TreeNode.create([10,8,20,4,9,11,30,None,None,None,None,None,None,25])
res = pairWithGivenSumInBST(root, 33)
print(res)

root = TreeNode.create([20,8,40,None,None,35])
res = pairWithGivenSumInBST(root, 49)
print(res)
import sys, os
sys.path.append(os.getcwd())
from PythonDataStructures.BinaryTree.TreeNode import TreeNode

def checkBSTIfTwoNodesSwapped(root):
  prev, first, second = None, None, None
  def checkBST(root):
    nonlocal prev,first,second
    if not root:
      return
    checkBST(root.left)
    if prev and prev.val > root.val:
      if not first:
        first = prev
      else:
        second = root
    prev = root
    checkBST(root.right)
  
  checkBST(root)
  first.val, second.val = second.val, first.val
  return root

root = TreeNode.create([18,60,70,4,None,8,80])
res = checkBSTIfTwoNodesSwapped(root)
print(res)
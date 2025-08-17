import sys, os
sys.path.append(os.getcwd())
from PythonDataStructures.BinaryTree.TreeNode import TreeNode
from collections import deque

# * Time: O(n) Space: O(n)
def levelOrderTraversal(root):
  q, res = deque(), []
  q.append(root)
  while q:
    curr = q.popleft()
    res.append(curr.val)
    if curr.left:
      q.append(curr.left)
    if curr.right:
      q.append(curr.right)
  return res

root = TreeNode.create([10,20,30,8,7,None,6,None,None,9,15])
res = levelOrderTraversal(root)
print(res)
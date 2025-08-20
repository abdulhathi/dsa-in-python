import sys, os
sys.path.append(os.getcwd())
from PythonDataStructures.BinaryTree.TreeNode import TreeNode
from collections import deque

def levelByLevelResult(root):
  res = []
  if not root: return res
  q = deque([root])
  while q:
    level = []
    for _ in range(len(q)):
      curr = q.popleft()
      level.append(curr.val)
      if curr.left:
        q.append(curr.left)
      if curr.right:
        q.append(curr.right)
    if level:
      res.append(level)
  return res

root = TreeNode.create([10,20,30,40,50,None,60,None,None,None,None,70,80])
res = levelByLevelResult(root)
print(res)
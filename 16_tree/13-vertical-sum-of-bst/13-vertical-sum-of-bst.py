import sys, os
sys.path.append(os.getcwd())
from PythonDataStructures.BinaryTree.TreeNode import TreeNode
from collections import defaultdict, deque

def verticalSumOfBST(root):
  dic = defaultdict(int)

  q = deque([[root, 0]])
  i, j = 0, 0
  while q:
    curr, col = q.popleft()
    i, j = min(i, col), max(j, col)
    dic[col] += curr.val
    if curr.left:
      q.append([curr.left, col-1])
    if curr.right:
      q.append([curr.right, col+1])
    
  return [dic[i] for i in range(i, j+1)]

root = TreeNode.create([10,20,30,5,15,None,None])
res = verticalSumOfBST(root)
print(res)
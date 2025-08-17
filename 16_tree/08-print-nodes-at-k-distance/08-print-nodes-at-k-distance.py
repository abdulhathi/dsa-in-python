import sys, os
sys.path.append(os.getcwd())
from PythonDataStructures.BinaryTree.TreeNode import TreeNode

def print_nodes_from_k_distance(root, k):

  def kDistanceNode(root, dist):
    if not root:
      return []
    left = kDistanceNode(root.left, dist+1)
    right = kDistanceNode(root.right, dist+1)
    curr = [root.val] if dist == k else []
    return left + curr + right

  return kDistanceNode(root, 0)

root = TreeNode.create([10,20,30,40,50,None,70])
res = print_nodes_from_k_distance(root, 2)
print(res)

root = TreeNode.create([10,6,8,None,None,None,7,11,12])
res = print_nodes_from_k_distance(root, 3)
print(res)

root = TreeNode.create([10,20,None,30])
res = print_nodes_from_k_distance(root, 1)
print(res)
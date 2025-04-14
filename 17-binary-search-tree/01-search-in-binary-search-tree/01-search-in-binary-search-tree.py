import os, sys
sys.path.append(os.getcwd())
from PythonDataStructures.BinarySearchTree.TreeNode import TreeNode


def search_in_binary_search_tree(root, key):
  if not root:
    return False
  elif key == root.val:
    return True
  elif key < root.val:
    return search_in_binary_search_tree(root.left, key)
  else:
    return search_in_binary_search_tree(root.right, key)


root = TreeNode.create(
    [20, 10, 40, 5, None, 30, 80, None, None, None, None, 50, 100])
# print(root)
res = search_in_binary_search_tree(root, 50)
print(res)

root = TreeNode.create([15, 10, 12])
res = search_in_binary_search_tree(root, 16)
print(res)

root = TreeNode.create([18, 16, 30, None, None, 20, 100])
res = search_in_binary_search_tree(root, 18)
print(res)
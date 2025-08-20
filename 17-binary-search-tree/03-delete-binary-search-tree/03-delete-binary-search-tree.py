import sys
import os
sys.path.append(os.getcwd())
from PythonDataStructures.BinarySearchTree.TreeNode import TreeNode


def deleteBST(root, key):
  def height(root):
    if not root:
      return 0
    return max(height(root.left), height(root.right)) + 1

  def inOrderPredecessor(root):
    predecessor = root
    while predecessor and predecessor.right:
      predecessor = predecessor.right
    return predecessor

  def inOrderSuccessor(root):
    successor = root
    while successor and successor.left:
      successor = successor.left
    return successor

  def delete(root, key):
    if not root:
      return None
    elif key < root.val:
      root.left = delete(root.left, key)
    elif key > root.val:
      root.right = delete(root.right, key)
    else:
      if not root.left and not root.right:
        return None
      else:
        leftHeight = height(root.left)
        rightHeight = height(root.right)
        if leftHeight > rightHeight:
          predecessor = inOrderPredecessor(root.left)
          root.val = predecessor.val
          root.left = delete(root.left, predecessor.val)
        else:
          successor = inOrderSuccessor(root.right)
          root.val = successor.val
          root.right = delete(root.right, successor.val)
    return root

  return delete(root, key)

root = TreeNode.create([50, 30, 70, 20, 40, 60, 80])
res = deleteBST(root, 40)
print(res)

root = TreeNode.create([50, 20, 70, None, None, 60, 80])
res = deleteBST(root, 50)
print(res)

root = TreeNode.create([50, 20, 70, None, 40, 60, 80, 45, None, None, None, None, 43, None, 42, 44])
res = deleteBST(root, 50)
print(res)

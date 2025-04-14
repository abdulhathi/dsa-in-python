require_relative '../../RubyDataStructure/BinarySearchTree/TreeNode.rb'

def search_in_bst(val, root)
  return false if root.nil?
  if root.val == val
    return true
  else
    return val < root.val ? search_in_bst(val, root.left) : search_in_bst(val, root.right)
  end
end

root = TreeNode.create([10,20,5,2,25])
puts search_in_bst(2, root)
puts search_in_bst(12, root)

# TreeNode.new(10)
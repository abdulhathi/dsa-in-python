require_relative '../../RubyDataStructure/BinaryTree/TreeNode.rb'

def iterative_pre_order_traversal(root)
  st, res = [], []
  while !st.empty? || !root.nil?
    if !root.nil?
      st.push(root)
      res.push(root.val)
      root = root.left
    else
      root = st.pop
      root = root.right
    end
  end
  return res
end

root = TreeNode.new(10, TreeNode.new(20), TreeNode.new(30, TreeNode.new(40)))
res = iterative_pre_order_traversal(root)
print res

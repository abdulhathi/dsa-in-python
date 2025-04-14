class TreeNode
  attr_accessor :val, :left, :right
  def initialize(val, left=nil, right=nil)
    @val = val
    @left = left
    @right = right
  end
end

# root = TreeNode.new(10, TreeNode.new(20))
# puts root.left
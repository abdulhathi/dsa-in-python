class TreeNode
  attr_accessor :val, :left, :right
  def initialize(val, left=nil, right=nil)
    @val = val
    @left = left
    @right = right
  end

  def self.create(nums)
    root = nil
    nums.each do |num|
      root = create_bst(num, root)
    end
    return root
  end

  private

  def self.create_bst(val, root)
    if root.nil?
      return TreeNode.new(val)
    elsif val < root.val
      root.left = create_bst(val, root.left)
    else
      root.right = create_bst(val, root.right)
    end
    return root
  end
end
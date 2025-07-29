class ListNode
  attr_accessor :next, :val
  def initialize(val=0, next_node=nil)
    @val = val
    @next = next_node
  end

  def self.create(arr)
    dummy = ListNode.new(0)
    temp = dummy
    arr.each do |num|
      temp.next = ListNode.new(num)
      temp = temp.next
    end
    return dummy.next
  end
end
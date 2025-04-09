class ListNode
  attr_accessor :val, :next, :prev
  def initialize(val, _next = nil, _prev = nil)
    @val = val
    @next = _next
    @prev = _prev
  end
end
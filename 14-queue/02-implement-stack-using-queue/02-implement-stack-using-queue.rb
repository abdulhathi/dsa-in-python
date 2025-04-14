class StackUsingQueue
  attr_accessor :q1, :q2
  def initialize()
    @q1, @q2 = [], []
  end

  def push(val)
    @q1, @q2 = @q2, @q1
    @q1.append(val)
    while @q2.length > 0
      @q1.append(@q2.shift)
    end
  end

  def pop
    return @q1.shift if @q1
  end

  def peek
    return @q1[0] if @q1
  end

  def size
    return @q1.length
  end
end

stack = StackUsingQueue.new()
stack.push(10)
stack.push(20)
stack.push(30)

puts stack.peek
puts stack.pop

puts stack.size

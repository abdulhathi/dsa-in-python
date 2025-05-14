def max_difference(nums)
  max_diff = -Float::INFINITY
  last_max = -Float::INFINITY
  nums.reverse_each do |num|
    diff = last_max - num
    max_diff = diff if diff > max_diff
    last_max = num if num > last_max
  end
  max_diff
end

p max_difference [7,10,4,10,6,5,2]
p max_difference [2,3,10,6,4, 8, 1]
p max_difference [10,20,30]
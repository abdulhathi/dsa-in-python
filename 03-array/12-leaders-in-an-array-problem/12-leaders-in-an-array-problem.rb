def leaders_in_an_array(nums)
  leaders = []
  last_max = -Float::INFINITY
  nums.reverse_each do |num|
    if last_max < num
      leaders.unshift(num)
      last_max = num
    end
  end
  leaders
end

print leaders_in_an_array [7,10,4,10,6,5,2]


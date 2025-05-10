def move_all_zeros_to_end(nums)
  zero_pos = 0
  (0..nums.length-1).each do |i|
    if nums[i] != 0
      nums[i], nums[zero_pos] = nums[zero_pos], nums[i] if i != zero_pos
      zero_pos += 1
    end
  end
  nums
end

print move_all_zeros_to_end [8,5,0,10,0,20]
puts
print move_all_zeros_to_end [0,0,0,10,0]

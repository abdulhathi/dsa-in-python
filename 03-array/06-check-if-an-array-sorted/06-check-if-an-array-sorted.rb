def check_if_an_array_sorted(nums)
 n = nums.length
 (1..n-1).each do |i|
    return false if nums[i-1] > nums[i]
 end
 return true
end

res = check_if_an_array_sorted([8,12,15])
puts(res)
res = check_if_an_array_sorted([8, 10, 10, 12])
puts(res)
res = check_if_an_array_sorted([100])
puts(res)
res = check_if_an_array_sorted([100, 20, 200])
puts(res)

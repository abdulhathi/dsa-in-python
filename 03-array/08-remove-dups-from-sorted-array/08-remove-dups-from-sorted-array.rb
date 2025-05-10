def remove_dups_from_sorted_array(nums)
  n, j = nums.length, 1
  (1..n-1).each do |i|
    if nums[j-1] != nums[i]
      nums[j] = nums[i]
      j += 1
    end
  end
  nums
end

print remove_dups_from_sorted_array [10,20,20,30,30,30,30]

def binary_search_in_sorted_array(numbers, key)
  left, right = 0, numbers.length-1
  while left <= right 
    mid = (left+right)/2
    return true if numbers[mid] == key
    key < numbers[mid] ? right = mid-1 : left = mid+1
  end
  return false
end

puts binary_search_in_sorted_array([10, 20, 30, 40, 50, 60], 20)

puts binary_search_in_sorted_array([10, 20, 30, 40, 50, 60], 70)
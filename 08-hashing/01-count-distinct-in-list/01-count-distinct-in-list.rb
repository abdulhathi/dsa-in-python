def count_distinct_elements_in_list(numbers)
  set = {}
  numbers.each do |number|
    set[number] = number
  end
  set.length
end

print count_distinct_elements_in_list [10, 20, 10, 30, 30, 20]
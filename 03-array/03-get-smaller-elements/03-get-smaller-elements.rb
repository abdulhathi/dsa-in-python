def get_smaller_elements(numbers, key)
  smaller = []
  numbers.each do |number|
    smaller.push(number) if number < key
  end
  smaller
end

print get_smaller_elements [1,2,3,4,5], 4

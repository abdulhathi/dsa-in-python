def average_of_list(numbers)
  sum = 0
  numbers.each do |num|
    sum += num
  end
  sum / numbers.length
end

puts average_of_list [10, 20, 30]
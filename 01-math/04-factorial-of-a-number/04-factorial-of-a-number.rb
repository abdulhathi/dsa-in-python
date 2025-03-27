def factorial_of_a_number(num)
  res = 1
  (1..num).each do |i|
    res *= i
  end
  res
end

puts factorial_of_a_number 4
puts factorial_of_a_number 6
puts factorial_of_a_number 0

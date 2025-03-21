def sum_of_n_natural_numbers(n)
  sum = 0
  (0..n).each do |i|
    sum += i
  end
  sum
end

puts sum_of_n_natural_numbers 10
puts sum_of_n_natural_numbers 5
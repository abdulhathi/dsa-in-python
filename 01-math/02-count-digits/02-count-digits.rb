def count_digits(num)
  count = 0
  while num > 0
    count += 1
    num /= 10
  end
  return count
end

puts count_digits 1000
puts count_digits 999
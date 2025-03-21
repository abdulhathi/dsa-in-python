def check_a_num_is_palindrome(num)
  temp, reversed = num, 0
  while temp > 0
    reversed *= 10
    reversed += temp % 10
    temp /= 10
  end
  reversed == num
end

puts check_a_num_is_palindrome 9999
puts check_a_num_is_palindrome 9998
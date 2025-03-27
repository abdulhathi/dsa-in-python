def separate_even_and_odd(numbers)
  odd, even = [], []
  numbers.each do |number|
    number % 2 == 0 ? even.push(number) : odd.push(number)
  end
  [odd, even]
end

print separate_even_and_odd [1,2,3,4,5]
